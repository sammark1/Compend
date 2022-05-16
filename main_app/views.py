from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Campaign, NPC, Location
from .forms import Profile_Delete_Form, Upload_File_Form, Location_Upload_Form
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from datetime import datetime
import csv
import re


class Home(TemplateView):
    template_name = "home.html"

def profile(request, username):
    user=User.objects.get(username=username)
    campaigns = Campaign.objects.filter(user=user)
    npcs=[]
    locations=[]
    for campaign in campaigns:
        npcs.extend(NPC.objects.filter(campaign=campaign))
        locations.extend(Location.objects.filter(campaign=campaign))
    return render(request, 'profile.html', {'user':user, 'campaigns_length':len(campaigns), 'npcs_length':len(npcs), 'locations_length':len(locations)})

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
        print('form',form)
        return render(request, 'login.html', {'form': form})

class Campaign_List (TemplateView):
    template_name = 'campaign_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("search")
        if search != None and search!="":
            context["campaigns"] = Campaign.objects.filter(name__icontains=search)
            context["header"] = f"Searching for {search}"
        else:
            context["campaigns"] = Campaign.objects.filter(user=self.request.user)
            context["header"] = ""
        return context
        

class Campaign_Create(CreateView):
    model = Campaign
    fields = ['name']
    template_name = 'campaign_create.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse('Campaign_Show', kwargs={'pk':self.object.pk}))
    
class Campaign_Show(DetailView):
    model = Campaign
    template_name = "campaign_show.html"

class Campaign_Update(UpdateView):
    model = Campaign
    fields = ['name']
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

class NPC_List(TemplateView):
    template_name='npc_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search')
        context["campaign"] = Campaign.objects.get(pk=self.kwargs['pk'])
        if search != None:
            context["npcs"] = NPC.objects.filter(
                Q(given_name__icontains=search) | Q(family_name__icontains=search) | Q(home__name__icontains=search), 
                campaign=context['campaign'])
        else:
            context["npcs"] = NPC.objects.filter(campaign=context['campaign'])
        return context

class NPC_Create(CreateView):
    model = NPC
    fields = ['title','given_name','family_name','alignment','pronoun','npc_class','npc_race','age','physical','profession','home']
    template_name = 'npc_create.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = Campaign.objects.get(pk=self.kwargs['pk'])
        # print(self)
        # print(context)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.campaign = Campaign.objects.get(pk=self.kwargs['pk'])
        self.object.save()
        return HttpResponseRedirect(reverse('NPC_Show', kwargs={'pk':self.object.pk}))
    
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
    
    def get_success_url(self, **kwargs):
        return reverse('NPC_List', args=[self.object.campaign.pk])
        



# !SECTION

#SECTION Location VIEWS

# class Location_List (TemplateView):
#     template_name = 'location_list.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["locations"] = Location.objects.all()
#         return context

class Location_List(TemplateView):
    template_name='location_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search')
        context["campaign"] = Campaign.objects.get(pk=self.kwargs['pk'])
        if search != None:
            context["locations"] = Location.objects.filter(
                Q(name__icontains=search), 
                campaign=context['campaign'])
        else:
            context["locations"] = Location.objects.filter(campaign=context['campaign'])
        return context
    
class Location_Create(CreateView):
    model = Location
    fields = ['name', 'location_type', 'geo_location', 'political_location', 'description']
    template_name = 'location_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = Campaign.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.campaign = Campaign.objects.get(pk=self.kwargs['pk'])
        self.object.save()
        return HttpResponseRedirect(reverse('Location_Show', kwargs={'pk':self.object.pk}))

    
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
            rows=data.split("\n")
            for line in rows[1:]:
                if re.search('("(?:[^,"\n]+,[^,"\n]+)+")',line):
                    print(line)
                    quoted = re.split('("(?:[^,"\n]+,[^,"\n]+)+")', line)
                    for i, section in enumerate(quoted):
                        if '"' in section:
                            section=section.replace(",",";")
                            section=section.replace('"','')
                            quoted[i]=section
                            # print(quoted)
                    line=''.join(quoted)
                    print(line)

                # ,(?=.*")(?<=".*) matches any comma between any quotes
                # (?<=")(.*?)(?=") matches anything between any quotes
                # "[^"]+" matches anything between pairs of quotes
                # ("[^"]+(?=,)) matches a quote and any characters upto but not including a ,
                # ("[^"\n]*(?=,)),((?<=,)[^"\n]*") captures all between quotes
                #  (?<="[^,\n]+(?=,)), almost works but only grabs one comma

                # ("[^,"\n]+),([^,"\n]+")
                    # for each hit on the search
                    # get string index of start of string
                    # store quotes string as temp string
                    # swap "," char with ";"
                    # insert temp string at stored index


                
                # blarp = re.split('("[^",]+),([^"]+")', line)
                # print(blarp)
                #     for i in range(len(blarp)):
                #         if '"' in blarp[i]:
                #             print(blarp[i])
                entries=line.split(',')
                match data_type:
                    case "NPC":
                        save_instance=NPC.objects.create(
                            title = entries[0],
                            given_name = entries[1],
                            family_name = entries[2],
                            campaign = campaign,
                            alignment = entries[3],
                            pronoun = entries[4],
                            npc_class = entries[5],
                            npc_race = entries[6],
                            
                            physical = [8],
                            profession = [9],
                        )
                        save_instance.save()
                    case "Location":
                        save_instance=Location.objects.create(
                            name=entries[0],
                            campaign=campaign,
                            location_type=entries[1],
                            description=entries[4],
                        )
                        save_instance.save()
            match data_type:
                case "NPC":
                    return HttpResponseRedirect('/npc/')
                case "Location":
                    return HttpResponseRedirect('/location/')
        else:
            print('something went wrong')
            return render(request, 'upload.html', {'form':form})
    else:
        form = Upload_File_Form()
        return render(request, 'upload.html', {'form':form, 'campaign':campaign})
                
# !SECTION