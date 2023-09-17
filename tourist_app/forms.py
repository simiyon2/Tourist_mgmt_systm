from tourist_app.models import login,reg,londonfield,chinafield,singaporefield,japanfield,thailandfield,indonesiafield,malaysiafield,contactfield,bookingfield,payment
from tourist_app.models import payment_one,payment_two,payment_three,payment_four,payment_five,payment_six,payment_seven
from django.forms import ModelForm
from .models import reg,londonfield
from django import forms
from datetime import datetime,date

class logForm(ModelForm):
    class Meta:
        model = login
        fields = '__all__'
        
class regForm(ModelForm):
    class Meta: 
        model = reg
        fields =  '__all__'

class londonform(ModelForm):
    class Meta:
        model = londonfield
        fields = '__all__' 

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 4 or len(name) > 10:
            raise forms.ValidationError("Name must be between 4 and 10 characters.")
        return name
    def clean_name1(self):
        name1 = self.cleaned_data.get('name1')
        if len(name1) < 4 or len(name1) > 10:
            raise forms.ValidationError("Name must be between 4 and 10 characters.")
        return name1
    def clean_age(self):
        age = self.cleaned_data['age']
        if age >= date.today():
            raise forms.ValidationError("Age should not be a future date.")
        return age

    def clean_age1(self):
        age1 = self.cleaned_data['age1']
        if age1 >= date.today():
            raise forms.ValidationError("Age should not be a future date.")
        return age1

    def clean_date2(self):
        date2 = self.cleaned_data['date2']
        if date2 <= date.today():
            raise forms.ValidationError("Date of journey must be a future date.")
        return date2

class chinaform(ModelForm):
    class Meta:
        model = chinafield
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 4 or len(name) > 10:
            raise forms.ValidationError("Name must be between 4 and 10 characters.")
        return name
    def clean_name1(self):
        name1 = self.cleaned_data.get('name1')
        if len(name1) < 4 or len(name1) > 10:
            raise forms.ValidationError("Name must be between 4 and 10 characters.")
        return name1
    def clean_age(self):
        age = self.cleaned_data['age']
        if age >= date.today():
            raise forms.ValidationError("Age should not be a future date.")
        return age

    def clean_age1(self):
        age1 = self.cleaned_data['age1']
        if age1 >= date.today():
            raise forms.ValidationError("Age should not be a future date.")
        return age1

    def clean_date2(self):
        date2 = self.cleaned_data['date2']
        if date2 <= date.today():
            raise forms.ValidationError("Date of journey must be a future date.")
        return date2
 
class singaporeform(ModelForm):
    class Meta:
        model = singaporefield
        fields = '__all__'
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 4 or len(name) > 10:
            raise forms.ValidationError("Name must be between 4 and 10 characters.")
        return name
    def clean_name1(self):
        name1 = self.cleaned_data.get('name1')
        if len(name1) < 4 or len(name1) > 10:
            raise forms.ValidationError("Name must be between 4 and 10 characters.")
        return name1
    def clean_age(self):
        age = self.cleaned_data['age']
        if age >= date.today():
            raise forms.ValidationError("Age should not be a future date.")
        return age

    def clean_age1(self):
        age1 = self.cleaned_data['age1']
        if age1 >= date.today():
            raise forms.ValidationError("Age should not be a future date.")
        return age1

    def clean_date2(self):
        date2 = self.cleaned_data['date2']
        if date2 <= date.today():
            raise forms.ValidationError("Date of journey must be a future date.")
        return date2

class japanform(ModelForm):
    class Meta:
        model = japanfield
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 4 or len(name) > 10:
            raise forms.ValidationError("Name must be between 4 and 10 characters.")
        return name
    def clean_name1(self):
        name1 = self.cleaned_data.get('name1')
        if len(name1) < 4 or len(name1) > 10:
            raise forms.ValidationError("Name must be between 4 and 10 characters.")
        return name1
    def clean_age(self):
        age = self.cleaned_data['age']
        if age >= date.today():
            raise forms.ValidationError("Age should not be a future date.")
        return age

    def clean_age1(self):
        age1 = self.cleaned_data['age1']
        if age1 >= date.today():
            raise forms.ValidationError("Age should not be a future date.")
        return age1

    def clean_date2(self):
        date2 = self.cleaned_data['date2']
        if date2 <= date.today():
            raise forms.ValidationError("Date of journey must be a future date.")
        return date2

class thailandform(ModelForm):
    class Meta:
        model = thailandfield
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 4 or len(name) > 10:
            raise forms.ValidationError("Name must be between 4 and 10 characters.")
        return name
    def clean_name1(self):
        name1 = self.cleaned_data.get('name1')
        if len(name1) < 4 or len(name1) > 10:
            raise forms.ValidationError("Name must be between 4 and 10 characters.")
        return name1
    def clean_age(self):
        age = self.cleaned_data['age']
        if age >= date.today():
            raise forms.ValidationError("Age should not be a future date.")
        return age

    def clean_age1(self):
        age1 = self.cleaned_data['age1']
        if age1 >= date.today():
            raise forms.ValidationError("Age should not be a future date.")
        return age1

    def clean_date2(self):
        date2 = self.cleaned_data['date2']
        if date2 <= date.today():
            raise forms.ValidationError("Date of journey must be a future date.")
        return date2

class indonesiaform(ModelForm):
    class Meta:
        model = indonesiafield
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 4 or len(name) > 10:
            raise forms.ValidationError("Name must be between 4 and 10 characters.")
        return name
    def clean_name1(self):
        name1 = self.cleaned_data.get('name1')
        if len(name1) < 4 or len(name1) > 10:
            raise forms.ValidationError("Name must be between 4 and 10 characters.")
        return name1
    def clean_age(self):
        age = self.cleaned_data['age']
        if age >= date.today():
            raise forms.ValidationError("Age should not be a future date.")
        return age

    def clean_age1(self):
        age1 = self.cleaned_data['age1']
        if age1 >= date.today():
            raise forms.ValidationError("Age should not be a future date.")
        return age1

    def clean_date2(self):
        date2 = self.cleaned_data['date2']
        if date2 <= date.today():
            raise forms.ValidationError("Date of journey must be a future date.")
        return date2

class malaysiaform(ModelForm):
    class Meta:
        model = malaysiafield
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 4 or len(name) > 10:
            raise forms.ValidationError("Name must be between 4 and 10 characters.")
        return name
    def clean_name1(self):
        name1 = self.cleaned_data.get('name1')
        if len(name1) < 4 or len(name1) > 10:
            raise forms.ValidationError("Name must be between 4 and 10 characters.")
        return name1
    def clean_age(self):
        age = self.cleaned_data['age']
        if age >= date.today():
            raise forms.ValidationError("Age should not be a future date.")
        return age

    def clean_age1(self):
        age1 = self.cleaned_data['age1']
        if age1 >= date.today():
            raise forms.ValidationError("Age should not be a future date.")
        return age1

    def clean_date2(self):
        date2 = self.cleaned_data['date2']
        if date2 <= date.today():
            raise forms.ValidationError("Date of journey must be a future date.")
        return date2

class contactform(ModelForm):
    class Meta:
        model = contactfield
        fields = '__all__'

class bookingform(ModelForm):
    class Meta:
        model = bookingfield
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 4 or len(name) > 10:
            raise forms.ValidationError("Name must be between 4 and 10 characters.")
        return name
    def clean_date(self):
        date = self.cleaned_data['date']
        if date <= date.today():
            raise forms.ValidationError("Date of journey must be a future date.")
        return date

class paymentform(ModelForm):
    class Meta:
        model = payment
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise forms.ValidationError("Name must only contain alphabetical characters.")
        return name

    def clean_expiration(self):
        expiration_str = self.cleaned_data['expiration']
        expiration = datetime.strptime(expiration_str, '%Y-%m').date()  # Assuming expiration_str is in 'YYYY-MM-DD' format
        if expiration <= date.today():
            raise forms.ValidationError("Expiration a valid date")
        return expiration
    
class paymentform_one(ModelForm):
    class Meta:
        model = payment_one
        fields = '__all__'
    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise forms.ValidationError("Name must only contain alphabetical characters.")
        return name

    def clean_expiration(self):
        expiration_str = self.cleaned_data['expiration']
        expiration = datetime.strptime(expiration_str, '%Y-%m').date()  # Assuming expiration_str is in 'YYYY-MM-DD' format
        if expiration <= date.today():
            raise forms.ValidationError("Expiration a valid date")
        return expiration

class paymentform_two(ModelForm):
    class Meta:
        model = payment_two
        fields = '__all__'
    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise forms.ValidationError("Name must only contain alphabetical characters.")
        return name

    def clean_expiration(self):
        expiration_str = self.cleaned_data['expiration']
        expiration = datetime.strptime(expiration_str, '%Y-%m').date()  # Assuming expiration_str is in 'YYYY-MM-DD' format
        if expiration <= date.today():
            raise forms.ValidationError("Expiration a valid date")
        return expiration

class paymentform_three(ModelForm):
    class Meta:
        model = payment_three
        fields = '__all__'
    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise forms.ValidationError("Name must only contain alphabetical characters.")
        return name

    # def clean_expiration(self):
    #     expiration = self.cleaned_data['expiration']
    #     if expiration <= date.today():
    #         raise forms.ValidationError("Expiration date must be a future date.")
    #     return expiration
def clean_expiration(self):
    expiration_str = self.cleaned_data['expiration']
    expiration = datetime.strptime(expiration_str, '%Y-%m').date()  # Assuming expiration_str is in 'YYYY-MM-DD' format

    if expiration <= date.today():
        raise forms.ValidationError("Expiration a valid date")
    return expiration    

class paymentform_four(ModelForm):
    class Meta:
        model = payment_four
        fields = '__all__'
    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise forms.ValidationError("Name must only contain alphabetical characters.")
        return name

    def clean_expiration(self):
        expiration_str = self.cleaned_data['expiration']
        expiration = datetime.strptime(expiration_str, '%Y-%m').date()  # Assuming expiration_str is in 'YYYY-MM-DD' format
        if expiration <= date.today():
            raise forms.ValidationError("Expiration a valid date")
        return expiration

class paymentform_five(ModelForm):
    class Meta:
        model = payment_five
        fields = '__all__'
    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise forms.ValidationError("Name must only contain alphabetical characters.")
        return name

    def clean_expiration(self):
        expiration_str = self.cleaned_data['expiration']
        expiration = datetime.strptime(expiration_str, '%Y-%m').date()  # Assuming expiration_str is in 'YYYY-MM-DD' format
        if expiration <= date.today():
            raise forms.ValidationError("Expiration a valid date")
        return expiration
class paymentform_six(ModelForm):
    class Meta:
        model = payment_six
        fields = '__all__'
    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise forms.ValidationError("Name must only contain alphabetical characters.")
        return name

    def clean_expiration(self):
        expiration_str = self.cleaned_data['expiration']
        expiration = datetime.strptime(expiration_str, '%Y-%m').date()  # Assuming expiration_str is in 'YYYY-MM-DD' format
        if expiration <= date.today():
            raise forms.ValidationError("Expiration a valid date")
        return expiration

class paymentform_seven(ModelForm):
    class Meta:
        model = payment_seven
        fields = '__all__'
    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise forms.ValidationError("Name must only contain alphabetical characters.")
        return name

    def clean_expiration(self):
        expiration_str = self.cleaned_data['expiration']
        expiration = datetime.strptime(expiration_str, '%Y-%m').date()  # Assuming expiration_str is in 'YYYY-MM-DD' format
        if expiration <= date.today():
            raise forms.ValidationError("Expiration a valid date.")
        return expiration
