
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    # path('delete/<int:taskid>/',views.delete,name='delete'),
    # path('update/<int:id>/',views.update,name='update'),
    path('Taskview/',views.Taskview.as_view(),name='Taskview'),
    path('Detailsview/<int:pk>/',views.Detailslview.as_view(),name='DetailsView'),
    path('Updateview/<int:pk>/',views.Updateview.as_view(),name='UpdateView'),
    path('Deleteview/<int:pk>/',views.Deleteview.as_view(),name='DeleteView')
]
