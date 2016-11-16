from django.shortcuts import render
import simplejson as json
from django.http import HttpResponse
from haystack.query import SearchQuerySet
# Create your views here.
def search(req):
    return render(req, 'search/search.html')

from django.shortcuts import render, redirect

def autocomplete(req):
    sqs = SearchQuerySet().autocomplete(content_auto=req.POST.get('search_text', ''))
    courses = [result.title for result in sqs]

    the_data = json.dumps({
        'results': courses
    })

    return HttpResponse(the_data, content_type='application/json')
