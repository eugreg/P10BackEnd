from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router
from usuario.router import router as usuario_router
from rest_framework.routers import DefaultRouter

from P10.views import ProdutosViewSet, FornecedorViewSet, CategoriaViewSet, DescontoViewSet, SubCategoriaViewSet

router = DefaultRouter()
router.register(r"produtos", ProdutosViewSet)
router.register(r"fornecedor", FornecedorViewSet)
router.register(r"categoria", CategoriaViewSet)
router.register(r"descontos", DescontoViewSet)
router.register(r"subcategoria", SubCategoriaViewSet)

urlpatterns = [
    path("api/media/", include(uploader_router.urls)),
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
