import requests
import random
import string
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def generate_random_email():
    domains = ["smus.ca"]
    letters = string.ascii_lowercase
    name_length = random.randint(5, 10)
    name = ''.join(random.choice(letters) for i in range(name_length))
    domain = random.choice(domains)
    return f"{name}@{domain}"

def generate_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password_length = random.randint(8, 16)
    password = ''.join(random.choice(characters) for i in range(password_length))
    return password
def generate_shit():
    # Generate and print a random email and password
    random_email = generate_random_email()
    random_password = generate_random_password()
    #print(f"Random Email: {random_email}")
    #print(f"Random Password: {random_password}")
    url = "https://www.topgetfoyyou.lat/"

    # URL parameters
    params = {
        "sl": "5737766-21cfa",
        "data1": random_email,
        "data2": random_password,
        "tag": "{External_ID_from_traffic_source}",
        "website": "{subID}",
        "placement": "{sub_subID}",
        "eyeg": "fc8f3b59f6a58798b4860b9f8558216e",
        "eyer": "0.9128213540276893",
        "eyei": "0",
        "eyew": "2097",
        "eyeh": "1313",
        "eyetd": "210",
        "eyef": "sheffergallery.com"
    }

    # Headers
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-CN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-GB;q=0.6,en-US;q=0.5",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-ch-ua-platform-version": "\"5.15.0\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "cross-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }
    return url,headers,params
reqcnt = 0
while True:
    url,headers,params = generate_shit()
    try:
        response = requests.get(url, headers=headers, params=params,verify=False)
        if response.status_code == 200:
            reqcnt += 1
            print(reqcnt)

            # Process the response here
            #print(response.text)
    except requests.exceptions.RequestException as e:
        continue
