from django.forms import *
from core.erp.models import *
class CategoriaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['autofocus'] =True
    
    class Meta:
        model = Categorias
        fields = '__all__' 

        widgets = {
            'nombre' : TextInput(
                attrs={
                    'placeholder': 'Nombre'
                }
            ),

            'descripcion' : Textarea(
                attrs={
                    'placeholder': 'Descripcion',
                    'rows' : 3
                }
            )
        }