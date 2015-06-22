from django.shortcuts import render

# Create your views here.
from django.views.generic.detail import DetailView
from .models import Artist

class ArtistDetailView(DetailView):
	model = Artist

	def get_template_names(self):
		return 'artist.html'

from rest_framework import viewsets

from .serializers import ArtistSerializer

class ArtistViewSet(viewsets.ModelViewSet):
	model = Artist
	serializer_class = ArtistSerializer
	filter_fields = ('id', )
	paginate_by = 2