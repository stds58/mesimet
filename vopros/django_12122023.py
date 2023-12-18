from django.db import models
from datetime import datetime

# Create your models here.

class Product (models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    composition = models.TextField(default="Состав не указан")

director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')
]

class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    labor_contract = models.IntegerField
    position = models.CharField(max_length=2,choices=POSITIONS,default=cashier)

    def get_last_name(self):
        return self.full_name.split()[0]
    #Напишите метод get_last_name() модели Staff, который возвращает только фамилию из поля full_name.
    # Предполагается, что ФИО записано в формате «Иванов Иван Иванович».
    # Вспомните функции строк, позволяющие это сделать.

class Order (models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField
    cost = models.FloatField(default=0.0)
    pickup = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    products = models.ManyToManyField("Product", through='ProductOrder')

    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()
    #В первой строке этого листинга кода мы импортировали модуль datetime, который позволяет получить текущее время.
    # В самом методе в поле time_out мы записали его с помощью функции now(), установили флаг «Завершён» в логическую переменную,
    # а после чего сохранили объект, передав это значение в базу данных. К методу save() мы ещё вернёмся в конце этого модуля, а сейчас продолжим.

    def get_duration(self):
        if self.complete:
            return (self.time_out - self.time_in).total_seconds() // 60
        else:
            return (datetime.now() - self.time_in).total_seconds() // 60
    #Напишите метод get_duration() модели Order, возвращающий время выполнения заказа в минутах (округлить до целого).
    # Если заказ ещё не выполнен, то вернуть количество минут с начала выполнения заказа.
    # seconds = (after — before).total_seconds()


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    #amount = models.IntegerField(default = 1)
    _amount = models.IntegerField(default=1, db_column='amount')

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = int(value) if value >= 0 else 0
        self.save()

    def product_sum(self):
        product_price = self.product.price
        return product_price * self.amount
    #Этот метод сначала получает цену за продукт.
    # Сам объект продукта содержится в переменной self в виде поля product.
    # Оно, в свою очередь, само является объектом модели Product, которая содержит поле price.
    # Создавая такую цепочку self → product → price, мы получаем нужное нам значение.
    # После этого мы умножаем его на self.amount — поле «количество» из текущего объекта.
    # Их произведение и даёт нам нужную сумму.

#python manage.py makemigrations
#python manage.py migrate

