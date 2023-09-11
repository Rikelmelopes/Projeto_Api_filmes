

from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from generos.views import genero_view

def hello_view(request):
    return JsonResponse ({'Hello word'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generos/', genero_view, name='generos-list')
]
