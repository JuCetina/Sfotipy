import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

import time
from django.core.cache import cache

from django.views.decorators.cache import cache_page

from .models import Track

#@cache_page(60)

def track_view(request, title):

	track = get_object_or_404(Track, title=title)
	#data = cache.get('data_%s', title)
	#if data is None:
	data = {
		'title': track.title,
		'order': track.order,
		'album': track.album.title,
		'artist': {
			'name': track.artist.first_name,
			'bio': track.artist.biography
		}
	}
		#time.sleep(5)
		#cache.set('data_%s' % title, data)
	#json_data = json.dumps(data) #Convierte el diccionario a json

	#return HttpResponse(json_data, content_type='application/json')

	return render(request, 'track.html', {'track': track})

from rest_framework import viewsets

class TrackViewSet(viewsets.ModelViewSet):
	model = Track