from django import forms

class FormArt(forms.Form):
    titulo = forms.CharField(
        label="Titulo",
        max_length=25,
        required=True,
        widget=forms.TextInput(
            #atributos de un html
                attrs={
                    'placeholder':"Cual es titulo?",
                    'class':'titulos'
                }
            )
        )
    contenido = forms.CharField(
        label="contenido",
        widget=forms.Textarea,
        required=True
    )
    opc = [(1,'si'),(0,'no')]
    publicado = forms.TypedChoiceField(
        label="publicado ?",
        choices = opc,
        
    )