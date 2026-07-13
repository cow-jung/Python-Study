# 이론
'''
count = 1

while count <= 5:
    print(count)
    count = count + 1 # count 값을 1씩 증가한다.

# 참고
while True: # 무한루프
    print(1)
# 무한루프를 사용할 경우에는 빠져나갈 구멍 먼저 만드는 것을 추천한다.
'''

# 연습문제
# while 사용하여 1~10까지 출력해보세요
'''
num = 1
while num <= 10 :
    print(num)
    num = num + 1
# 1~10까지 누적합계값을 출력해보세요
num = 1
hap = 0
while num <= 10 :
    hap = num + hap
    num = num + 1
    print(hap)
'''
'''
names = ['민수', '지연', '도윤']

for name in names:
    print(name)

scores = [80,95,70,88,55]
count = 0

for s in scores:
    if s >= 80:
        count = count + 1
        print(s)
print(f'80점 이상 갯수 : {count}')

print("============================================================")

student = {
    'name' : '민수',
    'age' : 20,
    'major' : 'Python'
}

# 딕셔너리 값 출력

for key in student:
    print(key, student[key])

print('--------------------')

# items() 사용
for key, value in student.items():
    print(key, value)

print('--------------------')

posts = [
    {'id': 1, 'title': '공지사항', 'writer': '관리자'},
    {'id': 2, 'title': '질문 있습니다', 'writer': '민수'},
    {'id': 3, 'title': '반복문 복습', 'writer': '지연'}
]

for post in posts:
    print(post['id'], post['title'], post['writer'])
'''

# 문제 1
print("문제1 -----------------------------------------------------------------------------")
for i in range(1, 6):
    print(i)

# 문제 2
print("문제2 -----------------------------------------------------------------------------")
names = ['민수', '지연', '도윤', '서연']

for add_name in names:
    print(f'학생 : ', add_name)

# 문제 3
print("문제3 -----------------------------------------------------------------------------")
scores = [90,75,80,100,65]
sum = 0

for score in scores:
    sum += score
    avg = sum / len(scores)

print('합계 : ', sum)
print('평균 : ', avg)

# 문제 4
print("문제4 -----------------------------------------------------------------------------")
scores = [90,75,80,100,65]

for score in scores:
    if score >= 80:
        print(score)

# 문제 5
print("문제5 -----------------------------------------------------------------------------")
posts = [
    {'id': 1, 'title': '공지사항', 'writer': '관리자'},
    {'id': 2, 'title': '질문 있습니다', 'writer': '민수'},
    {'id': 3, 'title': '반복문 복습', 'writer': '지연'}
]

for post in posts:
    print(post['id'], post['title'], post['writer'])
'''
# 문제 6
print("문제6 -----------------------------------------------------------------------------")
posts = [
    {'id': 1, 'title': '공지사항', 'writer': '관리자'},
    {'id': 2, 'title': '질문 있습니다', 'writer': '민수'},
    {'id': 3, 'title': '반복문 복습', 'writer': '지연'}
]

name = input('작성자 이름을 입력하세요 : ')
found = False

for post in posts:
    if name == post['writer']:
        print(post['title'])
        found = True

if found == False:
    print('검색 결과가 없습니다.')
'''
# 문제 7
print("문제7 -----------------------------------------------------------------------------")
num = 5
while num > 0:
    print(num)
    num = num - 1
'''
# 문제 8
print("문제8 -----------------------------------------------------------------------------")
while True:
    print('====================')
    print('1. 인사하기')
    print('2. 오늘 할 일 보기')
    print('0. 종료')
    menu = input('메뉴를 선택해주세요 : ')

    if menu == '1':
        print('안녕하세요.')
        print('====================')
    elif menu == '2':
        print('파이썬 반복문 복습')
        print('====================')
    elif menu == '0':
        print('종료합니다.')
        print('====================')
        break
    else:
        print('잘못된 메뉴입니다.')
        print('====================')
'''
# 도전 1
print("도전 1 -----------------------------------------------------------------------------")
products = [
    {'name' : '마우스', 'price' : 15000, 'stock' : 4},
    {'name': '키보드', 'price': 35000, 'stock': 2},
    {'name': 'USB', 'price': 8000, 'stock': 10}
]
sum_price = 0

for product in products:
    product_price = product['price'] * product['stock']
    print('상품 명: ',product['name'], ' 상품 가격 : ',product['price'],'원', ' 상품 재고 : ', product['stock'], ' 상품의 재고 금액 : ', product_price,'원')
    sum_price += product_price
print('전체 재고 금액 : ', sum_price, '원')
'''
# 도전 2
print("도전 2 -----------------------------------------------------------------------------")
posts = [
    {'id': 1, 'title': '공지사항', 'writer': '관리자'},
    {'id': 2, 'title': '질문 있습니다', 'writer': '민수'},
    {'id': 3, 'title': '반복문 복습', 'writer': '지연'}
]

keyword = input('검색어를 입력하세요 : ')
found = False # 검색어를 찾았는지의 유무를 기억하고있는 변수


for post in posts:
    if keyword in post['title']:
        print(post['id'], post['title'], post['writer'])
        found = True

if found == False:
    print('검색 결과가 없습니다.')

'''
# 도전 3
print("도전 3 -----------------------------------------------------------------------------")
traffic_data = [
    {'station': 'A01', 'speed': 45},
    {'station': 'A02', 'speed': -1},
    {'station': 'A03', 'speed': 70},
    {'station': 'A04', 'speed': -5}
]

for error in traffic_data:
    if error['speed'] < 0:
        print('오류 정류장 : ',error['station'],'속도 : ', error['speed'])

print('오류 개수 : ',len(error['station']))

# 도전 4
print("도전 4 -----------------------------------------------------------------------------")
book_list = [
    {'이름': "해리 포터", '저자': "J.K. 롤링"},
    {'이름': "어린 왕자", '저자': "앙투안 드 생텍쥐페리"},
    {'이름': "데미안", '저자': "헤르만 헤세"},
    {'이름': "1984", '저자': "조지 오웰"},
    {'이름': "아몬드", '저자': "손원평"}
]
while True:
    print('========== 독서 기록 관리 ==========')
    print('1. 책 목록 보기')
    print('2. 책 등록')
    print('3. 책 검색')
    print('4. 책 삭제')
    print('0. 종료')
    print('==================================')

    book_menu = input('메뉴를 선택하세요 >>> ')

    if book_menu == '1':
        print('========== 책 목록 ==========')
        for i, book in enumerate(book_list, start=1):
            print(f'{i}. 책 이름 : {book["이름"]}')
            print(f'   저자 : {book["저자"]}')
            print('-' * 30)

    elif book_menu == '2':
        print('============ 책 등록 ============')
        book_name = input('등록할 책 이름을 입력하세요 >>> ')
        book_writer = input('등록할 책의 저자를 입력하세요 >>> ')
        book_list.append({'이름': book_name, '저자': book_writer})
        print('책 등록이 완료되었습니다.')
        print(f'책 이름 : {book_list[-1]["이름"]}')
        print(f'   저자 : {book_list[-1]["저자"]}')

    elif book_menu == '3':
        print('============ 책 검색 ============')
        book_sel = input('검색할 책 이름을 입력하세요 >>> ')
        found = False
        for book in book_list:
            if book['이름'] == book_sel:
                print(f'책 이름 : {book["이름"]}')
                print(f'   저자 : {book["저자"]}')
                found = True

        if found == False:
            print('잘못 입력하셨습니다. 재입력 부탁드립니다.')

    elif book_menu == '4':
        print('============ 책 삭제 ============')
        found = False
        book_del = input('삭제할 책 이름을 입력하세요 >>> ')
        for book in book_list:
            if book['이름'] == book_del:
                book_list.remove(book)
                print('삭제되었습니다.')
                found = True

        if found == False:
            print('잘못 입력하였습니다. 재입력 부탁드립니다.')

    elif book_menu == '0':
        print('종료합니다.')
        break

    else:
        print('잘못 입력하셨습니다. 다시 입력 부탁드립니다.')
