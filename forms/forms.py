from django import forms
from .models import Student
import re
from django.core.exceptions import ValidationError

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name': 'Full Name',
            'university_id': 'University ID',
            'national_id': 'ID Number',
            'mobile': 'Mobile Number',
            'address': 'Address',
            'birth_date': 'Date of Birth',
            'image': 'Image',
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.match(r'^[A-Za-z\s]+$', name):
            raise ValidationError("No numbers or symbols allowed in the name")
        return name

    def clean_university_id(self):
        uid = str(self.cleaned_data['university_id'])
        if not re.match(r'^[12]\d{8}$', uid):
            raise ValidationError(
                "University ID  Must start with (1 or 2) only, and the number of digits must be 9 and unique."
            )
        return self.cleaned_data['university_id']

    def clean_national_id(self):
        nid = str(self.cleaned_data['national_id'])
        if not re.match(r'^[984]\d{8}$', nid):
            raise ValidationError(
                "ID Number Must start with (9, 8, or 4) only, and the number of digits must be 9"
            )
        return self.cleaned_data['national_id']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if not re.match(r'^(059|056)\d{7}$', mobile):
            raise ValidationError(
                "Mobile number Must begin with (059 or 056) only, and the number of digits must be 10"
            )
        return mobile

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and not image.name.lower().endswith(('.jpg', '.png')):
            raise ValidationError("Image Must be jpg or png only")
        return image
