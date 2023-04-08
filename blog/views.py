from django.shortcuts import render
from .models import IndexCounts,IndexHero,IndexSection,IndexWhysection,Courses,Trainers,Testimonials

# Create your views here.



from django.http.response import HttpResponse

# from .models import Courses,Trainer,Testimonials,Pricing
# aynı klasörün içinde views ve models bu şekilde import edilir  

# Create your views here.
# bu fonksiyon sadece index home sayfası çağırılınca çalışıyor courses sayfası burayı görmüyordu 

def index(request):
    context={
        'indexhero':IndexHero.objects.all(),
        'indexsection':IndexSection.objects.all(),
        'indexcounts':IndexCounts.objects.all(),
        'indexwhysection':IndexWhysection.objects.all(),
        'courses':Courses.objects.filter(is_home=True),
        'trainers':Trainers.objects.filter(is_home=True)

    }
   
    return render(request, 'partials/index.html',context)

def search (request):
    context={
        'indexhero':IndexHero.objects.all(),
        'indexsection':IndexSection.objects.all(),
        'indexcounts':IndexCounts.objects.all(),
        'indexwhysection':IndexWhysection.objects.all(),
        'courses':Courses.objects.filter(is_home=True),
        'trainers':Trainers.objects.filter(is_home=True)

    }
   
    return render(request, 'partials/index.html',context)

def about(request):
    context={
        'testimonials':Testimonials.objects.all(),
        'indexsection':IndexSection.objects.all(),
        'indexcounts':IndexCounts.objects.all()
    }
    
    return render(request,'partials/about.html',context)

def course_details(request):
    
    
    return render(request,'partials/course-details.html')
    




def trainers(request):
    context={
        "trainers":Trainers.objects.all()
    }
    
    return render(request,'partials/trainers.html',context)

def contact(request):
    return render(request,'partials/contact.html')

def courses(request):
    context={
        "courses":Courses.objects.all() # değişken burda courses ama sayfada blog amk 
    }
    
    return render(request,'partials/courses.html',context)

def pricing(request):
    # context={
    #     "pricing":Pricing.objects.all()
    # }
    return render(request,'partials/pricing.html')


