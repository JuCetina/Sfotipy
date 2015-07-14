from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
from artists.views import ArtistDetailView

from rest_framework import routers
from artists.views import ArtistViewSet
from albums.views import AlbumViewSet
from tracks.views import TrackViewSet

from userprofiles.views import LoginView
#from userprofiles.views import ProfileView
#from django.views.generic import RedirectView
from userprofiles.views import PerfilRedirectView

from artists.views import AlbumListView
from artists.views import AlbumDetailView

router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'tracks', TrackViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfotipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracks/(?P<title>[\w\-\W]+)/', 'tracks.views.track_view', name='track_view'),
    url(r'^signup/', 'userprofiles.views.signup', name='signup'),
    url(r'^signin/', 'userprofiles.views.signin', name='signin'),
    url(r'^artists/(?P<pk>[\d]+)', ArtistDetailView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^login/$', LoginView.as_view(), name='login'),
    #url(r'^profile/$', ProfileView.as_view(), name='profile'),
    #url(r'^perfil/$', RedirectView.as_view(url='/login/'), name='perfil'),
    url(r'^perfil/$', PerfilRedirectView.as_view(), name='perfil'),
    url(r'^albums/$', AlbumListView.as_view(), name='album_list'),
    url(r'^albums/(?P<artist>[\w\-]+)/$', AlbumListView.as_view(), name='album_list'),
    url(r'^albums/detail/(?P<title>[\w\-]+)/$', AlbumDetailView.as_view(), name='album_detail'),
)


urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
)
