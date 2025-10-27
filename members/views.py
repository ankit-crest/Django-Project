from django.forms.models import model_to_dict
from django.shortcuts import render,loader,redirect
from django.http import HttpResponse,JsonResponse
import django.template
import django.template.context_processors
from members.models import Members
# Create your views here.

def index(request):
    members = Members.objects.all()
    
    # gls_objects = members
    # data = []
    # for obj in gls_objects:
    #     data.append({"id": obj.id, "name": obj.name, "age": obj.age})
    # return JsonResponse(data, safe=False)                

    return render(request,'index.html',{'members':members})

def add_members(request):
    members = Members(name="Name",age=10,city="City")
    members.save()
    
    members_list = Members.objects.all()
    data = []
    for obj in members_list:
        data.append({
            "id": obj.id,
            "firstName": obj.name,
            "age": obj.age,
            "city":obj.city
        })
    return JsonResponse(data , safe=False)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')

        return JsonResponse({'name': name, 'age': age, 'city': city}, safe=False)

    context = {}
    return render(request, 'members/create.html', context)  
def store(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')

        Members(name=name,age=age,city=city).save()
    return redirect('members:index') 

def delete(request,id):
    Members.objects.filter(id=id).delete()
    return redirect('members:index') 

def edit(request,id):
    members=Members.objects.get(id=id)
    return render(request, 'members/edit.html', {'data':members})  
def update(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        Members.objects.filter(id=id).update(name=name,age=age,city=city)
    return redirect('members:index') 

def ajax_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        Members(name=name,age=age,city=city).save()
        return JsonResponse({'message':'success'}, safe=False)
    return render(request, 'members/ajax/create.html')

def getlist(request):
    members = Members.objects.all().values()
    return JsonResponse({'members': list(members)}, safe=False)
def ajax_delete(request,id):
    Members.objects.filter(id=id).delete()
    return JsonResponse({'message':'successfully delete'}, safe=False)

def ajax_edit(request,id):
    members = Members.objects.get(id=id)
    return JsonResponse({'members':model_to_dict(members)}, safe=False)

def ajax_update(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        Members.objects.filter(id=id).update(name=name,age=age,city=city)
    return JsonResponse({'message':'successfully update'}, safe=False)