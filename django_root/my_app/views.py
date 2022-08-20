from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404
# from django.shortcuts import render_to_response
from django.template import RequestContext
from pathlib import Path
import sys, os

import random
from json import dumps

import logging

logger = logging.getLogger(__name__)

from . import models
from . import forms
from my_app.forms import *
from my_app.models import *
# from my_app.forms import NameForm, RegistrationForm
# from my_app.models import NameModel

# Build paths inside the project like this: BASE_DIR / 'subdir'.
DJANGO_ROOT = Path(__file__).resolve().parent.parent

def index(request):
    page_title = "Dalton's Blog"
    page_heading = "Dalton's Blog"

    context = {
        'page_title': page_title,
        'page_heading': page_heading,
    }
    return render(request, 'index.html', context=context)

def four_Oh_four(request):
    page_title = "Whoops"
    page_heading = "Whoops"
    context = {
        'page_title': page_title,
        'page_heading': page_heading,
    }
    return render(request, "404.html", context=context)

def about(request):
    page_title = "About"
    page_heading = "About"

    context = {
        'page_title': page_title,
        'page_heading': page_heading,
    }
    return render(request, 'other/about.html', context=context)

def contact(request):
    page_title = "Contact"
    page_heading = "Contact"

    context = {
        'page_title': page_title,
        'page_heading': page_heading,
    }
    return render(request, 'other/contact.html', context=context)

def chat(request):
    data_list = {}
    data_list["rooms"] = []
    page_title = "RealTime Chat"
    page_heading = "RealTime Chat"
    messages = Message.objects.all()
    for message in messages:
        data_list["rooms"].append(message.room)
    
    context = {
        'page_title': page_title,
        'page_heading': page_heading,
        'rooms':data_list["rooms"]
    }
    return render(request, 'chat/lobby.html', context=context)

def chatRoom(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25]

    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages': messages})



def post(request, post_type, post_id):
    if request.method == "POST":
        print(request.POST)
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(request, id)
            print("Received Valid comment with Request method POST")
            return HttpResponseRedirect(reverse('blogpost', args=[str(id)]))
    else: 
        print(request.GET)
        form = CommentForm()
        if post_type == "articles":
            article = Article.objects.get(id=post_id) 
            category =  article.get_category()
            ancestors = category.get_ancestors()
            page_title = article.title
            page_heading = article.title
            sub_title = article.sub_title
            main_image = article.main_image.url
            article_content = article.article_content
            article_content_paragraphs = article_content.split('\n')
            sub_reqd = article.sub_reqd
            sub_image = article.sub_image
            sub_content = article.sub_content
            refs = article.references
            refLinks = refs.split('\n')
            comment_list = Comment.objects.filter(article=article)
            context = {
                'post_id': post_id,
                'page_title': page_title,
                'ancestors': ancestors,
                'object': category,
                'page_heading': page_heading,
                'sub_title': sub_title,
                'main_image': main_image,
                'article_content': article_content,
                'article_content_paragraphs': article_content_paragraphs,
                'sub_reqd': sub_reqd,
                'sub_image': sub_image,
                'sub_content': sub_content,
                'refs': refLinks,
                'comment_list': comment_list,
                'form': form,
            }
            return render(request, 'items/posts/article.html', context=context)

        elif post_type == "tutorials":
            tutorial = Tutorial.objects.get(id=post_id) 
            category =  tutorial.get_category()
            ancestors = category.get_ancestors()
            page_title = tutorial.title
            sub_title = tutorial.sub_title
            page_heading = tutorial.title
            videoURL =  tutorial.videoURL
            field_list = tutorial.fields.all()
            field_content_dict = {}
            for field in tutorial.fields.all():
                field_content_dict[field] = {}
                for content in field.content.all():
                    field_content_dict[field][content] = {}
                    image_list = []
                    for image in content.images.all():
                        image_list.append(image)
                    field_content_dict[field][content] = image_list
                    
            refs = tutorial.references
            refLinks = refs.split('\n')
            comment_list = Comment.objects.filter(tutorial=tutorial)
            context = {
                'post_id': post_id,
                'page_title': page_title,
                'sub_title': sub_title,
                'page_heading': page_heading,
                'ancestors': ancestors,
                'object': category,
                'field_list': field_list,
                'field_content_dict': field_content_dict,
                'refs': refLinks,
                'comment_list': comment_list,
                'form': form,
            }
            return render(request, 'items/posts/tutorial.html', context=context)
        
        else:
            page_title = "Whoops"
            page_heading = "Whoops"
            context = {
                'page_title': page_title,
                'page_heading': page_heading,
            }
            return render(request, "404.html", context=context)


def catree(request):
    Blogpost_list = Blogpost.objects.filter(isProject=False)
    p = Paginator(Blogpost_list, 8)  
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number) 
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {
        'page_title': "Catalog",
        'page_heading': "Blogpost Catalog",
        'page_obj': page_obj,
        'nodes': Category.objects.all()
    }
    return render(request,'catalog/catree.html', context=context)


def catalog(request, parent_id):
    data_list = {}
    data_list["categories"] = []
    cat_name = "Categories"
    if parent_id == 0:
        category = None
        parent_id = None
        ancestors = None
    else: 
        category = Category.objects.get(id=parent_id)
        cat_name = category.name
        parent_id = category.id
        ancestors=category.get_ancestors()
    category_list = Category.objects.filter(parent=parent_id)
    if category_list:
        for cat in category_list:
            cat_instance = {}
            cat_instance["id"] = cat.id
            cat_instance["title"] = cat.name
            cat_instance["image"] = cat.category_image.url
            cat_instance["desc"] = cat.cat_summary
            data_list["categories"].append(cat_instance)
            
        p = Paginator(data_list["categories"], 8)  
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number) 
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
        
        logger.debug('Do dis show up in the logs doe')
        context = {
            'page_title': cat_name,
            'page_heading': cat_name,
            'parent_id': parent_id,
            'ancestors': ancestors,
            'object': category,
            'page_obj': page_obj,
            'categories':data_list["categories"]
        }
        return render(request, 'catalog/catalog.html', context=context)
    else:   
        category = Category.objects.get(id=parent_id)
        ancestors=category.get_ancestors()
        Blogpost_list = category.post_in_cat()
        if(len(Blogpost_list) > 0):
            empty = False
        else:
            empty = True
        p = Paginator(Blogpost_list, 8)  
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number) 
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
            
        context = {
            'page_title': category.name,
            'page_heading': category.name,
            'empty': empty,
            'page_obj': page_obj,
            'ancestors': ancestors,
            'object': category
        }
        return render(request, 'catalog/posts-in-cat.html', context=context)


def searchCatalog(request):
    if request.method == "POST":
        results = False
        post_results = False
        service_results = False
        term = request.POST['searchbox']
        data_list = {}
        data_list["posts"] = []
        data_list["services"] = []
        
        post_list = list(chain(Tutorial.get_searchset(Tutorial, term), Article.get_searchset(Article, term)))
        service_list = Service.get_searchset(Service, term)
        if len(post_list) > 0 or len(service_list) > 0:
            results = True
            if len(post_list) > 0:
                post_results = True
            if len(service_list) > 0:
                service_results = True
        for post in post_list:
            post_instance = {}
            post_instance["id"] = post.id
            post_instance["title"] = post.title
            post_instance["desc"] = post.summary
            post_instance["image"] = post.item_image.url
            data_list["posts"].append(post_instance)

        for service in service_list:
            service_instance = {}
            service_instance["id"] = service.id
            service_instance["title"] = service.title
            service_instance["desc"] = service.summary
            data_list["services"].append(service_instance)
            
        context = {
            'page_title': "Search: "+ term,
            'page_heading': term,
            'post_results': post_results,
            'service_results': service_results,
            'results': results,
            'posts': post_list,
            'services': service_list,
            # 'posts': data_list["posts"],
            # 'services': data_list["services"],
        }
        return render(request, 'catalog/searchcatalog.html', context=context)
    else: 
       return HttpResponseRedirect(reverse('Blogpost', args=[str(id)]))

# def show_category(request,hierarchy= None):
#     category_slug = hierarchy.split('/')
#     parent = None
#     root = Category.objects.all()

#     for slug in category_slug[:-1]:
#         parent = root.get(parent=parent, slug = slug)

#     try:
#         instance = Category.objects.get(parent=parent,slug=category_slug[-1])
#     except:
#         instance = get_object_or_404(Blogpost, slug = category_slug[-1])
#         return render(request, "blogposts/blogpost.html", {'instance':instance})
#     else:
#         return render(request, 'catalog/categories.html', {'instance':instance})

# def nbody(request):
#     return render(request, 'nbody.html')

# def webAssembly(request):
#     page_title = "Webassembly"
#     page_heading = "Webassembly"
#     page_subheading = "Functional Webassembly Implementations"
#     page_text = "Below are the few Webassembly projects which were used to educate the developers of this site on how to use the Webassembly/Rust/Emscripten"
#     context = {
#         'page_title': page_title,
#         'page_heading': page_heading,
#         'page_subheading': page_subheading,
#         'page_text': page_text,
#     }
 
#     return render(request, "webassembly/webassembly.html", context=context)

# def webassembly(request, page):
#     page_title = "Webassembly"
#     page_heading = "Webassembly"
#     page_subheading = "Purpose"
#     context = {
#         'page_title': page_title,
#         'page_heading': page_heading,
#         'page_subheading': page_subheading,
#     }
#     url = 'webassembly/' + page + '.html'
 
#     return render(request, url, context=context)
# def registration_view(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/login/")
#     else:
#         form = RegistrationForm()
#     context = {
#         "title": "Register",
#         "form": form,
#     }
#     return render(request, "registration/registration.html", context=context)

# def pagination(request):

#     Blogpost_list = Blogpost.objects.all()
#     p = Paginator(Blogpost_list, 8)  
#     page_number = request.GET.get('page')
#     try:
#         page_obj = p.get_page(page_number) 
#     except PageNotAnInteger:
#         page_obj = p.page(1)
#     except EmptyPage:
#         page_obj = p.page(p.num_pages)
#     context = {
#         'page_title': "Catalog",
#         'page_heading': "Catalog",
#         'page_obj': page_obj
#     }
#     return render(request, 'catalogs/pagination.html', context=context)




# def category(request,hierarchy= None):
#     category_slug = hierarchy.split('/')
#     parent = None
#     root = Category.objects.all()

#     for slug in category_slug[:-1]:
#         parent = root.get(parent=parent, slug = slug)

#     try:
#         instance = Category.objects.get(parent=parent,slug=category_slug[-1])
#     except:
#         instance = get_object_or_404(Post, slug = category_slug[-1])
#         return render(request, "postDetail.html", {'instance':instance})
#     else:
#         return render(request, 'categories.html', {'instance':instance})







# def categoryCatalogView(request, catid):
#     data_list = {}
#     data_list["Blogposts"] = []
#     category = Category.objects.get(id=catid)
#     Blogpost_list = Blogpost.objects.filter(category=catid, approved=True)
#     p = Paginator(Blogpost_list, 8)  
#     page_number = request.GET.get('page')
#     try:
#         page_obj = p.get_page(page_number) 
#     except PageNotAnInteger:
#         page_obj = p.page(1)
#     except EmptyPage:
#         page_obj = p.page(p.num_pages)
#     context = {
#         'page_title': category.name+ " Catalog",
#         'page_heading': category.name+" Catalog",
#         'page_obj': page_obj
#     }
#     return render(request, 'catalogs/catalog.html', context=context)

# @login_required
# def leave_comment(request, id):
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form.save(request, id)
#             print("Received Valid comment with Request method POST")
#             return HttpResponseRedirect(reverse('rabbithole', args=[str(id)]))
#     else:
#         print("Received Comment with Request method GET")
#         form = CommentForm()
#     context = {
#         "form": form,
#         "hole_id":id,
#     }
#     return render(request, "forms/comment.html", context=context)



# @login_required
# def LikeView(request, id): 
#     rabbit_hole = Rabbithole.objects.get(id=id) 
#     if Like.objects.filter(user=request.user, rabbithole=rabbit_hole).exists():
#         Like.objects.filter(user=request.user, rabbithole=rabbit_hole).delete()
#     else: 
#         new_like, created = Like.objects.get_or_create(user=request.user, rabbithole=rabbit_hole)
#         Dislike.objects.filter(user=request.user, rabbithole=rabbit_hole).delete()
        
#     return HttpResponseRedirect(reverse('rabbithole', args=[str(id)]))

# @login_required
# def DisLikeView(request, id): 
#     rabbit_hole = Rabbithole.objects.get(id=id) 
#     if Dislike.objects.filter(user=request.user, rabbithole=rabbit_hole).exists():
#         Dislike.objects.filter(user=request.user, rabbithole=rabbit_hole).delete()
#     else: 
#         new_dislike, created = Dislike.objects.get_or_create(user=request.user, rabbithole=rabbit_hole)
#         Like.objects.filter(user=request.user, rabbithole=rabbit_hole).delete()

#     return HttpResponseRedirect(reverse('rabbithole', args=[str(id)]))

# @login_required
# def save_to_profile(request, id): 
#     rabbit_hole = Rabbithole.objects.get(id=id) 
#     if SavetoProfile.objects.filter(user=request.user, rabbithole=rabbit_hole).exists():
#         SavetoProfile.objects.filter(user=request.user, rabbithole=rabbit_hole).delete()
#     else:
#         new_save, created = SavetoProfile.objects.get_or_create(user=request.user, rabbithole=rabbit_hole)
        
#     return HttpResponseRedirect(reverse('rabbithole', args=[str(id)]))


# @login_required
# def submit_rabbithole(request):
#     if request.method == "POST":
#         form = RabbitholeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save(request)
#             return HttpResponseRedirect('')
#     else:
#         form = RabbitholeForm()
#     context = {
#         "form": form,
#     }
#     return render(request, "forms/rholesubmit.html", context=context)

# def rabbithole(request, hole_id):
#     if request.method == "POST":
#         print(request.POST)
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form.save(request, id)
#             print("Received Valid comment with Request method POST")
#             return HttpResponseRedirect(reverse('rabbithole', args=[str(id)]))
#     else: 
#         print(request.GET)
#         form = CommentForm()
#         rabbithole = Rabbithole.objects.get(id=hole_id) 
#         page_title = rabbithole.title
#         page_heading = rabbithole.title
#         intro = rabbithole.introduction
#         desc = rabbithole.description
#         media0 = rabbithole.s_media0.url
#         media1 = rabbithole.s_media1.url
#         media2 = rabbithole.s_media2.url
#         media3 = rabbithole.s_media3.url
#         media4 = rabbithole.s_media4.url
#         media5 = rabbithole.s_media5.url
#         refs = rabbithole.references
#         portfolio_image = rabbithole.p_media.url
#         portfolio_text = rabbithole.p_description
#         like_count = Rabbithole.like_count(hole_id)

#         refLinks = refs.split('\n')


#         profile_saved = False
#         user_liked = False
#         user_disliked = False
#         if request.user.is_authenticated:
#             if SavetoProfile.objects.filter(user=request.user, rabbithole=rabbithole).exists():
#                 profile_saved = True
#             if Like.objects.filter(user=request.user, rabbithole=rabbithole).exists():
#                 user_liked = True
#                 user_disliked = False
#             elif Dislike.objects.filter(user=request.user, rabbithole=rabbithole).exists():
#                 user_liked = False
#                 user_disliked = True
#             else:
#                 user_liked = False
#                 user_disliked = False
#         comment_list = Comment.objects.filter(rabbithole=rabbithole)
        
#         context = {
#             'hole_id': hole_id,
#             'page_title': page_title,
#             'page_heading': page_heading,
#             'intro': intro,
#             'desc': desc,
#             'media0': media0,
#             'media1': media1,
#             'media2': media2,
#             'media3': media3,
#             'media4': media4,
#             'media5': media5,
#             'refs': refLinks,
#             'portfolio_text': portfolio_text,
#             'portfolio_image': portfolio_image,
#             'likes': like_count,
#             'user_liked': user_liked,
#             'user_disliked': user_disliked, 
#             'profile_saved': profile_saved,
#             'comment_list': comment_list,
#             'form': form,
#         }
        
#     return render(request, 'rabbitholes/rabbithole.html', context=context)


# @login_required
# def profile(request):
#     if UserInfo.objects.filter(user=request.user).exists():
#         user_info = UserInfo.objects.get(user=request.user) 
#     else: 
#         UserInfo.objects.create(user=request.user)
#         user_info = UserInfo.objects.get(user=request.user)
#     saved_Blogposts = SavetoProfile.objects.filter(user=request.user) 
#     data_list = {}
#     data_list["Blogposts"] = []
    
#     for saved in saved_Blogposts:
#         hole_instance = {}
#         hole_instance["id"] = saved.Blogpost.id
#         hole_instance["title"] = saved.Blogpost.title
#         hole_instance["image"] = saved.Blogpost.p_media.url
#         hole_instance["desc"] = saved.Blogpost.summary
#         data_list["Blogposts"].append(hole_instance)
        
#     page_title = request.user.username + "'s Profile"
#     page_heading = request.user.username + "'s Profile"
#     page_subheading =  request.user.username
#     page_text = "WIP"
#     context = {
#         'page_title': page_title,
#         'page_heading': page_heading,
#         'page_subheading': page_subheading,
#         'page_text': page_text,
#         'profile_picture': user_info.profile_image.url,
#         'Blogposts':data_list["Blogposts"],
#     }
#     return render(request, 'registration/profile.html', context=context)

# def edit_profile_view(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/accounts/profile/")
#     else:
#         form = UserForm()
#     context = {
#         "title": "Edit Profile",
#         "form": form,
#     }
#     return render(request, "registration/edit_profile.html", context=context)



# def logout_view(request):
#     logout(request)
#     return redirect("/login/")