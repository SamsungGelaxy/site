


from django.urls import path, register_converter
from . import views as v
from django.contrib.auth import views
app_name="blog"



urlpatterns = [
    path('tag/<slug:tag_slug>/', v.post_list, name="tag"),

    path('', v.post_list, name="post_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', v.post_detail, name="post_detail"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('profile/', v.profile, name="profile"),
    path('add_post/', v.add_post, name="add_post"),
    path('edit_post/<int:post_id>/', v.edit_post, name="edit_post"),
    path('del_post/<int:post_id>/', v.del_post, name="del_post"),
    path('post_point_list/<int:post_id>/', v.post_point_list, name="post_point_list"),
    path('post_point_add/<int:post_id>/', v.post_point_add, name="post_point_add"),
    path('post_point_del/<int:id>/', v.del_post_point, name="post_point_del"),
    path('post_point_edit/<int:id>/', v.edit_post_point, name="post_point_edit"),
]
