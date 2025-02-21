from django.contrib import admin
from django.urls import path
from blog.views import home, tree_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home Page URL
    path('blog/', tree_list, name='tree_list'),  # Blog Page URL
]
