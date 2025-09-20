from django import forms
from .models import Transaction
from datetime import date


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction # Упращяем для дальнейшего использование и просто берем в forms данные из models
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'value': date.today().strftime('%Y-%m-%d')
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Комментарий...'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
                'onchange': 'updateTypes()'
            }),
            'operation_type': forms.Select(attrs={
                'class': 'form-control',
                'onchange': 'updateCategories()'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'onchange': 'updateSubcategories()'
            }),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk: # Авто-ое добавление даты в случае создания новой записи
            self.initial['date'] = date.today() # Установка даты: сейчас

        if self.instance and self.instance.pk: # Динамическое обновление выбора в шаблоне создания записи
            self.fields['operation_type'].choices = self.instance.get_type_choices()
            self.fields['category'].choices = self.instance.get_category_choices()
            self.fields['subcategory'].choices = [(sc, sc) for sc in self.instance.get_subcategory_choices()]
        else:
            self.fields['operation_type'].choices = [('', '---------')]
            self.fields['category'].choices = [('', '---------')]
            self.fields['subcategory'].choices = [('', '---------')]