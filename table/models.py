from django.db import models
from django_random_id_model import RandomIDModel
from django.contrib.postgres.fields import ArrayField
class login_table(models.Model):
    id = models.IntegerField(primary_key = True)
    password = models.CharField(max_length = 20)
    dept_name =  models.CharField(max_length = 6)
    pos = models.CharField(max_length = 10)
    curr_pos = models.CharField(max_length = 10)
    ##def __str__(self):
        ##return self.name


class login_time(models.Model):
    pro_id = models.IntegerField(primary_key = False)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    #ID = models.ForeignKey('Login_table.ID', on_delete=models.CASCADE)
    ##def __str__(self):
        ##return self.name


class num_of_leaves(models.Model):
    pro_id = models.IntegerField(primary_key = False)
    leaves = models.IntegerField(primary_key = False)
    #ID = models.ForeignKey('Login_table.ID', on_delete=models.CASCADE)
   ##def __str__(self):
        ##return self.name


class cur_running(models.Model):
    id = models.IntegerField(primary_key = True)
    pro_id = models.IntegerField(primary_key = False)
    datefrom = models.DateField(auto_now = False, auto_now_add = False)
    dateto = models.DateField(auto_now = False, auto_now_add = False)
    num_of_days = models.IntegerField(primary_key = False)
    reason = models.TextField(blank = True)
    #Pro_id = models.ForeignKey('Login_table.ID', on_delete=models.CASCADE)
    ##def __str__(self):
        ##return self.name


class app_status(models.Model):
    id = models.IntegerField(primary_key = True, unique = True)
    status = models.CharField(max_length = 10)
    #ID = models.ForeignKey('Cur_running.ID', on_delete=models.CASCADE)
    ##def __str__(self):
        ##return self.name


class cse_dep(models.Model):
    id = models.IntegerField(primary_key = True)
    pro_id = models.IntegerField(primary_key = False)
    datefrom = models.DateField(auto_now = False, auto_now_add = False)
    dateto = models.DateField(auto_now = False, auto_now_add = False)
    num_of_days = models.IntegerField(primary_key = False)
    reason = models.TextField(blank = True)
    ##def __str__(self):
        ##return self.name


class ee_dep(models.Model):
    id = models.IntegerField(primary_key = True)
    pro_id = models.IntegerField(primary_key = False)
    datefrom = models.DateField(auto_now = False, auto_now_add = False)
    dateto = models.DateField(auto_now = False, auto_now_add = False)
    num_of_days = models.IntegerField(primary_key = False)
    reason = models.TextField(blank = True)
    ##def __str__(self):
        ##return self.name


class mec_dep(models.Model):
    id = models.IntegerField(primary_key = True)
    pro_id = models.IntegerField(primary_key = False)
    datefrom = models.DateField(auto_now = False, auto_now_add = False)
    dateto = models.DateField(auto_now = False, auto_now_add = False)
    num_of_days = models.IntegerField(primary_key = False)
    reason = models.TextField(blank = True)
    ##def __str__(self):
        ##return self.name


class hoddean(models.Model):
    id = models.IntegerField(primary_key = True)
    pro_id = models.IntegerField(primary_key = False)
    datefrom = models.DateField(auto_now = False, auto_now_add = False)
    dateto = models.DateField(auto_now = False, auto_now_add = False)
    num_of_days = models.IntegerField(primary_key = False)
    reason = models.TextField(blank = True)
    ##def __str__(self):
        ##return self.name


class cse_hod(models.Model):
    id = models.IntegerField(primary_key = True)
    comm = models.TextField(blank = True)
    status =models.CharField(max_length = 10)
    #ID = models.ForeignKey('CSE_dep.ID', on_delete=models.CASCADE)
    ##def __str__(self):
        ##return self.name


class ee_hod(models.Model):
    id = models.IntegerField(primary_key = True)
    comm = models.TextField(blank = True)
    status =models.CharField(max_length = 10)
    #ID = models.ForeignKey('EE_dep.ID', on_delete=models.CASCADE)
    ##def __str__(self):
        ##return self.name


class mec_hod(models.Model):
    id = models.IntegerField(primary_key = True)
    comm = models.TextField(blank = True)
    status =models.CharField(max_length = 10)
    #ID = models.ForeignKey('MEC_dep.ID', on_delete=models.CASCADE)
    ##def __str__(self):
        ##return self.name

class hod_dean(models.Model):
    id = models.IntegerField(primary_key = True)
    pro_id = models.IntegerField(primary_key = False)
    datefrom = models.DateField(auto_now = False, auto_now_add = False)
    dateto = models.DateField(auto_now = False, auto_now_add = False)
    num_of_days = models.IntegerField(primary_key = False)
    reason = models.TextField(blank = True)
    #Pro_id = models.ForeignKey('Login_table.ID', on_delete=models.CASCADE)
    ##def __str__(self):
        ##return self.name


class dean(models.Model):
    id = models.IntegerField(primary_key = True)
    comm = models.TextField(blank = True)
    status =models.CharField(max_length = 10)
    #ID = models.ForeignKey('HOD_dean', on_delete=models.CASCADE)
    ##def __str__(self):
        ##return self.name


class director(models.Model):
    id = models.IntegerField(primary_key = True)
    comm = models.TextField(blank = True)
    status =models.CharField(max_length = 10)
    #ID = models.ForeignKey('hoddean', on_delete=models.CASCADE)
    ##def __str__(self):
        ##return self.name

class appid(models.Model):
    pro_id = models.IntegerField(primary_key = False)
    app_id = models.IntegerField(primary_key = False)
    

class hodapp(models.Model):
    app_id =  models.IntegerField(primary_key = True)
    pro_id =  models.IntegerField(primary_key = False)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)

class deanapp(models.Model):
    app_id =  models.IntegerField(primary_key = True)
    pro_id =  models.IntegerField(primary_key = False)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)


class dirapp(models.Model):
    app_id =  models.IntegerField(primary_key = True)
    pro_id =  models.IntegerField(primary_key = False)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)


class proffesor(models.Model):
    pro_id = models.IntegerField(primary_key = True)
    dept_name = models.CharField(max_length = 50)
    pos = models.CharField(max_length = 50,default = 'CSE')
    name  = models.CharField(max_length = 50)
    emailid = models.EmailField()
    biography = models.TextField()
    linkedin = models.URLField(max_length = 200)
    contactnumber = models.CharField(max_length = 12)
    courses = ArrayField(ArrayField(models.CharField(max_length=10, blank=True),size=2),size=8)
    qualifications = ArrayField(ArrayField(models.CharField(max_length=10, blank=True),size=4),size=8)
    
class education(models.Model):
     pro_id = models.IntegerField(primary_key = True)
     institute = models.CharField(max_length = 200)
     datefrom = models.DateField(auto_now = False, auto_now_add = False)
     dateto = models.DateField(auto_now = False, auto_now_add = False)
     major = models.CharField(max_length = 200)

class course(models.Model):
     pro_id = models.IntegerField(primary_key = True)
     courseid = models.CharField(max_length = 200)
     coursename = models.CharField(max_length = 200)


class educationproff(models.Model):
     pro_id = models.IntegerField(primary_key = False)
     institute = models.CharField(max_length = 200)
     datefrom = models.DateField(auto_now = False, auto_now_add = False)
     dateto = models.DateField(auto_now = False, auto_now_add = False)
     major = models.CharField(max_length = 200)

class courseproff(models.Model):
     pro_id = models.IntegerField(primary_key = False)
     courseid = models.CharField(max_length = 200)
     coursename = models.CharField(max_length = 200)
