from django.shortcuts import render
from django.http import HttpResponse
from app1.models import StudentDetails

def index1_view(request):
    data = StudentDetails.objects.all()
    context = {'data':data}
    return render(request,'index1.html',context)

def index2_view(request,id):
    data =  StudentDetails.objects.get(id = id)
    print(data.__dict__)
    context = {'data':data}
    return render(request,'index2.html',context) 

def index3_view(request):
    if request.method == "POST":
        name = request.POST['name']
        Roll_no = request.POST['Roll_no']
        Phone_no = request.POST['Phone_no']
        Standard = request.POST['Standard']
        Tamil = request.POST['Tamil']
        English = request.POST['English']
        Maths = request.POST['Maths']
        Science = request.POST['Science']
        Physics = request.POST['Physics']
        Chemistry = request.POST['Chemistry']
        StudentDetails.objects.create(Name = name, Roll_no = Roll_no, Phone_no = Phone_no, Standard = Standard, Tamil = Tamil, English = English, Maths = Maths, Science = Science, Physics = Physics, Chemistry = Chemistry)
        # return HttpResponse("created")
        return index1_view(request) 
    return render(request,'index3.html')

def update_view(request,id):
    data = StudentDetails.objects.get(id = id)
    if request.method == "POST":
        data.Standard = request.POST['Standard']
        data.Phone_no = request.POST['Phone_no']
        data.Tamil = request.POST['Tamil']
        data.English = request.POST['English']
        data.Maths = request.POST['Maths']
        data.Science = request.POST['Science']
        data.Physics = request.POST['Physics']
        data.Chemistry = request.POST['Chemistry']
        data.save()
        return index1_view(request) 
    context = {'data':data}
    return render(request,'update.html',context)

def delect_view(request,id):
    data = StudentDetails.objects.get(id=id)
    data.delete()
    return index1_view(request)     

def drop_down_view(request,Standard):
    std = StudentDetails.objects.filter(Standard=[10,11,12])
    print(std.__dict__)
    context = {'data':std}
    return index1_view(request,context)
