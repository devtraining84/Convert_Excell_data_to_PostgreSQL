from import_export import resources
from .models import PalukRidersModel



class PalukRidersModelResources(resources.ModelResource):
    class meta:
        model = PalukRidersModel