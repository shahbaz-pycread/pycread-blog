from django.urls import path
#from . import views
from .views import LikeView,CategoryView, CategoryListView,HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, AddCommentView # class based views,  


urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'), # pk = primary key # class based view
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),  # class based view
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),  # class based view
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/',CategoryView, name='category'),
    path('category-list/',CategoryListView, name='category-list'),
    path('like/<int:pk>/', LikeView, name='like_post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),

]
