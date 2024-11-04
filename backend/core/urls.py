from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('customers.urls')),  # Adiciona o app `customers` às rotas da API
]

# Para servir arquivos estáticos
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
                          
# para as rotas serem direcionadas para o frontend react
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
