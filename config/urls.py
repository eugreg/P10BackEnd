from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from P10.views import ProdutosViewSet

router = DefaultRouter()
router.register(r"produtos", ProdutosViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]