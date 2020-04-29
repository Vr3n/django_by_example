from django import forms
from django.utils.translation import gettext_lazy as _
# Create your forms here.


class CouponApplyForm(forms.Form):
    code = forms.CharField(label=_("Coupon code"))
