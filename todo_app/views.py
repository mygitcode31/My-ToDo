from django.http import HttpResponseRedirect

from django.shortcuts import render

from todo_app.models import Todo

# Create your views here.
def todo_list(request):
    # request is helping to show the data
    todos = Todo.objects.all()   # select * from todo;   => yasle sabae todo dinxa
    return render(
        request,
        "bootstrap/todo_list.html",  #tamplet name
        {"todos": todos},  # data
    )

#for delete function
def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect("/")


# for create
def todo_create(request):
   # print(request.method, request.POST)
   if request.method == "GET":
    return render(request, "bootstrap/todo_create.html")
   
   else:
      Todo.objects.create(title=request.POST["title"])
      return HttpResponseRedirect("/")
   
   # for update
def todo_update(request, id):
   # print(request.method, request.POST)
   if request.method == "GET":
    todo = Todo.objects.get(id=id)
    return render(
       request,
         "bootstrap/todo_update.html",
         {"todo": todo},
         )
   
   else:
      todo = Todo.objects.get(id=id)
      todo.title = request.POST["title"]
      todo.save()
      return HttpResponseRedirect("/")
