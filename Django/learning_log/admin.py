from django.contrib import admin
from .models import Topic, Entry

# register models so they show up in admin site
admin.site.register(Topic)
admin.site.register(Entry)
