from base64 import b64encode
from unittest.mock import patch, MagicMock

from django.test import TestCase
from django.test import Client
import unittest
from .models import Clothes, Feedback, Shop
import sys
import os

sys.path.insert(0, os.path.join(__file__, '../..'))
from catalog.utils import Queue


class TestQueue(TestCase):
    FIFO = "FIFO"
    LIFO = "LIFO"
    SUPPORTED_STRATEGES = [FIFO]

    def test_queue_init(self):
        queue = Queue("FIFO")

    def test_strategy_fifo(self):
        with self.assertRaises(ValueError) as error:
            queue = Queue("FIFA")

    # def test_add_fifo_value(self):
    #     for strategy in self.SUPPORTED_STRATEGES:
    #         queue = Queue(strategy)
    #         queue.add(2)

    def test_pop_fifo_value(self):
        for strategy in self.SUPPORTED_STRATEGES:
            queue = Queue(strategy)
            first_value = 1
            queue.add(first_value)
            value = queue.pop()
            self.assertEqual(value, first_value)

    def test_pop_fifo_multivalue(self):
        queue = Queue("FIFO")
        values = [1, 2, 3]
        for val in values:
            queue.add(val)

        for val in values:
            value = queue.pop()
            self.assertEqual(value, val)

    # def test_pop_lifo_multivalue(self):
    #     queue = Queue("LIFO")
    #     values = [1, 2, 3]
    #     for val in values:
    #         queue.add(val)
    #
    #     for val in reversed(values):
    #         value = queue.pop()
    #         self.assertEqual(value, val)

    def test_pop_fifo_multivalue_many_solt_value(self):
        queue = Queue("FIFO")
        values = [1, 1, 3]
        for val in values:
            queue.add(val)

        for val in values:
            value = queue.pop()
            self.assertEqual(value, val)

    def test_pop_fifo_multivalue_2(self):
        queue = Queue("FIFO")
        values = [1, 3, 1]
        for val in values:
            queue.add(val)

        for val in values:
            value = queue.pop()
            self.assertEqual(value, val)

    def test_empty_storage(self):
        for strategy in self.SUPPORTED_STRATEGES:
            with self.assertRaises(ValueError):
                queue = Queue(strategy)
                value = queue.pop()


if __name__ == "__main__":
    unittest.main()


class TestShopUrl(TestCase):
    def setUp(self):
        self.c = Client()

    def test_valid_shop_url(self):
        self.response = self.c.get('/goods/shops/')
        self.assertEqual(self.response.status_code, 200)
        print(self.response.context['shops'])

    def test_model_feedback(self):
        rating = 5
        comment = 'good job'
        self.feedback = Feedback.objects.create(rating=rating, comment=comment)
        self.assertEqual(self.feedback.rating, rating)
        self.assertEqual(self.feedback.comment, comment)
        self.assertEqual(self.feedback._meta.get_field('rating').verbose_name, 'рейтинг')
        self.assertEqual(self.feedback._meta.get_field('rating').blank, False)

    @patch('catalog.views.requests')
    def test_add_shop_form(self, fake_requests):
        img_content = b'12345678'
        fake_response = MagicMock()
        fake_requests.post.return_value = fake_response
        fake_response.json.return_value = {'images': [b64encode(img_content)]}

        adress = "Valensia"
        phone = '271812421'

        self.response = self.c.post('/goods/add_shop_form/', {
            'adress': adress,
            'phone': phone
        })
        self.assertEqual(self.response.status_code, 302)
        shop = Shop.objects.all()
        self.assertEqual(len(shop), 1)
        self.assertEqual(shop[0].adress, adress)
        self.assertEqual(shop[0].phone, phone)
        self.assertIsNotNone(shop[0].photo.url)
        self.assertEqual(shop[0].photo.read(), img_content)
