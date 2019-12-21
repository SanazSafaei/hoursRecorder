from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import WorksPackage
from .models import Work

# Create your views here.

def home(request):
    packs=WorksPackage.objects.all()
    return render(request, 'HomePage.html', {"packs": packs})

def work_view(request,pk):
    packs = WorksPackage.objects.all()
    works=Work.objects.filter(work=pk)
    return render(request,'HomePage.html',{"packs":packs,"works":works,"pk":pk})

def make_package(request):
    wp=WorksPackage(date=timezone.now())
    wp.save()
    packs = WorksPackage.objects.all()
    return render(request, 'HomePage.html', {"packs": packs,"pk": wp.pk})

def make_work(request,pk):
    if request.method == "POST":
        Package=get_object_or_404(WorksPackage,pk=pk)
        package_works=Work.objects.filter(work=Package)
        if(package_works):
            last_one=package_works[len(package_works)-1]
            last_one.end=timezone.now()
            last_one.save()
        w=Work(name=request.POST.get("input"),start=timezone.now(),end=None,work=Package)
        w.save()
        return redirect("boards:work",pk=pk)

def done(request,pk):
    if request.method == "POST":
        Package = get_object_or_404(WorksPackage, pk=pk)
        package_works = Work.objects.filter(work=Package)
        last_one = package_works[len(package_works)-1]
        last_one.end = timezone.now()
        last_one.save()
        print("heloooo22")
        return redirect("boards:work",pk=pk)
