from app import views
from django.urls import include, path

# TEMPLATE TAGGING
app_name = 'app'

urlpatterns = [
    path('rel_url_templates/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
    path('test/',views.test,name='test')
]
