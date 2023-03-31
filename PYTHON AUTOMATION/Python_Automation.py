# Visit https://textbelt.com/ to create an API for sending messages.


from credentials import mobile_number
import requests
import schedule
import time


def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': 'Hey King. How are you doing?',
        'key': 'textbelt',
    })
    print(resp.json())

# schedule.every().day.at("07:30").do(send_message())


schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
