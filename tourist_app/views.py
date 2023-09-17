from django.shortcuts import render,redirect,get_object_or_404
from tourist_app.models import login,reg,londonfield,chinafield,singaporefield,japanfield,thailandfield,indonesiafield,malaysiafield,bookingfield
from tourist_app.forms import logForm,regForm,londonform,chinaform,singaporeform,japanform,thailandform,indonesiaform,malaysiaform,contactform,bookingform,paymentform
from tourist_app.forms import paymentform_one,paymentform_two,paymentform_three,paymentform_four,paymentform_five,paymentform_six,paymentform_seven
from django.contrib import messages
from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponse,FileResponse
from PIL import Image
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
import re
from django.contrib.auth.decorators import login_required
# import logging
from django.contrib.auth import logout
from django.views.generic import View
from tourist_app.forms import londonform
from datetime import datetime
# pdf
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from django.template.loader import get_template
from io import BytesIO
from django.template import Context, Template
from xhtml2pdf import pisa
# import weasyprint
from django.views import View
import html  # Import the 'html' module to encode the address field
import io
from tourist_app import models
from .models import londonfield
# from .utils import render_to_pdf 
# new pdf
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tourist_app.models import londonfield
from datetime import date,datetime
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import random
import string
from django.urls import reverse
# Create your views here.

def funindex(request):
    return render (request,'index.html')

def funlogin(request):
    return render (request,'login.html')

def funlogout(request):
    logout(request)
    return redirect('home')

def funabout(request):
    return render (request,'about.html')

def fundestination(request):
    return render (request,'destination.html')

def funpackage(request):
    return render (request,'package.html') 

def funservice(request):
    return render (request,'service.html') 

def funteam(request):
    return render (request,'team.html')

def funtestimonial(request):
    return render (request,'testimonial.html')

def funclog(request):
    if request.method == 'POST':
        form = YourForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=name, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid name or password')
    else:
        form = YourForm()

    return render(request, 'login.html', {'form': form})

class YourForm(forms.Form):
    name = forms.CharField(max_length=10,min_length=5,error_messages={'required': 'Please enter a valid name.'})
    password = forms.CharField(widget=forms.PasswordInput,error_messages={'required': 'Please enter a valid password.'})

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        password = cleaned_data.get('password')
        
        if name == "admin" or password == "password":
            raise forms.ValidationError("Invalid credentials")
        return cleaned_data
@login_required
def home(request):
    current_user = request.user
    user_id = current_user.id
    print(user_id)
    context = {'user_id': user_id}
    return render(request, 'index.html',context)

# def loginview(request):
    data = login.objects.all()
    context = {'loginview_key':data}
    return render (request,'adminview.html',context)

# def logindelete(request,id):
    data = login.objects.get(id=id)
    data.delete()
    return redirect("/adminview")

# def loginupdate(request,id):
    data = login.objects.get(id=id)
    context = {'update':data}
    if request.method=='POST':
        form = logForm(request.POST,request.FILES,instance=data)
        a=request.POST['name']
        b=request.POST['password']

        data.name = a
        data.password = b
        form.save()
        data.save()

        return redirect('/adminview')   
    return render(request,"login.html",context)

def funcreg(request):
        if request.method == 'POST':
            form = myform(request.POST,request.FILES)
            if form.is_valid():
                name = form.cleaned_data['name']
                file = form.cleaned_data['file']
                email = form.cleaned_data['email']
                phonenumber = form.cleaned_data['phonenumber']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                confirmpassword = form.cleaned_data['confirmpassword']

                if User.objects.filter(username=username).exists():

                    form.add_error('username', 'Username is already exist.')
                    return render(request, 'registration.html', {'form': form})

                saform = reg.objects.create(
                    name=name, 
                    file=file,    
                    email=email,
                    phonenumber=phonenumber,
                    password=password,
                    username=username,
                    confirmpassword=confirmpassword,
                )
                saform.save()
                user = User.objects.create_user(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect( 'login')
        else:
            form = myform()
        return render(request, 'registration.html', {'form':form})

class myform(forms.Form):
    name = forms.CharField(max_length=10,min_length=5,error_messages={'required': 'Please enter a valid name.'})
    file = forms.FileField()
    email = forms.EmailField(max_length=30)
    phonenumber = forms.CharField(max_length=10,min_length=10,error_messages={'required': 'Please enter a valid phonenumber'})
    password = forms.CharField(widget=forms.PasswordInput,error_messages={'required': 'Please enter a valid password.'})
    username = forms.CharField(max_length=30)
    confirmpassword = forms.CharField(widget=forms.PasswordInput,error_messages={'required': 'Please enter a valid password.'})

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name') 
        file = cleaned_data.get('file')
        email = cleaned_data.get('email')
        phonenumber = cleaned_data.get('phonenumber')
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        confirmpassword = cleaned_data.get('confirmpassword')

        if name is not None and len(name) < 5:
            self.add_error('name', 'A minimum of 5 characters is required')

        if password is not None and len(password) < 8:
            self.add_error('password', 'Password length should not be less than 8 characters')

        if confirmpassword is not None and len(confirmpassword) < 8:
            self.add_error('confirmpassword', 'Password length should not be less than 8 characters')
        
        if password and confirmpassword and password != confirmpassword:
            self.add_error('confirmpassword', 'Password and confirm password must match.')

        if username is not None and len(username) < 5 :
                self.add_error('username', 'A minimum of 5 characters are required')

        if file is not None:
                # Check if the uploaded file is an image
                valid_image_extensions = ['.jpg', '.jpeg', '.png']
                file_extension = '.' + file.name.split('.')[-1].lower()

                try:
                    image = Image.open(file)
                    image.verify()  # Validate image integrity

                    if file_extension not in valid_image_extensions:
                        raise ValidationError('Upload a valid photo.')
                except Exception:
                    raise ValidationError('Upload a valid photo.')
        
                return cleaned_data
        
def regview(request):
    data = reg.objects.all()
    context = {'regview_key':data}
    print(context)
    return render (request,'adminview.html',context)

def regdelete(request,id):
    data = reg.objects.get(id=id)
    data.delete()
    return redirect("/adminview")
 
def regupdate(request,id):
    data = reg.objects.get(id=id)
    context = {'update':data}
    if request.method=='POST':
        form = regForm(request.POST,request.FILES,instance=data)
        a = request.POST['name']
        b = request.POST['file']
        c = request.POST['email']
        d = request.POST['phonenumber']
        e = request.POST['username'] 
        f = request.POST['password']
        g = request.POST['confirmpassword']

        data.name = a
        data.file = b
        data.email = c
        data.phonenumber = d
        data.username = e
        data.password = f
        data.confirmpassword = g
        form.save()
        data.save()

        return redirect('/adminview')   
    return render(request,"registration.html",context)
# @login_required(login_url='login')
# def london(request):
#     if request.method == 'POST':
#         form = londonform(request.POST)
#         if form.is_valid():
#             form.save()
#             print("Data saved successfully")
#         else:
#             print("Form is invalid")
#     else:
#         form = londonform()
#     return render(request, 'london.html', {'form': form})

# london

@login_required(login_url='login')
def london(request):
    if request.method == 'POST':
        form = londonform(request.POST)
        if form.is_valid():
            form.save()
            # Get the saved objects from the form
            person1 = form.instance
            person2 = form.instance
            # Convert date_of_journey to a date object
            date_of_journey_str = request.POST.get('date2')
            from datetime import datetime
            date_of_journey = datetime.strptime(date_of_journey_str, '%Y-%m-%d').date()
            # Calculate ages
            age_person1 = person1.calculate_age(date_of_journey)
            age_person2 = person2.calculate_age1(date_of_journey)

            # Render the template with the calculated ages
            return render(request, 'payment.html', {'age_person1': age_person1, 'age_person2': age_person2,'name_person1': person1.name,
                'name_person2': person2.name1,
                'gender_person1': person1.gender,
                'gender_person2': person2.gender1,'date_of_journey_str':date_of_journey_str})
    else:
        form = londonform() 

    return render(request, 'london.html', {'form': form})

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def generate_random_invoice_number():
    # Generate a random alphanumeric string of length 8 for the invoice number
    alphanumeric_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choices(alphanumeric_chars, k=8))

def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="invoice.pdf"'

    # Ensure there is at least one record in the queryset
    if londonfield.objects.exists():
        # Get the last (final) record from the queryset
        final_record = londonfield.objects.last()

        # Calculate the ages from the date_of_birth fields
        age = calculate_age(final_record.age)
        age1 = calculate_age(final_record.age1)

        # Convert date_of_journey to the desired format 'dd/mm/yyyy'
        date2 = final_record.date2.strftime('%d/%m/%Y')

        invoice_number = generate_random_invoice_number()

        # Generate the PDF
        pdf = canvas.Canvas(response, pagesize=letter)

        # Customize font and font size
        pdf.setFont("Helvetica-Bold", 12)

        pdf.drawString(500, 770, invoice_number)
        title = "INVOICE"
        pdf.drawString(250, 770, title)

        # Draw the additional content above the table
        content = "Company:Tourist || Paid amount = 1,85,00 Rs || Tourist place: London"
        pdf.drawString(100, 720, content)

        table_data = [
            ["Person 1", "Age", "Gender", "Person 2", "Age", "Gender", "Date of journey"],
            [final_record.name, age, final_record.gender, final_record.name1, age1, final_record.gender1, date2],
        ]

        # Customize the table style
        table_style = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ]

        # Create the table
        table = Table(table_data)
        table.setStyle(table_style)

        # Draw the table at the appropriate position
        table.wrapOn(pdf, 400, 400)
        table.drawOn(pdf, 100, 600)

        pdf.save()
        return response
    else:
        return HttpResponse("No data available.")
# china

@login_required(login_url='login')
def china(request):
    if request.method == 'POST':
        form = chinaform(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")

            person1 = form.instance
            person2 = form.instance
            date_of_journey_str = request.POST.get('date2')

            date_of_journey = datetime.strptime(date_of_journey_str, '%Y-%m-%d').date()
            age_person1 = person1.calculate_age(date_of_journey)
            age_person2 = person2.calculate_age1(date_of_journey)

            # Render the template with the calculated ages
            return render(request, 'payment1.html', {'age_person1': age_person1, 'age_person2': age_person2,'name_person1': person1.name,
                'name_person2': person2.name1,
                'gender_person1': person1.gender,
                'gender_person2': person2.gender1,'date_of_journey_str':date_of_journey_str})
        else:
            print("Form is invalid")

    else:
        form = chinaform() 

    return render(request, 'china.html', {'form': form})

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def generate_random_invoice_number():
    # Generate a random alphanumeric string of length 8 for the invoice number
    alphanumeric_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choices(alphanumeric_chars, k=8))

def generate_pdf_one(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="invoice.pdf"'
    # Ensure there is at least one record in the queryset
    if chinafield.objects.exists():
        # Get the last (final) record from the queryset
        final_record = chinafield.objects.last()
        # Calculate the ages from the date_of_birth fields
        age = calculate_age(final_record.age)
        age1 = calculate_age(final_record.age1)
        # Convert date_of_journey to the desired format 'dd/mm/yyyy'
        date2 = final_record.date2.strftime('%d/%m/%Y')

        invoice_number = generate_random_invoice_number()

        # Generate the PDF
        pdf = canvas.Canvas(response, pagesize=letter)

        # Customize font and font size
        pdf.setFont("Helvetica-Bold", 12)

        pdf.drawString(500, 770, invoice_number)
        title = "INVOICE"
        pdf.drawString(250, 770, title)

        # Draw the additional content above the table
        content = "Company:Tourist || Paid amount = 1,20,000 Rs || Tourist place: China"
        pdf.drawString(100, 720, content)

        table_data = [
            ["Person 1", "Age", "Gender", "Person 2", "Age", "Gender", "Date of journey"],
            [final_record.name, age, final_record.gender, final_record.name1, age1, final_record.gender1, date2],
        ]

        # Customize the table style
        table_style = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ]

        # Create the table
        table = Table(table_data)
        table.setStyle(table_style)

        # Draw the table at the appropriate position
        table.wrapOn(pdf, 400, 400)
        table.drawOn(pdf, 100, 600)

        pdf.save()
        return response
    else:
        return HttpResponse("No data available.")

# singapore
@login_required(login_url='login')
def singapore(request):
    if request.method == 'POST':
        form = singaporeform(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")
            person1 = form.instance
            person2 = form.instance
            date_of_journey_str = request.POST.get('date2')

            date_of_journey = datetime.strptime(date_of_journey_str, '%Y-%m-%d').date()
            age_person1 = person1.calculate_age(date_of_journey)
            age_person2 = person2.calculate_age1(date_of_journey)

            # Render the template with the calculated ages
            return render(request, 'payment2.html', {'age_person1': age_person1, 'age_person2': age_person2,'name_person1': person1.name,
                'name_person2': person2.name1,
                'gender_person1': person1.gender,
                'gender_person2': person2.gender1,'date_of_journey_str':date_of_journey_str})
        else:
            print("Form is invalid")
    else:
        form = singaporeform()
    return render(request, 'singapore.html', {'form': form})

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def generate_random_invoice_number():
    # Generate a random alphanumeric string of length 8 for the invoice number
    alphanumeric_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choices(alphanumeric_chars, k=8))

def generate_pdf_two(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="invoice.pdf"'
    # Ensure there is at least one record in the queryset
    if singaporefield.objects.exists():
        # Get the last (final) record from the queryset
        final_record = singaporefield.objects.last()
        # Calculate the ages from the date_of_birth fields
        age = calculate_age(final_record.age)
        age1 = calculate_age(final_record.age1)
        # Convert date_of_journey to the desired format 'dd/mm/yyyy'
        date2 = final_record.date2.strftime('%d/%m/%Y')

        invoice_number = generate_random_invoice_number()

        # Generate the PDF
        pdf = canvas.Canvas(response, pagesize=letter)

        # Customize font and font size
        pdf.setFont("Helvetica-Bold", 12)

        pdf.drawString(500, 770, invoice_number)
        title = "INVOICE"
        pdf.drawString(250, 770, title)

        # Draw the additional content above the table
        content = "Company:Tourist || Paid amount = 75,000 Rs || Tourist place: Singapore"
        pdf.drawString(100, 720, content)

        table_data = [
            ["Person 1", "Age", "Gender", "Person 2", "Age", "Gender", "Date of journey"],
            [final_record.name, age, final_record.gender, final_record.name1, age1, final_record.gender1, date2],
        ]

        # Customize the table style
        table_style = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ]

        # Create the table
        table = Table(table_data)
        table.setStyle(table_style)

        # Draw the table at the appropriate position
        table.wrapOn(pdf, 400, 400)
        table.drawOn(pdf, 100, 600)

        pdf.save()
        return response
    else:
        return HttpResponse("No data available.")

# japan
@login_required(login_url='login')
def japan(request):
    if request.method == 'POST':
        form = japanform(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")
            person1 = form.instance
            person2 = form.instance
            date_of_journey_str = request.POST.get('date2')

            date_of_journey = datetime.strptime(date_of_journey_str, '%Y-%m-%d').date()
            age_person1 = person1.calculate_age(date_of_journey)
            age_person2 = person2.calculate_age1(date_of_journey)

            # Render the template with the calculated ages
            return render(request, 'payment3.html', {'age_person1': age_person1, 'age_person2': age_person2,'name_person1': person1.name,
                'name_person2': person2.name1,
                'gender_person1': person1.gender,
                'gender_person2': person2.gender1,'date_of_journey_str':date_of_journey_str})
        else:
            print("Form is invalid")
    else:
        form = japanform()
    return render(request, 'japan.html', {'form': form})

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def generate_random_invoice_number():
    # Generate a random alphanumeric string of length 8 for the invoice number
    alphanumeric_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choices(alphanumeric_chars, k=8))

def generate_pdf_three(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="invoice.pdf"'
    # Ensure there is at least one record in the queryset
    if japanfield.objects.exists():
        # Get the last (final) record from the queryset
        final_record = japanfield.objects.last()
        # Calculate the ages from the date_of_birth fields
        age = calculate_age(final_record.age)
        age1 = calculate_age(final_record.age1)
        # Convert date_of_journey to the desired format 'dd/mm/yyyy'
        date2 = final_record.date2.strftime('%d/%m/%Y')

        invoice_number = generate_random_invoice_number()

        # Generate the PDF
        pdf = canvas.Canvas(response, pagesize=letter)

        # Customize font and font size
        pdf.setFont("Helvetica-Bold", 12)

        pdf.drawString(500, 770, invoice_number)
        title = "INVOICE"
        pdf.drawString(250, 770, title)

        # Draw the additional content above the table
        content = "Company:Tourist || Paid amount = 1,60,000 Rs || Tourist place: Japan"
        pdf.drawString(100, 720, content)

        table_data = [
            ["Person 1", "Age", "Gender", "Person 2", "Age", "Gender", "Date of journey"],
            [final_record.name, age, final_record.gender, final_record.name1, age1, final_record.gender1, date2],
        ]

        # Customize the table style
        table_style = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ]

        # Create the table
        table = Table(table_data)
        table.setStyle(table_style)

        # Draw the table at the appropriate position
        table.wrapOn(pdf, 400, 400)
        table.drawOn(pdf, 100, 600)

        pdf.save()
        return response
    else:
        return HttpResponse("No data available.")

# thailand
@login_required(login_url='login')
def thailand(request):
    if request.method == 'POST':
        form = thailandform(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")
            person1 = form.instance
            person2 = form.instance
            date_of_journey_str = request.POST.get('date2')

            date_of_journey = datetime.strptime(date_of_journey_str, '%Y-%m-%d').date()
            age_person1 = person1.calculate_age(date_of_journey)
            age_person2 = person2.calculate_age1(date_of_journey)

            # Render the template with the calculated ages
            return render(request, 'payment4.html', {'age_person1': age_person1, 'age_person2': age_person2,'name_person1': person1.name,
                'name_person2': person2.name1,
                'gender_person1': person1.gender,
                'gender_person2': person2.gender1,'date_of_journey_str':date_of_journey_str})
        else:
            print("Form is invalid")
    else:
        form = thailandform()
    return render(request, 'thailand.html', {'form': form})

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def generate_random_invoice_number():
    # Generate a random alphanumeric string of length 8 for the invoice number
    alphanumeric_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choices(alphanumeric_chars, k=8))

def generate_pdf_four(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="invoice.pdf"'
    # Ensure there is at least one record in the queryset
    if thailandfield.objects.exists():
        # Get the last (final) record from the queryset

        final_record = thailandfield.objects.last()
        # Calculate the ages from the date_of_birth fields
        age = calculate_age(final_record.age)
        age1 = calculate_age(final_record.age1)

        # Convert date_of_journey to the desired format 'dd/mm/yyyy'
        
        date2 = final_record.date2.strftime('%d/%m/%Y')

        invoice_number = generate_random_invoice_number()

        # Generate the PDF
        pdf = canvas.Canvas(response, pagesize=letter)

        # Customize font and font size
        pdf.setFont("Helvetica-Bold", 12)

        pdf.drawString(500, 770, invoice_number)
        title = "INVOICE"
        pdf.drawString(250, 770, title)

        # Draw the additional content above the table
        content = "Company:Tourist || Paid amount = 55,000 Rs || Tourist place: Thailand"
        pdf.drawString(100, 720, content)

        table_data = [
            ["Person 1", "Age", "Gender", "Person 2", "Age", "Gender", "Date of journey"],
            [final_record.name, age, final_record.gender, final_record.name1, age1, final_record.gender1, date2],
        ]

        # Customize the table style
        table_style = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ]

        # Create the table
        table = Table(table_data)
        table.setStyle(table_style)

        # Draw the table at the appropriate position
        table.wrapOn(pdf, 400, 400)
        table.drawOn(pdf, 100, 600)

        pdf.save()
        return response
    else:
        return HttpResponse("No data available.")

# indoneesia
@login_required(login_url='login')
def indonesia(request):
    if request.method == 'POST':
        form = indonesiaform(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")
            person1 = form.instance
            person2 = form.instance
            date_of_journey_str = request.POST.get('date2')

            date_of_journey = datetime.strptime(date_of_journey_str, '%Y-%m-%d').date()
            age_person1 = person1.calculate_age(date_of_journey)
            age_person2 = person2.calculate_age1(date_of_journey)

            # Render the template with the calculated ages
            return render(request, 'payment5.html', {'age_person1': age_person1, 'age_person2': age_person2,'name_person1': person1.name,
                'name_person2': person2.name1,
                'gender_person1': person1.gender,
                'gender_person2': person2.gender1,'date_of_journey_str':date_of_journey_str})
        else:
            print("Form is invalid")
    else:
        form = indonesiaform()
    return render(request, 'indonesia.html', {'form': form})

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def generate_random_invoice_number():
    # Generate a random alphanumeric string of length 8 for the invoice number
    alphanumeric_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choices(alphanumeric_chars, k=8))

def generate_pdf_five(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="invoice.pdf"'
    # Ensure there is at least one record in the queryset
    if indonesiafield.objects.exists():
        # Get the last (final) record from the queryset
        final_record = indonesiafield.objects.last()
        # Calculate the ages from the date_of_birth fields
        age = calculate_age(final_record.age)
        age1 = calculate_age(final_record.age1)
        # Convert date_of_journey to the desired format 'dd/mm/yyyy'

        date2 = final_record.date2.strftime('%d/%m/%Y')

        invoice_number = generate_random_invoice_number()

        # Generate the PDF
        pdf = canvas.Canvas(response, pagesize=letter)

        # Customize font and font size
        pdf.setFont("Helvetica-Bold", 12)

        pdf.drawString(500, 770, invoice_number)
        title = "INVOICE"
        pdf.drawString(250, 770, title)

        # Draw the additional content above the table
        content = "Company:Tourist || Paid amount = 68,000 Rs || Tourist place: Indonesia"
        pdf.drawString(100, 720, content)

        table_data = [
            ["Person 1", "Age", "Gender", "Person 2", "Age", "Gender", "Date of journey"],
            [final_record.name, age, final_record.gender, final_record.name1, age1, final_record.gender1, date2],
        ]

        # Customize the table style
        table_style = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ]

        # Create the table
        table = Table(table_data)
        table.setStyle(table_style)

        # Draw the table at the appropriate position
        table.wrapOn(pdf, 400, 400)
        table.drawOn(pdf, 100, 600)

        pdf.save()
        return response
    else:
        return HttpResponse("No data available.")

# malaysia
@login_required(login_url='login')
def malaysia(request):
    if request.method == 'POST':
        form = malaysiaform(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")
            person1 = form.instance
            person2 = form.instance
            date_of_journey_str = request.POST.get('date2')

            date_of_journey = datetime.strptime(date_of_journey_str, '%Y-%m-%d').date()
            age_person1 = person1.calculate_age(date_of_journey)
            age_person2 = person2.calculate_age1(date_of_journey)

            # Render the template with the calculated ages
            return render(request, 'payment6.html', {'age_person1': age_person1, 'age_person2': age_person2,'name_person1': person1.name,
                'name_person2': person2.name1,
                'gender_person1': person1.gender,
                'gender_person2': person2.gender1,'date_of_journey_str':date_of_journey_str})
        else:
            print("Form is invalid")
    else:
        form = malaysiaform()
    return render(request, 'malaysia.html', {'form': form})

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def generate_random_invoice_number():
    # Generate a random alphanumeric string of length 8 for the invoice number
    alphanumeric_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choices(alphanumeric_chars, k=8))

def generate_pdf_six(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="invoice.pdf"'
    # Ensure there is at least one record in the queryset
    if malaysiafield.objects.exists():
        # Get the last (final) record from the queryset
        final_record = malaysiafield.objects.last()
        # Calculate the ages from the date_of_birth fields
        age = calculate_age(final_record.age)
        age1 = calculate_age(final_record.age1)

        # Convert date_of_journey to the desired format 'dd/mm/yyyy'
        date2 = final_record.date2.strftime('%d/%m/%Y')
        invoice_number = generate_random_invoice_number()

        # Generate the PDF
        pdf = canvas.Canvas(response, pagesize=letter)

        # Customize font and font size
        pdf.setFont("Helvetica-Bold", 12)

        pdf.drawString(500, 770, invoice_number)
        title = "INVOICE"
        pdf.drawString(250, 770, title)

        # Draw the additional content above the table
        content = "Company:Tourist || Paid amount = 65,000 Rs || Tourist place: Malaysia"
        pdf.drawString(100, 720, content)

        table_data = [
            ["Person 1", "Age", "Gender", "Person 2", "Age", "Gender", "Date of journey"],
            [final_record.name, age, final_record.gender, final_record.name1, age1, final_record.gender1, date2],
        ]

        # Customize the table style
        table_style = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ]

        # Create the table
        table = Table(table_data)
        table.setStyle(table_style)

        # Draw the table at the appropriate position
        table.wrapOn(pdf, 400, 400)
        table.drawOn(pdf, 100, 600)

        pdf.save()
        return response
    else:
        return HttpResponse("No data available.")

@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")
        else:
            print("Form is invalid")
    else:
        form = contactform()
    return render(request, 'contact.html', {'form': form})

@login_required(login_url='login')
def booking(request):
    if request.method == 'POST':
        form = bookingform(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")
            # return redirect(reverse('payment_seven'))
            family = form.instance
            date_of_journey_str = request.POST.get('date')
            from datetime import datetime
            date_of_journey = datetime.strptime(date_of_journey_str, '%Y-%m-%d').date()
            destination = request.POST.get('destination', '')

            # Render the template with the calculated ages
            return render(request, 'payment7.html', {'name_person': family.name,
                'email': family.email,
                'date_of_journey_str':date_of_journey_str,'destination':destination})
        else:
            print("Form is invalid")
            print(form.errors)

    else:
        form = bookingform()
    return render(request, 'booking.html', {'form': form})


def generate_random_invoice_number():
    # Generate a random alphanumeric string of length 8 for the invoice number
    alphanumeric_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choices(alphanumeric_chars, k=8))

def generate_pdf_seven(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="invoice.pdf"'
    
    if bookingfield.objects.exists():
        final_record = bookingfield.objects.last()
        date = final_record.date.strftime('%d/%m/%Y')
        invoice_number = generate_random_invoice_number()
        destination = final_record.destination
        
        # Generate the PDF
        pdf = canvas.Canvas(response, pagesize=letter)
        pdf.setFont("Helvetica-Bold", 12)
        
        pdf.drawString(500, 770, invoice_number)
        title = "INVOICE"
        pdf.drawString(250, 770, title)
        
        content = f"Company: Tourist || Paid amount = 95,000 Rs || Tourist place: {destination}"
        pdf.drawString(100, 720, content)

        # Table data with header row and data row
        table_data = [
            ["Name", "Email", "Date of journey", "Destination"],
            [final_record.name, final_record.email, date, final_record.destination],
        ]

        # Customize the table style
        table_style = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ]

        # Create the table
        table = Table(table_data)
        table.setStyle(table_style)

        # Draw the table at the appropriate position
        table.wrapOn(pdf, 400, 400)
        table.drawOn(pdf, 100, 600)

        pdf.save()
        return response
    else:
        return HttpResponse("No data available.")    


@login_required(login_url='login')
def payment(request):
    if request.method == 'POST':
        form = paymentform(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")
            
            # Since there's no actual payment processing, we assume payment is successful after form submission.
            payment_completed = True
            
            context = {
                'form': form,
                'payment_completed': payment_completed,
            }

            return render(request, 'payment.html', context)
        else:
            print("Form is invalid")
    else:
        form = paymentform()

    # If payment is not completed, set payment_completed to False.
    payment_completed = False

    context = {
        'form': form,
        'payment_completed': payment_completed,
    }

    return render(request, 'payment.html', context)

@login_required(login_url='login')
def payment_one(request):
    if request.method == 'POST':
        form = paymentform_one(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")
            
            # Since there's no actual payment processing, we assume payment is successful after form submission.
            payment_completed = True
            
            context = {
                'form': form,
                'payment_completed': payment_completed,
            }

            return render(request, 'payment1.html', context)
        else:
            print("Form is invalid")
    else:
        form = paymentform_one()

    # If payment is not completed, set payment_completed to False.
    payment_completed = False

    context = {
        'form': form,
        'payment_completed': payment_completed,
    }

    return render(request, 'payment1.html', context)

@login_required(login_url='login')
def payment_two(request):
    if request.method == 'POST':
        form = paymentform_two(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")
            
            # Since there's no actual payment processing, we assume payment is successful after form submission.
            payment_completed = True
            
            context = {
                'form': form,
                'payment_completed': payment_completed,
            }

            return render(request, 'payment2.html', context)
        else:
            print("Form is invalid")
    else:
        form = paymentform_two()

    # If payment is not completed, set payment_completed to False.
    payment_completed = False

    context = {
        'form': form,
        'payment_completed': payment_completed,
    }

    return render(request, 'payment2.html', context)

@login_required(login_url='login')
def payment_three(request):
    if request.method == 'POST':
        form = paymentform_three(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")
            
            # Since there's no actual payment processing, we assume payment is successful after form submission.
            payment_completed = True
            
            context = {
                'form': form,
                'payment_completed': payment_completed,
            }

            return render(request, 'payment3.html', context)
        else:
            print("Form is invalid")
    else:
        form = paymentform_three()

    # If payment is not completed, set payment_completed to False.
    payment_completed = False

    context = {
        'form': form,
        'payment_completed': payment_completed,
    }

    return render(request, 'payment3.html', context)

@login_required(login_url='login')
def payment_four(request):
    if request.method == 'POST':
        form = paymentform_four(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")
            
            # Since there's no actual payment processing, we assume payment is successful after form submission.
            payment_completed = True
            
            context = {
                'form': form,
                'payment_completed': payment_completed,
            }

            return render(request, 'payment4.html', context)
        else:
            print("Form is invalid")
    else:
        form = paymentform_four()

    # If payment is not completed, set payment_completed to False.
    payment_completed = False

    context = {
        'form': form,
        'payment_completed': payment_completed,
    }

    return render(request, 'payment4.html', context)

@login_required(login_url='login')
def payment_five(request):
    if request.method == 'POST':
        form = paymentform_five(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")
            
            # Since there's no actual payment processing, we assume payment is successful after form submission.
            payment_completed = True
            
            context = {
                'form': form,
                'payment_completed': payment_completed,
            }

            return render(request, 'payment5.html', context)
        else:
            print("Form is invalid")
    else:
        form = paymentform_five()

    # If payment is not completed, set payment_completed to False.
    payment_completed = False

    context = {
        'form': form,
        'payment_completed': payment_completed,
    }

    return render(request, 'payment5.html', context)

@login_required(login_url='login')
def payment_six(request):
    if request.method == 'POST':
        form = paymentform_six(request.POST)
        if form.is_valid(): 
            form.save()
            print("Data saved successfully")
            
            # Since there's no actual payment processing, we assume payment is successful after form submission.
            payment_completed = True
            
            context = {
                'form': form,
                'payment_completed': payment_completed,
            }

            return render(request, 'payment6.html', context)
        else:
            print("Form is invalid")
    else:
        form = paymentform_six()

    payment_completed = False

    context = {
        'form': form,
        'payment_completed': payment_completed,
    }
    
    return render(request, 'payment6.html', context)

def payment_seven(request):
    if request.method == 'POST':
        form = paymentform_seven(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")
            context = {
                'form': form,
                'payment_completed': True,
            }

            return render(request, 'payment7.html', context)
        else:
            print("Form is invalid")
    else:
        form = paymentform_seven()

    # If payment is not completed, set payment_completed to False.
    context = {
        'form': form,
        'payment_completed': False,
    }

    return render(request, 'payment7.html', context)

def privacy(request):
    return render (request,'privacy.html')

