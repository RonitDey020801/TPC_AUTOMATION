from django import forms
from .models import Companies, Placements, Bulletin, Students, Marks

class StudentForm(forms.ModelForm):

    class Meta:
        model = Students
        fields = '__all__'


class PlacementForm(forms.ModelForm):

    class Meta:
        model = Placements
        fields = '__all__'


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Companies
        fields = '__all__'


class BulletinForm(forms.ModelForm):

    class Meta:
        model = Bulletin
        fields = '__all__'


class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = '__all__'