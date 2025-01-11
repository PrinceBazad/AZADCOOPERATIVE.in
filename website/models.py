from django.db import models

# Create your models here.
class director(models.Model):
    director_id=models.AutoField
    director_name=models.CharField(max_length=30)
    director_title=models.CharField(max_length=40)
    director_phone=models.IntegerField()

    def __str__(self):
        return self.director_name
    

class Product(models.Model):
    Product_id=models.AutoField
    Product_name=models.CharField(max_length=30)
    Product_desc=models.CharField(max_length=40)
    Product_image=models.ImageField(upload_to='website/products/images',default="")
    def __str__(self):
        return self.Product_name
    
class Branch(models.Model):
    Branch_name=models.CharField(max_length=30)
    Branch_address=models.CharField(max_length=100)
    Branch_phone=models.IntegerField()
    Branch_image=models.ImageField(upload_to='website/Branch/images',default="")

    def __str__(self):
        return self.Branch_name
    
class Byelaw(models.Model):
    Byelaw_document=models.FileField(upload_to='website/Byelaws',default="")
    

class NewsandUpdate(models.Model):
    News_date=models.DateField()
    News_title=models.CharField(max_length=20)
    News_desc=models.CharField(max_length=30)
    News_image=models.ImageField(upload_to='website/News/images',default="")
    News_attachment=models.FileField(upload_to='website/News/Attachments',default="")

    def __str__(self):
        return self.News_desc
    
class AnnualReport(models.Model):
    AnnualReport="Annual Report"
    AnnualReport_image=models.ImageField(upload_to='website/AnnualReport/images',default="")
    AnnualReport_file=models.FileField(upload_to='website/AnnualReport',default="")

    def __str__(self):
        return self.AnnualReport
    
class HomeSlide(models.Model):
    Heading=models.CharField(max_length=100)
    Establishedyear=models.IntegerField(max_length=4,default="2024")
    Registrationnumber=models.CharField(max_length=25,default="MSCS/CR/208/2005")
    Officetype=models.CharField(max_length=20)
    Address=models.CharField(max_length=100)
    Logo=models.ImageField(upload_to='website/HomeSlide/images/logo',default="")
    Banner=models.ImageField(upload_to='website/HomeSlide/images/banner',default="")
    news_heading=models.CharField(max_length=50,default="")
    news_date=models.DateField(default="2004-01-01")
    news_image=models.ImageField(upload_to="website/HomeSlide/images/news",default="")
    news_Attachment=models.FileField(upload_to="websit/HomeSlide/attachment",default="")
    Phone1=models.IntegerField()
    Phone2=models.IntegerField()
    Email=models.EmailField()

    def __str__(self):
        return self.Heading
    
class Aboutus(models.Model):
    Title="About"
    Aboutpage_fertilizer=models.CharField(max_length=1000,default="")
    About_visionpara=models.CharField(max_length=1000)
    About_missionpara=models.CharField(max_length=1000)

    def __str__(self):
        return self.Title
    
class Announcement(models.Model):
    Announcement="Announcement"
    Image=models.ImageField(upload_to='website/Announcements/images',default="")
    def __str__(self):
        return self.Announcement
    
    