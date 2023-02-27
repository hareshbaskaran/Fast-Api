from fastapi import APIRouter
from fastapi.responses import Response

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