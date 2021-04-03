from django.conf.urls import url

urlpatterns = [
    
    url(r'^park/(.*)/',   'carparking.views.park', name = 'park'),
    url(r'^unpark/(.*)/', 'carparking.views.unpark', name = 'unpark'),
    url(r'^info/',   'carparking.views.getInfo', name = 'getInfo'),
]
