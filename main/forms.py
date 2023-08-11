from django import forms
from main.models import Product, Version

banned_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', ]


class FormStileMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(FormStileMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('make_date', 'change_date', 'owner',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for banned_word in banned_list:
            if banned_word in cleaned_data.lower():
                raise forms.ValidationError('Нельзя добавть этот товар')
                break
            else:
                continue
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for banned_word in banned_list:
            if banned_word in cleaned_data.lower():
                raise forms.ValidationError('Нельзя добавть этот товар')
                break
            else:
                continue
        return cleaned_data


class VersionForm(FormStileMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
