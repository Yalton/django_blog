from decimal import DefaultContext
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User as auth_user
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify

class NameModel(models.Model):
    your_name = models.CharField(max_length=100)
    def __str__(self):
        return "%s"%(
            self.your_name
        )
class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category_image = models.ImageField(upload_to='uploads/categories/%Y/%m/%d/', null=True)
    cat_summary = models.CharField(max_length=300)
    description = models.TextField()
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
    )
    class MPTTMeta:
        order_insertion_by = ['name']

    # class Meta:
    #     unique_together = ('slug', 'parent',)    
    #     verbose_name_plural = "categories"   
        
    def blog_in_cat(self):
        return Blogpost.objects.filter(category=self)
        
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
        return reverse('blogs-by-category', args=[str(self.slug)])
    
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


    
class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=300, default="NULL")
    field1_title = models.CharField(max_length=100, default="NULL")
    field1_content = models.TextField(default="NULL")
    f1_m0 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/', null=True)
    f1_m1 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f1_m2 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f1_m3 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f1_m4 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f1_m5 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    field2_title = models.CharField(max_length=100, default="NULL")
    field2_content = models.TextField(default="NULL")
    f2_m0 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/', null=True)
    f2_m1 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f2_m2 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f2_m3 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f2_m4 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f2_m5 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    field3_title = models.CharField(max_length=100, default="NULL")
    field3_content = models.TextField(default="NULL")
    f3_m0 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/', null=True)
    f3_m1 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f3_m2 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f3_m3 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f3_m4 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f3_m5 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    field4_title = models.CharField(max_length=100, default="NULL")
    field4_content = models.TextField(default="NULL")
    f4_m0 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/', null=True)
    f4_m1 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f4_m2 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f4_m3 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f4_m4 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f4_m5 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    field5_title = models.CharField(max_length=100, default="NULL")
    field5_content = models.TextField(default="NULL")
    f5_m0 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/', null=True)
    f5_m1 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f5_m2 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f5_m3 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f5_m4 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    f5_m5 = models.ImageField(upload_to='uploads/posts/%Y/%m/%d/',null=True)
    references = models.TextField(default="NULL")
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,null=True,blank=True, on_delete=models.CASCADE)
    isProject = models.BooleanField(default=False)
    slug = models.SlugField(
      max_length=100,
    )
    def __str__(self):
         return self.title
    def get_searchset(self, term):
        return self.objects.filter( Q(title__icontains=term) | Q(summary__icontains=term) | Q(field1_title__icontains=term)| Q(field1_content__icontains=term)| Q(field2_title__icontains=term)| Q(field2_content__icontains=term)| Q(field3_title__icontains=term)| Q(field3_content__icontains=term)| Q(field4_title__icontains=term)| Q(field4_content__icontains=term)| Q(field5_title__icontains=term)| Q(field5_content__icontains=term))
    def get_absolute_url(self):
        kwargs = {
        'slug': self.slug
        }
        return reverse('blog-detail', kwargs=kwargs)
    
    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):
        comment = models.CharField(max_length=240)
        author = models.ForeignKey( auth_user, on_delete=models.CASCADE,null=True)
        blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
        created_on = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.author.username + " " + self.comment

class Message(models.Model):
    author = models.ForeignKey( auth_user, on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
     
      


# class Blogpost(models.Model):
#     title = models.CharField(max_length=100)
#     summary = models.CharField(max_length=300, default="NULL")
#     introduction = models.TextField(default="NULL")
#     description = models.TextField(default="NULL")
#     s_media0 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/', null=True)
#     s_media1 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/',null=True)
#     s_media2 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/',null=True)
#     s_media3 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/',null=True)
#     s_media4 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/',null=True)
#     s_media5 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/',null=True)
#     references = models.TextField(default="NULL")
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