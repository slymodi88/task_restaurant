from django.urls import path, include


urlpatterns = [
    path('reservations/', include("tables.api.urls")),
    path('user/',include("user.api.urls")),

]