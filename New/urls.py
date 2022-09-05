from django.urls import path
from New import views


urlpatterns = [
    path('' , views.index, name="index"),
    path('aboutus.html/', views.aboutus, name="aboutus"),
    path('Contactus/', views.Contactus, name="Contactus"),
    path('health.html/',views.health,name="healthfile"),
    path('entertainment.html/',views.entertainment,name="Entertainment"),
    path('sports.html/',views.sports,name="sports"),
    path('weather.html/',views.weather,name="weather"),
    path('crime.html/',views.crime,name="crime"),
    path('nature.html/',views.nature,name="nature"),
]
