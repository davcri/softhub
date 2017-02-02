from django.contrib import admin

# Register your models here.
from .models.OperatingSystem import OperatingSystem
from .models.Application import Application
from .models.User import User
from .models.Developer import Developer

# from .models.Executable import Executable
# from .models.Version import Version

admin.site.register(User)
admin.site.register(Developer)
admin.site.register(OperatingSystem)
admin.site.register(Application)
# admin.site.register(Executable)
# admin.site.register(Version)
