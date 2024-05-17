from django.shortcuts import render

# Create your views here.

def event(request):
    return render(request, "event.html", locals())

def add_activity(request):
    return render(request, "add_activity.html", locals())