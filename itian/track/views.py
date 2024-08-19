
from django.shortcuts import render

TRACKS = [
    {'id': 1, 'title': 'Web Development', 'description': 'Learn how to build websites.'},
    {'id': 2, 'title': 'Data Science', 'description': 'Learn about data analysis and machine learning.'},
]

def list_track(request):
    return render(request, 'track/list.html', {'tracks': TRACKS})




def track_detail(request, pk):
    track = next((track for track in TRACKS if track['id'] == pk), None)
    return render(request, 'track/detail.html', {'track': track})


  

def update_track(request, pk):
    track = next((track for track in TRACKS if track['id'] == pk), None)
    if request.method == 'POST':
        new_title = request.POST.get('title')
        new_description = request.POST.get('description')
        if track:
            track['title'] = new_title
            track['description'] = new_description
    return render(request, 'track/update.html', {'track': track})



def delete_track(request, pk):
    global TRACKS
    TRACKS = [track for track in TRACKS if track['id'] != pk]
    return render(request, 'track/list.html', {'tracks': TRACKS})




from django.http import HttpResponse

def create_track(request):
    return HttpResponse("Track created")









