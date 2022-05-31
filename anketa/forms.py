from . models import Info
from django.forms import ModelForm,TextInput,DateInput,Textarea

class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = '__all__'

        widgets = {
           
            "name": TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'Имя'
            }),

            "last_name": TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'Фамилия'
            }),

            "date_of_birth": TextInput(attrs={
                'class' : 'form-control',
                'placeholder':'Дата рождение'

            }), 

            "formation": TextInput(attrs={
                'class' : 'form-control',
                'placeholder':'Образования, Сертификат'
            }), 

            "position": TextInput(attrs={
                'class' : 'form-control',
                'placeholder':'Опыт сколко лет'
            }), 

            "title": TextInput(attrs={
                'class' : 'form-control',
                'placeholder':'Отделшик, Покрасшик, Сантехник, Водитель, Сваршик ',
            }), 

            "description": Textarea(attrs={
                'class' : 'form-control',
                'placeholder':'О себе',
            }), 
           
        }