from django.contrib import admin
from .models import Inmueble, TipoInmueble, Region, Comuna

# Register your models here.
admin.site.register(Inmueble)
admin.site.register(TipoInmueble)
admin.site.register(Region)
admin.site.register(Comuna)