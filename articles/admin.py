from django.contrib import admin
from . import models
from .models import Article

admin.site.register(models.Article)
