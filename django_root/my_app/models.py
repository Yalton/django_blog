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
    class Meta:
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"   
        
    def blog_in_cat(self):
        return Blogpost.objects.filter(category=self)
        
    def hasParent(self, givenParent):                           
        if self.parent.name == givenParent:
            return True
        else: 
            return False

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
    introduction = models.TextField(default="NULL")
    description = models.TextField(default="NULL")
    s_media0 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/', null=True)
    s_media1 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/',null=True)
    s_media2 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/',null=True)
    s_media3 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/',null=True)
    s_media4 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/',null=True)
    s_media5 = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/',null=True)
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
        return self.objects.filter( Q(title__icontains=term) | Q(summary__icontains=term) | Q(description__icontains=term)| Q(introduction__icontains=term))
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
     
      


# class Category(MPTTModel):
#     name = models.CharField(max_length=settings.BLOG_TITLE_MAX_LENGTH, unique=True)
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
#     slug = models.SlugField(max_length=settings.BLOG_TITLE_MAX_LENGTH, null=True, blank=True)
#     description = models.TextField(null=True, blank=True)
    
#     class MPTTMeta:
#         order_insertion_by = ['name']

#     class Meta:
#         verbose_name_plural = 'Categories'

#     def __str__(self):
#         return self.name

#     def save(self, *args, **kwargs):
#         value = self.title
#         if not self.slug:
#             self.slug = slugify(value, allow_unicode=True)
#             super().save(*args, **kwargs)

#     def get_absolute_url(self):
#         return reverse('items-by-category', args=[str(self.slug)])

# class Blogpost(models.Model):
#     title = models.CharField(max_length=settings.BLOG_TITLE_MAX_LENGTH)
#     category = TreeForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
#     slug = models.SlugField(
#       max_length=settings.BLOG_TITLE_MAX_LENGTH,
#     )

#     def __str__(self):
#       return self.title

#     def get_absolute_url(self):
#       kwargs = {
#         'slug': self.slug
#       }
#       return reverse('item-detail', kwargs=kwargs)

#     def save(self, *args, **kwargs):
#       if not self.slug:
#         value = self.title
#         self.slug = slugify(value, allow_unicode=True)
#       super().save(*args, **kwargs)

# class SubCategory(models.Model):
#     name = models.CharField(max_length=100)
#     category_image = models.ImageField(upload_to='uploads/categories/%Y/%m/%d/', null=True)
#     cat_summary = models.CharField(max_length=300)
#     description = models.TextField()
#     parent_category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    
#     def blog_in_cat(self):
#         return Blogpost.objects.filter(category=self).count()


# class UserInfo(models.Model):
#     user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
#     bio = models.TextField(null=True)
#     profile_image = models.ImageField(upload_to='uploads/profiles/%Y/%m/%d/', default='default/default.jpg')
#     created = models.DateTimeField(auto_now_add=True)
    
# class Rabbithole(models.Model):
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
#     p_media = models.ImageField(upload_to='uploads/rholes/%Y/%m/%d/',null=True)
#     p_description = models.TextField(default="NULL")
#     created_on = models.DateTimeField(auto_now_add=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
#     approved = models.BooleanField(default=False)
    
#     def like_count(self):
#         return Like.objects.filter(rabbithole=self).count() - Dislike.objects.filter(rabbithole=self).count()
    
#     def get_searchset(self, term):
#         return self.objects.filter( Q(title__icontains=term) | Q(summary__icontains=term) | Q(description__icontains=term)| Q(introduction__icontains=term)| Q(p_description__icontains=term))

#     class Meta:
#         ordering = ['-created_on']
        


#class Like(models.Model):
    #     user = models.ForeignKey( auth_user, on_delete=models.CASCADE,null=True)
#     rabbithole = models.ForeignKey(Rabbithole, on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)

# class Dislike(models.Model):
#     user = models.ForeignKey( auth_user, on_delete=models.CASCADE,null=True)
#     rabbithole = models.ForeignKey(Rabbithole, on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)

# class SavetoProfile(models.Model):
#     user = models.ForeignKey( auth_user, on_delete=models.CASCADE,null=True)
#     rabbithole = models.ForeignKey(Rabbithole, on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)
    
#     def count(self):
#         return SavetoProfile.objects.filter(rabbithole=self).count()

