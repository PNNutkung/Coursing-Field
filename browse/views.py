from django.shortcuts import render, redirect, get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'browse/index.html'
    context_object_name = 'latest_course_list'

    def get_queryset(self):
        '''Return the last courses.'''
        return None
