# Function2.py
# 약간 더 복잡한 함수
# 합집합
def union(*ar):
    #지역변수
    result = []  #--> 빈 리스트 생성
    for item in ar: #--> 단어 하나씩 가져오기 "HAM" // "EGG" // "SPAM"
        for x in item: #--> 음절 하나씩 가져오기 "H" "A" "M" 등
            if x not in result:
                result.append(x)
    return result

# 호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

#########################################
# 람다함수 정의
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print( (lambda x:x*x) (3) )
print( globals() )
print("  ")
print(dir())

########################################
# 분기
