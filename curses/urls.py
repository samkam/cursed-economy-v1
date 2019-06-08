from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:curse_id>/', views.get_curse, name="get_curse"),
    path('all/',views.get_all_curses, name="get_all_curses"),
    path('my_curses', views.user_curses,name="user_curses"),
    path('submit_curse', views.submit_curse,name="submit_curse")
    #post result for getting vote numbers
]