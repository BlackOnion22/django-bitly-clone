from django.forms import ModelForm
from Bitly.models import Links
class createform(ModelForm):
    class Meta:
        model=Links
        fields=['name','url','slug']
