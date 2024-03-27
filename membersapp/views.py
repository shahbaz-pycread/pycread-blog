from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView, CreateView 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from blogapp.models import Profile
from django.shortcuts import get_object_or_404
# Create your views here.
# User Registration Form
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

# User Profile Updation Form
    
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url  = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
# Password Change Views
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url  = reverse_lazy('password_success')

# redirect to page after the password change is success
def password_success(request):
    return render(request, 'registration/password_success.html', {})

# User Profile Page View
class ShowProfilePageView(generic.DetailView):  
    model = Profile
    template_name = 'registration/user_profile.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

    #     page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

    #     context["page_user"] = page_user
    #     return context      

    def get_context_data(self, *args, **kwargs):
        #users = Profile.objects.all()
        #total_posts = Post.objects.count()
        context = super(ShowProfilePageView,self).get_context_data(*args, **kwargs)
        # Page User
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        #context["total_posts"] = total_posts
        return context

# Edit Profile Page View
class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url']
    success_url = reverse_lazy('home')

# Create Profile Page View
class CreateProfilePageView(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    #fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)