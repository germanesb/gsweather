from django.forms import ModelForm, TextInput
from .models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ["name"]
        # Next line access the widget for the name
        widgets = {
            "name": TextInput(attrs={"class": "input", "placeholder": "City Name"})
        }
