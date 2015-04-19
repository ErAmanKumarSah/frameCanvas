import os

from django.conf import settings

from django.db import models


class Album(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=1024)
	created_at = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey('auth.User')

	def __unicode__(self):
		return self.title

class ImageDetail(models.Model):
	title = models.CharField(max_length=100)
	original = models.ImageField(upload_to='uploads/%Y-%m/%d')
	thumbnail = models.CharField(max_length=150, null =True, blank=True)
	uploaded_at = models.DateTimeField(auto_now_add=True)
	uploaded_by = models.ForeignKey('auth.User')
	album = models.ForeignKey('Album')
		
	def __unicode__(self):
		return self.title

