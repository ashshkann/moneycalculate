import datetime
from django.http.response import HttpResponseServerError
from django.shortcuts import render, redirect
from .models import creat_todo_models
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def views_todo(request):
    todo_models =  creat_todo_models.objects.all()
    context = {
        'todo_models': todo_models,
    }
    return render(request, 'todo.html', context)

@login_required(login_url='/login')
def creat_todo(request):
    data_time = datetime.datetime.now()
    start_time = request.POST['StartTime']
    end_time = request.POST['EndTime']
    # data_start = int(start_time.replace(":",""))
    # data_end = int(end_time.replace(":",""))
    # data_calculate = data_end - data_start
    # print(data_calculate)
    # print(start_time, end_time)
    s1 = start_time
    s2 = end_time
    FMT = '%H:%M'
    tdelta = datetime.datetime.strptime(s2, FMT) - datetime.datetime.strptime(s1, FMT)
    data_str =  str(tdelta)
    find_data = data_str.replace(":00","")
    data_models = creat_todo_models(todo_start_time=start_time, todo_day=data_time.strftime("%A"), todo_end_time=end_time, todo_date=data_time.strftime("%d/%m/%Y"), todo_all_time=find_data)
    data_models.save()
    return HttpResponseRedirect('/todo-list/')

@login_required(login_url='/login')
def delet_todo(request, todoid):
    delete_data = creat_todo_models.objects.get(id=todoid)
    delete_data.delete()
    return HttpResponseRedirect('/todo-list/')

