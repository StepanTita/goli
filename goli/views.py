from django.shortcuts import render

# Create your views here.
from rest_framework_swagger.views import get_swagger_view

docs_view = get_swagger_view(title='Goli API')