import requests

headers = {
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://api.ftcscout.org',
}

json_data = {
    'query': '{teamByNumber(number:15118){name}}',
}

response = requests.post('https://api.ftcscout.org/graphql', headers=headers, json=json_data)
print(response.text)