from django.shortcuts import render

# Create your views here.
def get_data(request): 
  content = request.GET('con')