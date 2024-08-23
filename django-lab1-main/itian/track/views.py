from django.shortcuts import render, get_object_or_404, redirect
from .models import Track

def list_track(request):
    tracks = Track.objects.all()
    return render(request, 'track/list.html', {'tracks': tracks})

def track_detail(request, pk):
    track = get_object_or_404(Track, pk=pk)
    return render(request, 'track/detail.html', {'track': track})

def update_track(request, pk):
    track = get_object_or_404(Track, pk=pk)
    if request.method == 'POST':
        new_title = request.POST.get('title')
        new_description = request.POST.get('description')
        track.title = new_title
        track.description = new_description
        track.save()
        return redirect('list_track')
    return render(request, 'track/update.html', {'track': track})

def delete_track(request, pk):
    track = get_object_or_404(Track, pk=pk)
    if request.method == 'POST':
        track.delete()
        return redirect('list_track')
    return render(request, 'track/confirm_delete.html', {'track': track})

def create_track(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Track.objects.create(title=title, description=description)
        return redirect('list_track')
    return render(request, 'track/create.html')

