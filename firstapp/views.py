from django.shortcuts import get_object_or_404, render
from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cart, udp, user_tbl,Products


# Create your views here.
def base(request):
    return render(request, "base.html")

#register

def regi(request):
    return render(request, "regi.html")


 #login

def login(request):
    return render(request, "login.html") 

def index(request):
    data=udp.objects.all()
    products=Products.objects.all()
    try:
        data=udp.objects.get(userdt__id=request.user.id)
        products=Products.objects.all()
    except udp.DoesNotExist:
        user = None
    context={'data':data,'products':products}
    return render(request, "index.html" , context )



def userlogin(request):
    if request.method=="POST":
        user_name=request.POST['username']
        pass_word=request.POST['Password']
        user=auth.authenticate(username=user_name,password=pass_word)
        # request.session["lin"] = user.id
        print(user)
        if user is not None:
            auth.login(request,user)
            print('user not none')
            return redirect('index')
        else:
            print('failed')
            return redirect('login')
    return render(request, "login.html")



def userregister(request):
    if request.method=="POST":
        username=request.POST['name']
        email=request.POST['email']
        mob=request.POST['mob']
        password=request.POST['pass']
        password2=request.POST['rpass']
        if password==password2:
            if User.objects.filter(username=username).exists():
                print('user already exists')
                return redirect('login')
            # elif User.objects.filter(email=email).exists():
            #     print('email already exists')
            #     return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                mo=udp(userdt=user,contact_no=mob)
                mo.save()
                print('user created')
                return redirect('login')
        else:
            print('password not matching')
            return redirect('signup')
    else:
        return render(request, "login.html")





def changepass(request):
    return render(request, "changepass.html")
def logout(request):
    request.session["lin"] = ""
    auth.logout(request)
    return redirect('login')
def logoutt(request):
    return render(request,'logout.html')
#change password

def changepassword(request):
    if 'lin' in request.session:
        return render(request,'changepass.html')
    else:
        return redirect('login')
def changepasswordauth(request):
    if request.method=="POST":
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        newpassword2=request.POST['newpassword2']
        user = User.objects.get(username=request.user)
        check=user.check_password(oldpassword)

        if check==True:
            if newpassword==newpassword2:
                user.set_password(newpassword)
                user.save()
              #  messages.info(request,'password changed successfully')
                print('password changed')
                return redirect('login')
            else:
             #   messages.info(request,'password not matching')
                print('password22 not matching')
                return render(request,'changepass.html')
        else:
            # messages.info(request,'old password not matching')
             return render(request,'changepass.html')
    else:
        return render(request,'changepass.html')

def cart(request):
    return render(request, "cart.html")


def userpro(request):
    data=udp.objects.get(userdt__id=request.user.id)
    context={}
    context['data']=data
    return render(request, "userpro.html", context)
def editpro(request):
    return render(request, "editpro.html")



@login_required(login_url='login')
def  editauth(request):
    data=udp.objects.get(userdt__id=request.user.id)
    context={}
    context['data']=data
    if request.method=="POST":
        na=request.POST['name']
        em=request.POST['email']
        mo=request.POST['mob']
        ci=request.POST['city']
        ad=request.POST['address']
        us=User.objects.get(id=request.user.id)
        us.username=na
        us.email=em
        us.save()
        data.Address=ad
        data.contact_no=mo
        data.city=ci
        data.save()
        if "pic" in request.FILES:
            data.dp=request.FILES['pic']
            data.save()
        else:
            print("no pic")
        context['msg']="updated"
        return render(request,'userpro.html',context)
    return render(request,'editpro.html',context)


@login_required(login_url='login')
def add_to_cart(request):
    items=Cart.objects.filter(user__id=request.user.id,status=False)
    context={}
    context['items']=items
    data=udp.objects.all()
    try:
        data=udp.objects.get(userdt__id=request.user.id)
    except udp.DoesNotExist:
        user = None
    context['data']=data
    if request.user.is_authenticated:
        if request.method=="POST":
            print(request.POST)
            pid=request.POST['pid']
            qty=request.POST['qty']
            print(pid,qty)
            is_exist=Cart.objects.filter(user_id=request.user.id,product_id=pid,status=False)
            if len(is_exist)>0:
                is_exist[0].quantity=int(is_exist[0].quantity)+int(qty)
                is_exist[0].save()
            else:
                product=get_object_or_404(Products,id=pid)
                print(product)
                usr=get_object_or_404(User,id=request.user.id)
                print(usr)
                ct=Cart(user=usr,product=product,quantity=qty)
                ct.save()
                print("added") 

        else:    
               
            #total (cart)
    
                da=Cart.objects.filter(user__id=request.user.id)
                context={'da':da}

                total = 0
                for i in da:
                    total=total+int(i.quantity)*int(i.product.price)
                print(total)
                context={'total':total}
    

    else:
        return redirect('login')
    return render(request,'cart.html',context)   


def product(request):
    return render(request, "product.html")

