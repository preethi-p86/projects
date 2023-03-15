from django.shortcuts import render
from django.http import HttpResponse
import decimal
import csv
import hashlib
# from Crypto import Random
# from Crypto.Cipher import AES
# from base64 import b64encode, b64decode

from pkn.models import register_new,login_new, predict, contacting_new, collect_new

from joblib import load
regressor = load('./saved_models/regressor.joblib')

# from .forms import PersonForm
# Create your views here.
def home(request):
    return render(request,'pkn/htmlfile.html')

def services(request):
    return render(request,'pkn/services.html')

def contacting(request):
    if request.method == 'POST':
        contact_name = request.POST.get("contact_name")
        contact_mail = request.POST.get("contact_mail")
        country = request.POST.get('country')
        subject = request.POST.get('subject')
        my2 = contacting_new(contact_name=contact_name,contact_mail=contact_mail,country=country,subject=subject)
        my2.save()
        return HttpResponse("Feedback is sent!")
    else:
        return render(request, 'pkn/htmlfile.html')
#views
def insert_data(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST["lname"]
        mail_id = request.POST["mail_id"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password==confirm_password:
            salt = "5gz"
            database_password = password + salt
            hashed = hashlib.md5(database_password.encode())
            crypted_pass = hashed.hexdigest()
            ins = register_new(fname=fname, lname=lname,mail_id=mail_id,password=crypted_pass,confirm_password=crypted_pass)
            ins.save()
        return HttpResponse("Data Saved")
    else:
        return render(request, 'pkn/login.html')
    
def login(request):
    if request.method == 'POST':
        email_id = request.POST['email_id']
        password2 = request.POST['password2']
        salt = '5gz'
        pass1 = password2 + salt
        hashed1 = hashlib.md5(pass1.encode())
        decrypt_pass = hashed1.hexdigest()
        register_user = register_new.objects.filter(mail_id=email_id,password=decrypt_pass)
        if register_user:
            print("Data written to DB")
            return render(request,'pkn/inside_loin.html')
        else:
            print("Not registered")
    return render(request,'pkn/login.html')

def inside_loin(request):
    return render(request,'pkn/inside_loin.html')

def next_page(request):
    return render(request,'pkn/inside_loin.html')

def predict_data(request):
    if request.method == 'POST':
        # predict_name = request.POST["predict_name"]
        # predict_mail = request.POST["predict_mail"]
        age = request.POST["age"]
        sex = request.POST["sex"]
        bmi = request.POST["bmi"]
        children = request.POST["children"]
        smoker = request.POST["smoker"]
        region = request.POST["region"]
        # charges = request.POST["charges"]
        my = predict(age=age, sex=sex.lower(), bmi=bmi,children=children,smoker=smoker.lower(), region=region.lower().replace(' ',''))
        my.save()
# or sex=='FEMALE' or sex=='Female',  or smoker=='YES' or smoker=='Yes'
        if sex.lower=='female':
            new_sex=0
        else:
            new_sex=1
        if smoker.lower()=='yes':
            new_smoker=1
        else:
            new_smoker=0
        y_pred = regressor.predict([[age,new_sex,bmi,children,new_smoker]])
        print('\n\n', y_pred, '\n\n')
        decimalValue = decimal.Decimal(y_pred[0])
        # rounding the number upto 2 digits after the decimal point
        roundedNumber = decimalValue.quantize(decimal.Decimal('0.00'))

        csv_file_path = "C:/Users/Hp/Desktop/DPS_Project/webapp/pkn/charges2.csv"

        # Open the CSV file in write mode
        with open(csv_file_path, mode='a', newline='') as csv_file:
            # Create a CSV writer object
            writer = csv.writer(csv_file)
            
            writer.writerow([age,sex.lower(),bmi,children,smoker.lower(),region.lower().replace(' ','')])

        return render(request, 'pkn/inside_loin.html', {'result':roundedNumber} )
    else:
        return render(request, 'pkn/inside_loin.html')


# def my_view(request):
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             person = form.save()
#             return render(request, 'pkn/inside_loin.html', {'person': person})
#     else:
#         form = PersonForm()
#     return render(request, 'pkn/htmlfile.html', {'form': form})


def collected_data(request):
    if request.method == 'POST':
        predict_name = request.POST["predict_name"]
        predict_mail = request.POST["predict_mail"]
        age = request.POST["age"]
        sex = request.POST["sex"]
        bmi = request.POST["bmi"]
        children = request.POST["children"]
        smoker = request.POST["smoker"]
        region = request.POST["region"]
        # charges = request.POST["charges"]
        my = collect_new(predict_name=predict_name,predict_mail=predict_mail,age=age, sex=sex.lower(), bmi=bmi,children=children,smoker=smoker.lower(), region=region.lower().replace(' ',''))
        my.save()
# or sex=='FEMALE' or sex=='Female',  or smoker=='YES' or smoker=='Yes'
        if sex.lower=='female':
            new_sex=0
        else:
            new_sex=1
        if smoker.lower()=='yes':
            new_smoker=1
        else:
            new_smoker=0
        y_pred = regressor.predict([[age,new_sex,bmi,children,new_smoker]])
        print('\n\n', y_pred, '\n\n')
        decimalValue = decimal.Decimal(y_pred[0])
        # rounding the number upto 2 digits after the decimal point
        roundedNumber = decimalValue.quantize(decimal.Decimal('0.00'))

        csv_file_path = "C:/Users/Hp/Desktop/DPS_Project/webapp/pkn/charges2.csv"

        # Open the CSV file in write mode
        with open(csv_file_path, mode='a', newline='') as csv_file:
            # Create a CSV writer object
            writer = csv.writer(csv_file)
            
            writer.writerow([age,sex.lower(),bmi,children,smoker.lower(),region.lower().replace(' ','')])

        return render(request, 'pkn/inside_loin.html', {'result':roundedNumber} )
    else:
        return render(request, 'pkn/inside_loin.html')

