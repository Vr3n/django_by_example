from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify
from urllib import request

from .models import Image

import re
import pdb

# Create your forms here.


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        # extension = url.rsplit('.', 1)[1].lower()
        reg_ext = re.search("jpeg|jpg|png", url)
        extension = reg_ext.group()
        if extension not in valid_extensions:
            raise forms.ValidationError(
                'The given URL does not match valid image extensions.')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        # pdb.set_trace()
        image = super(ImageCreateForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        reg_ext = re.search("jpeg|jpg|png", image_url)
        extension = reg_ext.group()
        image_name = '{}.{}'.format(
            slugify(image.title), extension)

        # Download image from given url.
        req = request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
        response = request.urlopen(req)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        if commit:
            image.save()
        return image
