from django.contrib import admin
from .models import *

class SceneAdmin (admin.ModelAdmin):
    list_display = ["sceneType",]

    class Meta:
        model = Scene

admin.site.register(Scene, SceneAdmin)


class PerfTypeAdmin (admin.ModelAdmin):
    list_display = ["perfType",]

    class Meta:
        model = PerfType

admin.site.register(PerfType, PerfTypeAdmin)


class PerformanceAdmin (admin.ModelAdmin):
    list_display = ["name",]

    class Meta:
        model = Performance

admin.site.register(Performance, PerformanceAdmin)