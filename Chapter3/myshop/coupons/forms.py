from django import forms

# Create your forms here.


class CouponApplyForm(forms.Form):
    code = forms.CharField()
