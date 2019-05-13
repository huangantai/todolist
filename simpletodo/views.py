from django.shortcuts import render,render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from simpletodo.models import Todo
# Create your views here.

def todolist(request):
  todolist=Todo.objects.filter(flag=1)
  finishtodos=Todo.objects.filter(flag=0)
  return render_to_response('simpletodo.html',{'todolist':todolist,'finishtodos':finishtodos})

def todofinish(request,id=''):
  todo=Todo.objects.get(id=id)
  if todo.flag==1:
    todo.flag=0
    todo.save()
    return HttpResponseRedirect('/simpletodo/')
  todolist=Todo.objects.filter(flag=1)
  return render_to_response('simpletodo.html', {'todolist': todolist})

def todoback(request,id=''):
  todo=Todo.objects.get(id=id)
  if todo.flag==0:
    todo.flag=1
    todo.save()
    return HttpResponseRedirect('/simpletodo/')
  todolist = Todo.objects.filter(flag=1)
  return render_to_response('simpletodo.html', {'todolist': todolist})

def tododelete(request,id=''):
  try:
    todo=Todo.objects.get(id=id)
  except Exception:
    raise Http404
  if todo:
    todo.delete()
    return HttpResponseRedirect('/simpletodo/')
  todolist = Todo.objects.filter(flag=1)
  return render_to_response('simpletodo.html', {'todolist': todolist})

def addtodo(request):
  if request.method=='POST':
    atodo=request.POST['todo']
    priority=request.POST['priority']
    if not priority:priority=0
    user = User.objects.get(id='1')
    todo = Todo(user=user, todo=atodo, priority=priority, flag=1)
    todo.save()
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render_to_response('showtodo.html',{'todolist': todolist, 'finishtodos': finishtodos})   
  else:
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render_to_response('simpletodo.html',{'todolist': todolist, 'finishtodos': finishtodos})

def updatetodo(request,id=''):
  if request.method == 'POST':
    atodo = request.POST['todo']
    priority = request.POST['priority']
    user = User.objects.get(id='1')
    todo=Todo.objects.get(id=id)
    todo.todo=atodo
    todo.priority=priority
    todo.save()
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render_to_response('simpletodo.html',{'todolist': todolist, 'finishtodos': finishtodos})
  else:
    try:
      todo = Todo.objects.get(id=id)
    except Exception:
      raise Http404
    return render_to_response('updatatodo.html', {'todo': todo})
