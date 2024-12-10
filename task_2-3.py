from requests import get
from json import loads
from matplotlib import pyplot
from datetime import timedelta, datetime

Last_date = datetime.today()
First_date = (Last_date - timedelta(7))
Last_date = Last_date.strftime('%Y%m%d')
First_date = First_date.strftime('%Y%m%d')


site = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={int(First_date)}&end={int(Last_date)}&valcode=usd&json"
print(site)
reply = get(site)

reply_json = loads(reply.text)

output_dict = {}
for item in reply_json:
    output_dict[item['exchangedate']] = item['rate']

fig, ax = pyplot.subplots()
ax.plot(output_dict.keys(), output_dict.values())
pyplot.show()