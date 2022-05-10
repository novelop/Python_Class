# STEP 1
import pymysql

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', port=3305, charset='utf8') # 한글처리 (charset = 'utf8')
 
# STEP 3: Connection 으로부터 Cursor 생성
cur = con.cursor()
 
# STEP 4: SQL문 실행 및 Fetch
sql = "SELECT * FROM emp"
cur.execute(sql)
 
# 데이타 Fetch
rows = cur.fetchall()

#print(rows)     # 전체 rows

for row in rows:
    print(row[0],row[1],row[2],row[3])

cur.close();
# STEP 5: DB 연결 종료
con.close()