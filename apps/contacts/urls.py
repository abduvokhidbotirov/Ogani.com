from django.urls import path

from apps.contacts.views import contact_view

app_name = 'contact'

urlpatterns = [
    path('', contact_view, name='contact')
]