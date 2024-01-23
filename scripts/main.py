from fastapi import FastAPI
#導入 Item.py 的 Item Class
from Item import Item
#導入 Gmail 發信範例
import mail
app = FastAPI()

# 定義 POST API URL 並指定 Function parameter 為 Item Class
@app.post("/items/")
async def create_item(item: Item):
    # 在此獲取 item object
    print(f"物件名稱：{item.name}",
          f"產品描述：{item.description}",
          f"價格：{item.price}",
          f"稅率：{item.tax}")
    # 將接收 Body 寄送郵件，郵件發送與接收端都設定在 mail.py 中
    mail.send_email(item)
    # 回傳 Response Object
    return item
