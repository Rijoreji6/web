from django.contrib import admin

# Register your models here.
from .models import DigitData
from .models import StringData
from .models import AlphaData

admin.site.register(DigitData)
admin.site.register(StringData)
admin.site.register(AlphaData)