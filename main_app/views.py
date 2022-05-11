from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Campaign, NPC, Location
from .forms import Profile_Delete_Form, Upload_File_Form, Location_Upload_Form
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from datetime import datetime
import csv


class Home(TemplateView):
    template_name = "home.html"

def profile(request, username):
    user=User.objects.get(username=username)
    return render(request, 'profile.html', {'user':user})

class profile_update(UpdateView):
    model = User
    fields = ['username', 'email']
    # fields = '__all__'
    template_name = "profile_update.html"
    def get_success_url(self):
        return reverse('profile', kwargs={'username':self.object.username})

def profile_delete (request, username):
    user = User.objects.get(username=username)
    form = Profile_Delete_Form(request.POST)
    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'profile_delete.html', {'form':form, 'user':user})

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
            return render(request, 'login.html', {'form': form})
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
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.updated_at = datetime.now()
        self.object.save()
        return HttpResponseRedirect(f'/campaign/{self.object.id}')

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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.updated_at = datetime.now()
        self.object.save()
        return HttpResponseRedirect(f'/npc/{self.object.id}')

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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.updated_at = datetime.now()
        self.object.save()
        return HttpResponseRedirect(f'/location/{self.object.id}')

# def Location_Update (request, location_id):
#     location = Location.objects.get(id=location_id)
#     if request.method == 'POST':
#         form = Location_Update_Form(request.POST)
#         if form.is_valid():
#             location
#             location.save()
#             return HttpResponseRedirect(f'/location/{location_id}')
#         else:
#             return render(request, 'location_show.html', {'form':form, 'location':location})
#     else:
#         form = Location_Update_Form()
#         return render(request, 'location_update.html', {'form':form, 'location':location})


class Location_Delete(DeleteView):
    model = Location
    template_name = "location_delete.html"
    success_url = "/location/"

# !SECTION

#SECTION File up

def upload_csv(request, pk):
    campaign = Campaign.objects.get(pk=pk)
    if request.method == 'POST':
        form = Upload_File_Form(request.POST, request.FILES)
        if form.is_valid() and str(request.FILES['file'])[-4:]==".csv":
            data=(request.FILES['file'].read()).decode("utf-8")    
            data_type = (form.cleaned_data['data_type'])
            match data_type:
                case "NPC":
                    print("NPC")
                case "Location":
                    rows=data.split("\n")
                    for line in rows:
                        print(line)
                        entries=line.split(',')
                        save_instance=Location.objects.create(
                            name=entries[0],
                            campaign=campaign,
                            location_type=entries[1],
                            description=entries[4],
                        )
                        save_instance.save()
                        # data_dict = {
                        #     "name":entries[0],
                        #     "location_type":entries[1],
                        #     # "geo_location":entries[3],
                        #     # "political_location":entries[2],
                        #     "description":entries[4],
                        # }
                        # print ('data_dict',data_dict)
                        # save_form=Location_Upload_Form(data_dict)
                        # if save_form.is_valid():
                        #     save_form.save()
                        # else:
                        #     print('something went wrong with form saving')
                        #     return render(request, 'upload.html', {'form':form})
            return HttpResponseRedirect('/location/')
        else:
            print('something went wrong')
            return render(request, 'upload.html', {'form':form})
    else:
        form = Upload_File_Form()
        return render(request, 'upload.html', {'form':form, 'campaign':campaign})
                
# !SECTION