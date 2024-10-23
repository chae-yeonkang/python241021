# db1.py

import sqlite3

# 일단 메모리에서 연습
# 영구적으로 파일에 저장
# r: row string notcation
conn = sqlite3.connect(r"c:\work\sample.db")

# 커서 인스턴스 생성
cur = conn.cursor()

# 테이블 구조 생성
cur.execute("create table if not exists PhoneBook (Name text, PhoneNum text);")

# 1건 데이터 입력
cur.execute("insert into PhoneBook values ('derick', '010-222-3333');")

# 입력 파라메터 처리
name = "홍길동"
phoneNumber = "010-111-2222"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))

# 여러건을 입력
datalist = (("전우치", "010-333-4444"), ("박문수", "010-444-5555"))
cur.executemany("insert into PhoneBook values(?, ?);", datalist)

# 입력 데이터 확인
cur.execute("select * from PhoneBook;")
# print(cur.fetchone())
# for row in cur:
#     # print(row)  
#     print(row[0], row[1])

print(cur.fetchall())

# print(cur.fetchmany(2))

# 완료(입력, 수정, 삭제 등)
conn.commit()