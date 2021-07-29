from django.forms import forms, ModelForm

from web.models import YOURFEELS


class C_YF(ModelForm):
    class Meta:
        model = YOURFEELS
        fields = '__all__'
        exclude= ['own_poem']
