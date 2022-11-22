from body_bot import VisaBot
from get_data import get_data
from get_data import proxy

if __name__ == '__main__':
    data = get_data()
    print(proxy[0])
    # Start bot
    a = VisaBot(data=data[0], proxy=proxy[0])
    for person in data:
        counter = 0
        a.get_new_data(person)
        counter = 0
        a.get_book_link()
        a.auth()
        a.put_data(person)
        a.logout()
        if (data.index(person) + 1) % 2 == 0:
            counter +=1
            a.quite()
            a=VisaBot(data=person, proxy=proxy[counter])
            print('new proxy was get')
    a.quite()