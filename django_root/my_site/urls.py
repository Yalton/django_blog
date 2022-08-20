"""hello_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from my_app import views
# from my_app.views import ItemsByCategoryView, CategoryListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="homepage"), 
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('404/', views.four_Oh_four),
    # path('nbody/', views.nbody),
    path('chat/', views.chat, name='chat'),
    path('chat/<str:room_name>/', views.chatRoom, name='chatRoom'),
    path('post/<str:post_type>/<int:post_id>/', views.post, name="post"),
    path('search/', views.searchCatalog, name="search"),


    path('catree/', views.catree, name="catree"),

    path('catalog/<int:parent_id>/', views.catalog, name="catalog"),
    # path('show_category/<hierarchy>/', views.show_category, name="show_category"),
    # path('webassembly/', views.webAssembly, name="webassembly"),
    # path('webassembly/<str:page>/', views.webassembly, name="webassembly"),
    # path('catalog/', CategoryListView.as_view() , name='category-list'),
    # path('catalog/<str:slug>/', ItemsByCategoryView.as_view() , name='category-detail'),
    # path('pagination/', views.pagination, name="pagination"),
    
    # path('categoryCatalog/', CategoryListView.as_view() , name='category-list'),
    # path('categoryCatalog/<str:slug>/', ItemsByCategoryView.as_view() , name='category-detail'),
    # path('categoryCatalog/', views.categoryCatalog, name="categoryCatalog"),
    

    
    # path('rabbithole/<int:hole_id>/', views.rabbithole, name="rabbithole"),
    # path('like/<int:id>/', views.LikeView, name="like"),
    # path('dislike/<int:id>/', views.DisLikeView, name="dislike"),
    # path('profilesave/<int:id>/', views.save_to_profile, name="save_to_profile"),
    # path('comment/<int:id>/', views.leave_comment, name="commnent"),
    # path('submit/', views.submit_rabbithole, name="submit"),
    # path('editProfile/', views.edit_profile_view, name="editprofile"),
    # path('accounts/profile/',views.profile, name="profile"),
    # path('accounts/profile/edit/', views.edit_profile_view, name="editprofile"), 
    # path('login/', auth_views.LoginView.as_view()),
    # path('register/', views.registration_view),
    # path('logout/', views.logout_view),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
