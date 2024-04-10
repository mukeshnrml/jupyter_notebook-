
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1 style=color:blue;>This is NSTI Dehradun</h1>")


def home(request):
    return render(request,'index.html')



def home(request):
    return render(request,'form.html')





def form(request):
    c = 0
    try:
        a = int(request.GET.get('first'))
        b = int(request.GET.get('second'))
       
        c = a+b

    except:
        pass 


    return render(request, 'form.html', {'sum':c})
    #return redirect(request, 'index.html')


    def regs(request):
        inp = ''
        try:
            a = request.POST.get('name')
            b = request.POST.get('mail')
            c = request.POST.get('phone')
            inp = 'Thank you for registration' + a 
            d = '/thank/?output={}'.format(inp)
            e = {'message'}
            return redirect(d)
        
        except:pass

        return render(request,'reg.html',{'message':inp})
    

    def form1(request):
        a = register()
        b = {'form':a}
        
            