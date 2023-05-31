headers = ['date', '"media"', '"medium"', '"daypart"', '"audiocode"', '"duration"', '"grp_a_18_24"', '"grp_a_20_30"', '"cost"']

# Usuń cudzysłowy z elementów listy
headers = [header.replace('"', '') for header in headers]

print(headers)
