from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router
from usuario.router import router as usuario_router

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from P10.views import ProdutosViewSet, FornecedorViewSet, CategoriaViewSet, DescontoViewSet, SubCategoriaViewSet, SazonalViewSet, CompraViewSet, MarcaViewSet, TagViewSet

router = DefaultRouter()
router.register(r"produtos", ProdutosViewSet)
router.register(r"compras", CompraViewSet)
router.register(r"sazonal", SazonalViewSet)
router.register(r"marca", MarcaViewSet)
router.register(r"fornecedores", FornecedorViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"descontos", DescontoViewSet)
router.register(r"tag", TagViewSet)
router.register(r"subcategorias", SubCategoriaViewSet)

urlpatterns = [
    path("api/media/", include(uploader_router.urls)),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
