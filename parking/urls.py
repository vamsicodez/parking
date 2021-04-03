from django.conf.urls import url

urlpatterns = [
    
    url(r'^park/([a-zA-Z0-9]+)/',   'carparking.views.park', name = 'park'),
    url(r'^unpark/([a-zA-Z0-9]+)/', 'carparking.views.unpark', name = 'unpark'),
    url(r'^info/',   'carparking.views.getInfo', name = 'getInfo'),
]
