
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.forms import ModelForm
from .models import Cliente
from .models import Ingeniero
from .models import Proyecto
from .models import Actividad
from .models import Bitacora
from django.contrib.auth.models import User

from django import forms



class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'Tipo_ID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digita el tipo de ID'}),
            'NID': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digita el numero de identificacion'}),
            'Razon_social': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digita la razon social de la empresa'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digita la direccion de la empresa'}),
            'Email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digita el e-mail de contacto empresarial'}),
            'Telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digita el numero telefonico de contacto'}),
        }
        
class IngenieroForm(forms.ModelForm):
    class Meta:
        model = Ingeniero
        exclude = ['COD_ingeniero']
        fields = '__all__'
        widgets = {
            
            'COD_ingeniero': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el codigo del Ingeniero'}),
            'Identificacion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el numero de identificacion'}),
            'Nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite los nombres'}),
            'Apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite los apellidos'}),
            'ROL': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite el ROL del ingeniero'}),
            'Email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite la direccion e-mail'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite la direccion de residencia'}),
            'Telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el numero de telefono'}),
            
        }

   
from django import forms

class ProyectoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    ingenieros_a_cargo = forms.ModelMultipleChoiceField(queryset=Ingeniero.objects.all(), widget=forms.CheckboxSelectMultiple)  # Opción checkboxes
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ingenieros_a_cargo'].label_from_instance = lambda obj: f"{obj.Nombres} {obj.Apellidos} - {obj.Username}"
        self.fields['cliente'].label_from_instance = lambda obj: f"{obj.Razon_social}"
    
    class Meta:
        model = Proyecto
        exclude = ['Codigo']
        fields = '__all__'
        widgets = {
            'Codigo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el codigo del Proyecto','readonly': 'readonly'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite el nombre del proyecto'}),
            'Descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'De una descripcion del proyecto'}),
            'Costo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el costo del proyecto'}),
        }

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['COD_actividad', 'Nombre', 'Descripcion', 'Costo']
        widgets = {
            'COD_actividad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el codigo de la actividad'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite el nombre del proyecto'}),
            'Descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'De una descripcion del proyecto'}),
            'Costo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el costo del proyecto'}),
        }

        
class BitacoraForm(forms.ModelForm): 
    
    
    class BitacoraForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['user'].disabled = True
            if self.instance.user:
                user = User.objects.get(pk=self.instance.user.pk)
            self.fields['user'].initial = user.username
        
        #Ingeniero = forms.ModelChoiceField(queryset=Ingeniero.objects.all())
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    Proyecto = forms.ModelChoiceField(queryset=Proyecto.objects.all())
    Actividad = forms.ModelChoiceField(queryset=Actividad.objects.all())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['Ingeniero'].label_from_instance = lambda obj: f"{obj.Nombres} {obj.Apellidos}"
        self.fields['Proyecto'].label_from_instance = lambda obj: f"{obj.Nombre}"
        self.fields['cliente'].label_from_instance = lambda obj: f"{obj.Razon_social}"
        self.fields['Actividad'].label_from_instance = lambda obj: f"{obj.Nombre}"
        
    class Meta:
        model = Bitacora
        exclude = ['COD_bitacora','user']
        fields = '__all__'
        
        widgets = {
            'Fecha': forms.DateInput(attrs={'type': 'date'}),
            'COD_bitacora': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el codigo de la Bitacora','readonly': 'readonly'}),
            'Numero_de_fuentes': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el numero de fuentes correspondiente a la anterior seleccion'}),
            'Indique_los_fuentes_trabajados': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Si su opcion es diferente a las desplegables indique el o los fuentes '}),
            'Nota': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite aquí si tiene alguna novedad'}),
        }

    