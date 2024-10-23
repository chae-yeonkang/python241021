import re

def check_email(email):
    """
    이메일 주소가 유효한지 검사하는 함수.
    유효한 이메일은 다음과 같은 형식을 가집니다:
    1. 이메일 앞 부분: 영문자, 숫자, 마침표, 대시(-), 밑줄(_) 허용
    2. '@' 기호
    3. 도메인 이름: 영문자와 숫자로 시작하며, 마침표(.)로 구분된 부분을 포함
    4. 최종 도메인: 최소 2글자 이상의 영문자
    """
    # 이메일 정규표현식 (올바른 형식을 검증하기 위한 패턴)
    pattern = r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # re.search를 이용해 이메일 형식을 체크 (패턴에 맞는지 확인)
    if re.search(pattern, email):
        return True  # 이메일이 유효한 경우
    else:
        return False  # 이메일이 유효하지 않은 경우

# 테스트할 샘플 이메일 10개 (유효한 것과 유효하지 않은 것)
test_emails = [
    "test@example.com",         # 유효한 이메일 (정상적인 형식)
    "user.name@domain.co",      # 유효한 이메일 (도메인 이름이 짧음)
    "user123@domain.com",       # 유효한 이메일 (숫자가 포함된 경우)
    "user-name@domain.org",     # 유효한 이메일 (대시(-)가 포함된 경우)
    "user_name@domain.net",     # 유효한 이메일 (밑줄(_)이 포함된 경우)
    "user@sub.domain.com",      # 유효한 이메일 (서브도메인 포함)
    "invalid-email@domain",     # 유효하지 않은 이메일 (최종 도메인이 없음)
    "@domain.com",              # 유효하지 않은 이메일 (이메일 앞 부분이 없음)
    "username@.com",            # 유효하지 않은 이메일 (도메인 이름이 없음)
    "username@domain..com"      # 유효하지 않은 이메일 (연속된 마침표가 있음)
]

# 각 이메일 샘플에 대해 유효성 체크
for email in test_emails:
    result = check_email(email)  # 이메일이 유효한지 검사
    print(f"'{email}' 은(는) 유효한 이메일인가? {result}")  # 결과 출력
