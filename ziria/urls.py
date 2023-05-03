from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/admin/<str:store_slug>/", include("ziria.api.admin.urls")),
]
