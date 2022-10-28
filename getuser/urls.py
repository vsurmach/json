from django.urls import path

from getuser.views import get_user, get_detail_user, delete_users, get_posts, get_comments

app_name = 'getuser'

urlpatterns = [
    path('', get_user, name='get_persons'),
    path('delete/', delete_users, name='delete_persons'),
    path('get_user/<int:id>/', get_detail_user, name='get_detail_person'),
    path('get_posts/<int:id>/', get_posts, name='get_posts'),
    path('get_comments/<int:id>', get_comments, name='get_comments'),
]