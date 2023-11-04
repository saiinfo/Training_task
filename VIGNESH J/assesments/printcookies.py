import requests

url='https://www.google.com/'
response=requests.get(url)

if response.status_code ==200:
    print("Response cookies")
    for name,value in response.cookies.items():
        print(f"Cookie Name:{name},value:{value}")
else:
    print(f"Request failed with status code{response.status_code}")
