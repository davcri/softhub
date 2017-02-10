from rest_framework import viewsets, generics

from softhub.models.OperatingSystem import OperatingSystem
from softhub.models.Application import Application
from softhub.models.Executable import Executable
from softhub.models.Developer import Developer
from softhub.models.Version import Version

from .serializers import OperatingSystemSerializer, ApplicationSerializer
from .serializers import VersionSerializer, ExecutableSerializer
from .serializers import DeveloperSerializer


class OperatingSystemViewSet(viewsets.ModelViewSet):
    queryset = OperatingSystem.objects.all()
    serializer_class = OperatingSystemSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer


class ExecutableViewSet(viewsets.ModelViewSet):
    queryset = Executable.objects.all()
    serializer_class = ExecutableSerializer


class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
