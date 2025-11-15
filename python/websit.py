url=input("enter website URL:")
try:
    response=requests.get(url)
    if response.status_code==200:
        print("website is UP")
    else: 
        print("websit returned error:",response.status_code)
except:
    print("website is DOWN or unreachable")
