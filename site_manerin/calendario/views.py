from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm

def index(request):
    events = Event.objects.all()
    return render(request, "calendario/index.html", {"events": events})

def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("calendario_index")
    else:
        form = EventForm()
    return render(request, "calendario/create.html", {"form": form})

def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect("calendario_index")
    else:
        form = EventForm(instance=event)
    return render(request, "calendario/update.html", {"form": form, "event": event})

def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        event.delete()
        return redirect("calendario_index")
    return render(request, "calendario/delete.html", {"event": event})
