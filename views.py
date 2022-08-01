
from django.shortcuts import render
from django.shortcuts import HttpResponse
from enterdata.models import Info
from django.contrib import messages

def InsertData(request):
    if request.method == 'POST':
        if request.POST.get('uname') and request.POST.get('upassword'):
            tobesaved = Info()
            tobesaved.uname=request.POST.get('uname')
            tobesaved.upassword=request.POST.get('upassword')

            tobesaved.save()
            messages.success(request,'your data is stored sucessfuly')
            return render(request,'index.html')
        else:
            return render(request,'index.html')
    else:
        return render(request,'index.html')
        messages.failure(request,'your data is not been stored')


            

            



