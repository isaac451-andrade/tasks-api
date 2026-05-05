from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #cria o token de acesso e o de refresh
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # pega o refresh e cria o access
    path('api/v1/tasks/', include('routes.tasks.urls'))
]
