'''
#문제 2
students = int(input("학생 수를 입력하세요 : "))
seats = int(input("한 줄 좌석 수를 입력하세요 : "))

full_rows = students //seats # 꽉 찬 줄 수(몫)
last_row = students % seats # 이외 나머지
total_rows = full_rows + 1 # 전체 줄 수

print("=" * 20)
print("[강의실 좌석 배치]")
print(f"전체 학생 수 : {students}명")
print(f"한 줄 좌석 수 : {seats}명")
print(f"꽉 찬 줄 수 : {full_rows}줄")
print(f"마지막 줄 학생 수 : {last_row}명")
print(f"필요한 총 줄 수 : {total_rows}줄")
print("=" * 20)
'''

'''
#문제 3
site_name = input("사이트 이름을 입력하세요 : ")
password = input("비밀번호를 입력하세요 : ")

password_len = len(password)
hidden_password = "*" * password_len
length_score = password_len * password_len # password_len**2
length_total = len(site_name) + password_len

print(f"사이트 이름 : {site_name}")
print(f"비밀번호 길이 : {password_len}자")
print(f"가린 비밀번호 : {hidden_password}")
print(f"길이 제곱값 : {length_score}")
print(f"사이트+비밀번호 전체 길이 : {length_total}자")
'''

'''
#문제 4
base_fee = int(input("기본 요금을 입력하세요 : "))
distance = float(input("이동 거리(km)를 입력하세요 : "))
fee_per_km = int(input("1km 당 추가요금을 입력하세요 : "))

distance_fee = distance * fee_per_km # 거리 요금
total_fee = distance_fee + base_fee # 총 요금
fee_per_person = total_fee / 3 # 1명당 금액

print("[택시 요금 계산]")
print(f"기본요금 : {base_fee}원")
print(f"이동 거리 : {distance}km")
print(f"거리 요금 : {distance_fee:.0f}원")
print(f"예상 총 요금 : {total_fee:.0f}원")
#print(f"거리 요금 : {int(distance_fee)}원")
#print(f"예상 총 요금 : {int(total_fee)}원")
print(f"3명 기준 1인당 금액 : {fee_per_person:.2f}원")
'''

'''
#문제 5
seconds = int(input("총 초를 입력하세요 : "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
second = seconds % 60

print("[시간 변환 결과]")
print(f"입력한 시간 : {seconds}초")
print(f"변환 결과 : {hours}시간 {minutes}분 {second}초")
'''

# 문제 6
