from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as auth_user
from django.core.validators import validate_slug, validate_email
from my_app.models import *

from . import models


def must_be_unique(value):
    users = auth_user.objects.filter(email=value)
    if len(users) >= 1:
        raise forms.ValidationError("User with that email already exists")
    return value

def must_be_ten(value):
    if not len(value) > 10:
        raise forms.ValidationError("Needs to be more than 10 chars")
    # Always return the cleaned data
    return value

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        validators=[must_be_unique]
    )

    class Meta:
        model = auth_user
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class SearchForm(forms.Form):
    term = forms.CharField(label='term', max_length=100)

class RabbitholeForm(forms.Form):
    title_field = forms.CharField(label='Title',max_length=100)
    summary_field = forms.CharField(label='Summary',max_length=300)
    introduction_field = forms.CharField(widget=forms.Textarea, label='Introduction',)
    p_description_field = forms.CharField(widget=forms.Textarea, label='Short Description',)
    description_field = forms.CharField(widget=forms.Textarea, label='Description',)
    s_media0_field = forms.ImageField(label='Supporting Media #1')
    s_media1_field = forms.ImageField(label='Supporting Media #2')
    s_media2_field = forms.ImageField(label='Supporting Media #3')
    s_media3_field = forms.ImageField(label='Supporting Media #4')
    s_media4_field = forms.ImageField(label='Supporting Media #5')
    s_media5_field = forms.ImageField(label='Supporting Media #6')
    references_field = forms.CharField(widget=forms.Textarea, label='References (Endline after each link)',)
    p_media_field = forms.ImageField(label='Catalog Media')

    def save(self, request):
        rhole_instance = models.Rabbithole()
        rhole_instance.title = self.cleaned_data["title_field"]
        rhole_instance.summary = self.cleaned_data["summary_field"]
        rhole_instance.introduction = self.cleaned_data["introduction_field"]
        rhole_instance.description = self.cleaned_data["description_field"]
        rhole_instance.s_media0 = self.cleaned_data["s_media0_field"]
        rhole_instance.s_media1 = self.cleaned_data["s_media1_field"]
        rhole_instance.s_media2 = self.cleaned_data["s_media2_field"]
        rhole_instance.s_media3 = self.cleaned_data["s_media3_field"]
        rhole_instance.s_media4 = self.cleaned_data["s_media4_field"]
        rhole_instance.s_media5 = self.cleaned_data["s_media5_field"]
        rhole_instance.references = self.cleaned_data["references_field"]
        rhole_instance.p_media = self.cleaned_data["p_media_field"]
        rhole_instance.p_description = self.cleaned_data["p_description_field"]
        # rhole_instance.author = request.user
        rhole_instance.save()
        
class EditForm(UserCreationForm):
    email = forms.EmailField(
        label="email",
        required=True,
        validators=[must_be_unique]
    )

    class Meta:
        model = auth_user
        fields = (
            "username",
            "email",
            "password1",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["New Email"]
        if commit:
            user.save()
        return user


class CommentForm(forms.Form):
    comment_field = forms.CharField(
        label='Comment',
        max_length=240,
    )

    def save(self, request, rhole_id):
        print("Attempting to save new comment...")
        rhole_instance = models.Rabbithole.objects.get(id=rhole_id)
        comment_instance = models.Comment()
        comment_instance.comment = self.cleaned_data["comment_field"]
        comment_instance.author = request.user
        comment_instance.rabbithole = rhole_instance
        comment_instance.save()

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class UserForm(forms.Form):
    bio_field = forms.CharField(widget=forms.Textarea, label='Bio')
    profile_image = forms.ImageField(label='Profile Image')

    def save(self, request):
        userinfo_instance = models.UserInfo()
        userinfo_instance.bio_field = self.cleaned_data["bio_field"]
        userinfo_instance.profile_image = self.cleaned_data["profile_image"]
        userinfo_instance.save()

class NameForm(forms.ModelForm):
    class Meta:
        model = NameModel
        fields = ['your_name',]