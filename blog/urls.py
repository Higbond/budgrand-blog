from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contacts', views.contacts, name='contacts'),
    path('blog', views.ShowBlogView.as_view(), name='blog'),
    path('blog/add', views.CreateBlogView.as_view(), name='blog-add'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='news'),
    path('blog/<int:pk>/update', views.UpdateBlogView.as_view(), name='news-update'),
    path('blog/<int:pk>/delete', views.DeleteBlogView.as_view(), name='news-delete'),

]
