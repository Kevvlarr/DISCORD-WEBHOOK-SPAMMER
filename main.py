import time
import requests
import pyfiglet
banner = pyfiglet.figlet_format("KEVVLARR")
print(banner)
msg = input("Please Insert WebHook Spam Message: ")
webhook = input("Please Insert WebHook URL: ")
def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
            time.sleep(5)
            exit()
kevvlarr_top = 1
while kevvlarr_top == 1:
    spam(msg, webhook)
