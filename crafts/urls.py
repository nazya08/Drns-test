from django.urls import path
from .views import CraftListCreate, CraftDetail

app_name = 'crafts'

urlpatterns = [
    path('', CraftListCreate.as_view(), name='craft-list-create'),
    path('craftsman/<int:craftsman_id>/', CraftListCreate.as_view(), name='craft-list-for-craftsman'),
    path('<int:id>/', CraftDetail.as_view(), name='craft-detail'),
]
