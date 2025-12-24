from django import forms
from .models import Feedback   # import your Feedback model

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["message"]
        widgets = {
            "message": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Write your feedback..."
                }
            )
        }
