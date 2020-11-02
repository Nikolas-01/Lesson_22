"""poetry_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from analytics import views


app_name = 'analytics'

urlpatterns = [
   path('', views.form_analytics, name='PA'),
   path('all_words_counter/', views.all_words_counted, name='word_counter'),
   path('phrase_generator/', views.view_generator, name='phrase_generator'),
   path('phrase/', views.phrase_generator, name='phrase'),

]
