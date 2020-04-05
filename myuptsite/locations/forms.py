from django import forms
from .models import Location


class LocationForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                'cols': 120
            }
        )
    )
    #price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Location
        fields = [
            'title',
            'description',
            #'price'
        ]