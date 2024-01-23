from pydantic import BaseModel
# 透過繼承 pydantic 的 BaseModel 來自定義 POST API 的 Request Body
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None