from django.shortcuts import render
# from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def projects(request):
  return render(request, 'projects.html')