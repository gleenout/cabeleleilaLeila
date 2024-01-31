from django.shortcuts import render

# Create your views here.
def servicos(request):
  return render(request,  'servicos.html')