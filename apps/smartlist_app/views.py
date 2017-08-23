from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import error
import bcrypt
import pprint
from googleapiclient.discovery import build
from models import *

def index(request):
    return render(request,'smartlist_app/index.html')

def dashboard(request):
    todos = Todo.objects.filter(created_by=1)
    context = {
        "todos":todos,
    }
    return render(request,'smartlist_app/dashboard.html', context)

def add_todo(request):
    request.session["query"] = request.POST["query"]
    user_id = User.objects.get(id=1)
    todo = Todo.objects.create(name=request.session["query"], created_by=user_id)
    resources = main(request)
    for r in resources:
        Resource.objects.create(title=r["title"], link=r["link"], snippet= r["snippet"], resource_owner=todo)


    return redirect("/dashboard")

def main(request):
    #build the the service url
    res = []
    if "query" in request.session:
        service = build("customsearch", "v1",
                developerKey="AIzaSyAR8ys4lyNRUgoPbqQpycajlv1j4PiOGPk")

        res = service.cse().list(

          q=request.session["query"],
          cx="005614876608685890370:czwekc7ki7q",
        ).execute()
        return res["items"]
    else:
        return res

def delete_todo(request,id):
    Todo.objects.get(id=id).delete()
    return redirect("/dashboard")

def delete_resource(request,id):
    Resource.objects.get(id=id).delete()
    return redirect("/dashboard")

def history(request):
    return render(request,'smartlist_app/history.html')
