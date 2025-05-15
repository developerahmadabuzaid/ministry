from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Activity

class ActivityListView(ListView):
    model = Activity
    template_name = 'activities.html'  # اسم ملف الـ HTML
    context_object_name = 'activities'  # اسم المتغير اللي رح تستعمله في التمبلت
    ordering = ['-date']  # ترتيب حسب التاريخ من الأحدث للأقدم
    
class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'activity_detail.html'
    context_object_name = 'activity'
def home(request):
    return render(request, 'home.html')

def strategies(request):
    return render(request, 'strategies.html')

def activities(request):
    activities = Activity.objects.all().order_by('-date')
    return render(request, 'activities.html',{'activities': activities})

def statements(request):
    return render(request, 'statements.html')

def contact(request):
    return render(request, 'contact.html')


