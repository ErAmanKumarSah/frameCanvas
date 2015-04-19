
from django.contrib import admin


from gallery.models import Album, ImageDetail


#class ImageDetailInline(admin.StackedInline):
class ImageDetailInline(admin.TabularInline):
	model = ImageDetail
	exclude = ('thumbnail',)#'uploaded_by')
	#readonly_fields = ('thumbnail','uploaded_by')
	#list_display = ('title', 'original')
	
	def save_model(self, request, obj, form, change):
		obj.uploaded_by = request.user
        	obj.save(form=form)

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'created_at')
	list_filter = ('created_at',)
	inlines = (ImageDetailInline,)

admin.site.register(Album, AlbumAdmin)
admin.site.register(ImageDetail)
