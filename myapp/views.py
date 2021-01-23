from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from .models import Education
from .models import Experience
from .models import Award
from.models import About
from.models import Number
from.models import Project
from .models import Query
from .models import Catagory
from .models import Blog
from .models import Comment
from .models import Skill
import datetime
from .models import Image


from .templatetag import custom_tags


# Create your views here.
def index(request):
    abouts=About.objects.all()
    eduations=Education.objects.all().order_by('id')
    experiences=Experience.objects.all()
    awards = Award.objects.all()
    numbers=Number.objects.all()
    projects = Project.objects.all()
    lalitpurs = Blog.objects.all()
    skills= Skill.objects.all().order_by('id')
    images=Image.objects.all().order_by('id')




    return render(request,'index.html',{'eduations':eduations,'experiences':experiences,'awards':awards,'abouts':abouts,'numbers':numbers,'projects':projects,'lalitpurs':lalitpurs,'skills':skills,'images':images})



def add(request):
    name = request.POST['name']
    subject = request.POST['subject']
    email=request.POST['email']
    mesg = request.POST['message']
    someth=Query(name=name, email=email, subject=subject,mesg=mesg)
    someth.save()
    send_mail(name,
              'Thankyou for your message',
              'pradipchapagain123@gmail.com',
              [ email])
    return  render(request,'index.html')

def single(request,id):
      if request.POST:
          name=request.POST['name']
          email=request.POST['email']
          cmnt=request.POST['message']
          post_id =id
          query=Comment(name=name,email=email,cmnt=cmnt)
          query.post_id_id = post_id
          query.save()


      datas=Blog.objects.get(id=id)
      batas=[datas]
      lalitpurs = Blog.objects.all()
      categories=Catagory.objects.all()
      comments=Comment.objects.all().filter(post_id=id)
      return  render(request,'single.html',{'batas':batas,'lalitpurs': lalitpurs,'categories':categories,'comments':comments})




