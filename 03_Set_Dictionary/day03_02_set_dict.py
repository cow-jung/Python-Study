# 이론
'''
변수는 무조건 하나의 값 | data = 10

파이썬 자료구조를 위한 컬렉션
1. 리스트 [대괄호]
2. 튜플 (소괄호)
3. 셋 {중괄호} = 집합
    중복이 없도록 값을 관리한다.
    집합 연산을 주로 한다.

4. 딕셔너리 {중괄호}
'''
'''
# set 셋 이란?
tags = {"python", "web", "python", "ai"}

print(tags) >>> {'python', 'web', 'ai'}
'''
'''
#셋 추가(add) / 삭제(remove)
tags = {"python", "web"}
tags.add("ai")
print(tags) >>> {'python', 'web', 'ai'}

tags.remove("web")
print(tags) >>> {'ai', 'python'}
'''
'''
# 포함 여부 확인 | in 을 사용하여 어떤 값이 컬렉션 안에 있는지 확인한다.
roles = {"admin", "teacher", "student"}

print("teacher" in roles) >>> True
print("guest" in roles) >>> False
'''
'''
# len() 함수 | 셋에 들어있는 값의 개수를 알려주는데 셋은 중복을 제거하므로 넣은 개수와 결과 개수가 다를 수 있다.
attendees = {"민수", "지연", "민수", "도윤"}
print(len(attendees)) >>> 3
'''
'''
# 셋의 집합 연산
python_class = {"민수", "지연", "도윤", "서연"}
web_class = {"지연", "서연", "하준", "유나"}

A & B: 교집합, A와 B에 모두 있는 값
print(python_class & web_class) >>> {'서연', '지연'}

A | B: 합집합, A와 B를 모두 합친 값
print(python_class | web_class) >>> {'민수', '지연', '도윤', '서연', '하준', '유나'}

A - B: 차집합, A에는 있지만 B에는 없는 값
print(python_class - web_class) >>> {'민수', '도윤'}

A ^ B: 대칭 차집합, A 또는 B 한쪽에만 있는 값
print(python_class ^ web_class) >>> {'민수', '도윤', '하준', '유나'}
'''
#======================================================================================================
# 이론
'''
변수는 무조건 하나의 값 | data = 10

파이썬 자료구조를 위한 컬렉션
1. 리스트 [대괄호]
2. 튜플 (소괄호)
3. 셋 {중괄호} 
4. 딕셔너리 {중괄호}
    키 : 값 형태로 데이터를 저장하는 자료구조
    키로 값을 꺼낸다.
    하나의 키에 값을 여러개 넣고싶으면 리스트로 넣을 수 있다~
    
'''
student = {
    "name": "민수",
    "age": 20,
    "major": "컴퓨터공학"
}
'''
# 딕셔너리 값 조회
student = {"name": "민수", "score": 90}

print(student["name"]) >>> 민수
print(student["score"]) >>> 90
'''
'''
# 딕셔너리 값 수정과 추가
student = {"name": "민수", "score": 90}
student["score"] = 95
print(student) >>> {'name': '민수', 'score': 95}

student["grade"] = "A"
print(student) >>> {'name': '민수', 'age': 20, 'major': '컴퓨터공학', 'grade': 'A'}
'''
'''
# 딕셔너리 값 삭제
student = {"name": "민수", "score": 90, "temp": "삭제예정"}
del student["temp"]
print(student) >>> {'name': '민수', 'score': 90}
'''
'''
# 딕셔너리의 keys(), values(), items()
# keys() : 딕셔너리의 키만 보고 싶을 때 사용
user = {"name": "지연", "email": "jiyeon@example.com", "active": True}
print(user.keys()) >>> dict_keys(['name', 'email', 'active'])

# values() : 값만 보고 싶을 때 사용
print(user.values()) >>>dict_values(['지연', 'jiyeon@example.com', True])

# items() : 키와 값을 함께 보고 싶을 때 사용
print(user.items()) >>> dict_items([('name', '지연'), ('email', 'jiyeon@example.com'), ('active', True)])
'''

# 문제 1
print("문제1 -----------------------------------------------------------------------------")
tags = {"python", "web", "python", "ai", "web"}
print(f"태그 목록 : {tags}")
print(f"태그 개수 : {len(tags)}")

# 문제 2
print("문제2 -----------------------------------------------------------------------------")
attendance = {"민수", "지연", "민수", "서연", "도윤", "지연"}
print(f"실제 출석 학생 : {attendance}")
print(f"실제 출석 인원 : {len(attendance)}")

# 문제 3
print("문제3 -----------------------------------------------------------------------------")
interests = {"파이썬", "웹", "AI"}
interests.add("데이터분석")
print(f'관심 분야 : {interests}')

# 문제 4
print("문제4 -----------------------------------------------------------------------------")
post_tags = {"공지", "중요", "초안", "파이썬"}
post_tags.remove("초안")
print(f'게시글 태그 : {post_tags}')

# 문제 5
print("문제5 -----------------------------------------------------------------------------")
roles = {"admin", "teacher", "student"}
print(f'teacher 권한 : {"teacher" in roles}')
print(f'guest 권한 : {"guest" in roles}')

# 문제 6
print("문제6 -----------------------------------------------------------------------------")
visited = {"home", "login", "notice"}
visited.add("profile")
print(f'방문 페이키 : {visited}')
print(f'login 권한 : {"login" in visited}')
print(f'방문 페이지 수 : {len(visited)}')

# 문제 7
print("문제7 -----------------------------------------------------------------------------")
subjects = {"파이썬", "웹", "DB", "파이썬", "DB"}
print(f'최종 수강 과목 : {subjects}')
print(f'최종 과목 수 : {len(subjects)}')

# 문제 8
print("문제8 -----------------------------------------------------------------------------")
blocked_words = {"spam", "ads", "fake"}
word = "ads"
print(f'검사 단어 : {word}')
print(f'금지어 여부 : {word in blocked_words}')

# 문제 9
print("문제9 -----------------------------------------------------------------------------")
student = {
    "name": "민수",
    "age": 20,
    "major": "컴퓨터공학"
}
print(f'이름 : {student["name"]}')
print(f'나이 : {student["age"]}')
print(f'전공 : {student["major"]}')

# 문제 10
print("문제10 -----------------------------------------------------------------------------")
product = {
    "name": "키보드",
    "price": 45000,
    "stock": 8
}
print(f'상품명 : {product["name"]}')
print(f'가격 : {product["price"]}원')
print(f'재고 : {product["stock"]}개')
print(f'총 재고 금액 : {product["price"] * product["stock"]}원')

# 문제 11
print("문제11 -----------------------------------------------------------------------------")
student = {"name": "지연", "score": 88}
student["score"] = 95
print(f'수정된 학생 정보 : {student}')

# 문제 12
print("문제12 -----------------------------------------------------------------------------")
member = {
    "name": "도윤",
    "email": "doyun@example.com"
}
member["phone"] = "010-1111-2222"
print(f'회원 정보 : {member}')

# 문제 13
print("문제13 -----------------------------------------------------------------------------")
account = {
    "username": "seoyeon",
    "level": 3,
    "temp": "삭제할 값"
}
del account["temp"]
print(f'계정 정보 : {account}')

# 문제 14
print("문제14 -----------------------------------------------------------------------------")
book = {
    "title": "파이썬 입문",
    "author": "김코딩",
    "price": 18000
}
print(f'키 목록 : {book.keys()}')
print(f'값 목록 : {book.values()}')
print(f'키-값 목록 : {book.items()}')

# 문제 15
print("문제15 -----------------------------------------------------------------------------")
student = {
    "name": "하준",
    "scores": [80, 90, 85]
}
total_scores = sum(student["scores"])
avg_scores = total_scores / len(student["scores"])

print(f'학생 이름 : {student["name"]}')
print(f'점수 목록 : {student["scores"]}')
print(f'총점 : {total_scores}')
print(f'평균 : {avg_scores:.2f}')

# 문제 16
print("문제16 -----------------------------------------------------------------------------")
route = {
    "number": "740",
    "stations": ["덕은동", "연세대", "서울역", "강남역"]
}
print(f'노선 번호 : {route["number"]}')
print(f'첫 정류장 : {route["stations"][0]}')
print(f'마지막 정류장 : {route["stations"][-1]}')
print(f'정류장 수 : {len(route["stations"])}')

# 문제 17
print("문제17 -----------------------------------------------------------------------------")
user = {
    "username": "minsu",
    "roles": {"viewer", "editor"}
}
user["roles"].add("student")
print(f'사용자 : {user["username"]}')
print(f'editor 권한 여부 : {"editor" in user["roles"]}')
print(f'수정된 사용자 정보 : {user}')

# 문제 18
print("문제18 -----------------------------------------------------------------------------")
post = {
    "title": "컬렉션 정리",
    "tags": {"파이썬", "초안", "자료구조"}
}
post["tags"].remove("초안")
post["tags"].add("공개")

print(f'게시글 제목 : {post["title"]}')
print(f'최종 태그 : {post["tags"]}')

# 문제 19
print("문제19 -----------------------------------------------------------------------------")
product = {
    "name": "무선 마우스",
    "price": 39000,
    "badges": {"new", "hot", "sale"}
}
print(f'상품명 : {product["name"]}')
print(f'hot 뱃지 여부 : {"hot" in product["badges"]}')
print(f'뱃지 개수 : {len(product["badges"])}')

# 문제 20
print("문제20 -----------------------------------------------------------------------------")
course = {
    "title": "파이썬 기초",
    "students": {"민수", "지연", "도윤", "민수"},
    "scores": [88, 92, 79]
}
avg_scores = sum(course["scores"]) / len(course["scores"])

print(f'강의명 : {course["title"]}')
print(f'수강생 수 : {len(course["students"])}')
print(f'평균 점수 : {avg_scores:.2f}')

# 문제 21
print("문제21 -----------------------------------------------------------------------------")
attendance = {"민수", "지연", "민수", "도윤", "하준"}
attendance.add("서연")
print(f'출석 명단 : {attendance}')
print(f'실제 축석 인원 : {len(attendance)}')
print(f'민수 출석 여부 : {"민수" in attendance}')

# 문제 22
print("문제22 -----------------------------------------------------------------------------")
tags = {"파이썬", "자료구조", "초안", "중요"}
tags.remove("초안")
tags.add("공개")
print(f'최종 태그 : {tags}')
print(f'태그 개수 : {len(tags)}')

# 문제 23
print("문제23 -----------------------------------------------------------------------------")
member = {
    "name": "지연",
    "grade": "BASIC",
    "point": 12000
}
member["grade"] = "VIP"
member["point"] += 3000

print(f'회원명 : {member["name"]}')
print(f'등급 : {member["grade"]}')
print(f'포인트 : {member["point"]}원')

# 문제 24
print("문제24 -----------------------------------------------------------------------------")
product = {
    "name": "무선 키보드",
    "price": 69000,
    "stock": 5
}
product["category"] = "주변기기"
stock_price = product["price"] * product["stock"]
print(f'상품명 : {product["name"]}')
print(f'카테고리 : {product["category"]}')
print(f'재고 금액 : {stock_price}원')

# 문제 25
print("문제25 -----------------------------------------------------------------------------")
user = {
    "username": "doyun",
    "email": "doyun@example.com",
    "temp": "삭제할 값"
}
del user["temp"]
print(f'사용자 정보 : {user}')
print(f'키 목록 : {user.keys()}')

# 문제 26
print("문제26 -----------------------------------------------------------------------------")
student = {
    "name": "민수",
    "scores": [88, 92, 79, 95]
}
total_scores = sum(student["scores"])
avg_scores = total_scores / len(student["scores"])
max_scores = max(student["scores"])
min_scores = min(student["scores"])

print(f'학생 이름 : {student["name"]}')
print(f'총점 : {total_scores}')
print(f'평균 : {avg_scores:.2f}')
print(f'최고점 : {max_scores}')
print(f'최저점 : {min_scores}')

# 문제 27
print("문제27 -----------------------------------------------------------------------------")
route = {
    "number": "143",
    "stations": ["정릉", "미아", "종로", "강남"]
}
print(f'노선 번호 : {route["number"]}')
print(f'첫 정류장 : {route["stations"][0]}')
print(f'마지막 정류장 : {route["stations"][-1]}')
print(f'정류장 수 : {len(route["stations"])}')

# 문제 28
print("문제28 -----------------------------------------------------------------------------")
user = {
    "username": "seoyeon",
    "roles": {"student", "viewer"}
}
user["roles"].add("editor")

print(f'사용자 : {user["username"]}')
print(f'권한 목록 : {user["roles"]}')
print(f'admin 권한 여부 : {"admin" in user["roles"]}')
print(f'권한 수 : {len(user["roles"])}')

# 문제 29
print("문제29 -----------------------------------------------------------------------------")
course = {
    "title": "웹 기초",
    "students": {"민수", "지연", "민수", "도윤"},
    "scores": [80, 90, 85]
}
total_students = sum(course["scores"])
avg_scores = total_students / len(course["students"])

print(f'강의 명 : {course["title"]}')
print(f'수강생 수 : {len(course["students"])}')
print(f'평균 점수 : {avg_scores:.2f}')

# 문제 30
print("문제30 -----------------------------------------------------------------------------")
order = {
    "items": ["마우스", "키보드", "모니터"],
    "prices": [30000, 45000, 250000]
}

print(f'첫 상품 : {order["items"][0]}')
print(f'마지막 상품 : {order["items"][-1]}')
print(f'총 주문 금액 : {sum(order["prices"])}원')

# 문제 31
print("문제31 -----------------------------------------------------------------------------")
post = {
    "title": "시험 공지",
    "tags": {"공지", "중요"}
}
post["tags"].add("공개")

print(f'제목 : {post["title"]}')
print(f'태그 목록 : {post["tags"]}')
print(f'태그 수 : {len(post["tags"])}')
print(f'중요 태그 여부 : {"중요" in post["tags"]}')

# 문제 32
print("문제32 -----------------------------------------------------------------------------")
book = {
    "title": "파이썬 입문",
    "author": "김코딩",
    "available": True,
    "temp": "삭제"
}
del book["temp"]

print(f'도서 정보 : {book["title"]}')
print(f'대출 가능 여부 : {book["available"]}')
print(f'값 목록: {book.values()}')

# 문제 33
print("문제33 -----------------------------------------------------------------------------")
profile = {
    "name": "하준",
    "courses": ["파이썬", "웹", "DB"],
    "interests": {"파이썬", "AI", "데이터"}
}

print(f'학생 이름 : {profile["name"]}')
print(f'수강 과목 수 : {len(profile["courses"])}')
print(f'첫 과목 : {profile["courses"][0]}')
print(f'AI 관심 여부 : {"AI" in profile["interests"]}')

# 문제 34
print("문제34 -----------------------------------------------------------------------------")
product = {
    "name": "후드티",
    "options": ["black", "white"],
    "badges": {"new", "old", "sale"}
}
product["options"].append("blue")
product["badges"].remove("old")

print(f'상품명 : {product["name"]}')
print(f'옵션 목록: {product["options"]}')
print(f'옵션 수 : {len(product["options"])}')
print(f'최종 뱃지 : {product["badges"]}')

# 문제 35
print("문제35 -----------------------------------------------------------------------------")
activity = {
    "username": "minsu",
    "pages": ["home", "login", "profile", "notice"],
    "tags": {"study", "python", "study", "web"}
}
print(f'사용자 : {activity["username"]}')
print(f'방문 페이지 수 : {len(activity["pages"])}')
print(f'활동 태그 수 : {len(activity["tags"])}')
print(f'첫 방문 페이지 : {activity["pages"][0]}')
print(f'login 방문 여부: {"login" in activity["pages"]}')