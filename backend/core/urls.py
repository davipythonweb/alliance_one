from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('customers.urls')),  # Adiciona o app `customers` às rotas da API
]

# para as rotas serem direcionadas para o frontend react
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
