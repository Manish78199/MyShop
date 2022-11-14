from ast import Try
from datetime import date
import email
from pyexpat import model
from django.test import Client
from flask import jsonify
from matplotlib.font_manager import json_dump
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers


from datetime import datetime
import json
from math import ceil
from django.template import loader
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import OrderUpdate, order, product

def index(request):
     
   
   para=[] 
   check=product.objects.all().values("product_category") 
   unique={i["product_category"] for i in check}
   for v in unique:
       
        allprod=product.objects.filter(product_category=v).values()
        n=len(allprod)
        nslides=n//4+ceil((n/4)-(n//4))
        para.append([allprod,range(nslides),nslides])
        
   return render(request,"pages/index.html",{"para":para})







def signin(request):
     if not request.user.is_authenticated:
         return render(request,"pages/Login.html")
     else:
          return redirect(signup)
def signup(request):
    
     
     return render(request,"pages/SignUp.html")
 
  
 
 
def loginmethod(request,method):
     if method=="signin":
      if request.method=="POST":
           print(request.POST["email1"],request.POST["password1"])
           user = authenticate(username=request.POST["email1"], password=request.POST["password1"])
           print(user)
           if user is not None:
               
               login(request,user)
               print("yeh!")
               return redirect(index)
           else:
                messages.success(request,"invalid")
                return redirect(signin) 
     elif method=="signup":
           if request.method=="POST":
                username=request.POST['username']
                email2=request.POST['email2']
                password=request.POST['password2']
                cpassword=request.POST['cpassword2']
                if password==cpassword:
                   alluser= User.objects.filter(email=email2)
                   print(alluser)
                   if len(alluser)>0:
                        messages.error(request,"User Already Resister with this email")
                   else:     
                      user = User.objects.create_user(email2, email2, password)
                      user.first_name=username
                      user.save()
                      messages.success(request,"Success")
                      return redirect(signin)
               
                else:
                    messages.success(request,"hf")
                    return redirect(signup) 
 
def Logout(request):
     logout(request)
     return redirect(signin)
      
      
def OrderNow(request):
     if request.method=="POST":
          cartjson=request.POST["cartJson"]
          username=request.POST["username"]
          number=request.POST["number"]
          email=request.POST["Email"]
          address=request.POST["address"]
          address2=request.POST["address2"]
          tprice=request.POST["tprice"]
          print(request.POST["Email"])
          
          order1=order(order_product=cartjson,user_name=username,user_number=number,user_email=email,user_address1=address,user_address2=address2,order_price=tprice,order_date=datetime.now()) 
          order1.save()
          orderupdate=OrderUpdate(order_id=order1.order_id,order_status="Placed",order_desc="Order has been placed",update_time=datetime.now())
          orderupdate.save()
     return redirect(status) 
      
      
      
@login_required(login_url='/signin/') 
def checkout(request):
     return render(request,"pages/Checkout.html")
 
def contact(request):
     return render(request,"pages/Contact.html")
 
def veiw(request,pid):
     
   
     prod=product.objects.filter(id=str(pid)[4:-4]).values()
     
     para={"prod":prod[0]}
     return render(request,"pages/ProductVeiw.html",para)






def find1(request,cat='',pname=''):
     if cat=='':
       return redirect(index)
     else:
          return render(request,"pages/Find.html")
          
def find2(request,cat):
     
     
     
     prod=product.objects.filter(product_category=cat,product_Name__contains="").values()
     
     para={"cat":cat,"prod":prod,"value":""}
     return render(request,"pages/Find.html",para)

def find3(request,cat,pname):
     
     
     prod=product.objects.filter(product_Name__contains=pname ).values()
    
     para={"cat":cat,"prod":prod,"value":pname}
     return render(request,"pages/Find.html",para)




class ser(serializers.ModelSerializer):
     class Meta:
        model=product
        fields = '__all__'
 
# @api_view(["POST","GET"])  
@csrf_exempt
def cartdetails(request):
   if request.method=="POST":
      
      allp=json.load(request)['prods']
      
      senditems=[]
      for x in allp:  
           if x[2:]!="":
            senditems.append(ser(product.objects.filter(id=int(x[2:])),many=True).data[0])  
      
      return JsonResponse({"status":"200","result":senditems})
   return JsonResponse({"status":"400"})   

# @api_view(["POST","GET"])     
# def cartdetails(request):
#    if request.method=="POST":
      
#       allp=json.load(request)['prods']
#       print(allp)
#       senditems=[]
#       for x in allp:  
#            senditems.append(ser(product.objects.filter(id=int(x[2:])),many=True).data[0])  
#       print(senditems)
#       return Response({"status":"200","result":senditems})
#    return Response({"status":"400"})   




@api_view(["POST","GET"])    
def Test(request):
     if request.method=="POST":
      global allp    
      allp=json.load(request)['prods']
      print(allp)
     #  senditems=[]
     #  for x in allp:  
     #       senditems.append(ser(product.objects.filter(id=int(x[2:])),many=True).data[0])  
     # ,"result":senditems
      return Response({"status":"200"})
     return Response({"status":"400"})

@login_required(login_url='/cart/') 
def status(request):
      orders=[]
      items=order.objects.filter(user_email=request.user.email).values("order_id","order_product","order_date","order_price")
      for x in items: 
           prodall=json.loads(x["order_product"])
           products=[]
           for pi in prodall.keys():   
               
              prod={
                "product":(product.objects.filter(id=pi[2:]).values("id","product_Name","product_price","product_image"))[0],
                 "quantity": prodall[pi]   
               }
              products.append(prod)
           neworder={
                "order":x,
                "products":products,
                "orderUpdate":OrderUpdate.objects.filter(order_id=x["order_id"]).values()
                }    
           orders.append(neworder)
      orders.reverse()     
     
      return render(request,"pages/Status.html",{"orders":orders})
 
def cart(request): 
     #  senditems=[]
     #  for x in allp:  
     #       senditems.append(ser(product.objects.filter(id=int(x[2:])),many=True).data[0]) 
      return render(request,"pages/Cart.html")
 



@api_view(["POST","GET"])     
def search(request,findi):
     print(findi)
     if findi:
       
       allresult=product.objects.filter(product_Name__contains=findi).values_list("product_Name")
       
       if len(allresult)>0:
         result=[]      
         for x in allresult:
            result.append(x[0])   
         return Response({"status":"200","result":result})     
     return Response({"status":"400"})