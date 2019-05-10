from django.urls import path,include
from simpletodo import views
import xadmin
xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path(r'', views.todolist),
    path(r'simpletodo/',include('simpletodo.urls'))
]
