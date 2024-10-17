from django.shortcuts import render,redirect

# Create your views here.
from research.models import teacher,researchpapers
from django.contrib import messages
from django.http import HttpResponse
from .forms import paperform

# Create your views here.
def home(request):
    return render(request,"homepage.html")

def login(request) :
    if request.method=='POST' :
        global username
        username=request.POST['username']
        password=request.POST['password']
        teach_list=teacher.objects.all()
        for i in teach_list :
            if i.email==username and i.password==password:
                return redirect("/teacherview")
        else :
            messages.info(request,'Invalid username or password')
            return redirect('/login')
    else  :
        return render(request,'login.html')

def teachview(request) :
    research=researchpapers.objects.all()
    return render(request,'teachview.html',{'research':research,'username':username})

def delete(request, id):
        record_to_delete =researchpapers.objects.get(id=id)
        record_to_delete.delete()
        return redirect('/teacherview/')

def edit(request, id):
    research=researchpapers.objects.get(id=id)
    return render(request, 'edit.html', {'research':research})

def update(request,id) :
    research=researchpapers.objects.get(id=id)
    form=paperform(request.POST,instance=research)
    if (form.is_valid()):
        form.save()
        return redirect('/teacherview/')
    return render(request,'edit.html',{'research':research,'username':username})

def add(request):
    research=researchpapers.objects.all()
    for i in research:
        if i.temail==username:
            res=i
            break
    res.pk=None
    res.save()
    return render(request, 'add.html', {'res':res})

def addnew(request,id):
    research=researchpapers.objects.get(id=id)
    form=paperform(request.POST,instance=research)
    if (form.is_valid()):
        form.save()
        return redirect('/teacherview/')
    return render(request,'add.html',{'research':research})


def viewers_page(request):
    research = researchpapers.objects.all()
    research_math = set()
    research_cse = set()
    research_eee = set()
    research_it = set()

    for i in research:
        if i.tdept == 'Mathematics':
            research_math.add(i.tname)
        elif i.tdept == 'CSE':
            research_cse.add(i.tname)
        elif i.tdept == 'IT':
            research_it.add(i.tname)
        elif i.tdept == 'EEE':
            research_eee.add(i.tname)

    return render(request, 'viewers.html', {'research_math': research_math,'research_cse': research_cse,'research_it': research_it,'research_eee': research_eee})

def viewers_info(request,name) :
    research=researchpapers.objects.filter(tname=name)
    return render(request, 'view2.html', {'research':research})
