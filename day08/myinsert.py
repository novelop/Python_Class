# STEP 1
import pymysql

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', port=3305, charset='utf8') # 한글처리 (charset = 'utf8')
 
# STEP 3: Connection 으로부터 Cursor 생성
cur = con.cursor(pymysql.cursors.DictCursor)
 
# STEP 4: SQL문 실행 및 Fetch
sql = """insert into emp(e_id,e_name,sex,addr) 
            values(%s,%s,%s,%s)"""
cnt = cur.execute(sql,(5,'5','5','5'))

print("cnt",cnt)

con.commit() 
 

cur.close();
# STEP 5: DB 연결 종료
con.close()