import re

from cProfile import label
from datetime import date
from email.policy import default
from unittest.util import _MAX_LENGTH
from django import forms
from .models import PalukRidersModel


class RidersForm(forms.Form):
    class meta:
        model = PalukRidersModel
        fields = ('date','firstname','secondname','lastname','payment','region','brand','model','kind','shirt','road','passenger','p_shirt')
    
    


           
    


