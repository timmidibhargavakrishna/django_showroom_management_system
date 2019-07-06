from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,get_object_or_404
from bike.models import Bike
from django.conf import settings

# Create your views here.
def login(request):
    return render(request,'account/login.html')


def show_Home(request):    
    rec = Bike.objects.all()

    return render(request,'home_Page.html',{'rec':rec})

def showBike(request,modify_res=None):
    return render(request, 'bike/add_bike.html', {'res':modify_res})

def addBike(request):
    bike_id = request.POST.get('bike_id')
    bike_customer = request.POST.get('bike_customer')
    bike_number = request.POST.get('bike_number')
    bike_company = request.POST.get('bike_company')
    bike_type = request.POST.get('bike_type')
    bike_desc = request.POST.get('bike_desc')
    price= request.POST.get('price')
    #Uploading biker image ..
    uploaded_file = request.FILES['bike_image']
    fs = FileSystemStorage()
    fs.save(uploaded_file.name,uploaded_file)
    
   # bike_price=request.POST.get('bike_price')
   
    #bike_id,bike_customer,bike_number,bike_type,bike_description
    add_bike = Bike(bike_id=bike_id,bike_company=bike_company,bike_customer=bike_customer,
                    bike_number=bike_number,bike_type=bike_type,bike_description=bike_desc,bike_pic=uploaded_file.name,price=price)
    add_bike.save()
   
   
    return showBike(request)
def uploaded_bike_img(request):
    if request.method == "POST":
            bike_image = request.FILES['bike_image']
            fs = FileSystemStorage()
            fs.save(bike_image.name,bike_image)
            Bike.objects.filter(bike_number=request.session.get('bike_number')).update(profile_pic=bike_image.name)
            res = Bike.objects.filter(bike_number=request.session.get('bike_number'))
            res = list(res)[0]

def showEditBike(request,msg=None):
    rec = Bike.objects.all()
    return render(request, 'bike/edit_bike.html', {'my_rec':rec, 'msg':msg})

def editBike(request,msg=None):
    bike_id = request.POST.get('bike_id')
    print("Bike Id : ",bike_id)
    update_data = Bike.objects.filter(bike_id = bike_id)
    res = list(update_data)[0]
    return showBike(request,modify_res=res)

def deleteBike(request):
    id = request.POST.get('bike_id')
    Bike.objects.filter(bike_id = id).delete()
    return showEditBike(request, msg='Delete Bike Successfully')

def searchBike(request):
    pid = request.POST.get('bike_id')
    search_data = Bike.objects.filter(bike_id=pid)
    res = list(search_data)[0]
    return show_searchBike(request,modify_res=res)

def show_searchBike(request,modify_res=None):
    return render(request, 'bike/search_bike.html', {'res':modify_res})
