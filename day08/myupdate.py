# STEP 1
import pymysql

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', port=3305, charset='utf8') # 한글처리 (charset = 'utf8')
 
# STEP 3: Connection 으로부터 Cursor 생성
cur = con.cursor()
 
 
e_id = "5"
e_name = "5"
sex = "5"
addr = "5"
# STEP 4: SQL문 실행 및 Fetch
sql = f"""
    update emp
    set 
        e_name='{e_name}',
        sex='{sex}',
        addr='{addr}'
    where e_id='{e_id}'
            """
cnt = cur.execute(sql)

print("cnt",cnt)

con.commit() 
 

cur.close();
# STEP 5: DB 연결 종료
con.close()