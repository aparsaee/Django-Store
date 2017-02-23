# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from .models import Sold
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class SoldForm(forms.ModelForm):

    def validate(value):
        if not (str(value).startswith('090') or str(value).startswith('091') or str(value).startswith('092') or str(value).startswith('092')):
            raise ValidationError(
                _('%(value)s یک شماره موبایل معتبر نیست!'),
                params={'value': value},
            )

    phone = forms.CharField(widget=forms.NumberInput(), label='تلفن همراه',
                            validators=[validate], max_length=11, min_length=11)
    address = forms.CharField(label='آدرس')
    zip_code = forms.CharField(label='کدپستی', error_messages={'max_length': _("این کدپستی نامعتبر است"), 'min_length': _("این کدپستی نامعتبر است")},
                               widget=forms.NumberInput, min_length=10, max_length=10)

    class Meta:
        model = Sold
        fields = ['amount', 'address', 'zip_code', 'phone']

    def __init__(self, *args, **kwargs):
        quant = kwargs.pop("quant")
        super(SoldForm, self).__init__(*args, **kwargs)
        self.fields['amount'] = forms.IntegerField(min_value=1, initial=1,
                                                   label='تعداد', max_value=quant)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
