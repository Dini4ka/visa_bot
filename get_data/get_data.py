import pandas as pd

def get_data():
    data = []
    logins = pd.ExcelFile('config/mails.xlsx')
    logins_sheet = logins.parse(0)
    mails = logins_sheet['Почта']
    for mail in mails:
        data.append({'mail': mail, 'password':'Megapolis77@'})
    return data


