# 파일을 쓰기
# 유니코드로 쓰기: 한글, 중국어, 일본어
f = open("demo.txt", "wt", encoding="utf-8")
f.write("첫번쩨\n두번째\n세번째\n")
f.close()

# 파일을 읽기
f = open("demo.txt", "rt", encoding="utf-8")
print(f.read())
print(f.readline() )
f.close()




#str클래스의 메서드 연습
# print(dir(str))
# 원본 데이터
data = "<<< spam and ham >>>"
result = data.strip("<>").strip()
print(result)
print(data)
result2 = result.replace("spam", "spam and egg")
print(result2)
lst = result2.split()
print(lst)
print(":)".join(lst))



print("MBC2580".isalnum())
print("MBC2580".isalpha())
print("2580".isdigit())
print("2580".isdecimal())
print("2580".isnumeric())
print()
