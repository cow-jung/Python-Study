# 문제 1
from day03_02_set_dict import student

print("문제1 -----------------------------------------------------------------------------")
tags = ['보고서', 'AI', '보고서', '엑셀', '자동화', 'AI']
new_tags = set(tags)

print(f'중복 제거 태그 : {new_tags}')
print(f'태그 수 : {len(new_tags)}')

'''
# 문제 2
print("문제2 -----------------------------------------------------------------------------")
name = input('이름: ')
subject = input('과목: ')
score = int(input('점수: '))

student = {'name': name, 'subject': subject, 'score': score}

student_score = (student['subject'], student['score'])

print(f'이름 : {student["name"]}')
print(f'과목 : {student["subject"]}')
print(f'점수 : {student["score"]}')
print(f'학색 카드 : {student}')
print(f'점수 기록 :{student_score}')
'''
# 문제 3
print("문제3 -----------------------------------------------------------------------------")
product_code = ('IT', 'MOUSE', 30000)
category, name, price = product_code

new_product = {'category': category, 'name': name, 'price': price}

print(f'상품 정보 :  {new_product}')


# 문제 4
print("문제4 -----------------------------------------------------------------------------")
sales = [(120, '1월'), (135, '2월'), (160, '3월'), (155, '4월')]

# 금액과 월을 나누기
amounts, months = zip(*sales)  # 튜플 리스트에서 같은 위치의 값들끼리 묶어서 분리하기 위해

amounts = list(amounts)
months = list(months)
#print(amounts) # [120, 135, 160, 155]
#print(months)  # ['1월', '2월', '3월', '4월']

# 금액 평균 구하기
avg_amount = sum(amounts)/len(amounts)
print(f'평균 : {avg_amount:.2f}')

# 금액 기준 내림차순 정렬
# 튜플 목록에서 x(금액)을 기준으로 내림차순
# 만약 y(월)을 기준으로 내림차순 하고싶다면 key=lambda x: x[1]로 작성
sorted_sales = sorted(sales, key=lambda x: x[0], reverse=True)
# print(f'금액 기준 내림차순 정렬: {sorted_sales}')
# [(160, '3월'), (155, '4월'), (135, '2월'), (120, '1월')]

# 상위 2개 꺼내기 (슬라이싱)
# for item in sorted_sales[:2] : 각 튜플에서 1번재 요소(월)만 인덱싱을 꺼내기 위함
# sorted_sales[:2] : 슬라이싱으로 정렬된 리스트의 앞 2개만 자르기 위함
top2_months = [item[1] for item in sorted_sales[:2]]
print(f'상위 2개월 : {top2_months}')
# [(160, '3월'), (155, '4월')]

# 문제 5
print("문제5 -----------------------------------------------------------------------------")
customer_a = {'AI', '자동화', '엑셀'}
customer_b = {'엑셀', '보고서', '대시보드'}

# 합집합
inter_customer = customer_a | customer_b
# 교집합
union_customer = customer_a & customer_b

print(f'전체 관심사 : {inter_customer}')
print(f'공통 관심사 : {union_customer}')

'''
# 문제 6
print("문제6 -----------------------------------------------------------------------------")
roles = {'기획': '민수', '디자인': '지연', '개발': '도윤'}
role = input('조회할 역할: ')

print(f'조회할 역할 : {role}')
print(f'{role} 담당자: {roles.get(role, "미정")}')
'''

# 문제 7
print("문제7 -----------------------------------------------------------------------------")
item1 = {'menu': '김밥', 'price': 3500, 'count': 2}
item2 = {'menu': '라면', 'price': 4500, 'count': 1}

kimbab = item1["price"] * item1["count"]
raman = item2["price"] * item2["count"]
total = kimbab + raman

print(f'김밥 금액 : {kimbab}원')
print(f'라면 금액 : {raman}원')
print(f'총 주문 금액 : {total}원')

# 문제 8
print("문제8 -----------------------------------------------------------------------------")
raw = '  민수 | 010-1111-2222 | vip  '
print(raw)

# strip() 공백 제거
raw = raw.strip( )

# strip() 문자열로 나눠서 리스트로 변경
new_raw = raw.split('|')

name, phone, grade = new_raw
name = name.strip()
phone = phone.strip()
grade = grade.strip()

person = {'name': name, 'phone': phone, 'grade': grade}

print(f'고객 카드 : {person}')

# 문제 9
print("문제9 -----------------------------------------------------------------------------")
items = [(30000, '마우스'), (250000, '모니터'), (45000, '키보드')]

sorted_items = sorted(items, reverse=True)
print(sorted_items)

price, name = zip(*sorted_items)
name = list(name)

print(f'가격 낮은 순서 : {name}')

'''
# 문제 10
print("문제10 -----------------------------------------------------------------------------")
name = input('회원명: ')
point = int(input('포인트: '))

person = {'name': name, 'point': point}

point_list = []
point_list.append(person['point'])

print(f'회원명 : {person["name"]}')
print(f'포인트 : {person["point"]}')
print(f'회원 정보 : {person}')
print(f'포인트 목록 : {point_list}')
'''

# 문제 11
print("문제11 -----------------------------------------------------------------------------")
responses = ['A', 'B', 'A', 'C', 'A']

cnt_A = responses.count('A')
cnt_B = responses.count('B')
cnt_C = responses.count('C')

responses_dict = {'A' : cnt_A, 'B' : cnt_B, 'C' : cnt_C}
max_cnt = max(set(responses), key=responses.count)

print(f'응답 수 : {responses_dict}')
print(f'최다 선택 : {max_cnt}')

# 문제 12
print("문제12 -----------------------------------------------------------------------------")
response = {'code': 200,
            'message': 'OK',
            'data': {'name': '민수', 'point': 3200}
            }

# 데이터 추출
response_data = response['data']
data_name = response_data['name']
data_point = response_data['point']

# 추출한 데이터로 딕셔너리 만든다
new_response = {'code': response["code"],
                'name': data_name,
                'point': data_point
                }
print(f'사용자 정보 : {new_response}')
print(f'포인트 : {new_response["point"]}')

# 문제 13
print("문제13 -----------------------------------------------------------------------------")
code_text = 'IT-MOUSE-30000'

new_code_text = code_text.split('-')
category, name, price = new_code_text

dict_code = {'category': category, 'name': name, 'price': price}

print(f'상품 코드 : {dict_code}')

# 문제 14
print("문제10 -----------------------------------------------------------------------------")
completed = {'파이썬', '웹', 'DB'} # 이수 완료
required = {'파이썬', 'DB'} # 필수

required_check = required - completed
result = not required_check

print(f'필수 강의 이수 여부 : {result}')

'''
# 문제 15
print("문제15 -----------------------------------------------------------------------------")
customer1 = input('고객명1: ')
amount1 = int(input('금액1: '))
customer2 = input('고객명2: ')
amount2 = int(input('금액2: '))
customer3 = input('고객명3: ')
amount3 = int(input('금액3: '))

customer_total = {'customer1': customer1,
                 'amount1': amount1,
                 'customer2': customer2,
                 'amount2': amount2,
                 'customer3': customer3,
                 'amount3': amount3
                 }
print(customer_total)
'''

# 문제 16
print("문제16 -----------------------------------------------------------------------------")
courses = ['파이썬', '웹', 'DB', 'AI']

courses_dirt = {
    'first' : courses[0],
    'second' : courses[1],
    'other' : courses[2:],
    'count' : len(courses)
}

print(f'수강 요약 : {courses_dirt}')

# 문제 17
print("문제17 -----------------------------------------------------------------------------")
scores = [88, 95, 74]
avg_scores = sum(scores) / len(scores)

print(f'평균 : {avg_scores:.2f}')

# 문제 18
print("문제18 -----------------------------------------------------------------------------")
ordered = {'마우스', '키보드', '모니터'}
stocked = {'키보드'}

req_total = ordered - stocked
req_total = sorted(req_total)

cnt_req_total = len(req_total)

print(f'재주문 후보 : {req_total}')
print(f'후보 수 : {cnt_req_total}')

# 문제 19
print("문제19 -----------------------------------------------------------------------------")
products = [
    {'name': '노트북', 'stock_value': 3600000, 'stock': 3},
    {'name': '마우스', 'stock_value': 450000, 'stock': 15},
    {'name': '키보드', 'stock_value': 180000, 'stock': 4}
]

# 재고 부족 상품 리스트
low_stock = [products[0], products[2]]
low_name = [(item['name']) for item in low_stock]
print(f'재고 부족 : {low_name}')

# 전체 상품 리스트
products_total = [(item['stock_value'], item['name']) for item in products]

# 재고 금액 정렬
sorted_products = sorted(products_total, reverse=True)

# name만 뽑기
products_name = [x[1] for x in sorted_products]

print(f'재고 금액 순서 : {products_name}')


# 문제 20
print("문제20 -----------------------------------------------------------------------------")
memo = 'AI 보고서 자동화 AI 엑셀 보고서'

new_memo = memo.split()

total = set(new_memo)

print(f'키워드 : {total}')

# 문제 21
print("문제21 -----------------------------------------------------------------------------")
reserved = {'A1', 'A2', 'B1'}
seat = 'A3'

print(f'A3 예약 가능 여부 : {seat not in reserved}')

# 문제 22
print("문제22 -----------------------------------------------------------------------------")
minsu = [120000, 90000]
jiyeon = [70000]
doyun = [30000]

# 각 고객별 구매 금액 합계
minsu_price = sum(minsu)
jiyeon_price = sum(jiyeon)
doyun_price = sum(doyun)

person_total = {'민수' : minsu_price, '지연' : jiyeon_price, '도윤': doyun_price}

max_price = max(person_total.values())

print(f'고객별 합계 : {person_total}')
print(f'최고 구매 금액 : {max_price}')

'''
# 문제 23
print("문제23 -----------------------------------------------------------------------------")
coupon = input('쿠폰 코드: ')

# 공백 제거
split_coupon = coupon.strip()

# 대문자 변경
upper_coupon = split_coupon.upper()

total_coupon = {'raw' : coupon, 'clean' : upper_coupon}

print(f'쿠폰 코드 : {coupon}')
print(f'쿠폰 카드 : {total_coupon}')
'''

# 문제 24
print("문제24 -----------------------------------------------------------------------------")
tool = {'name': '보고서 자동화', 'users': ['민수', '지연'], 'tags': {'AI', '문서'}}

print(f'도구명 : {tool["name"]}')
print(f'사용자 수 : {len(tool["users"])}')
print(f'태그 수 : {len(tool["tags"])}')

# 문제 25
print("문제25 -----------------------------------------------------------------------------")
line = '민수,영업,3500000'

# 쉼표 구분으로 데이터 쪼개기
line_data = line.split(',')

person_data = {'name': line_data[0], 'dept': line_data[1], 'salary': line_data[2]}

print(f'직원 정보 : {person_data}')

# 문제 26
print("문제26 -----------------------------------------------------------------------------")
buses = [(3, '740'), (9, '360'), (5, '143')]

# 예상 버스 도착 시간 기준 내림차순 정렬
bus = sorted(buses)
print(bus)

# 버스 번호 추출
buses_num = [x[1] for x in bus]
print(buses_num[:2])

# 문제 27
print("문제27 -----------------------------------------------------------------------------")
user_tags = {'AI', '자동화', '보고서'}
content_tags = {'AI', '엑셀', '보고서'}

# 사용자 관심 태그와 콘텐츠 태그 겹치는 정보 확인
common_tags = user_tags & content_tags
sorted_common_tags = sorted(common_tags)

print(f'겹치는 태그 : {sorted_common_tags}')
print(f'추천 점수 : {len(common_tags)}')

# 문제 28
print("문제28 -----------------------------------------------------------------------------")
cart = {'total': 80000, 'coupon': 'WELCOME'}
coupons = {'WELCOME': 5000, 'VIP': 10000}

# coupons 딕셔너리에 cart 쿠폰이 있는 지 확인하여 금액 추출
use_coupon = coupons.get(cart['coupon'])

total_price = cart['total'] - use_coupon

print(f'최종 결제 금액 :  {total_price}원')

# 문제 29
print("문제29 -----------------------------------------------------------------------------")
order1 = {'customer': '민수', 'amount': 30000}
order2 = {'customer': '지연', 'amount': 45000}
order3 = {'customer': '민수', 'amount': 15000}




# 문제 30
print("문제30 -----------------------------------------------------------------------------")
sales = [
    (3600000, '노트북'),
    (1200000, '마우스'),
    (900000, '키보드'),
    (2000000, '모니터')
]

sorted_sales = sorted(sales, reverse=True)

print(f'1위 : {sorted_sales[0][1]} {sorted_sales[0][0]}원')
print(f'2위 : {sorted_sales[1][1]} {sorted_sales[1][0]}원')
print(f'3위 : {sorted_sales[2][1]} {sorted_sales[2][0]}원')

# 문제 31
print("문제31 -----------------------------------------------------------------------------")
post1 = {'tags': {'AI', '업무', '자동화'}}
post2 = {'tags': {'AI', '보고서'}}
post3 = {'tags': {'AI', '엑셀'}}

# 전체 태그
total_tags = set(post1['tags']) | set(post2['tags']) | set(post3['tags'])

# 공통된 태그
common_tags = set(post1['tags']) & set(post2['tags']) & set(post3['tags'])

print(f'전체 태그 : {total_tags}')
print(f'공통 태그 : {common_tags}')

# 문제 32
print("문제32 -----------------------------------------------------------------------------")
task1 = {'title': '보고서', 'status': '진행'}
task2 = {'title': '발표자료', 'status': '완료'}
task3 = {'title': '견적서', 'status': '보류'}

total_title = [task1['title'], task2['title'], task3['title']]

total_status = task1['status'], task2['status'], task3['status']
total_status = set(total_status)

print(f'업무 목록 : {total_title}')
print(f'상태 종류 : {total_status}')
print(f'업무 수 : {len(total_title)}')
print(f'상태 종류 수 : {len(total_status)}')

# 문제 33
print("문제33 -----------------------------------------------------------------------------")
tasks = ['보고서', '정산', '고객 응대']
sales = [120000, 80000, 50000]
tags = {'AI', '보고서', '자동화'}

cnt_tasks = len(tasks)
sum_sales = sum(sales)
cnt_tags = len(tags)

total_data = {'task_count':cnt_tasks, 'sales_total':sum_sales, 'tag_count':cnt_tags}

print(f'대시보드 : {total_data}')

# 문제 34
print("문제34 -----------------------------------------------------------------------------")
email1 = 'a@naver.com'
email2 = 'b@gmail.com'
email3 = 'c@naver.com'

# 이메일에 도메일만 추출
total_email = [email1, email2, email3]
domain = [email.split('@')[1] for email in total_email]

# 겹치는 도메인 확인
domain_count = {}
for email in domain:
    domain_count[email] = domain_count.get(email, 0) + 1

print(f'도메인 집계 : {domain_count}')

# 문제 35
print("문제35 -----------------------------------------------------------------------------")
words = 'AI 보고서 AI 자동화 엑셀 AI'.split()

# 단어 카운트
words_count = {}
for word in words:
    words_count[word] = words_count.get(word, 0) + 1

# 최다 키워드
max_word = max(words_count, key=words_count.get)

print(f'키워드 빈도 : {words_count}')
print(f'최다 키워드 : {max_word}')

# 문제 36
print("문제36 -----------------------------------------------------------------------------")
meeting = {'title': '기획 회의', 'members': ['민수', '지연'], 'topics': ['일정', '예산', '역할']}

meeting_summary = {
    'title': meeting['title'],
    'member_count': len(meeting['members']),
    'first_topic': meeting['topics'][0],
    'last_topic': meeting['topics'][-1],
}

print(f'회의 요약 : {meeting_summary}')

# 문제 37
print("문제37 -----------------------------------------------------------------------------")
responses = ['민수', '지연', '민수', '도윤', '지연']

set_responses = set(responses)
sorted_responses = sorted(set_responses, reverse=True)
len_responses = len(sorted_responses)

print(f'실제 응답자 : {sorted_responses}')
print(f'응답자 수 : {len_responses}')

# 문제 38
print("문제38 -----------------------------------------------------------------------------")
sale1 = {'channel': '온라인', 'amount': 120000}
sale2 = {'channel': '온라인', 'amount': 80000}
sale3 = {'channel': '오프라인', 'amount': 150000}

total_sales = [sale1, sale2, sale3]

channel_count = {}
for item in total_sales:
    channel = item['channel']
    amount = item['amount']
    channel_count[channel] = channel_count.get(channel, 0) + amount

print(f'채널별 매출 : {channel_count}')

# 문제 39
print("문제39 -----------------------------------------------------------------------------")
counts = [(3, 'AI'), (1, '보고서'), (1, '자동화'), (1, '엑셀')]

sorted_counts = sorted(counts, reverse=True)

top2_counts = [top2[1] for top2 in sorted_counts]

print(f'상위 키워드 : {top2_counts[:2]}')

# 문제 40
print("문제40 -----------------------------------------------------------------------------")
courses = ['파이썬', '웹', 'DB', 'AI']
completed = {'파이썬', '웹'}

# 미완료 확인하기
diff_courses = set(courses) - set(completed)

# 완료율 구하기
completion_rate = len(diff_courses)/len(courses) * 100


print(f'완료율 : {completion_rate:.2f}%')
print(f'미완료 : {diff_courses}')