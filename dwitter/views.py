# dwitter/views.py

from django.shortcuts import render, redirect
from .forms import DweetForm, ProfileForm, gimageForm
from .models import Dweet, Profile, gimage
from django.contrib.auth.decorators import login_required
from pprint import pprint

@login_required
def dashboard(request):
    if request.user.is_authenticated:
    
        followed_dweets = Dweet.objects.filter(
            user__profile__in=request.user.profile.follows.all()
        ).order_by("-created_at")
        
        gimages = gimage.objects.all()
        print('test')
        print(gimages)
        return render(request, "dwitter/dashboard.html", {"dweets": followed_dweets, "gimages": gimages},)
    else:
        return redirect('dwitter:login')

@login_required
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})

@login_required
def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
    
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile": profile})

def index(request):
    if request.user.is_authenticated:
        return redirect("dwitter:dashboard")
    else:
        return render(request, "dwitter/index.html")
    
@login_required    
def profile_update(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("dwitter:dashboard")
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'dwitter/profile_form.html', {'form': form, "profile": profile})

@login_required    
def dweet_upload(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = DweetForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("dwitter:dashboard")
    else:
        form = DweetForm(instance=profile)
    return render(request, 'dwitter/dweet_upload_form.html', {'form': form, "profile": profile})

# @login_required    
# def gimage_upload(request, pk):
#     profile = Profile.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = gimageForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
            
#             form.save(commit=False)
#             form.user = request.user
#             form.save()
#             gimg_obj =form.instance
#             #gimg_obj = form.files['gimage']
#             #file_contents = gimg_obj.read()

#             #file_contents = gimg_obj.file
#             #file_type = gimg_obj.content_type
#             #file_name = gimg_obj.name

           
#             #return HttpResponse(f"Image uploaded successfully! {gimg_obj}")
#             return render(request, 'dwitter/gimage_upload_form.html', {'form': form, 'gimg_obj':gimg_obj})
#     else:
#         form = gimageForm()
#     return render(request, 'dwitter/gimage_upload_form.html', {'form': form})

@login_required    
def gimage_upload(request):
    if request.method == 'POST':
        form = gimageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.save()
            #gimg_obj =form.instance
            #https://stackoverflow.com/questions/42158922/django-modelform-does-not-save-because-of-missing-user-id
            gimg_obj = form.files['gimage']
            #file_contents = gimg_obj.read()

            #file_contents = gimg_obj.file
            #file_type = gimg_obj.content_type
            #file_name = gimg_obj.name

           
            #return HttpResponse(f"Image uploaded successfully! {gimg_obj}")
            return render(request, 'dwitter/gimage_upload_form.html', {'form': form, 'gimg_obj':gimg_obj})
    else:
        form = gimageForm()
    return render(request, 'dwitter/gimage_upload_form.html', {'form': form})