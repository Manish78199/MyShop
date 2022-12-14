from django.db import models

# # Create your models here.
class product(models.Model):
    product_id=models.AutoField
    product_brand=models.CharField(max_length=1000,default="")
    product_Name=models.CharField(max_length=50)
    product_category=models.CharField(max_length=100,default="")
    product_subcat=models.CharField(max_length=100,default="")
    
    product_details=models.CharField(max_length=200 ,default="")
    product_price=models.IntegerField()
    product_image=models.ImageField(upload_to="Myshop/media",default="")
    product_publish_date=models.DateField()
    def __str__(self) :
        return "#"+str(self.id)+" ("+self.product_Name+")"
    
# class User(models.Model):
#     user_id=models.AutoField
#     user_name=models.CharField(max_length=100,default="")
#     user_phone=models.CharField(max_length=10,default="")    
#     user_email=models.EmailField()
#     user_country=models.CharField(max_length=30,default="")
    
class order(models.Model):
    order_id=models.AutoField(primary_key=True)
    order_product=models.CharField(max_length=10000,default="")
    user_name=models.CharField(max_length=50)
    user_number=models.CharField(max_length=10,default="")
    user_email=models.CharField(max_length=200 ,default="")
    user_address1=models.CharField(max_length=1000 ,default="")
    user_address2=models.CharField(max_length=1000 ,default="")
    order_price=models.IntegerField()
    order_date=models.DateTimeField()
    def __str__(self) :
        return str(self.order_id)+" "+str(self.user_name)+" "+str(self.order_date)
    
    
class OrderUpdate(models.Model):
    order_id=models.CharField(max_length=50,default="")
    order_status=models.CharField(max_length=100,default="")
    order_desc=models.CharField(max_length=500,default="")
    update_time=models.DateTimeField()
    def __str__(self) :
        return "Order ID is "+str(self.order_id)+" , Update Time "+str(self.update_time)
    
    
        
    
    
    
    