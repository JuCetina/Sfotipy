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

from django.views.generic import ListView
from albums.models import Album

class AlbumListView(ListView):
	model = Album
	template_name = 'album_list.html'
	paginate_by = 2

	def get_queryset(self):
		if self.kwargs.get('artist'):
			#Devolver albumes de Artista
			queryset = self.model.objects.filter(artist__first_name__contains=self.kwargs['artist'])
		else:
			#Devuelva todos los albumes del modelo
			queryset = super(AlbumListView, self).get_queryset()

		return queryset

