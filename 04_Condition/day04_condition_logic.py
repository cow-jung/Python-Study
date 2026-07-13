# 이론
# IF(조건문)
# 결과값이 True, False로 나오게 해서 다양한 방향의 코드를 만들 수 있게 하는 기능

# 1. if
# 2. if ~ else
# 3. if ~ elif ~ else

# 예시 1
# 사용자로부터 나이를 입력받아 나이가 20세 이상이면
# 성인이라고 출력하시오.
'''

age = int(input('나이를 입력하세요 : '))

if age >= 20:
    print('성인 입니다.')
'''
from day03_03_collection_total import required, reserved, category

# 예시 2
# 사용자로부터 나이를 입력받아 나이가 20세 이상이면 성인이
# 20세 미만이면 미성년자 라고 출력하시오.
'''
age = int(input('나이를 입력하세요 : '))

if age >= 20:
    print('성인 입니다.')

else :
    print('미성년자 입니다.')
'''

# 예시 2
# 사용자로부터 나이를 입력받아 나이가 20세 이상이면 성인이
# 20세 미만이면 미성년자 라고 출력하시오.
'''
age = int(input('나이를 입력하세요 : '))

if age >= 20:
    print('성인 입니다.')

elif age >= 9:
    print('청소년 입니다.')

else:
    print('유아 입니다.')
'''

# 실습
# 사용자로부터 점수를 입력받아 90 이상이면 '수', 80 이상이면 '우'
# 70 이상이면 '미', 60 이상이면 '양' 그외는 '가'
'''
score = int(input('점수를 입력하세요 : '))
if score >= 90:
    print('수')

elif score >= 80:
    print('우')

elif score >= 70:
    print('미')

elif score >= 60:
    print('양')

else:
    print('가')
'''

# 예제 1
print("예제1 -----------------------------------------------------------------------------")
age = 22
if age >= 20:
    print('성인입니다.')

# 예제 2
print("예제2 -----------------------------------------------------------------------------")

score = 58

if score >= 60:
    print('합격')
else:
    print('불합격')

# 예제 3
print("예제3 -----------------------------------------------------------------------------")

stock = 4
if stock >= 5:
    print('발주 필요')
else:
    print('재고 충분')

# 예제 4
print("예제4 -----------------------------------------------------------------------------")

user_id = 'student01'
user_pw = 'python1234'

if user_id != '' and len(user_pw) >= 8:
    print('로그인 정보 형식 통과')
else:
    print('로그인 정보 형식 오류')

# 예제 5
print("예제 5 -----------------------------------------------------------------------------")

is_member = False
has_coupon = True

if is_member or has_coupon:
    print('할인 가능')
else:
    print('할인 불가')

# 예제 6
print("예제 6 -----------------------------------------------------------------------------")

score = 87

if score >= 90:
    print('A등급')
elif score >= 80:
    print('B등급')
elif score >= 70:
    print('C등급')
else :
    print('재시험')

# 예제 7
print("예제 7 -----------------------------------------------------------------------------")

tasks = ['보고서 작성', '고객 문의 정리', '회의 준비']

if len(tasks) >= 3:
    print('오늘은 업무가 많은 날입니다.')
else:
    print('오늘은 업무가 적은 편입니다.')

# 예제 8
print("예제 8 -----------------------------------------------------------------------------")

completed_courses = {'파이썬', '웹', 'DB'}
required_courses = '파이썬'

if required_courses in completed_courses:
    print('필수 강의 이수 완료')
else:
    print('필수 강의 미이수')

# 예제 9
print("예제 9 -----------------------------------------------------------------------------")

product = {'name': '키보드', 'stock': 4}

if product['stock'] <= 5 :
    print(f'{product['name']} 재고가 부족합니다.')
else:
    print(f'{product['name']} 재고가 충분합니다.')

# 예제 10
'''
print("예제 10 -----------------------------------------------------------------------------")

score = int(input('점수 : '))

if score >= 90:
    print('매우 우수')
elif score >= 80:
    print('우수')
elif score >= 60:
    print('통과')
else:
    print('재시험')
'''

# 별도연습문제
# 사용자로부터 id와 비밀번호를 받아서 로그인 처리를 할 것이다.
# 사용자로부터 id를 받을 때 값이 비어있거나 4글자 이하이면 '아이디 오류'라고 출력한다
# 비밀번호가 8글자 미만이거나 비밀번호가 안맞으면 '비밀번호 오류' 라고 출력한다
# id가 admin, 비밀번호가 python1234 인 경우에만 '로그인되었습니다.'라고 출력한다
'''
print('=========== 로그인 기능 ===========')
save_id = 'admin'
save_pw = 'python1234'

user_id = input('아이디를 입력하세요 : ')
user_pw = input('비밀번호를 입력하세요 : ')

if user_id == '' or len(user_id) <= 4:
    print('아이디 오류')

elif user_id != save_id:
    print('아이디가 틀렸습니다.')

elif user_pw == '' or len(user_pw) < 8  :
    print('비밀번호 오류')

elif user_pw != save_pw:
    print('비밀번호가 틀렸습니다.')

else:
    print('로그인되었습니다.')
'''

# 문제 1
'''
print("문제1 -----------------------------------------------------------------------------")
age = int(input('나이를 입력하세요 : '))
if age >= 19 :
    print('출입 가능')
else:
    print('출입 불가')
'''

# 문제 2
'''
print("문제2 -----------------------------------------------------------------------------")
price = int(input('주문 금액 : '))

if price >= 50000 :
    print('배송비 : 무료')
else:
    print('배송비 : 3000원')
'''

# 문제 3
'''
print("문제3 -----------------------------------------------------------------------------")
password = input('비밀번호 : ')

if len(password) >= 8 :
    print('사용 가능한 비밀번호입니다.')
else:
    print('비밀번호가 너무 짧습니다.')
'''

# 문제 4
'''
print("문제4 -----------------------------------------------------------------------------")
save_id = 'python'
save_pw = '1234'

id = input('id : ')
pw = input('pw : ')

if id == save_id and pw == save_pw :
    print('로그인 성공')
else:
    print('로그인 실패')
'''

# 문제 5
'''
print("문제5 -----------------------------------------------------------------------------")
price = int(input('구매 금액 : '))

if price >= 200000 :
    print('VIP')
elif price >= 100000 :
    print('GOLD')
else:
    print('BASIC')
'''
# 문제 6
'''
print("문제6 -----------------------------------------------------------------------------")
reserved = {'A1', 'A2', 'B1'}
seat = input('예약할 좌석 :')

if seat not in reserved :
    print('예약 가능')
else:
    print('이미 예약된 좌석입니다.')
'''

# 문제 7
'''
print("문제7 -----------------------------------------------------------------------------")
completed = {'파이썬', '웹', 'DB'}
course = input('확인할 강의 명 : ')

if course in completed :
    print('이수 완료')
else:
    print('미이수')
'''

# 문제 8
'''
print("문제8 -----------------------------------------------------------------------------")
important = input('중요한 업무인가요? (예/아니요) : ')
urgent = input('긴급한 업무인가요? (예/아니요) : ')

if important == '예' and urgent == '예' :
    print('즉시 처리')
elif important == '예' and urgent == '아니요' :
    print('일정 등록')
elif important == '아니요' and urgent == '예':
    print('빠른 확인')
else:
    print('나중에 처리')
'''

# 문제 9
'''
print("문제9 -----------------------------------------------------------------------------")
menu = input('메뉴 선택(1.목록 2.작성 3.종료): ')

if menu == '1' :
    print('글 목록 보기')
elif menu == '2' :
    print('글 작성하기')
elif menu == '3' :
    print('프로그램 종료')
else:
    print('잘못된 메뉴입니다.')
'''

# 문제 10
'''
print("문제10 -----------------------------------------------------------------------------")
title = input('제목 : ')
content = input('내용 : ')

if title == '':
    print('제목은 필수입니다.')
else:
    print('게시글이 등록되었습니다.')
    post = {'title': title, 'content': content}
    post['content'] = content
    print(post)
'''

# 문제 11
'''
print("문제11 -----------------------------------------------------------------------------")
title = input('제목 : ')
secret = input('비밀글인가요? (예/아니요) : ')

post = {'title': title, 'content': secret}

if secret == '예':
    print('비밀글로 등록됩니다.')
    print(post)
else:
    print('일반글로 등록됩니다.')
    print(post)
'''

# 문제 12
'''
print("문제12 -----------------------------------------------------------------------------")
post_user = '민수'
user_name = input('사용자 이름 : ')

if user_name == post_user:
    print('수정 가능')
else:
    print('수정 권한이 없습니다.')
'''

# 문제 13
'''
print("문제13 -----------------------------------------------------------------------------")
post_user = {'name' : '민수'}
user_name = input('사용자 이름 : ')
user_role = input('사용자 권한 : ')

if user_name == post_user['name'] or user_role == 'admin' :
    print('삭제 가능')
else:
    print('삭제 권한이 없습니다.')
'''

# 문제 14
'''
print("문제14 -----------------------------------------------------------------------------")
post_state = input('게시글 상태 (공개/비공개/삭제) : ')
login = input('로그인 했나요? (예/아니요) : ')

if post_state == '공개' and login == '예' :
    print('댓글 작성 가능')
else :
    print('댓글 작성 불가')
'''

# 문제 15
'''
print("문제15 -----------------------------------------------------------------------------")
grade = input('고객 등급 (VIP/일반) : ')
category = input('상담 유형 (결제/오류/기타) : ')

if grade == 'VIP' and (category == '결제' or category == '오류'):
    print('최우선 상담')
elif grade == 'VIP' :
    print('우선 상담')
else:
    print('일반 상담')
'''

# 문제 16
'''
print("문제16 -----------------------------------------------------------------------------")
name = input('상품명 : ')
stock = int(input('재고 수량 : '))
selling = input('판매 여부 (예/아니요) : ')

if selling == '아니요':
    print('판매 중지 상품')
elif selling == '예' and  stock == 0 :
    print('품절')
elif selling == '예' and stock <= 5 :
    print(f'{name}: 재고 부족')
else:
    print(f'{name}: 판매 가능')
'''

# 문제 17
'''
print("문제17 -----------------------------------------------------------------------------")
person_num = int(input('현재 신청 인원 : '))
total_person_num = int(input('정원 : '))
paid = input('결제했나요? (예/아니요) : ')

if paid == '예' and person_num < total_person_num :
    print('수강 신청 완료')
elif paid == '예' and person_num >= total_person_num :
    print('정원 마감')
else:
    print('결제가 필요합니다.')
'''

# 문제 18
'''
print("문제18 -----------------------------------------------------------------------------")
start_time = int(input('출근 시간 : '))
end_time = int(input('퇴근 시간 : '))

if start_time > 9 and end_time < 18:
    print('지각 및 조퇴')
elif  start_time > 9:
    print('지각')
elif end_time < 18:
    print('조퇴')
else:
    print('정상 근무')
'''

# 문제 19
'''
print("문제19 -----------------------------------------------------------------------------")
payment = input('결제 수단 (카드/계좌이체/포인트) : ')
pay_price = int(input('결제 금액 : '))

if payment == '카드' and pay_price >= 100000:
    print('카드 무이자 할부 가능')
elif payment == '계좌이체':
    print('입금 확인 후 처리됩니다.')
elif payment == '포인트':
    print('포인트가 차감됩니다.')
else:
    print('일반 결제 처리')
'''

# 문제 20
'''
print("문제20 -----------------------------------------------------------------------------")
item1 = input('상품명 1 : ')
item2 = input('상품명 2 : ')
item3 = input('상품명 3 : ')

if item1 == '':
    print('장바구니가 비어 있습니다.')
else:
    print('장바구니 확인 필요')
    total_item = [item1, item2, item3]
    print(total_item)
'''

# 문제 21
'''
print("문제21 -----------------------------------------------------------------------------")
content_tags = {'엑셀', '자동화', '보고서'}
tag = input('관심 태그: ')

if tag in content_tags:
    print('추천 콘텐츠와 관련 있음')
else:
    print('추천 콘텐츠와 관련 없음')
'''

# 문제 22
'''
print("문제22 -----------------------------------------------------------------------------")
name = input('이름 : ')
point = int(input('포인트 : '))
member = {'name' : name, 'point' : point}

if point >= 10000 :
    grade = 'VIP'

elif point >= 5000 :
    grade = 'GOLD'
else:
    grade = 'BASIC'

print(f'{member["name"]} 등급 : {grade}')
'''

# 문제 23
'''
print("문제23 -----------------------------------------------------------------------------")
question_type = input('문의 유형 (결제/환불/배송/기타): ')

if question_type == '결제' or question_type == '환불':
    print('재무팀')
elif question_type == '배송':
    print('물류팀')
elif question_type == '기타':
    print('고객지원팀')
else:
    print('확인이 필요한 문의입니다.')
'''

# 문제 24
'''
print("문제24 -----------------------------------------------------------------------------")
keyword = input('검색어: ')
search_type = input('검색 범위(제목/내용/작성자): ')
valid_types = {'제목', '내용', '작성자'}

if keyword == '':
    print('검색어를 입력해야 합니다.')
elif search_type in valid_types:
    print('검색을 시작합니다.')
else:
    print('검색 범위가 올바르지 않습니다.')
'''
# 도전 1
'''
print("도전 1 -----------------------------------------------------------------------------")
title = input('제목 : ')
content = input('내용 : ')
category = input('카테고리 (공지/질문/자유) : ')
secret = input('비밀글인가요? (예/아니요) : ')

total = {
    'title' : title,
    'content' : content,
    'category' : category,
    'secret' : secret
}

if  title == '': # 제목이 비어 있다면
    print('등록 실패 : 제목은 필수입니다.')
elif len(content) <= 10 : # 내용이 10자 미만이라면
    print('등록 실패 : 내용은 10자 이상 이어야 합니다.')
elif category not in {'공지', '질문', '자유'} : # 카테고리가 허용 카테고리에 없다면
    print('등록 실패 : 존재하지 않는 카테고리입니다.')
elif category == '공지' and secret == '예': # 카테고리가 공지이고 비밀글 여부가 예 이면
    print('등록 실패: 공지는 비밀글로 등록할 수 없습니다.')
else:
    print('등록 성공')
    print(total)
'''

# 도전 2
'''
print("도전 2 -----------------------------------------------------------------------------")
writer = '민수' # 게시글 작성자
content_state = input('게시글 상태 (공개/비밀/삭제) : ')
user_name = input('사용자 이름 : ')
user_state = input('권한 (admin/user) : ')

if content_state == '삭제': # 게시글 상태가 삭제이면
    print('열람 불가 : 삭제된 글입니다.')
    
elif user_state == 'admin' and content_state != '삭제': # 권한이 admin이면 삭제 제외하고 확인 가능
    print('관리자 열람 가능')
    
elif content_state == '공개' : # 게시글 상태가 공개이면
    print('열람 가능')
    
elif content_state == '비밀' and user_name == writer: # 게시글 상태가 비밀이고 로그인 사용자가 작성자와 같으면
    print('작성자 열람 가능')
    
else: # 그 외
    print('열람 권한이 없습니다.')
'''

# 도전 3
'''
print("도전 3 -----------------------------------------------------------------------------")
name = input('이름: ')
age = int(input('나이 : '))
person_num = int(input('현재 신청 인원 : '))
max_person_num = int(input('정원 : '))
paid = input('결제 여부 (예/아니요) : ')
required_done = input('필수 과정 이수 여부 (예/아니요) : ')

if age < 19 : # 나이가 19세 미만이면
    print('신청 불가 : 성인만 신청할 수 있습니다.')
    
elif person_num >= max_person_num : # 현재 신청 인원이 정원 이상이면
    print('신청 불가 : 정원이 마감되었습니다.')
    
elif paid == '아니요': # 결제하지 않았으면
    print('신청 보류 : 결제가 필요합니다.')
    
elif required_done == '아니요': # 필수 과정을 이수하지 않았으면
    print('신청 보류 : 필수 과정을 먼저 이수해야 합니다.')
    
else:
    completed_total = {'name':name, 'age':age, 'paid':paid, 'required_done':required_done}
    print('신청 완료')
    print(completed_total)
'''

# 도전 4
'''
print("도전 4 -----------------------------------------------------------------------------")
user_grade = input('고객 등급 (VIP/GOLD/BASIC) : ')
content_tag = input('문의 유형 (결제/오류/배송/기타) : ')
wait_time = int(input('대기 시간(분) : '))
again = input('재문의인가요? (예/아니요) : ')

if user_grade == 'VIP' and (content_tag == '결제' or content_tag=='오류') : # vip이면서 문의 유형이 결제/오류이면
    print('긴급 처리')
    result = '긴급 처리'

elif (user_grade == 'VIP' or user_grade == 'GOLD') and wait_time >= 60 : # gold 이상이면서 대기시간이 60분 이상이면
    print('우선 처리')
    result = '우선 처리'
elif again == '예' and wait_time >= 30 : # 재문의이고 대기 시간이 30분 이상이면
    print('우선처리')
    result = '우선 처리'

elif content_tag == '기타' and wait_time < 10 : # 문의 유형이 기타이고 대기 시간이 10분 미만이면
    print('일반 처리')
    result = '일반 처리'

else:
    print('접수 완료')
    result = '접수 완료'

total_info = {'grade' : user_grade, 'content' : content_tag, 'result' : result}
print(total_info)
'''

'''
# 사용자로 부터 주민등록번호를 입력받아 성별을 구별하는 코드를 작성하세요.
user_info = input('주민등록번호를 입력하세요 (- 포함): ')

if user_info[7] == '1' or user_info[7] == '3' or user_info[7] == '5':
    print('당신은 남자입니다.')
else:
    print('당신은 여자입니다.')
'''


