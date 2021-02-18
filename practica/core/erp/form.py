from django.forms import ModelForm
from core.erp.models import *
class CategoriaForm(ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__' 