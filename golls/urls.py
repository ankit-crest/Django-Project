from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('show/<slug>/', views.show, name='show'),
    path('list/', views.show_list, name='list'),
    path('add_gls/', views.add_gls, name='add_gls'),
    path('edit/<str:id>/', views.edit, name='edit'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('textInput/', views.textInput, name='textInput'),
    path('speak_text/', views.speak_text, name='speak_text'),
    path('voice_speak/', views.voice_speak_view, name='voice_speak'),
    path('voice_page/', views.voice_page, name='voice_page'),
    path('process_audio/', views.process_audio, name='process_audio'),

]