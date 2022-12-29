from django.http import HttpResponse


def index(request):
    name = "Alex"
    return HttpResponse(f"""
        <html>
            <body>
                <h3>hello Django my name is {name}</h3>
            </body>
        </html>
    """)
