from django.urls import path
from .views import lead_list, lead_detail, lead_create, lead_update, lead_delete, LeadDeleteView, LeadCreateView

app_name = "leads"

urlpatterns = [
    path('', lead_list, name='lead-list' ),
    path('<int:pk>/', lead_detail , name='lead-detail'),
    path('<int:pk>/update/', lead_update , name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view() , name='lead-delete'),
    path('create/', LeadCreateView.as_view() , name='lead-create')
]