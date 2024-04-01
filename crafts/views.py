from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models.crafts import Craft
from .permissions import IsAdminOrCraftsman
from .serializers import CraftSerializer


class CraftListCreate(generics.ListCreateAPIView):
    serializer_class = CraftSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Craft.objects.all()
        craftsman_id = self.kwargs.get('craftsman_id')

        if craftsman_id is not None:
            queryset = Craft.objects.filter(craftsman=craftsman_id)
        return queryset

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return super().get_permissions()


class CraftDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = CraftSerializer
    permission_classes = (IsAdminOrCraftsman,)

    def get_queryset(self):
        craft_id = self.kwargs.get('id')
        craft = Craft.objects.filter(id=craft_id)

        if not craft:
            raise Http404()
        return craft
