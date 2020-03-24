from django.forms import ModelForm
from .models import *
from material import *

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields= ['nome','sobrenome','idade','salario','bio','foto']


