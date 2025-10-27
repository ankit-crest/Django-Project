from django.urls import path
from golls.views import delete
from . import views as memberRoute

app_name = 'members' 

urlpatterns = [
    path('', memberRoute.index, name='index'),
    path('add_members/', memberRoute.add_members, name='add_members'),
    path('create/', memberRoute.create, name='add_create'),
    path('store/', memberRoute.store, name='store'),
    path('delete/<int:id>/', memberRoute.delete, name='delete'),
    path('edit/<int:id>/', memberRoute.edit, name='edit'),
    path('update/<int:id>', memberRoute.update, name='update'),

    path('ajax_create/', memberRoute.ajax_create, name='ajax_create'),
    path('getlist/', memberRoute.getlist, name='getlist'),
    path('ajax_delete/<int:id>/', memberRoute.ajax_delete, name='ajax_delete'),
    path('ajax_edit/<int:id>/', memberRoute.ajax_edit, name='ajax_edit'),
    path('ajax_update/<int:id>/', memberRoute.ajax_update, name='ajax_update'),
    # path('store/', memberRoute.store, name='store'),
    # 
    # path('edit/<int:id>/', memberRoute.edit, name='edit'),
    # path('update/<int:id>', memberRoute.update, name='update'),
]