from fastapi import APIRouter,Path,Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder


from service.supplier import SupplierService
from schemas.supplier import Supplier
from config.database import Session 


supplier_router = APIRouter()

@supplier_router.get('/supplier', tags = ['supplier'], status_code=200)
def get_supplier():
    db = Session()
    result = SupplierService(db).get_supplier()
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@supplier_router.get('/supplier_for_id', tags = ['supplier'], status_code=200)
def get_supplier_for_id(id:int):
    db = Session()
    result = SupplierService(db).get_for_id_supplier(id)
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@supplier_router.post('/supplier', tags=['supplier'], status_code= 200)
def create_supplier(supplier:Supplier):
    db = Session()
    SupplierService(db).create_supplier(supplier)
    return JSONResponse(content={"message":"supplier created", 'status_code': 200})


@supplier_router.put('/supplier{id}', tags=['supplier'])
def update_supplier(id:int,data:Supplier):
    db = Session()
    result = SupplierService(db).get_for_id_supplier(id)
    if not result:
        return JSONResponse(content= {"message":"supplier don't found", "status_code":400})
    SupplierService(db).update_supplier(id,data)
    return JSONResponse(content={"message":"supplier update", "status_code":200}, status_code= 200)

@supplier_router.delete('/supplier{id}',tags=['supplier'])
def delete_supplier(id:int):
    db = Session()
    result = SupplierService(db).get_for_id_supplier(id)
    if not result:
        return JSONResponse(content= {"message":"supplier don't found", "status_code": 404})
    SupplierService(db).delete_supplier(id)
    return JSONResponse(content={"message":"supplier delete succesfully", "status_code": 200}, status_code=200)
