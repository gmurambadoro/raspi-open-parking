from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'gates', views.GateViewSet, basename='gates')
router.register(r'movements', views.MovementViewSet, basename='movements')
router.register(r'products', views.ProductViewSet, basename='products')

urlpatterns = router.urls
