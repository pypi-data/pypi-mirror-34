from django.urls import path
from django.views.generic.base import RedirectView
from edc_action_item.admin_site import edc_action_item_admin

app_name = 'edc_action_item'

urlpatterns = [
    path('admin/', edc_action_item_admin.urls),
    path('', RedirectView.as_view(url='admin/edc_action_item/'), name='home_url'),
]
