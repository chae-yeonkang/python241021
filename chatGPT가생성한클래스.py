# Person 클래스
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        # f-srting: 포맷 스트링(python3.6이상부터 가능)
        print(f"ID: {self.id}, Name: {self.name}")

# Manager 클래스 (Person 상속)
class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

# Employee 클래스 (Person 상속)
class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 테스트 코드
def test_classes():
    print("테스트 1: Person 클래스")
    p1 = Person(1, "Alice")
    p1.printInfo()

    print("\n테스트 2: Person 클래스")
    p2 = Person(2, "Bob")
    p2.printInfo()

    print("\n테스트 3: Manager 클래스")
    m1 = Manager(3, "Charlie", "Team Lead")
    m1.printInfo()

    print("\n테스트 4: Manager 클래스")
    m2 = Manager(4, "David", "Project Manager")
    m2.printInfo()

    print("\n테스트 5: Employee 클래스")
    e1 = Employee(5, "Eve", "Python")
    e1.printInfo()

    print("\n테스트 6: Employee 클래스")
    e2 = Employee(6, "Frank", "Java")
    e2.printInfo()

    print("\n테스트 7: Manager 클래스 상속 확인")
    assert isinstance(m1, Person), "m1은 Person의 인스턴스가 아닙니다."

    print("\n테스트 8: Employee 클래스 상속 확인")
    assert isinstance(e1, Person), "e1은 Person의 인스턴스가 아닙니다."

    print("\n테스트 9: Manager 클래스 인스턴스 변수 확인")
    assert hasattr(m1, 'title'), "m1에는 title이 없습니다."

    print("\n테스트 10: Employee 클래스 인스턴스 변수 확인")
    assert hasattr(e1, 'skill'), "e1에는 skill이 없습니다."

# 테스트 실행
test_classes()
