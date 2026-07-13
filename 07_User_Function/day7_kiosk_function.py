# 함수를 사용하여 사칙연산 계산기 만들기
# 콘솔창에서 두수를 입력받아 사칙연산을 하는 프로그램
# 단, 무한루프와 메뉴판 형식을 사용할것
def add(a, b): # 더하기
    return a + b
def subtract(a, b): # 빼기
    print(f'{a} - {b} = {a-b}')
    return a - b
def multiply(a, b): # 곱하기
    c = list()
    multi = a * b
    c.append(multi)
    return c

def divide(a, b): # 나누기
    print(f'정수 : {a} // {b} = {a//b}') # 정수
    print(f'실수 : {a} / {b} = {a/b}')   # 실수
    print(f'나머지 : {a} % {b} = {a%b}')   # 나머지 값

    c = list()
    divide_result = a / b.0
    c.append(divide_result)
    print(f'리스트 : {a} / {b} = {divide_result}') # 리스트

    d = dict()
    d['결과'] = divide_result
    print(f'딕셔너리 : {a} / {b} = {d}')


while True:
    print('========== 사칙연산 계산기 ==========')
    print('1. 더하기')
    print('2. 빼기')
    print('3. 곱하기')
    print('4. 나누기')
    print('5. 종료')

    calculator = input('기능 선택 : ')
    if calculator == '5':
        print('종료합니다.')
        break

    print('-' * 30)
    num1 = int(input('첫 번째 숫자 : '))
    num2 = int(input('두 번째 숫자 : '))

    if calculator == '1':
        result = add(num1, num2)
        print(f'{num1} + {num2} = {result}')

    elif calculator == '2':
        subtract(num1, num2)

    elif calculator == '3':
        result = multiply(num1, num2)
        print(f'{num1} * {num2} = {result[0]}')

    elif calculator == '4':
        divide(num1, num2)

    else:
        print('잘못 선택하였습니다.')

