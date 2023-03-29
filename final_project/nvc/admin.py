from django.contrib import admin

# Register your models here.

from .models import Feeling, FeelingGroup, FeelingSelection, FeelingSession

admin.site.register(Feeling)
admin.site.register(FeelingGroup)
admin.site.register(FeelingSelection)
admin.site.register(FeelingSession)