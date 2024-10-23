import sqlite3
import random

# 전자제품 관리 클래스
class ElectronicsDatabase:
    def __init__(self, db_name='electronics.db'):
        # 데이터베이스 연결
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # 전자제품 테이블 생성
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS electronics (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_product(self, product_name, price):
        # 전자제품 데이터 삽입
        self.cursor.execute('''
            INSERT INTO electronics (product_name, price) 
            VALUES (?, ?)
        ''', (product_name, price))
        self.conn.commit()
        print(f"'{product_name}' 제품이 추가되었습니다.")

    def update_product(self, product_id, new_name, new_price):
        # 전자제품 데이터 수정
        self.cursor.execute('''
            UPDATE electronics 
            SET product_name = ?, price = ?
            WHERE product_id = ?
        ''', (new_name, new_price, product_id))
        self.conn.commit()
        print(f"ID {product_id}번 제품이 수정되었습니다.")

    def delete_product(self, product_id):
        # 전자제품 데이터 삭제
        self.cursor.execute('''
            DELETE FROM electronics 
            WHERE product_id = ?
        ''', (product_id,))
        self.conn.commit()
        print(f"ID {product_id}번 제품이 삭제되었습니다.")

    def select_all_products(self):
        # 모든 전자제품 조회
        self.cursor.execute('SELECT * FROM electronics')
        products = self.cursor.fetchall()
        for product in products:
            print(product)

    def close(self):
        # 데이터베이스 연결 종료
        self.conn.close()

# 샘플 데이터 생성 및 데이터베이스 조작
def generate_sample_data():
    # 전자제품 이름 샘플
    sample_names = [
        "TV", "Laptop", "Smartphone", "Headphone", "Tablet", 
        "Smartwatch", "Camera", "Printer", "Speaker", "Monitor"
    ]
    
    # ElectronicsDatabase 클래스 인스턴스 생성
    db = ElectronicsDatabase()

    # 100개의 샘플 데이터 삽입
    for i in range(1, 101):
        name = random.choice(sample_names) + f" {i}"  # 제품 이름에 숫자를 추가하여 구분
        price = round(random.uniform(100, 5000), 2)   # 가격은 100~5000 사이의 랜덤 값
        db.insert_product(name, price)

    # 모든 제품 출력
    print("\n--- 모든 전자제품 목록 ---")
    db.select_all_products()

    # 예시로 제품 수정
    db.update_product(1, "Updated TV", 2999.99)
    
    # 예시로 제품 삭제
    db.delete_product(2)

    # 업데이트 후 목록 출력
    print("\n--- 업데이트 후 전자제품 목록 ---")
    db.select_all_products()

    # 데이터베이스 연결 종료
    db.close()

# 샘플 데이터 생성 및 실행
generate_sample_data()
