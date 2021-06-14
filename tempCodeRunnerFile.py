import requests
import json
def sendsms(number, message):
    url = "https://www.fast2sms.com/dev/bulkV2"
    params = {  
        'authorization':'yJ4q2fPYXGNhtvIB6ZR7c9M5pjO8gnil1sACbWaHrFEDUkL3xmLWeIERarSPONoQBXcMfys13dj4kAiF',
        'sender_id': 'TXTIND',
        'message':message,
        'language':'english',
        'route':'v3',
        'numbers':number
    }
    response=requests.get(url,params=params)
    a=response.json()
    print(a)

sendsms("9479875508","Hello mummaaaa")