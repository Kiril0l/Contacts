from weather.models import City
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = "__all__"
        widgets = {"name": TextInput(attrs={"placeholder": "Введите город"})}