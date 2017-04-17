from django.contrib import admin

# Register your models here.
from .models.OperatingSystem import OperatingSystem
from .models.Application import Application
from .models.Category import Category
from .models.User import User
from .models.Developer import Developer
from .models.Version import Version
from .models.Executable import Executable
from .models.License import License
from .models.Review import Review
from .models.Rating import Rating


admin.site.register(User)
admin.site.register(Developer)
admin.site.register(OperatingSystem)
admin.site.register(Application)
admin.site.register(Category)
admin.site.register(Version)
admin.site.register(Executable)
admin.site.register(License)
admin.site.register(Review)
admin.site.register(Rating)
