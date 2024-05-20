from rest_framework import serializers
from .models import Details

class Detailsserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Details
        fields = "__all__"