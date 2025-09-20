from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm

def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-date')

    # После получения всех записей из БД(6), получаем параметры фильтрации из URL
    date_after = request.GET.get('date_after')
    date_before = request.GET.get('date_before')
    status_filter = request.GET.get('status')
    type_filter = request.GET.get('operation_type')

    # Далее применяем фильты if они указаны
    if date_after:
        transactions = transactions.filter(date__gte=date_after)
    if date_before:
        transactions = transactions.filter(date__lte=date_before)
    if status_filter:
        transactions = transactions.filter(status=status_filter)
    if type_filter:
        transactions = transactions.filter(operation_type=type_filter)

    # Вставляем данные в шаблон и показываем пользователю
    context = {
        'transactions': transactions,
        'current_filters': {
            'date_after': date_after,
            'date_before': date_before,
            'status': status_filter,
            'operation_type': type_filter,
        }
    }
    return render(request, 'transaction_list.html', context)


def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()

    return render(request, 'transaction_form.html', {'form': form})


def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction) # Берет данные из forms
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'transaction_form.html', {'form': form, 'object': transaction})


def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')

    return render(request, 'transaction_confirm_delete.html', {'object': transaction})