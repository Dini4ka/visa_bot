import pandas as pd
from body_bot import VisaBot

xls = pd.ExcelFile('config/mails.xlsx')
sheet = xls.parse(0)
mails = sheet['Почта']
passwords = sheet['Пароль от аккаунта vfsglobal.com']
print(passwords[1])
print(mails[1])


if __name__ == '__main__':
    a = VisaBot()
    try:
        a.get_book_link()
        a.auth()
        a.logout()
    except Exception as exc:
        print(exc)
    finally:
        a.quite()