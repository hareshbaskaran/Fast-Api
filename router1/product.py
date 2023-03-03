from fastapi import APIRouter,Header,Cookie
from fastapi.responses import Response,PlainTextResponse,JSONResponse

router = APIRouter(
    prefix='/article',
    tags=['article']
    )

product=[
    'watch',
    'cloth',
    'tripod',
    'human'
]
@router.get('/all')
def get_all_products():
    data = " ".join(product)
    return Response(
        content=data,
        media_type="text/plain"
    )
#adding resposes as a set of json data
@router.get('/{id}', responses={
    200:{
        "message":"product available"
    },
    202:{
        "message":"product unavailable"
    }
})    
def get_product(id:int):
    if id > len(product):
        out="Product unavailable"
        return PlainTextResponse(
            status_code=202,
            content={
                "message":out
            }
        
        ) 
    if id < len(product):
        return JSONResponse(
            status_code=202,
            content={
                "message":"Product not listed"
            }
        )   
        
@router.post("/{id}/products")
async def create_products(
    response:Response,
    parameter:str= Header(
        default=None,
        convert_underscores=True
    )
):
    response.set_cookie(
        hey="session",
        value="session-cookie-value"
    )        
    return{
        "Header":parameter,
        "message":"this link uses cookies"
    }
 
    