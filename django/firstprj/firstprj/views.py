from django.http import HttpResponse #HttpResponseRedirect
from django.shortcuts import render,redirect
from services.models import service
from news.models import newss
from form.models import forms
from django.core.paginator import Paginator



# django form
# from .forms import djangoform

# def home(request): # index file in main python folder
#     # return HttpResponse("index.html") # only shows string
#     data={
#         'title':'HTML',
#         'box1':'Header',
#         'box2':['PHP','JAVA','PYTHON'],
#         'box3':{'name':'anas','phone':12345},
#         'box4':[{'name':'anas','phone':12345},{'name':'amaan','phone':12345}],
#         'box5':[10,20,30,40,50,60,70,80,90],
#         'box6':[]
#         }
#     return render(request,"index.html",data) # show full html file #'' means main page
    
# def aboutus(request):
#     return HttpResponse('<i>hi world</i>') # myadmin/aboutus

# def course(request):
#     return HttpResponse('<b>hello world</b>') # myadmin/course
    
# def coursdetails(request,courseid): # myadmin/course/dynamic
#     return HttpResponse(courseid)



def main1(request):
    c={}
    try:

    # pagination
        x=service.objects.all()
        if request.method=="GET":
            pagi=Paginator(x,1)
            pgno=request.GET['page']
            if pgno!=None:
                final=pagi.get_page(pgno)
                count=pagi.num_pages
                c={'d':final,'e':count,'f':[n+1 for n in range(count)]}

    # search
        else:
            if request.method=="POST":
                b=request.POST["input"]
                if b!=None:
                    x=service.objects.filter(head__icontains=b)
                    c={'d':x}

    except:
        pass

    return render(request,"main1.html",c)



def main2(request):
    x=newss.objects.all()
    y={'z':x}
    return render(request,"main2.html",y)



def saveform(request):
    if request.method=="POST":
        v1=request.POST['name']
        v2=request.POST['phone']
        v3=request.POST['email']
        v4=request.POST['website']
        v5=request.POST['message']
        val=forms(name=v1,phone=v2,email=v3,website=v4,message=v5)
        val.save()
    return render(request,"main2.html")



# def news(request,urlid):
    # n1=newss.objects.get(id=urlid)
def news(request,slug):
    n1=newss.objects.get(slug=slug)
    n2={'n':n1}
    return render(request,"main6.html",n2)



def main3(request):
    val=''
    number={}
    try:
        if request.method=="POST":
            if request.POST['val']=='':
                return render(request,"main3.html",{'error':True})
            
            num=eval(request.POST['val'])
            if num<1:
                val='Not Prime'
            else:
                for i in range(2,num):
                    if num%i==0:
                        val='Not Prime'
                        break
                    else:
                        val='Prime'

            number={'vl':num,'op':val}
    except:
        pass

    return render(request,"main3.html",number)



def main4(request):
    ans=''
    data={}
    try:
        if request.method=="POST":
            if request.POST['num1']=='' or request.POST['num1']=='':
                return render(request,"main4.html",{'error':True})

            # n1=int(request.GET['num1'])     # way 1
            # n2=int(request.GET.get('num2')) # way 2
            n1=eval(request.POST['num1']) # way 1
            n2=eval(request.POST['num2']) # way 1
            op=request.POST.get('opr')    # way 2

            if op=="+":
                ans=n1+n2
            
            elif op=="-":
                ans=n1-n2
            
            elif op=="*":
                ans=n1*n2
            
            elif op=="/":
                ans=n1/n2

            data={'value1':n1,'value2':n2,'output':ans}
            
            # url="/?output={}".format(ans) 
             # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  
            # redirect:-
            # return HttpResponseRedirect("/about/") # same
            # return HttpResponseRedirect("/")       # same


            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            # return HttpResponseRedirect(url)       # same
            # return redirect(url)                     # same
    except:
        ans="Invalid"
    return render(request,"main4.html",data) 



def main5(request):
    total=''
    div=''
    result={}
    try:
        if request.method=="POST":
            if request.POST['sub1']=='' or request.POST['sub2']=='' or request.POST['sub3']=='' or request.POST['sub4']=='' or request.POST['sub5']=='':
                return render(request,"main5.html",{'invalid':True})

            m1=eval(request.POST['sub1'])
            m2=eval(request.POST['sub2'])
            m3=eval(request.POST['sub3'])
            m4=eval(request.POST['sub4'])
            m5=eval(request.POST['sub5'])

            total=m1+m2+m3+m4+m5
            per=total/500*100
            
            if 100>=per>=80:
                div='1st Division'
            elif 79>=per>=60:
                div='2nd Division'
            elif 59>=per>=40:
                div='3rd Division'
            elif 39>=per>=0:
                div='Fail'
            else:
                total="Invalid"
                per="Invalid"
                div="Invalid"

            result={'mk1':m1,'mk2':m2,'mk3':m3,'mk4':m4,'mk5':m5,'ttl':total,'ptg':per,'dvn':div}
    except:
        pass

    return render(request,"main5.html",result)



def main6(request):
    # a=service.objects.all()
    # a=service.objects.all().order_by('desc') # ascending
    # a=service.objects.all().order_by('-id')  # descending
    a=service.objects.all().order_by('head')  # descending

    # c=a[0],a[2] # show 1 n 3
    c=a[0:3:-1]   # reverse
    # for i in a:
        # print(i.head)

    data={'b':c}
    return render(request,"main6.html",data)

# def actionform(request):
#     ans=0
#     data={}
#     try:
#         if request.method=="POST":
#         #     # n1=int(request.GET['num1'])     # way 1
#         #     # n2=int(request.GET.get('num2')) # way 2
#             n1=int(request.POST['num1'])     # way 1
#             n2=int(request.POST.get('num2')) # way 2
#             ans=n1+n2
#             data={'value1':n1,'value2':n2,'output':ans}
#             # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             # return render(request,"main4.html",data) 
            
#             url="/?output={}".format(ans)

#             # return HttpResponseRedirect("/")       # address 1
#             # return HttpResponseRedirect("/about/") # address 2


#             # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             # return HttpResponseRedirect(url)       # same
#             return redirect(url)                     # same # this
#             # return HttpResponse(ans)               # or this
#     except:
#         pass
#     #################################

# django form
# def djangoform(request):
#     ans=0
#     fun1=fun2()
#     data={'fun3':fun1}
#     try:
#         if request.method=="POST":
#             n1=int(request.POST.get['num1'])
#             n2=int(request.POST.get('num2'))
#             ans=n1+n2
#             data={'fun3':fun1,'output':ans}
#             # data={'value1':n1,'value2':n2,'output':ans}
#             url="/?output={}".format(ans)
#             return redirect(url)
#     except:
#         pass
#     return render(request,"main4.html",data) 