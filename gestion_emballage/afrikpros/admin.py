from django.contrib import admin

# Register your models here.
from .models import *



admin.site.register(Depot)
admin.site.register(Fournisseur)
admin.site.register(Personnel)
admin.site.register(EchangeInterne)
admin.site.register(EchangeExterne)
admin.site.register(Emballage)