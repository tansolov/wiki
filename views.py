import re
from django.shortcuts import render, redirect
import random
import markdown2
from django import forms
from django.http import HttpResponseRedirect 
from django.core.files.storage import default_storage
from django.urls import reverse


from . import util
class NewPageForm(forms.Form):
   newpage=forms.CharField(label="New Task")


def index(request):
    return render(request, "encyclopedia/index.html", {"entries":util.list_entries(),
      })
def entries(request,name):
        print(request)
        return render(request,"encyclopedia/wiki.html",{
        "entries": markdown2.markdown(util.get_entry(name)),"title":name})

def search(request):
  _, filenames = default_storage.listdir("entries")
  list=util.list_entries()
  if request.POST.get('q'):
        name=request.POST.get('q')
        if(name in list):
          return render(request,"encyclopedia/wiki.html",{
        "entries": markdown2.markdown(util.get_entry(name))})
        else:
          for i in range(len(list)) :
            res=[sub for sub in list[i] if sub in name]
            if(len(res)==len(name)):
                    print(len(res)," ",len(name))
                    return render(request,"encyclopedia/index.html",{
         "entry": list[i], "kol":1} )
  else:
      i=random.randrange(0,len(list))
      name=list[i]
      return render(request,"encyclopedia/wiki.html",{
        "entries": markdown2.markdown(util.get_entry(name))})  
    
def get_newpage(request):
     if request.method=="POST":
       title=request.POST.get('newtitle')
       content=request.POST.get('newpage')
       print("title=",title)
       print("content=",content)
       util.save_entry(title, content)
       return render(request,"encyclopedia/index.html")

     return render(request,"encyclopedia/get.html")
def edit_page(request,name):
     '''
     if request.method=="POST":
       title=request.POST.get('edittitle')
       content=request.POST.get('editpage')
       print("title=",title)
       print("content=",content)
       return render(request,"encyclopedia/wiki/edit.html")
     else:
     print("title=",title)        
     util.get_entry(title)
     '''
     f = default_storage.open(f"entries/{name}.md")
     content=f.read().decode("utf-8")
     return render(request,"encyclopedia/edit.html",{"title":name,"content":content})

def get_edit(request,name):      
    if request.method=="POST":
       title=name
       content=request.POST.get('page')
       print("title=",title)
       print("content=",content)
       util.save_entry(title, content)
       return render(request,"encyclopedia/wiki.html",{"title":name})
       '''
       return HttpResponseRedirect(reverse("wiki:entry"),{"entry":title})      
       '''
        

    
 
