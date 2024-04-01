from rest_framework import serializers
from .models.crafts import Craft


class CraftSerializer(serializers.ModelSerializer):
    # craftsman = serializers.SerializerMethodField()

    class Meta:
        model = Craft
        fields = '__all__'

    # def get_craftsman(self, obj):
    #     craftsman_info = obj.craftsman
    #     return {'id': craftsman_info.id, 'username': craftsman_info.username}
