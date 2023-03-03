from django.shortcuts import render
from main.models import PalukRidersModel
from django.views import View
from django.db.models import Count
# Create your views here.


class StatisticView(View):
    def get(self, request):
        queryset_brands = (PalukRidersModel.objects
                .filter(canceled = False)
                .values('brand')
                .annotate(dcount=Count('brand'))
                .order_by('-dcount'))

        queryset_brands_z = (PalukRidersModel.objects
                .filter(payment = True)
                .values('brand')
                .annotate(dcount=Count('brand'))
                .order_by('-dcount'))        
    
        queryset_regions = (PalukRidersModel.objects
                .filter(canceled = False)
                .values('region')
                .annotate(dcount=Count('region'))
                .order_by('-dcount'))

        queryset_regions_z = (PalukRidersModel.objects
                .filter(payment = True)
                .values('region')
                .annotate(dcount=Count('region'))
                .order_by('-dcount'))        

        queryset_kinds = (PalukRidersModel.objects
                .filter(canceled = False)
                .values('kind')
                .annotate(dcount=Count('kind'))
                .order_by('-dcount'))

        queryset_kinds_z = (PalukRidersModel.objects
                .filter(payment = True)
                .values('kind')
                .annotate(dcount=Count('kind'))
                .order_by('-dcount'))   

        queryset_firstnames = (PalukRidersModel.objects
                .filter(canceled = False)
                .values('firstname')
                .annotate(dcount=Count('firstname'))
                .order_by('-dcount'))[:5]
                              

        queryset_firstnames_z = (PalukRidersModel.objects
                .filter(payment = True)
                .values('firstname')
                .annotate(dcount=Count('firstname'))
                .order_by('-dcount'))[:5]  

        queryset_lastnames = (PalukRidersModel.objects
                .filter(canceled = False)
                .values('lastname')
                .annotate(dcount=Count('lastname'))
                .order_by('-dcount'))[:2]
                              
        queryset_lastnames_z = (PalukRidersModel.objects
                .filter(payment = True)
                .values('lastname')
                .annotate(dcount=Count('lastname'))
                .order_by('-dcount'))[:2]          
        
        amount_BMW_GS = len((PalukRidersModel.objects
                .filter(canceled = False)
                .filter(brand = 'BMW')
                .filter(kind__icontains='enduro')
                .filter(model__icontains='GS')))

        amount_transalp = len((PalukRidersModel.objects
                .filter(canceled = False)
                .filter(brand = 'HONDA')
                .filter(kind__icontains='enduro')
                .filter(model__icontains='trans')))        
        
        amount_africa = len((PalukRidersModel.objects
                .filter(canceled = False)
                .filter(brand = 'HONDA')
                .filter(kind__icontains='enduro')
                .filter(model__icontains='africa'))) 

        amount_VT = len((PalukRidersModel.objects
                .filter(canceled = False)
                .filter(brand = 'HONDA')
                .filter(kind__icontains='cruiser')))

        amount_DL = len((PalukRidersModel.objects
                .filter(canceled = False)
                .filter(brand = 'SUZUKI')
                .filter(kind__icontains='turystyczne')
                .filter(model__icontains='DL')))

        amount_BMW_GS_z = len((PalukRidersModel.objects
                .filter(payment = True)
                .filter(brand = 'BMW')
                .filter(kind__icontains='enduro')
                .filter(model__icontains='GS')))

        amount_transalp_z = len((PalukRidersModel.objects
                .filter(payment = True)
                .filter(brand = 'HONDA')
                .filter(kind__icontains='enduro')
                .filter(model__icontains='trans')))        
        
        amount_africa_z = len((PalukRidersModel.objects
                .filter(payment = True)
                .filter(brand = 'HONDA')
                .filter(kind__icontains='enduro')
                .filter(model__icontains='africa'))) 

        amount_VT_z = len((PalukRidersModel.objects
                .filter(payment = True)
                .filter(brand = 'HONDA')
                .filter(kind__icontains='cruiser')))

        amount_DL_z = len((PalukRidersModel.objects
                .filter(payment = True)
                .filter(brand = 'SUZUKI')
                .filter(kind__icontains='turystyczne')
                .filter(model__icontains='DL')))  

        queryset_tshirt = (PalukRidersModel.objects
                .filter(payment = True)
                .values('shirt')
                .annotate(dcount=Count('shirt'))
                .order_by('shirt'))

        queryset_pass_shirt = (PalukRidersModel.objects
                .filter(payment = True)
                .values('p_shirt')
                .annotate(dcount=Count('p_shirt'))
                .order_by('p_shirt'))
        data = [
                 {'group':'Suzuki DL V-Strom','amount': amount_DL},
                 {'group':'Honda Shadow','amount': amount_VT},
                 {'group':'BMW GS','amount': amount_BMW_GS},
                 {'group':'Africa Twin','amount': amount_africa},
                 {'group':'Transalp','amount': amount_transalp}
        ]

        data_z = [
                 {'group':'Suzuki DL V-Strom','amount': amount_DL_z},
                 {'group':'Honda Shadow','amount': amount_VT_z},
                 {'group':'BMW GS','amount': amount_BMW_GS_z},
                 {'group':'Africa Twin','amount': amount_africa_z},
                 {'group':'Transalp','amount': amount_transalp_z}
        ]

        sort_data =  sorted(data, key=lambda d: -d['amount'])
        sort_data_z =  sorted(data_z, key=lambda d: -d['amount'])

        ctx = {'queryset_brands' : queryset_brands,
                'queryset_brands_z' : queryset_brands_z,
               'queryset_regions': queryset_regions,
               'queryset_regions_z': queryset_regions_z,
               'queryset_kinds':queryset_kinds,
               'queryset_kinds_z':queryset_kinds_z,
               'data' : sort_data,
               'data_z' : sort_data_z,
               'firstnames' : queryset_firstnames,
               'firstnames_z' : queryset_firstnames_z,
               'lastnames' : queryset_lastnames,
               'lastnames_z' : queryset_lastnames_z,
               'shirt': queryset_tshirt,
               'p_shirt': queryset_pass_shirt
                                 }
        
        
        return render(request, 'statistics.html', ctx)




class ShirtsView(View):
        def get(self, request):
                m_s = len(PalukRidersModel.objects.filter(payment=True).filter(shirt='Męska S')) + len((PalukRidersModel.objects.filter(payment=True).filter(p_shirt='Męska S')))   
                m_m = len(PalukRidersModel.objects.filter(payment=True).filter(shirt='Męska M')) + len((PalukRidersModel.objects.filter(payment=True).filter(p_shirt='Męska M')))                   
                m_l = len(PalukRidersModel.objects.filter(payment=True).filter(shirt='Męska L')) + len((PalukRidersModel.objects.filter(payment=True).filter(p_shirt='Męska L')))
                m_xl = len(PalukRidersModel.objects.filter(payment=True).filter(shirt='Męska XL')) + len((PalukRidersModel.objects.filter(payment=True).filter(p_shirt='Męska XL')))
                m_xxl = len(PalukRidersModel.objects.filter(payment=True).filter(shirt='Męska XXL')) + len((PalukRidersModel.objects.filter(payment=True).filter(p_shirt='Męska XXL')))
                m_xxxl = len(PalukRidersModel.objects.filter(payment=True).filter(shirt='Męska XXXL')) + len((PalukRidersModel.objects.filter(payment=True).filter(p_shirt='Męska XXXL')))
                d_s = len(PalukRidersModel.objects.filter(payment=True).filter(shirt='Damska S')) + len((PalukRidersModel.objects.filter(payment=True).filter(p_shirt='Damska S')))
                d_m = len(PalukRidersModel.objects.filter(payment=True).filter(shirt='Damska M')) + len((PalukRidersModel.objects.filter(payment=True).filter(p_shirt='Damska M'))) 
                d_l = len(PalukRidersModel.objects.filter(payment=True).filter(shirt='Damska L')) + len((PalukRidersModel.objects.filter(payment=True).filter(p_shirt='Damska L')))
                d_xl = len(PalukRidersModel.objects.filter(payment=True).filter(shirt='Damska XL')) + len((PalukRidersModel.objects.filter(payment=True).filter(p_shirt='Damska XL'))) 
                d_xxl = len(PalukRidersModel.objects.filter(payment=True).filter(shirt='Damska XXL')) + len((PalukRidersModel.objects.filter(payment=True).filter(p_shirt='Damska XXL'))) 

                control_driver = len(PalukRidersModel.objects.filter(payment=True))
                control_passenger = len(PalukRidersModel.objects.filter(payment=True).filter(passenger = True))
                teams = control_passenger + control_driver        
                
                sizes = [
                        {'size':'Męska S' ,'amount': m_s}, 
                        {'size':'Męska M','amount' : m_m}, 
                        {'size':'Męska L' ,'amount': m_l}, 
                        {'size':'Męska XL', 'amount': m_xl}, 
                        {'size':'Męska XXL','amount': m_xxl}, 
                        {'size':'Męska XXXL','amount': m_xxxl}, 
                        {'size':'Damska S', 'amount' : d_s}, 
                        {'size':'Damska M', 'amount': d_m}, 
                        {'size':'Damska L', 'amount': d_l}, 
                        {'size':'Damska XL', 'amount' : d_xl}, 
                        {'size':'Damska XXL','amount': d_xxl}, 
                        {'size':'SUMA','amount': m_s + m_m + m_l + m_xl + m_xxl + m_xxxl + d_s + d_m + d_l + d_xl + d_xxl}
                ]

                ctx = {
                        'sizes': sizes,
                        'drivers' : control_driver,
                        'passengers': control_passenger,
                        'teams': teams                               
                }
                        
                return render(request, 'sizes.html', ctx)        
                        
                        
                  
              
              