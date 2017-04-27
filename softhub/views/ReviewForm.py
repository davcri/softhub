from django import forms

from softhub.models.Review import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['application', 'user']
