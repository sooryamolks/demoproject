from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def allcategories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'category.html',context)
def allproducts(request,p):
    c=Category.objects.get(id=p)
    p=Product.objects.filter(category=c)
    context={'cat':c,'product':p}
    return render(request,'product.html',context)

def productdetails(request,p):

    pro=Product.objects.get(id=p)
    context={'product':pro}
    return render(request,'detail.html',context)

def register(request):
    if(request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']

        if(p==cp):
            u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            u.save()

            return redirect('shop:categories')


    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u, password=p)
        if user:
            login(request,user)
            return redirect('shop:categories')
        else:
            messages.error(request,"invalid credentials")
    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return redirect('shop:categories')

def add_categories(request):
    if(request.method=="POST"):
        n=request.POST['n']
        i=request.FILES['i']
        d=request.POST['d']
        c=Category.objects.create(name=n,image=i,desc=d)
        c.save()
        return redirect('shop:categories')
    return render(request,'add_categories.html')

def add_products(request):
    if (request.method == "POST"):
        n = request.POST['n']
        i = request.FILES['i']
        d = request.POST['d']
        s=request.POST['s']
        p=request.POST['p']
        c=request.POST['c']
        cat=Category.objects.get(name=c)
        p = Product.objects.create(name=n, image=i, desc=d,stock=s,price=p,category=cat)
        p.save()
        return redirect('shop:categories')
    return render(request,'add_products.html')

def add_stock(request,p):
    product=Product.objects.get(id=p)
    if (request.method == "POST"):
        product.stock = request.POST['n']
        product.save()
        return redirect('shop:categories')
    context={'pro':product}

    return render(request,'add_stock.html',context)
