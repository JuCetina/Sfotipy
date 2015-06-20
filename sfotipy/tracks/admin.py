from django.contrib import admin
from actions import export_as_excel
from .models import Track

class TrackAdmin(admin.ModelAdmin):
	list_display = ('artist','title','order','album','player','es_pharrell')
	list_filter = ('artist','album')
	search_fields = ('title','artist__first_name','artist__last_name')
	list_editable = ('title', 'album')
	actions = (export_as_excel,)
	raw_id_fields = ('artist',) #No muestra todo el objeto sino solo el id

	def es_pharrell(self, obj):
		return obj.id == 1

	es_pharrell.boolean = True

admin.site.register(Track, TrackAdmin)