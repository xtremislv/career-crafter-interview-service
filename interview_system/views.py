from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from interview_system import myprosody as mps
import subprocess
from interview_system import predict_pose, delete_files_in_folder, extract_frames
from interview_system import myspgend, myspsr, mysppaus, myspatc, myspod, myspst, mysppron


def index(request):
    return render(request,'carteer_home.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username=request.POST['Username']
        password=request.POST['Password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('carteer_login.html')
    else:
        return render(request,'carteer_login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['Username']
        email=request.POST['Email']
        password=request.POST['Password']

        if User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('carteer_register.html')
        elif User.objects.filter(username=username).exists():
            messages.info(request,"Username already exists")
            return redirect('carteer_register.html')
        else:
            user=User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
            user.save()
            auth.login(request,user)
            return redirect('/')
    else:
        return render(request,'carteer_register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def contact(request):
    return render(request,'carteer_contactus.html')
    
def account(request):
    if request.user.is_authenticated:
        user=request.user
        if request.method=="POST":
            username=user.username
            old_password=request.POST['old_password']
            user=auth.authenticate(username=username,password=old_password)
            if user is not None:
                new_password1=request.POST['new_password1']
                new_password2=request.POST['new_password2']

                if new_password1 != new_password2:
                    messages.info(request,"Passwords do not match")
                    return redirect('account')
                
                user.set_password(new_password1)
                user.save()
                auth.login(request,user)
                messages.info(request,"Successfully updated password")
                return redirect('account')
            else:
                messages.info(request,"Wrong Password")
                return redirect('account')
        return render(request,"account")
    else:
        return redirect('/carteer_login.html')
    
def interview(request):
    return render(request,'interview.html')
    # if request.user.is_authenticated:
    #     return render(request,'interview.html')
    # else:
    #     return redirect('/carteer_login.html')
    
@csrf_exempt
def submit(request):
    # if request.user.is_authenticated:
    if request.method=="POST":
        video_file = request.FILES.get('video_data')
        # decoded_data = base64.b64decode(audio_file.read())
        webm_path='dataset/audioFiles/record1.webm'
        decoded_data=video_file.read()
        with open(webm_path, 'wb') as f:
            f.write(decoded_data)

        wav_path='dataset/audioFiles/record1.wav'
        path='C:/Users/lovyv/Downloads/Career-Crafter-Interview-System'

        command=['ffmpeg','-y','-i',webm_path,'-c:a','pcm_f32le',wav_path]
        subprocess.run(command)

        delete_files_in_folder(r'C:\Users\lovyv\Downloads\Career-Crafter-Interview-System\dataset\videofile\input_files')
        extract_frames(r'C:\Users\lovyv\Downloads\Career-Crafter-Interview-System\dataset\audioFiles\record1.webm', r'C:\Users\lovyv\Downloads\Career-Crafter-Interview-System\dataset\videofile\input_files')

        result={"Gender":myspgend('record1',path),
                "Number of Pauses":mysppaus('record1',path),
                "Rate of Speech":myspsr('record1',path),
                "Articulation Rate":myspatc('record1',path),
                "Speaking Duration":myspst('record1',path),
                "Original Duration":myspod('record1',path),
                "Pronunciation Score":mysppron('record1',path),
                'posture_remark':predict_pose(path)
                }

        return HttpResponse(json.dumps(result),content_type='application/json')
    # else:
    #     return redirect('/carteer_login.html')
