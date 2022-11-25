from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .models import myfrd

# Create your views here.

def InsertPageView(request):
    return render(request,"app/insert.html")


#Data come from html to view
def InsertData(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    dob = request.POST['dob']
    email = request.POST['email']
    contact = request.POST['contact']

# Creating object of Model Class
# Inserting Data into table

    newuser = myfrd.objects.create(FirstName = fname , LastName=lname ,DOB = dob , Email = email , Contact =contact)

# After Insert render on showpage view

    return redirect('showpage')

#Show Page View
def ShowPage(request):

    # Select * from Table Name
    # For fetching all the data of the table
    all_data = myfrd.objects.all()
    
    return render(request,"app/show.html",{'key1':all_data})

# Edit Page View

def EditPage(request,pk):
    # Fetching the data of particular ID
    get_data = myfrd.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})

# Update Data View
def UpdateData(request,pk):
    Udata = myfrd.objects.get(id=pk)
    Udata.FirstName = request.POST['fname']
    Udata.LastName = request.POST['lname']
    Udata.DOB = request.POST['dob']
    Udata.Email = request.POST['email']
    Udata.Contact = request.POST['contact']
    # Query for Update
    Udata.save()
    # Render to Show Page
    return redirect('showpage')

# Delete Data View

def DeleteData(request,pk):
    ddata = myfrd.objects.get(id=pk)
    # Query for Delete
    ddata.delete()
    return redirect('showpage')

# def SearchView(request):
#     #allPost = myfrd.objects.all()
#     query = request.GET['query']
#     allPost = myfrd.objects.filter(title__icontains=query)
#     params = {'allPosts':allPost}
#     return render(request,"app/search.html",params)

def SearchView(request):
    all_data = myfrd.objects.all()
    if request.method =="GET":
        st=request.GET.get('search')
        if st!=None:
            form=myfrd.objects.filter(FirstName__icontains=st)
    return render(request,"app/show.html",{'key3':all_data}) 
    



    








