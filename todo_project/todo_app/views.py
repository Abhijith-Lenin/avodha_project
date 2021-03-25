from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import task
from . forms import Todoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    obj1=task.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        priority = request.POST['priority']
        date = request.POST['date']
        new = task(name=name, priority=priority,date=date)
        new.save()
    return render(request,"home.html",{'objects':obj1})

# def delete(request,taskid):
#     task1=task.objects.get(id=taskid)
#     if request.method == 'POST':
#         task1.delete()
#         return redirect('/')
#     return render(request,'delete.html',{'taskss':task1})

# def update(request,id):
#     tsk=task.objects.get(id=id)
#     forms=Todoforms(request.POST or None,instance=tsk)
#     if forms.is_valid():
#         forms.save()
#         return redirect('/')
#     return render(request,'update.html',{'task':tsk,'form':forms})

class Taskview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'objects'

class Detailslview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'j'
class Updateview(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('DetailsView',kwargs={'pk':self.object.id})
class Deleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = ('Taskview')
