from django import forms
from .models import Birthday



# Для использования формы с моделями меняем класс на forms.ModelForm.
class BirthdayForm(forms.ModelForm):
    # Удаляем все описания полей.

    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        fields = ('first_name', 'last_name', 'birthday', 'image')
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        } 