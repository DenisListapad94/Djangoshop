from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from .models import Shop


def validate_words(value):
    if len(value.split()) < 3:
        raise ValidationError(
            '(value) must be more then 3 words',
            params={'value': value},
        )


class FeedbackForm(forms.Form):
    rating = forms.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ]
    )
    comment = forms.CharField(
        validators=[
            # validate_words,
            MinLengthValidator(5, message="to short comment")
        ],
        widget=forms.Textarea(
            attrs={
                "rows": 5,
                "cols": 30,
                "placeholder": 'Ваш комментарий',
                "class": "form-control"
            }
        )
    )


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['adress', 'phone']
        # exclude = ['orders']
        widgets = {
            # 'adress' : forms.Textarea()
        }
