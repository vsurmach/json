from django.urls import path

from getuser.views import get_user, get_detail_user, delete_users

app_name = 'getuser'

urlpatterns = [
    path('', get_user, name='get_persons'),
    path('delete/', delete_users, name='delete_persons'),
    path('/<int:id>/', get_detail_user, name='get_detail_person'),
]