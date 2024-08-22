from django.contrib.auth.models import User
from django.forms import ModelForm, modelform_factory, DecimalField
from django.forms.widgets import Select
from django import forms

from bboard.models import Bb, Rubric


# BbForm = modelform_factory(Bb,
#                            fields=('title', 'content', 'price', 'rubric'),
#                            labels={'title': 'Название товара'},
#                            help_texts={'rubric': 'Не забудьте выбрать рубрику!'},
#                            field_classes={'price': DecimalField},
#                            widgets={'rubric': Select(attrs={'size': 4})}
#                            )


# class BbForm(ModelForm):
#     class Meta:
#         model = Bb
#         fields = ('title', 'content', 'price', 'rubric')
#         labels = {'title': 'Название товара'},
#         help_texts = {'rubric': 'Не забудьте выбрать рубрику!'},
#         field_classes = {'price': DecimalField},
#         widgets = {'rubric': Select(attrs={'size': 4})}


class BbForm(ModelForm):
    # title = forms.CharField(label='Название товара', strip=True)
    # content = forms.CharField(label='Описание',
    #                           widget=forms.widgets.Textarea())
    price = forms.DecimalField(label='Цена', decimal_places=2, initial=0.0)
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),
                                    label='Рубрика',
                                    # label_suffix=':',
                                    help_text='Не забудьте выбрать рубрику!',
                                    widget=forms.widgets.Select(attrs={'size': 4}),
                                    # required=False,
                                    # disabled=True,
                                    )

    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')
        labels = {'title': 'Название товара'},


# class RegisterUserForm(ModelForm):
#     password1 = forms.CharField(label='Пароль',
#                                 widget=forms.widgets.PasswordInput())
#     password2 = forms.CharField(label='Пароль (повторно)',
#                                 widget=forms.widgets.PasswordInput())
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2',
#                   'first_name', 'last_name')
