import requests
import random, string
import datetime
from time import sleep

V2B_REG_REL_URL = '/api/v1/passport/auth/register'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

home_urls = (
    'https://user.bafang.vip',
    'https://cloud.hhygj.xyz'
)
times = 2

subs = []
for current_url in home_urls:
    i = 0
    while i < times:
        form_data = {
            'email': ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(12))+'@gmail.com',
            'password': 'autosub_v2b',
            'invite_code': '',
            'email_code': ''
        }
        headers = {
            'Referer': current_url,
            'User-Agent': USER_AGENT,
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        try:
            response = requests.post(current_url+V2B_REG_REL_URL, data=form_data, headers = headers, timeout=20)
        except Exception as e:
            print(e.args)
            i += 1
            continue
        # print(response.text)
        try:
            subscription_url = f'{current_url}/api/v1/client/subscribe?token={response.json()["data"]["token"]}'
            subs.append(subscription_url)
        except:
            print(f'Invalid response: {response.text.encode("utf-8")}')
            i += 1
            sleep(3)
        else:
            print(f'Number succeeded: {i}\t{subscription_url}')
            break

print(f'{times} accounts created for each site. Subscription URLs:\n----------')
print(*subs, sep='\n')

ind = 0
for sub in subs :
  ind += 1 
  try:
      response = requests.get(sub, timeout=20)
      print(len(response.text))
      with open('base64_subs_' + str(ind), 'w') as f:
        print(response.text, sep='\n', file=f)
  except Exception as e:
      print(e.args)
      continue
    
