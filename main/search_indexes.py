#from haystack import indexes
#from main.models import *

#class ProductIndex(indexes.SearchIndex, indexes.Indexable):
#    name = indexes.CharField(document=True, use_template=True)
#    price = indexes.IntegerField(model_attr='price')

#    content_auto= indexes.EdgeNgramField(model_attr='name')

#    def get_model(self):
#        return Product

#    def index_queryset(self, using=None):
#        return self.get_model().objects.all()


