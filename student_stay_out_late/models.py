from django.db import models
class stuinfo(models.Model):
    userid = models.CharField(primary_key=True,max_length=45)
    username=models.CharField(max_length=45, blank=True, null=True)
    gender= models.CharField(max_length=1, blank=True, null=True)
    classname = models.CharField(max_length=45, blank=True, null=True)
    major=models.CharField(max_length=45, blank=True, null=True)
    department=models.CharField(max_length=45, blank=True, null=True)
    permise=models.CharField(max_length=5, blank=True, null=True)
    fudaoyuanid=models.CharField(max_length=45, blank=True, null=True)
    fudaoyuanname=models.CharField(max_length=45, blank=True, null=True)
class Vthdpass(models.Model):
    userid = models.ForeignKey(stuinfo)
    passinout = models.IntegerField(blank=True, null=True)
    passdtday = models.CharField(max_length=45, blank=True, null=True)
    passdttime = models.CharField(max_length=45, blank=True, null=True)
    passdt=models.DateTimeField(blank=True, null=True)
class Timesetting(models.Model):
    starttime=models.CharField(max_length=45, blank=True, null=True)
    latetime=models.CharField(max_length=45, blank=True, null=True)
class Care(models.Model):
    caretime=models.DateTimeField(auto_now=True)
    carecontent=models.CharField(max_length=100,blank=True,null=True)
class Explain(models.Model):
    explaintime=models.DateTimeField(auto_now=True)
    explaimcontent=models.CharField(max_length=100,blank=True,null=True)
    ifagree=models.IntegerField(default=0)
class Passresults(models.Model):
    userid = models.ForeignKey(stuinfo)
    passinout = models.IntegerField(blank=True, null=True)
    passdtday = models.CharField(max_length=45, blank=True, null=True)
    tasktype= models.CharField(max_length=50, blank=True, null=True)
    passdttime= models.CharField(max_length=50, blank=True, null=True)
    lastpasstime= models.DateTimeField(blank=True, null=True)
    care=models.ForeignKey(Care,blank=True,null=True)
    explain=models.ForeignKey(Explain,blank=True,null=True)


