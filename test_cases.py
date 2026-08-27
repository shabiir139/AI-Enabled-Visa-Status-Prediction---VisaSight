import requests

def test_pagination():
    res = requests.get('http://127.0.0.1:8000/api/cases?page=1&per_page=10')
    if res.status_code == 200:
        data = res.json()
        print("Success! Items:", len(data['items']), "Total:", data['total'])
    else:
        print("Failed!", res.status_code, res.text)

test_pagination()
