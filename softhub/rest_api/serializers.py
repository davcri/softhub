from rest_framework.serializers import ModelSerializer

from softhub.models.OperatingSystem import OperatingSystem
from softhub.models.Application import Application
from softhub.models.Executable import Executable
from softhub.models.Developer import Developer
from softhub.models.Version import Version


class OperatingSystemSerializer(ModelSerializer):
    class Meta:
        model = OperatingSystem
        #fields = ('name', 'release_date', 'family')
        fields = '__all__'


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class VersionSerializer(ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'


class ExecutableSerializer(ModelSerializer):
    class Meta:
        model = Executable
        fields = '__all__'


class DeveloperSerializer(ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'
