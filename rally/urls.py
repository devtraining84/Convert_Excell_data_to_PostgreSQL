"""rally URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main.views import CancelView, CreateRiderView, DeleteRiderView, GroupCreateView, MakeCancelView
from main.views import RestoreView, RiderUpdateView, StartView, ImportExcelView, TableDeleteView, TableUnPaymentView, TableView
from dataresearch.views import ShirtsView, StatisticView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StartView.as_view(), name="index"),
    path('import/',ImportExcelView.as_view(),name="import-excel"),
    path('table/', TableView.as_view(), name='table'),
    path('table/<slug:pk>/update/', RiderUpdateView.as_view(), name="edit-view"),
    path('table/<int:id>/cancel/', MakeCancelView.as_view(), name="make-cancel-view"),
    path('table/<int:id>/restore/', RestoreView.as_view(), name="restore-view"),
    path('table/deleterider/<int:id>', DeleteRiderView.as_view(), name="delete-rider"),
    path('table/delete/', TableDeleteView.as_view(), name='table-delete'),
    path('table/unpayment/', TableUnPaymentView.as_view(), name='table-unpayment'),
    path('table/create/', CreateRiderView.as_view(), name='table-delete'),
    path('statistics/',StatisticView.as_view(),name="statistics"),
    path('shirts/',ShirtsView.as_view(), name="shirts"),
    path('cancelation/',CancelView.as_view(),name="cancelations"),
    path('addgroup/',GroupCreateView.as_view(),name="create-group")
]
