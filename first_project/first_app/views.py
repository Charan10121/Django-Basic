from django.db.models import indexes
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *
from first_app.models import Topic,Webpage,AccessRecord

# Create your views here.
def myfirstpage(request):
    webpage_list=AccessRecord.objects.order_by('date')  #order_by is from sql
    date_dict={'access_records':webpage_list, 'text':"Hello World"}
    return render(request,'index.html',context=date_dict)

def error_404_view(request,exception):
    return render(request,'404.html')

def myfunctioncall(request):
    return HttpResponse("Hello world")


def myfuncabout(request):
    return HttpResponse("About")


def add(request, a, b):
    # make sure that parameters are same as the ones declared in urls.py
    return HttpResponse(a+b)


def intro(request, name, age):
    mydictionary = {
        "name": name, "age": age
    }
    return JsonResponse(mydictionary)  # must define a dictionary to pass this


def mysecondpage(request):
    return render(request, "second.html")


def mythirdpage(request):
    var = "hello world"
    fruits = ['apple', 'mango', 'grape']
    num1, num2 = 2, 5
    ans = num1+num2
    mydict = {
        "varkey": var,
        "myfruits": fruits,
        "num1": num1,
        "num2": num2,
        "answer": ans
    }
    return render(request, "third.html", context=mydict)


def myimagepage(request):
    return render(request, "imagepage.html")


def myimagepage2(request):
    return render(request, "imagepage2.html")


def myimagepage3(request, imagename):
    imagename = imagename.lower()
    if(imagename == "spidey"):
        var = True
    elif(imagename == 'weeknd'):
        var = False
    mydict = {
        'variable': var
    }
    return render(request, "imagepage3.html", context=mydict)


def myformpage(request):
    return render(request, "formpage.html")


def submitmyform(request):
    mydict = {
        "var1": request.POST['mytext'],  # give name of text
        "var2": request.POST['mytextarea'],  # give name of textarea
        'method': request.method
    }
    return JsonResponse(mydict)


def myform2(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if (form.is_valid()):
            title = request.POST['title']  # or request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            mydict = {
                'formkey': FeedbackForm()
            }
            errorflag = False
            Errors = []
            if title != title.upper():
                errorflag = True
                Errors.append('Title must be capital')
            import re
            regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$' #regex for email
            if not re.search(regex,email):
                errorflag = True
                Errors.append('Not valid email')

            if errorflag==False:
                mydict['success'] = True
                mydict['successmsg']='Form Submitted'
                return render(request, "formpage2.html", context=mydict)
            else:
                mydict['error'] = True
                mydict['errors'] = Errors
                return render(request, "formpage2.html", context=mydict)


    elif request.method == 'GET':
        form=FeedbackForm()  # an object 'form' is created
        mydict={
            'formkey': form
        }
        return render(request, "formpage2.html", context=mydict)


# def users(request):
#     form = NewUserform()

#     if request.method == 'POST':
#         form = NewUserform(request.POST)
#         if (form.is_valid()):
#             form.save(commit=True)
#             return myfirstpage(request)
#         else:
#             print('Error form invalid')

#     return render(request,'users.html',{'form':form})