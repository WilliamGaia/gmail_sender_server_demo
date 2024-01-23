from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from prettytable import PrettyTable
import smtplib
import os
from Item import Item

# 從環境變量設定發信信箱
FROM = os.getenv("SENDER")
# 從環境變量設定 Gmail application password
PASSWORD = os.getenv("PASSWORD")
# 從環境變量設定接收信箱
TO = os.getenv("RECEIVER")

def send_email(product_info: Item):
    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["subject"] = "Google mail demo Email"  #郵件標題
    content["from"] = FROM  #寄件者
    content["to"] = TO #收件者
    message = ("以下為測試資訊：")

    tabular_fields = ["產品名稱", "產品描述", "費用", "稅率"]
    tabular_table = PrettyTable()
    tabular_table.field_names = tabular_fields
    tabular_table.add_row([product_info.name,
                               product_info.description,
                               product_info.price,
                               product_info.tax])

    text = tabular_table.get_html_string()

    html = """\
    <html>
        <head>
        <style>
            table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
            }
            th, td {
                padding: 5px;
                text-align: left;    
            }    
        </style>
        </head>
    <body>
    <p></p>
       %s
       您可以透過下列連結來登入管理介面進行確認：<br>
       <a href="https://console.cloud.google.com/welcome">點選以跳轉至 Console 管理介面</a><br>
       
    </p>
    </body>
    </html>
    """ % (text)


    content.attach(MIMEText(message, 'plain'))  #郵件內容 
    content.attach(MIMEText(html, 'html'))

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login(FROM, PASSWORD)  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Message send")
        except Exception as e:
            print("Error message: ", e)