from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm

# Listar todos
def index(request):
    expenses = Expense.objects.all()
    return render(request, "spending/index.html", {"expenses": expenses})

# Criar novo
def create_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("spending_index")
    else:
        form = ExpenseForm()
    return render(request, "spending/create.html", {"form": form})

# Editar
def update_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("spending_index")
    else:
        form = ExpenseForm(instance=expense)
    return render(request, "spending/update.html", {"form": form})

# Deletar
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        expense.delete()
        return redirect("spending_index")
    return render(request, "spending/delete.html", {"expense": expense})
