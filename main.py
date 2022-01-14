import requests

''' Variaveis'''
latitude = '-23.5401128'
longitude='-46.6130155'

params = {
    "headers": {
    "accept": "*/*",
    "accept-language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)"
  },
  "referrer": "https://www.ifood.com.br/",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": None,
  "method": "OPTIONS",
  "mode": "cors",
  "credentials": "omit",
  "User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)",
}


url = "https://marketplace.ifood.com.br/v2/merchants?latitude="+latitude+"&longitude="+longitude+"&page=0&channel=IFOOD&size=300&features=&categories=&payment_types=&delivery_fee_from=0&delivery_fee_to=0&delivery_time_from=0&delivery_time_to=240"
with requests.get(url = url, params = params,verify=False) as r:
    print(r.cookies)
    data = r.json() 

lista = list()
for temp in data['merchants']:
    if temp['minimumOrderValue'] <= 10.0 and temp['available'] == True:
        print ("--------------\n")
        print("Restaurante: "+temp['name'])
        print("Link: https://www.ifood.com.br/delivery/"+temp['slug']+"/"+temp['id'])
        lista.append([temp['id'],temp['name'],temp['slug']])

print(lista)

