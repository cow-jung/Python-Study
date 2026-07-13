# 이론
'''
변수는 무조건 하나의 값 | data = 10

파이썬 자료구조를 위한 컬렉션
1. 리스트 [대괄호] | data = [1,2,3,4,5]  data[0] = 1 <- 인덱스
    * 순서대로 저장하는 자료구조
    * 추가, 삭제, 수정 가능
    * 중복 허용
    data = [1,2,3,4,5]
    data[0 : 2] = 1,2
    data[2 : ] = 3,4,5
    data[:] = [1,2,3,4,5]

2. 튜플 (소괄호)
    * 수정할 수 없음 | 리스트처럼 insert, remove 등을 사용 못함
    * 튜플을 단일로 값을 넣고싶다면 data=(4,) 으로 해야한다. data=(4)X
    * 수정이 되지 않으니 고정된 값에 적합(좌표, 크기, 색상값 등)
3. 셋 {중괄호}
4. 딕셔너리 {중괄호}
'''

'''
# 리스트
# 변수 인덱스
name = '홍길동'
print(name[0])
>> 홍

# 리스트 혼합 가능
data=[1,2,3,'가','나','다']
print(data)
data.remove(3)
print(data)
data.remove('다')
print(data)

# 리스트 병합
  * 리스트는 연산의 목적이 아니므로 +를 사용하면 리스트의 병합이 일어난다
morning = ["국어", "영어"]
afternoon = ["수학", "과학"]

today = morning + afternoon
print(today) 
>> ['국어', '영어', '수학', '과학]

# 일부 함수
scores = [80, 90, 75, 95]

print(sum(scores)) >> 340
print(max(scores)) >> 90
print(min(scores)) >> 75

# 다중리스트 : 리스트 안에 리스트
data = [["홍길동", 20, "수원시"], ["홍길동", 20, "수원시"], ["홍길동", 20, "수원시"]]
print(data[0][0]) >> 홍길동
'''

'''
# 튜플
# 튜플 언패킹 : 튜플 안에 있는 값을 여러 변수에 나눠 넣어준다.
size = (1920, 1080)
width, height = size
print(width) >> 1920
print(height) >> 1080
'''

'''
# 문제 1
students = ['민수', '지연', '도윤', '서연', '하준']
print(f"학생 목록 : {students}")
'''

'''
# 문제 2
fruits = ["사과", "바나나", "포도", "딸기", "수박"]
print(f"첫 번째 과일 : {fruits[0]}")
print(f"마지막 과일 : {fruits[4]}") #  {fruits[-1]}
'''

'''
# 문제 3
stations = ["강남역", "양재역", "교대역", "서초역", "방배역"]
print(f"마지막 정류장 : {stations[-1]}") # stations[4]
print(f"뒤에서 세 번째 정류장 : {stations[-3]}") # stations[2]
'''

'''
# 문제 4 
scores = [75, 82, 88, 91]
scores[1] = 90
print(f"수정된 점수 : {scores}")
'''

'''
# 문제 5 (리스트 마지막에 요소 추가 append)
menu = ["김밥", "라면", "우동"]
menu.append("돈까스")
# menu_cnt = len(menu)
print(f"전체 메뉴 : {menu}")
# print(f"메뉴 개수 : {menu_cnt}")
print(f"메뉴 개수 : {len(menu)}")
'''

'''
# 문제 6 (리스트 원하는 위치에 요소 추가 insert)
# insert는 (인덱스, 추가 요소) 인덱스 앞에 추가됨
seats = [1, 2, 4, 5]
seats.insert(2,3)
# seats.insert(1,3) # seats[1],3
print(f"좌석 목록 : {seats}")
'''

'''
# 문제 7 (리스트 삭제 remove)
reservations = ["민수", "지연", "도윤", "서연"]
reservations.remove("지연")
# reservations.remove(reservations[1])
print(f"남은 예약자 : {reservations}")

# remove 중복 요소
tasks = ["자료 조사", "코드 작성", "발표 준비", "코드 작성"]
tasks.remove("코드 작성")
print(tasks)
>> ['자료 조사', '발표 준비', '코드 작성'] 
    * 첫 번째로 찾은 값 하나만 삭제
'''

'''
# 문제 8 (리스트 마지막 값 꺼내기 pop)
tasks = ["자료 조사", "코드 작성", "발표 준비"]
tasks_pop = tasks.pop() # 마지막 값을 변수에 저장

print(f"완료 처리한 작업 : {tasks_pop}") # 마지막 값 확인
print(f"남은 작업 : {tasks}") # 마지막 값 꺼낸 후 결과
'''

'''
# 문제 9
route = ["덕은동", "연세대", "서울역", "시청", "강남역", "양재역"]
print(f"앞 구간: {route[:3]}")
'''

'''
# 문제 10
route = ["덕은동", "연세대", "서울역", "시청", "강남역", "양재역"]
back = route[3:]
print(f"뒷 구간 : {back}")
print(f"뒷 구간 : {route[3:]}")
'''

'''
# 문제 11
route = ["덕은동", "연세대", "서울역", "시청", "강남역", "양재역"]
middle = route[1:5]
print(f"중간 구간 : {middle}")
print(f"중간 구간 : {route[1:-1]}")
print(f"중간 구간 : {route[1:5]}")
'''

'''
# 문제 12
classes = ["국어", "영어", "수학", "과학", "파이썬", "프로젝트"]
morning = classes[:3]
afternoon = classes[3:]
print(f"오전 수업 : {morning}")
print(f"오후 수업 : {afternoon}")
print(f"오전 수업 : {classes[:3:1]}")
print(f"오후 수업 : {classes[3::1]}")
'''

'''
# 문제 13
orders = ["A001", "A002", "B001", "B002", "C001", "C002"]
received = orders[:2]
packed = orders[2:4]
shipping = orders[4:]
print(f"접수 단계 : {received}")
print(f"포장 단계 : {packed}")
print(f"배송 단계 : {shipping}")

print(f"접수 단계 : {orders[0:2]}")
print(f"포장 단계 : {orders[2:4]}")
print(f"배송 단계 : {orders[4:]}")
'''

'''
# 문제 14
scores = [98, 95, 91, 88, 82, 76]
top3 = scores[:3]
others = scores[3:]
print(f"상위 3명: {top3}")
print(f"나머지: {others}")

print(f"상위 3명 : {scores[:3]}")
print(f"나머지 : {scores[3:]}")
'''

'''
# 문제 15
group1 = ["민수", "지연"]
group2 = ["도윤", "서연"]
group3 = ["하준", "유나"]

all_students = group1 + group2 + group3
print(f"전체 출석부: {all_students}")
print(f"전체 학생 수: {len(all_students)}")

print(f"전체 출석부 : {group1+group2+group3}")
print(f"전체 학생 수 : {len(group1+group2+group3)}")
'''

'''
# 문제 16
online_cart = ["마우스", "키보드"]
offline_cart = ["노트", "펜", "파일"]

all_cart = online_cart + offline_cart

print(f"전체 구매 목록 : {all_cart}")

print(f"전체 구매 목록 : {online_cart+offline_cart}")
'''

'''
# 문제 17
scores = [86, 92, 78, 95, 88]
total = sum(scores)
average = total / len(scores)
print(f"총점 : {total}")
print(f"평균 : {average:.2f}")
'''

'''
# 문제 18
temperatures = [23.5, 24.1, 22.8, 25.0, 24.6]

print(f"최고 온도 : {max(temperatures)}")
print(f"최저 온도 : {min(temperatures)}")
'''

'''
# 문제 19
sales = [120, 135, 150, 160, 155, 170, 180, 175, 190, 200, 210, 230]
sales1 = sales[:3]
sales2 = sales[3:6]
sales3 = sales[6:9]
sales4 = sales[9:]
print(f"1분기 매출: {sales1}, 합계 : {sum(sales1)}")
print(f"2분기 매출: {sales2}, 합계 : {sum(sales2)}")
print(f"3분기 매출: {sales3}, 합계 : {sum(sales3)}")
print(f"4분기 매출: {sales4}, 합계 : {sum(sales4)}")
'''

'''
# 문제 20
route = ["A역", "B역", "C역", "D역", "E역", "F역"]
front = route[:3]
back = route[3:]
new_route = front + back
print(f"앞 구간 : {front}")
print(f"뒤 구간 : {back}")
print(f"재조립 노선 : {new_route}")
print(f"재조립 노선 : {front+back}")
'''

'''
# 문제 21
school = (37.5012, 127.0396)
print(f"위도 : {school[0]}")
print(f"경도 : {school[1]}")
'''

'''
# 문제 22
color = (255, 180, 90)
R, G, B = color
print(f"R: {R}")
print(f"G: {G}")
print(f"B: {B}")
print(f"R: {color[0]}")
print(f"G: {color[1]}")
print(f"B: {color[2]}")
'''

'''
# 문제 23
screen = (1920, 1080)
width, height = screen
total = width * height
print(f"가로 : {width}")
print(f"세로 : {height}")
print(f"전체 픽셀 수: {total}")
'''

'''
# 문제 24
course = ("파이썬 기초", 3, "김교수")
print(f"과목명 : {course[0]}")
print(f"학점 : {course[1]}")
print(f"담당 교수 : {course[2]}")
'''

'''
# 문제 25
students = ["민수", "지연", "도윤"]
classroom = (3, 205)
print(f"학생 수 : {len(students)}")
print(f"교실 위치 : {classroom[0]}층 {classroom[1]}호")
'''

'''
# 문제 26
home = (37.1, 127.1)
school = (37.5, 127.0)
library = (37.3, 127.2)

total = (home, school, library)

print(f"좌표 목록 : {total}")
print(f"첫 번째 장소 위도 : {total[0][0]}")
'''

'''
# 도전 문제
names = ["민수", "지연", "도윤", "서연"]
scores = [88, 92, 79, 95]
total = sum(scores)/len(scores)
print(sum(scores))

print(f"첫 학생 : {names[0]}, {scores[0]}점")
print(f"마지막 학생 : {names[-1]}, {scores[-1]}점")
print(f"전체 평균 : {total:.2f}")
'''

'''
# 문제 28
seoul = ["경복궁", "남산"]
busan = ["해운대", "광안리"]
jeju = ["성산일출봉", "한라산"]

plans = seoul + busan + jeju

print(f"전체 일정 : {plans}")
print(f"첫 2일 일정 : {plans[:2]}")
print(f"남은 일정 : {plans[2:]}")
'''

'''
# 문제 29
products = ["노트북", "마우스", "오타상품", "키보드", "모니터"]
products.append("헤드셋")
#products.insert(5,"헤드셋")
products.remove("오타상품")
print(f"정리된 상품 : {products}")
print(f"대표 상품 : {products[:3]}")
'''

'''
# 문제 30
front_route = ["덕은동", "연세대", "서울역"]
back_route = ["시청", "강남역", "양재역"]
total_route = front_route + back_route

print(f"전체 노선 : {total_route}")
print(f"출발 정류장 : {total_route[0]}")
print(f"종점 정류장 : {total_route[-1]}")
print(f"중간 구간 : {total_route[1:-1]}")
'''

'''
# 문제 31
morning_class = ["민수", "지연", "도윤"]
afternoon_class = ["서연", "하준", "유나"]
total_class = morning_class + afternoon_class

print(f"전체 명단 : {total_class}")
print(f"첫 번째 학생 : {total_class[0]}")
print(f"마지막 학생 : {total_class[-1]}")
print(f"전체 학생 수 : {len(total_class)}")
'''

'''
# 문제 32
scores = [99, 95, 91, 88, 84, 77, 70]
first_score = scores[:2]
second_score = scores[2:5]
third_score = scores[5:]
print(f"상위권 : {first_score}")
print(f"중위권 : {second_score}")
print(f"하위권 : {third_score}")
print("-"*30)
print(f"상위권 : {scores[:2]}")
print(f"중위권 : {scores[2:5]}")
print(f"하위권 : {scores[5:]}")
'''

'''
# 문제 33
books = ["파이썬 입문", "웹 기초", "오등록", "DB 기초"]
books.remove("오등록")
books.append("자료구조")
#books.insert(5,6)
print(f"정리된 도서 : {books}")
print(f"도서 수 : {len(books)}")
'''

'''
# 문제 34
reserved_seats = [1, 2, 3, 4, 5]
reserved_seats.remove(3)
reserved_seats.append(6)
#reserved_seats.insert(5,6)
print(f"최종 예약 좌석 : {reserved_seats}")
'''

'''
# 문제 35
sales = [120000, 135000, 128000, 150000, 170000, 210000, 190000]
day_sales = sales[:5]
end_sales = sales[5:]

print(f"주중 매출: {day_sales}")
print(f"주중 합계 : {sum(day_sales)}원")
print(f"주말 매출 : {end_sales}")
print(f"주말 합계 : {sum(end_sales)}원")
print("-"*30)
print(f"주중 매출: {sales[:5]}")
print(f"주중 합계 : {sum(sales[:5])}원")
print(f"주말 매출 : {sales[5:]}")
print(f"주말 합계 : {sum(sales[5:])}원")
'''

'''
# 문제 36
start = (3, 5)
end = (10, 12)
start_x, start_y = start
end_x, end_y = end

print(f"출발 좌표 : x = {start_x}, y = {start_y}")
print(f"도착 좌표 : x = {end_x}, y = {end_y}")
print(f"x 차이 : {end_x - start_x}")
print(f"y 차이 : {end_y - start_y}")
'''

'''
# 문제 37
drinks = ["아메리카노", "라떼"]
desserts = ["케이크", "쿠키", "마카롱"]
menu = drinks + desserts

print(f"전체 주문 : {menu}")
print(f"음료 구간 : {drinks}")
print(f"디저트 구간 : {desserts}")
'''

'''
# 문제 38
tasks = ["기획", "자료조사", "화면구현", "기능구현", "테스트", "발표"]

ready = tasks[:2]
start = tasks[2:4]
end = tasks[4:]

print(f"준비 단계: {ready}")
print(f"개발 단계: {start}")
print(f"마무리 단계: {end}")
print("-"*30)
print(f"준비 단계: {tasks[:2]}")
print(f"개발 단계: {tasks[2:4]}")
print(f"마무리 단계: {tasks[4:]}")
'''

'''
# 문제 39
products = ["마우스", "키보드", "모니터", "스피커"]
prices = [30000, 45000, 250000, 60000]
avg_price = sum(prices)/len(prices)

print(f"첫 상품 : {products[0]}, {prices[0]}원")
print(f"마지막 상품 : {products[-1]}, {prices[-1]}원")
print(f"마지막 상품 : {products[3]}, {prices[3]}원")
print(f"평균 가격 : {avg_price:.2f}원")
'''

'''
# 문제 40
mobile = (390, 844)
tablet = (820, 1180)
desktop = (1920, 1080)
total = [mobile, tablet, desktop]
mobile_width, mobile_height = mobile
tablet_width, tablet_height = tablet
desktop_width, desktop_height = desktop

print(f"화면 크기 목록 : {total}")
print(f"첫 번째 화면 가로 : {total[0][0]}")
print(f"두 번째 화면 세로 : {total[1][0]}")
print(f"첫 번째 화면 가로 : {mobile_width}")
print(f"두 번째 화면 세로 : {tablet_height}")
print(f"전체 화면 개수 : {len(total)}")
'''

'''
# 문제 41
class1_scores = [88, 92, 79]
class2_scores = [95, 84, 90]
total_scores = class1_scores + class2_scores
max_score = max(total_scores)
min_score = min(total_scores)
avg_score = sum(total_scores)/len(total_scores)

print(f"전체 점수 : {total_scores}")
print(f"전체 인원 : {len(total_scores)}")
print(f"최고점 : {max_score}")
print(f"최저점 : {min_score}")
print(f"평균 : {avg_score:.2f}")
print(f"앞의 3명 점수 : {total_scores[:3]}")
print(f"나머지 점수 : {total_scores[3:]}")
'''
