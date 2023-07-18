from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from hello.models import Question, Answer

# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        raw_password = request.POST.get('password')

        #사용자 인증
        user = authenticate(username= username , password = raw_password)
        user = User.objects.create_user(username = username, password=raw_password)
        login(request, user)
        return redirect('hello:index')
    return render(request , 'common/signup.html')

def mypage(request):
    myquestion_list=Question.objects.filter(author = request.user)
    context = {'myquestion_list': myquestion_list}
    return render(request, 'common/mypage.html',context)
def logout(request):
    return redirect('hello:index')