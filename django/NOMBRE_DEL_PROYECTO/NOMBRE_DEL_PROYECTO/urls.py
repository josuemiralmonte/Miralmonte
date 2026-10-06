"""
URL configuration for NOMBRE_DEL_PROYECTO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,  include #step 14 adds include
#Step 2 importing the logic of the file views 
from . import views

#In step 2, this homepage has to be defined to have access to it, in order to do that, we set up URL routing in 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),

    #step 14 adds this path
    path('escaparate/', include('escaparate.urls')),  
]  



