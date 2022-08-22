from decimal import DefaultContext
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User as auth_user
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from itertools import chain
from embed_video.fields  import  EmbedVideoField


class NameModel(models.Model):
    your_name = models.CharField(max_length=100)
    def __str__(self):
        return "%s"%(self.your_name)


class PersonalData(models.Model):
    name = models.CharField(max_length=100, null=True,blank=True,)
    # resume = models.FileField(upload_to='uploads/personaldata/resume/%Y/%m/%d/', null=True,blank=True)
    resume = models.FileField(upload_to='static/personaldata/resumes/%Y/%m/%d/', null=True,blank=True)
    def __str__(self):
        return "%s"%(self.name)

class Category(MPTTModel):
    name = models.CharField(max_length=100, null=True,blank=True,)
    slug = models.SlugField(unique=True, null=True,blank=True,)
    category_image = models.ImageField(upload_to='uploads/categories/%Y/%m/%d/', null=True)
    cat_summary = models.CharField(max_length=300, null=True,blank=True,)
    description = models.TextField()
    parent = TreeForeignKey('self',blank=True,null=True,related_name='child', on_delete=models.CASCADE)
    show_in_posts = models.BooleanField(default=False)
    show_in_services = models.BooleanField(default=False)
    class MPTTMeta:
        order_insertion_by = ['name']
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"   

    def item_in_cat(self):
        return Item.objects.filter(category=self)
    def post_in_cat(self):
         return list(chain(Tutorial.objects.filter(category=self), Article.objects.filter(category=self)))
    def serv_in_cat(self):
         return Service.objects.filter(category=self)

    def hasParent(self, givenParent):                           
        if self.parent.name == givenParent:
            return True
        else: 
            return False

    def getParentId(self):
        if(self.parent is not None):
            return self.parent.id
        else:
            return 0
   
    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])
    
    def get_absolute_url(self):
        return reverse('catalog', args=[str(self.slug)])
    
    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [ i.slug for i in ancestors]
        slugs = []
        for i in range(len(ancestors)):
         slugs.append('/'.join(ancestors[:i+1]))
        return slugs


    


class Item(models.Model):
    title = models.CharField(max_length=100, null=True,blank=True,)
    summary = models.CharField(max_length=300,  null=True,blank=True,)
    item_image = models.ImageField(upload_to='uploads/items/%Y/%m/%d/', null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True,blank=True,)
    category = models.ForeignKey(Category,null=True,blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100,null=True)
    class Meta:
        abstract = True
        ordering = ['-created_on']
    
    def __str__(self):
         return self.title
    def get_searchset(self, term):
        return self.objects.filter( Q(title__icontains=term) | Q(summary__icontains=term) | Q(field1_title__icontains=term)| Q(field1_content__icontains=term)| Q(field2_title__icontains=term)| Q(field2_content__icontains=term)| Q(field3_title__icontains=term)| Q(field3_content__icontains=term)| Q(field4_title__icontains=term)| Q(field4_content__icontains=term)| Q(field5_title__icontains=term)| Q(field5_content__icontains=term))
    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('item-detail', kwargs=kwargs)
    


class Post(Item):
    sub_title = models.TextField( null=True,blank=True,)
    references = models.TextField(null=True,blank=True,)
    class Meta:
        abstract = True

class Service(Item):
    link = models.URLField(max_length=200, null=True,blank=True,)
    def get_searchset(self, term):
        return self.objects.filter( Q(title__icontains=term) | Q(summary__icontains=term) | Q(link__icontains=term))
    def __str__(self):
        return self.title


class Notes(Post):
    notes = models.FileField(upload_to='uploads/notes/videos/%Y/%m/%d/', null=True,blank=True)
    def get_searchset(self, term):
         return self.objects.filter( Q(title__icontains=term) | Q(summary__icontains=term) )
    def get_category(self):
        return self.category
    def is_article(self):
        return False
    def is_tutorial(self):
        return False
    def __str__(self):
        return self.title
    def post_type(self):
        return "notes"

class Article(Post):
    main_image = models.ImageField(upload_to='uploads/articles/%Y/%m/%d/', null=True,blank=True,)
    article_content = models.TextField( null=True,blank=True,)
    sub_reqd = models.BooleanField(default=False)
    sub_image = models.ImageField(upload_to='uploads/articles/sub_images/%Y/%m/%d/', null=True,blank=True,)
    sub_content = models.TextField( null=True,blank=True,)
    def get_searchset(self, term):
        return self.objects.filter( Q(title__icontains=term) | Q(summary__icontains=term)  | Q(article_content__icontains=term)| Q(sub_content__icontains=term))
    def get_category(self):
        return self.category
    def post_type(self):
        return "articles"
    def is_article(self):
        return True
    def is_tutorial(self):
        return False
    def __str__(self):
        return self.title

class Tutorial(Post):
    # video = models.FileField(upload_to='uploads/tutorials/videos/%Y/%m/%d/'null=True,blank=True)
    video = models.FileField(upload_to='uploads/tutorials/videos/%Y/%m/%d/', null=True,blank=True)
    def get_searchset(self, term):
         return self.objects.filter( Q(title__icontains=term) | Q(summary__icontains=term) )
    def get_category(self):
        return self.category
    def is_article(self):
        return False
    def is_tutorial(self):
        return True
    def __str__(self):
        return self.title
    def post_type(self):
        return "tutorials"
    
class TutorialField(models.Model):
    tutorial = models.ForeignKey(Tutorial, related_name='fields', null=True,blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True,blank=True,)
    def __str__(self):
        return self.title


class TutorialFieldContent(models.Model):
    field = models.ForeignKey(TutorialField, related_name='content', null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True,blank=True,)
    content = models.TextField( null=True,blank=True,)
    def __str__(self):
        return self.name


class TutorialFieldContentMedia(models.Model):
    field_content = models.ForeignKey(TutorialFieldContent, related_name='images', null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True,blank=True,)
    media = models.ImageField(upload_to='uploads/tutorials/fieldmedia/%Y/%m/%d/', null=True,blank=True,)
    def __str__(self):
        return self.name

class Comment(models.Model):
    comment = models.CharField(max_length=240, null=True,blank=True,)
    author = models.CharField(max_length=240, null=True,blank=True,)
    article = models.ForeignKey(Article, null=True,blank=True, on_delete=models.CASCADE)
    tutorial = models.ForeignKey(Tutorial, null=True,blank=True, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username + " " + self.comment

class Message(models.Model):
    author = models.ForeignKey( auth_user, on_delete=models.CASCADE, null=True,blank=True,)
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
    
    def __str__(self):
        return self.username + " : " + self.content

    


# class Blogpost(models.Model):
#     title = models.CharField(max_length=100)
#     summary = models.CharField(max_length=300, null=True,blank=True,)
#     field1_title = models.CharField(max_length=100, null=True,blank=True,)
#     field1_content = models.TextField( null=True,blank=True,)
#     f1_m0 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/', null=True)
#     f1_m1 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f1_m2 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f1_m3 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f1_m4 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f1_m5 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     field2_title = models.CharField(max_length=100, null=True,blank=True,)
#     field2_content = models.TextField( null=True,blank=True,)
#     f2_m0 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/', null=True)
#     f2_m1 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f2_m2 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f2_m3 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f2_m4 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f2_m5 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     field3_title = models.CharField(max_length=100, null=True,blank=True,)
#     field3_content = models.TextField( null=True,blank=True,)
#     f3_m0 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/', null=True)
#     f3_m1 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f3_m2 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f3_m3 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f3_m4 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f3_m5 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     field4_title = models.CharField(max_length=100, null=True,blank=True,)
#     field4_content = models.TextField( null=True,blank=True,)
#     f4_m0 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/', null=True)
#     f4_m1 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f4_m2 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f4_m3 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f4_m4 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f4_m5 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     field5_title = models.CharField(max_length=100, null=True,blank=True,)
#     field5_content = models.TextField( null=True,blank=True,)
#     f5_m0 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/', null=True)
#     f5_m1 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f5_m2 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f5_m3 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f5_m4 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     f5_m5 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
#     references = models.TextField( null=True,blank=True,)
#     created_on = models.DateTimeField(auto_now_add=True)
#     category = models.ForeignKey(Category,null=True,blank=True, on_delete=models.CASCADE)
#     isProject = models.BooleanField(default=False)
#     slug = models.SlugField(max_length=100,null=True)
#     def __str__(self):
#          return self.title
#     def get_searchset(self, term):
#         return self.objects.filter( Q(title__icontains=term) | Q(summary__icontains=term) | Q(field1_title__icontains=term)| Q(field1_content__icontains=term)| Q(field2_title__icontains=term)| Q(field2_content__icontains=term)| Q(field3_title__icontains=term)| Q(field3_content__icontains=term)| Q(field4_title__icontains=term)| Q(field4_content__icontains=term)| Q(field5_title__icontains=term)| Q(field5_content__icontains=term))
#     def get_absolute_url(self):
#         kwargs = {
#         'slug': self.slug
#         }
#         return reverse('blog-detail', kwargs=kwargs)
    
#     class Meta:
#         ordering = ['-created_on']



# class Blogpost(models.Model):
#     title = models.CharField(max_length=100)
#     summary = models.CharField(max_length=300, null=True,blank=True,)
#     introduction = models.TextField( null=True,blank=True,)
#     description = models.TextField( null=True,blank=True,)
#     s_media0 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/', null=True)
#     s_media1 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/',null=True)
#     s_media2 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/',null=True)
#     s_media3 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/',null=True)
#     s_media4 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/',null=True)
#     s_media5 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/',null=True)
#     references = models.TextField( null=True,blank=True,)
#     created_on = models.DateTimeField(auto_now_add=True)
#     category = models.ForeignKey(Category,null=True,blank=True, on_delete=models.CASCADE)
#     isProject = models.BooleanField(default=False)
#     slug = models.SlugField(
#       max_length=100,
#     )
#     def __str__(self):
#          return self.title
#     def get_searchset(self, term):
#         return self.objects.filter( Q(title__icontains=term) | Q(summary__icontains=term) | Q(description__icontains=term)| Q(introduction__icontains=term))
#     def get_absolute_url(self):
#         kwargs = {
#         'slug': self.slug
#         }
#         return reverse('blog-detail', kwargs=kwargs)
    
#     class Meta:
#         ordering = ['-created_on']