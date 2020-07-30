from rest_framework import serializers
from gustavo.models import Gordinho


class GordinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gordinho
        fields = "__all__"
