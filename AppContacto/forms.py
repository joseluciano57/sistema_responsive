# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:01:42 2021

@author: Luciano
"""

from django import forms

class FormularioContacto(forms.Form):
    asunto=forms.CharField(label="Asunto",required=True)
    email=forms.CharField(label="Email",required=True)
    mensaje=forms.CharField(label="Mensaje",widget=forms.Textarea)