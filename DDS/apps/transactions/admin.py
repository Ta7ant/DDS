from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['date', 'status', 'operation_type', 'category', 'subcategory', 'amount']
    list_filter = ['date', 'status', 'operation_type', 'category'] # Фильтры которые можно применить в виджете с права от центра экрана
    search_fields = ['comment'] # Поиск по комм-ям
