from django.db import models
from datetime import date


class Transaction(models.Model):
    STATUS_CHOICES = [
        ('Бизнес', 'Бизнес'),
        ('Личное', 'Личное'),
        ('Налог', 'Налог'),
    ]

    TYPE_CHOICES = {
        'Бизнес': [
            ('Зарплата', 'Зарплата'),
            ('Расходы', 'Расходы'),
            ('Инвестиции', 'Инвестиции'),
        ],
        'Личное': [
            ('Доход', 'Доход'),
            ('Расход', 'Расход'),
            ('Сбережения', 'Сбережения'),
        ],
        'Налог': [
            ('Уплата', 'Уплата'),
            ('Возврат', 'Возврат'),
        ]
    }

    CATEGORY_CHOICES = {
        'Бизнес-Зарплата': [
            ('Разработчики', 'Разработчики'),
            ('Менеджеры', 'Менеджеры'),
            ('Дизайнеры', 'Дизайнеры'),
        ],
        'Бизнес-Расходы': [
            ('Офис', 'Офис'),
            ('Маркетинг', 'Маркетинг'),
            ('Инфраструктура', 'Инфраструктура'),
        ],
        'Бизнес-Инвестиции': [
            ('Оборудование', 'Оборудование'),
            ('Недвижимость', 'Недвижимость'),
            ('Акции', 'Акции'),
        ],
        'Личное-Доход': [
            ('Зарплата', 'Зарплата'),
            ('Подарки', 'Подарки'),
            ('Проценты', 'Проценты'),
        ],
        'Личное-Расход': [
            ('Дом', 'Дом'),
            ('Машина', 'Машина'),
            ('Еда', 'Еда'),
        ],
        'Личное-Сбережения': [
            ('Накопления', 'Накопления'),
            ('Инвестиции', 'Инвестиции'),
        ],
        'Налог-Уплата': [
            ('НДФЛ', 'НДФЛ'),
            ('НДС', 'НДС'),
        ],
        'Налог-Возврат': [
            ('Вычет', 'Вычет'),
            ('Переплата', 'Переплата'),
        ]
    }

    SUBCATEGORY_CHOICES = {
        'Разработчики': ['Frontend', 'Backend', 'Mobile'],
        'Менеджеры': ['Проектные', 'Продуктовые'],
        'Дизайнеры': ['UI/UX', 'Графика'],
        'Офис': ['Аренда', 'Канцелярия'],
        'Маркетинг': ['Реклама', 'SMM'],
        'Инфраструктура': ['Сервера', 'Домены'],
        'Дом': ['Коммуналка', 'Ремонт'],
        'Машина': ['Запчасти', 'ТО'],
        'Еда': ['Продукты', 'Рестораны'],
    }

    date = models.DateField('Дата операции', default=date.today)
    amount = models.DecimalField('Сумма', max_digits=12, decimal_places=2)
    comment = models.TextField('Комментарий', blank=True, null=True)

    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES)
    operation_type = models.CharField('Тип операции', max_length=20)
    category = models.CharField('Категория', max_length=20)
    subcategory = models.CharField('Подкатегория', max_length=20)

    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        ordering = ['-date']

    # Все что ниже(98-109) являеться ключ ответом для выбора в заявке, все возможное варианты смотрите выше(6-79)

    def __str__(self):
        return f"{self.date} - {self.amount} руб."

    def get_type_choices(self):
        return self.TYPE_CHOICES.get(self.status, [])

    def get_category_choices(self):
        key = f"{self.status}-{self.operation_type}"
        return self.CATEGORY_CHOICES.get(key, [])

    def get_subcategory_choices(self):
        return self.SUBCATEGORY_CHOICES.get(self.category, [])
