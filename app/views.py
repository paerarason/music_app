from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .models import Music,Music_Lover,Folder_repo,Email,Email_Folder_conn
from .form import SignINForm,LoginINForm,MUSICForm
# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dash')

class RegisterPage(FormView):
    template_name = 'signin.html'
    form_class = SignINForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('dash')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

  

@login_required
def upload_music(request):
  if request.method == "POST":
    print(request.user.email)
    lover_music = Music_Lover.objects.get(person=request.user)
    file_music = Music.objects.create(
        name=request.POST.get('name'),
        description=request.POST.get('description'),
        audio=request.FILES.get('audio'),
        person=lover_music
    )
    file_music.save()
    folder_type = request.POST.get('access')
    folder = Folder_repo.objects.create(
        folder_type=folder_type,
        music_lover=lover_music,
        music=file_music
    )
    folder.save()

    if folder_type == "protected":
        emails = request.POST.getlist('email')
        connect = Email_Folder_conn.objects.create(protect=folder)
        connect.emails.set(emails)
        connect.save()
    return render_dashboard(request)

  elif request.method=="GET":
     form=MUSICForm()
     return render(request,"radio.html",{"form":form})

@login_required
def render_dashboard(request):
         content={}
         # get the login  user's  profile and then folders related to him  and list the musics
         try:
            folders=Folder_repo.objects.get(music_lover=Music_Lover.objects.get(person=request.user))
            content['own_musics']=[files.music for files in folders]
         except:
                connect=Email_Folder_conn.objects.filter(emails=request.user.email)
                content['others_music']=[files.protect.music for files in connect]
                folder=Folder_repo.objects.filter(folder_type="public")
                print(folder.count())
                content['public_music']=[files.music for files in folder]
         return render(request,"dashboard.html",{"content":content})


def check_mails(emails):
   values=Email.objects.all()
   return [ i for i in values if i.email in emails ]