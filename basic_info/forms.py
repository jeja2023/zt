from django import forms
from .models import Ypbg,Ypjl

class YpbgForm(forms.ModelForm):
    class Meta:
        model = Ypbg
        fields = ['ztrybh','swsj','name','id_card','swdw','sbsj','fz','zg']
        widgets = {
            'swsj': forms.DateInput(attrs={'type': 'datetime-local'}),
            'sbsj': forms.DateInput(attrs={'type': 'datetime-local'}),
        }

class ZtQueryForm(forms.Form):
    ztrybh = forms.CharField(required=False, label="在逃人员编号")
    name = forms.CharField(required=False, label="姓名")
    id_card = forms.CharField(required=False, label="身份证号码")
    ajlb = forms.CharField(required=False, label="案件类别")
    swdw = forms.CharField(required=False, label="上网单位")
    swsj = forms.CharField(required=False, label="上网日期")

class YzQueryForm(forms.Form):
    ztrybh = forms.CharField(required=False, label="在逃人员编号")
    name = forms.CharField(required=False, label="姓名")
    id_card = forms.CharField(required=False, label="身份证号码")
    ajlb = forms.CharField(required=False, label="案件类别")
    swdw = forms.CharField(required=False, label="上网单位")
    swsj = forms.CharField(required=False, label="上网日期")

class BsQueryForm(forms.Form):
    ztrybh = forms.CharField(required=False, label="在逃人员编号")
    name = forms.CharField(required=False, label="姓名")
    id_card = forms.CharField(required=False, label="身份证号码")
    ajlb = forms.CharField(required=False, label="案件类别")
    swdw = forms.CharField(required=False, label="上网单位")
    swsj = forms.CharField(required=False, label="上网日期")

class YpjlForm(forms.ModelForm):
    class Meta:
        model = Ypjl
        fields = ['ztrybh', 'ypnr', 'ypr']
        widgets = {
            'ypnr': forms.Textarea(attrs={'rows': 4, 'placeholder': '请输入研判内容'}),
        }
