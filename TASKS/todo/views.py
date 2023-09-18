from django.shortcuts import render, redirect
from datetime import date
from todo.forms import modelform
from .models import Task

def home(request):
    obj = Task.objects.order_by('date')
    if request.method == 'POST':
        task = request.POST['task']
        prio = request.POST['prio']
        taskdate = request.POST['date']
        if not taskdate:
            taskdate = date.today()

        s = Task(task=task, prio=prio, date=taskdate)
        s.save()

    return render(request, 'index.html', {'obj': obj})

def delete(request, id):
    if request.method == 'POST':
        obj = Task.objects.get(id=id)
        obj.delete()
        return redirect('/')
    
    return render(request, 'delete.html')

from django.shortcuts import render, redirect
from datetime import date
from todo.forms import modelform
from .models import Task

def update(request, id):
    obj = Task.objects.get(id=id)
    
    if request.method == 'POST':
        form = modelform(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            taskdate = form.cleaned_data['date']
            if not taskdate:
                taskdate = date.today()  
            obj.date = taskdate  
            obj.save()
            return redirect('/')
    else:
        form = modelform(instance=obj)
    
    
    if not form['date'].value():
        today_date = date.today()
    else:
        today_date = None
    
    return render(request, "update.html", {'form': form, "obj": obj, 'today_date': today_date})

