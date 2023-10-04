from django.shortcuts import render
from .models import Robot

def robot_list(request):
    robots = Robot.objects.all()
    return render(request, 'robots/templates/robot_list.html', {'robots': robots})

def robot_detail(request, pk):
    robot = Robot.objects.get(pk=pk)
    return render(request, 'robots/templates/robot_detail.html', {'robot': robot})
