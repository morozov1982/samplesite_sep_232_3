from django.db import models


def is_active_default():
    return True


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, unique=True,
                            verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']


class Bb(models.Model):
    # KINDS = (
    #     ('b', 'Куплю'),
    #     ('s', 'Продам'),
    #     ('c', 'Обменяю'),
    # )
    # KINDS = (
    #     ('Купля-продажа', (
    #         ('b', 'Куплю'),
    #         ('s', 'Продам'),
    #     )),
    #     ('Обмен', (
    #         ('c', 'Обменяю'),
    #     ))
    # )
    KINDS = (
        (None, 'Выберите тип публикуемого объявления'),
        ('b', 'Куплю'),
        ('s', 'Продам'),
        ('c', 'Обменяю'),
    )

    kind = models.CharField(max_length=1, choices=KINDS, default='s')

    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT,
                               verbose_name='Рубрика', related_name='entries')
    title = models.CharField(max_length=50, verbose_name='Товар')  # primary_key=True
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    # price = models.FloatField(  # default=0,
    #                           null=True, blank=True, verbose_name='Цена')
    price = models.DecimalField(max_digits=15, decimal_places=2,
                                null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True,
                                     verbose_name='Опубликовано')
    # is_active = models.BooleanField(  # default=True
    #                                 default=is_active_default
    #                                 )

    def __str__(self):
        return f'{self.title} ({self.price} тг.)'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']
