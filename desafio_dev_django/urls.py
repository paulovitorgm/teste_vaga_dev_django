from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tarefas/', include('apps.cadastro_de_tarefas.urls')),
]
