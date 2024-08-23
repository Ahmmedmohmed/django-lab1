from django.shortcuts import render, get_object_or_404, redirect
from .models import Trainee

def list_trainees(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/list.html', {'trainees': trainees})

def trainee_detail(request, pk):
    trainee = get_object_or_404(Trainee, pk=pk)
    return render(request, 'trainee/detail.html', {'trainee': trainee})

def update_trainee(request, pk):
    trainee = get_object_or_404(Trainee, pk=pk)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_trainee_id = request.POST.get('trainee_id')
        trainee.name = new_name
        trainee.trainee_id = new_trainee_id
        trainee.save()
        return redirect('list_trainees')
    return render(request, 'trainee/update.html', {'trainee': trainee})

def delete_trainee(request, pk):
    trainee = get_object_or_404(Trainee, pk=pk)
    if request.method == 'POST':
        trainee.delete()
        return redirect('list_trainees')
    return render(request, 'trainee/confirm_delete.html', {'trainee': trainee})

def create_trainee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        trainee_id = request.POST.get('trainee_id')
        Trainee.objects.create(name=name, trainee_id=trainee_id)
        return redirect('list_trainees')
    return render(request, 'trainee/create.html')


   



