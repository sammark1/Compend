from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Campaign, NPC, Location
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class Home(TemplateView):
    template_name = "home.html"

def profile(request, username):
    user=User.objects.get(username=username)
    return render(request, 'profile.html', {'username':username})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            return render(request, 'signup.html', {'form': form})    
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
                    return render(request, 'login.html', {'form': form})
            else:
                print('The username and/or password is incorrect.')
                return render(request, 'login.html', {'form': form})
        else: 
            return render(request, 'signup.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

class Campaign_List (TemplateView):
    template_name = 'campaign_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("search")
        if search != None:
            context["campaigns"] = Campaign.objects.filter(name__icontains=search)
            context["header"] = f"Searching for {search}"
        else:
            context["campaigns"] = Campaign.objects.all()
            context["header"] = "search"
        return context
        

class Campaign_Create(CreateView):
    model = Campaign
    fields = '__all__'
    template_name = 'campaign_create.html'
    def get_success_url(self):
        return reverse('Campaign_Show', kwargs={'pk':self.object.pk})
    
class Campaign_Show(DetailView):
    model = Campaign
    template_name = "campaign_show.html"

class Campaign_Update(UpdateView):
    model = Campaign
    fields = '__all__'
    template_name = "campaign_update.html"
    def get_success_url(self):
        return reverse('Campaign_Show', kwargs={'pk':self.object.pk})

class Campaign_Delete(DeleteView):
    model = Campaign
    template_name = "campaign_delete.html"
    success_url = "/campaign/"

#SECTION NPC VIEWS

class NPC_List (TemplateView):
    template_name = 'npc_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["npcs"] = NPC.objects.all()
        return context
    
class NPC_Create(CreateView):
    model = NPC
    fields = '__all__'
    template_name = 'npc_create.html'
    def get_success_url(self):
        return reverse('NPC_Show', kwargs={'pk':self.object.pk})
    
class NPC_Show(DetailView):
    model = NPC
    template_name = "npc_show.html"

class NPC_Update(UpdateView):
    model = NPC
    fields = '__all__'
    template_name = "npc_update.html"
    def get_success_url(self):
        return reverse('NPC_Show', kwargs={'pk':self.object.pk})

class NPC_Delete(DeleteView):
    model = NPC
    template_name = "npc_delete.html"
    success_url = "/npc/"

# !SECTION

#SECTION Location VIEWS

class Location_List (TemplateView):
    template_name = 'location_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["locations"] = Location.objects.all()
        return context
    
class Location_Create(CreateView):
    model = Location
    fields = '__all__'
    template_name = 'location_create.html'
    def get_success_url(self):
        return reverse('Location_Show', kwargs={'pk':self.object.pk})
    
class Location_Show(DetailView):
    model = Location
    template_name = "location_show.html"

class Location_Update(UpdateView):
    model = Location
    fields = '__all__'
    template_name = "location_update.html"
    def get_success_url(self):
        return reverse('Location_Show', kwargs={'pk':self.object.pk})

class Location_Delete(DeleteView):
    model = Location
    template_name = "location_delete.html"
    success_url = "/location/"

# !SECTION