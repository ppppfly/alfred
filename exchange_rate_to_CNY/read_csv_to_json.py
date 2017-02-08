import json

objs = []
with open('country_currency_code.csv', 'r') as f:
    for line in f:
        currency, code, country = line.split(',')
        objs.append({
            'currency': currency,
            'code': code,
            'country': country.strip()
        })

with open('contry_currency_code.json', 'w+') as f:
    f.write(json.dumps(objs, ensure_ascii=False))
