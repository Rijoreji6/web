from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .models import DigitData
from .models import StringData
from .models import AlphaData

# Create your views here.
def home(request):
    if request.method == 'POST':
        data=DigitData()
        string=StringData()
        alpha=AlphaData()
        val=request.POST.get('data')
        if val.isnumeric():
            print('digit')
            data.digit=val
            data.save()
        elif val.isalpha():
            print('str')
            string.string=val
            string.save()
        elif val.isalnum():
            print('aplha')
            alpha.alpha=val
            alpha.save()
        else:
            return render(request,'home.html',{'msg':'enter correct data!'})
            
    data_digit=DigitData.objects.all()
    # print(data_digit)
    str_data=StringData.objects.all()
    alpha_data=AlphaData.objects.all()
    
    return render(request,'home.html',{'data_digit':data_digit,'str_data':str_data,'alpha_data':alpha_data})

def delete_num(request,id):
    print(id)
    dl1=DigitData.objects.get(id=id)
    dl1.delete()
    return HttpResponseRedirect('/')

def delete_str(request,id):
    print(id)
    dl2=StringData.objects.get(id=id)
    dl2.delete()
    return HttpResponseRedirect('/')
def delete_al(request,id):
    print(id)
    dl3=AlphaData.objects.get(id=id)
    dl3.delete()
        
    return HttpResponseRedirect('/')