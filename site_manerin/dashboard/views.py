from django.shortcuts import render
from calendario.models import Event
from spending.models import Expense
from tasks.models import Task  # supondo que você tenha um app tasks

def home(request):
    context = {
        "event_count": Event.objects.count(),
        "expense_count": Expense.objects.count(),
        "task_count": Task.objects.count(),
    }
    return render(request, "dashboard/home.html", context)
