"""firstprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from firstprj import views
from django.conf import settings           # img
from django.conf.urls.static import static # img

urlpatterns = [
    path('myadmin/', admin.site.urls), # can change name
    # path('', views.home),              # '' means main page
    # path('aboutus/', views.aboutus),   # myadmin/aboutus
    # path('course/', views.course),     # myadmin/course
    # path('course/<courseid>', views.coursdetails), # myadmin/course/dynamic
    
    path('', views.main1,name='home'),
    path('about/', views.main2),
    path('prime/', views.main3),
    path('calculator/', views.main4,name='main4'),
    path('marksheet/', views.main5,name='main5'),
    path('contact/', views.main6,name='main6'),
    # path('news/<urlid>', views.news),
    path('news/<slug>', views.news),
    path('userform/', views.saveform,name='saveform'),
    # path('actionform/', views.submitform,name='actionform'),
]

# img

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)