from django.contrib import admin
from moim.models import Meeting, RunPythonExample


# Register your models here.

class MeetingAdmin(admin.ModelAdmin):
    pass


class RunPythonExampleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Meeting, MeetingAdmin)
admin.site.register(RunPythonExample, RunPythonExampleAdmin)
