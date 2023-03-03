
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from import_export import *
from .models import CopyPalukModel, PalukPermamentUnPaymentModel, PalukRidersModel, SubGroupModel, SubGroupNameModel
from tablib import Dataset
from django.http import request, HttpResponse, HttpRequest
from main.resources import PalukRidersModelResources
from django.db.models import Count
from datetime import datetime, timedelta, date
class StartView(TemplateView):
    template_name="base.html"



class ImportExcelView(View):
    def get(self, request):
        return render(request, 'upload.html', {})
    
    def post(self, request):
        person_resource =PalukRidersModelResources()
        dataset = Dataset()
        new_records = request.FILES['my_file']
        imported_data = dataset.load(new_records.read(),format='xlsx')

        for data in imported_data:
            value = PalukRidersModel(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4],
            data[5],
            data[6],
            data[7],
            data[8],
            data[9],
            data[10],
            data[11],
            data[12],
            data[13]
            )
            value.save()
        return redirect('/')




class TableView(View):
    def get(self, request):
        rider_list = PalukRidersModel.objects.filter(canceled = False).order_by('id').values()
        return render(request, 'table.html', {'rider_list': rider_list,})




class TableDeleteView(View):
    def get(self, request):
        rider_list = PalukRidersModel.objects.filter(canceled = False).order_by('id').values()
        return render(request, 'table_delete.html', {'rider_list': rider_list,})




class TableUnPaymentView(View):
    def get(self, request):
        pass




        # for i in range(0,100,1):
        #     a = PalukRidersModel.objects.filter(id=i)
        #     if a.exists():
        #         a = PalukRidersModel.objects.get(id=i)
        #         b = CopyPalukModel()
                
        #         b.date = a.date
        #         b.firstname = a.firstname
        #         b.secondname = a.secondname
        #         b.lastname = a.lastname
        #         b.payment = a.payment
        #         b.region = a.region
        #         b.brand = a.brand
        #         b.model = a.model
        #         b.kind = a.kind
        #         b.shirt = a.shirt
        #         b.road = a.road
        #         b.passenger = a.passenger
        #         b.p_shirt = a.p_shirt
        #         b.canceled = a.canceled
        #         b.save()
        #     else:
        #         pass
        return render(request, 'table.html', {})           



class RiderUpdateView(UpdateView):
    model = PalukRidersModel
    fields = ('date','firstname','secondname','lastname','payment','region','brand','model','kind','shirt','road',
                'passenger','p_shirt')
    template_name = 'update.html'
    success_url = "/table/"



#class TableUnPaymentView(View):
#    def get(self, request):
#        rider_list = PalukRidersModel.objects.filter(payment=False).filter(canceled = False).order_by('id').values()
#        return render(request, 'table.html', {'rider_list': rider_list,})



class DeleteRiderView(View):
    def get(self, request, id):
        rider = PalukRidersModel.objects.get(id=id)
        rider.delete()
        return redirect('/table/')




# class CreateRiderView(CreateView):
#     model = PalukRidersModel
#     fields = ('date','firstname','secondname','lastname','payment','region','brand','model','kind','shirt','road',
#                 'passenger','p_shirt')
#     template_name = 'create.html'
#     success_url = "/table/"


# Here I could'nt use the ModelForm and generic View 
# because it interferes with the existing table and 
# there would be an id increment conflict

class CreateRiderView(View):
    def get(self, request):
        return render(request, 'create.html',{})
   
    def post(self,request):
        last_record = PalukRidersModel.objects.all().order_by("-id")[0]
        
        a = PalukRidersModel()
        a.id = last_record.id + 1
        a.date = request.POST.get("date")
        a.firstname = request.POST.get("firstname")
        a.secondname = request.POST.get("secondname")
        a.lastname = request.POST.get("lastname")
        a.payment = request.POST.get("payment")
        a.region = request.POST.get("region")
        a.brand = request.POST.get("brand")
        a.model = request.POST.get("model")
        a.kind = request.POST.get("kind")
        a.shirt = request.POST.get("shirt")
        a.road = request.POST.get("road")
        a.passenger = request.POST.get("passenger")
        a.p_shirt = request.POST.get("p_shirt")
        a.save()        
        
        return redirect('/table/')




class CancelView(View):
    def get(self, request):
        
        how_many_days = 12
       
        rider_list_black = PalukRidersModel.objects.filter(payment = False).filter(date__gt=datetime.now()-timedelta(days=how_many_days)).filter(canceled = False).order_by('id').values()
        rider_list_red = PalukRidersModel.objects.filter(payment = False).filter(date__lte=datetime.now()-timedelta(days=how_many_days)).filter(canceled = False).order_by('id').values()
        cancel_list = PalukRidersModel.objects.filter(canceled = True).order_by("id")
        ctx = {
              'rider_list_black': rider_list_black,
              'rider_list_red': rider_list_red ,
              'cancel_list': cancel_list
              }
        
        return render(request, 'red_list.html', ctx)


 

class MakeCancelView(View):
    def get(self, request, id):
        record = PalukRidersModel.objects.get(id=id)
        record.canceled = True
        record.save()
        return redirect('/cancelation/')





class RestoreView(View):
    def get(self, request, id):
        record = PalukRidersModel.objects.get(id=id)
        record.canceled = False
        record.save()
        return redirect('/cancelation/')




class GroupCreateView(CreateView):
    model = SubGroupNameModel
    fields = ['group']
    template_name = 'subgroupname_form.html'
    success_url = '/'


