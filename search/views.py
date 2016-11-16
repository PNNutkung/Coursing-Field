from django.shortcuts import render

# Create your views here.
def search(req):
    return render(req, 'search/search.html')
