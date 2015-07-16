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

from userprofiles.mixins import LoginRequireMixin

class AlbumListView(LoginRequireMixin, ListView):
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

from django.views.generic import DetailView

class AlbumDetailView(LoginRequireMixin, DetailView):
	model = Album
	template_name = 'album_detail.html'
	slug_field = 'title' #Campo por el que busa en la BD
	slug_url_kwarg = 'title' #Variable que recibe de urls.py