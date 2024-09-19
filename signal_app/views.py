from django.http import HttpResponse
from .models import MyModel

def create_model(request):
    MyModel.objects.create(name='test')
    return HttpResponse('MyModel instance created')