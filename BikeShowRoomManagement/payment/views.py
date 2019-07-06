from django.shortcuts import render
from .models import Payment
import urllib
import random
# Create your views here.
def index(request):
    return render(request,'payment/index.html')

def showPayment(request,modify_res=None):
    return render(request,'payment/add_payment.html',{'res':modify_res})

def addPayment(request):
    #print('Button Working')
    pid = request.POST.get('pid')
    pcid  = request.POST.get('pcid')
    pdt = request.POST.get('pdt')
    pbill = request.POST.get('pbill')
    ptype = request.POST.get('ptype')
    pdesc = request.POST.get('pdesc')
    add_payment = Payment(payment_id = pid, payment_customer_id = pcid, payment_date = pdt, payment_bill = pbill, payment_type = ptype, payment_description = pdesc)
    add_payment.save()
    sendSms(request)
    return showPayment(request)

def showEditPayment(request,msg=None):
    rec = Payment.objects.all()
    return render(request,'payment/edit_payment.html',{'my_rec':rec,'msg':msg})

def editPayment(request,msg=None):
    pid = request.POST.get('pid')
    update_data = Payment.objects.filter(payment_id = pid)
    res = list(update_data)[0]
    # print("Res : ",res)
    #print(update_data.payment_id,update_data.payment_custmer_id)
    return showPayment(request,modify_res=res)

def deletePayment(request):
    id = request.POST.get('pid')
    Payment.objects.filter(payment_id = id).delete()
    return showEditPayment(request, msg='Delete Record Sucessfully')

def searchPayment(request):
    pid = request.POST.get('pid')
    search_data = Payment.objects.filter(payment_id=pid)
    res = list(search_data)[0]
    #print("Res : ",res)
    # print(update_data.payment_id,update_data.payment_custmer_id)
    return show_searchPayment(request,modify_res=res)

def show_searchPayment(request,modify_res=None):
    return render(request,'payment/search_payment.html',{'res':modify_res})

def sendSms(request):
    otp = random.SystemRandom().randint(100000, 999999)
    authkey = "267734AuabG429Xov5c8bce1e"  # Your authentication key.
    mobiles = "8096084783" # Multiple mobiles numbers separated by comma.
    message = "Status Demo Testing Payment App..." # Your message to send.
    sender = "MSGIND"  # Sender ID,While using route4 sender id should be 6 characters long.
    route = "4"  # Define route
    # Prepare you post parameters
    values = {
        'authkey': authkey,
        'mobiles': mobiles,
        'message': "Ignore Number :" + str(otp) + '\n' + message ,
        # 'message': message,
        'sender': sender,
        'route': route
    }
    url = "https://control.msg91.com/api/sendhttp.php"  # API URL
    postdata = urllib.parse.urlencode(values)  # URL encoding the data here.
    postdata = postdata.encode('utf-8')
    req = urllib.request.Request(url, postdata)
    response = urllib.request.urlopen(req)
    return response