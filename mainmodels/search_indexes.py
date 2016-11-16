from haystack import indexes
from django.contrib.auth.models import User
from mainmodels.models import Course

class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    courseName = indexes.CharField(model_attr='courseName')
    owner = indexes.CharField(model_attr='owner')
    content_auto = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return Course

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
