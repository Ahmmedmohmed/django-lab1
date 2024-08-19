
from django.shortcuts import render

TRAINEES = [
    {'id': 1, 'name': 'Mohamed Salah', 'trainee_id': '35'},
    {'id': 2, 'name': 'Fatma Ali', 'trainee_id': '40'},
]

def list_trainees(request):
    return render(request, 'trainee/list.html', {'trainees': TRAINEES})




def trainee_detail(request, pk):
    trainee = next((trainee for trainee in TRAINEES if trainee['id'] == pk), None)
    return render(request, 'trainee/detail.html', {'trainee': trainee})


    # trainee/views.py

def update_trainee(request, pk):
    trainee = next((trainee for trainee in TRAINEES if trainee['id'] == pk), None)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_trainee_id = request.POST.get('trainee_id')
        if trainee:
            trainee['name'] = new_name
            trainee['trainee_id'] = new_trainee_id
    return render(request, 'trainee/update.html', {'trainee': trainee})


def delete_trainee(request, pk):
    global TRAINEES
    TRAINEES = [trainee for trainee in TRAINEES if trainee['id'] != pk]
    return render(request, 'trainee/list.html', {'trainees': TRAINEES})

   



