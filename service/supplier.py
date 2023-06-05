from models.supplier import Supplier as Suppliermodel
from schemas.supplier import Supplier

class SupplierService():

    def __init__(self,db) -> None:
        self.db = db

    def get_supplier(self):
        result = self.db.query(Suppliermodel).all()
        return result
    
    def create_supplier(self, supplier:Suppliermodel):
        new_supplier = Suppliermodel(
        sub_name=supplier.sub_name,
        address=supplier.address,
        phone=supplier.phone,
        email=supplier.email
        )
        self.db.add(new_supplier)
        self.db.commit()
        return
    
    def update_supplier(self,id:int, data:Supplier):
        supplier = self.db.query(Suppliermodel).filter(Suppliermodel.id == id).first()
        supplier.sub_name = data.sub_name
        supplier.address = data.address
        supplier.phone = data.phone
        supplier.email = data.email
        self.db.commit()
        return 
    
    def delete_supplier(self, id: int):
        self.db.query(Suppliermodel).filter(Suppliermodel.id == id).delete()
        self.db.commit()
        return 
    
    def get_for_id_supplier(self, id:int):
        result = self.db.query(Suppliermodel).filter(Suppliermodel.id == id).first()
        return result
        