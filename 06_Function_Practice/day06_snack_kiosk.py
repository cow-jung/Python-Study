'''
menus = [
    {'id': 1, 'name': '떡볶이', 'price': 3500},
    {'id': 2, 'name': '순대', 'price': 4000},
    {'id': 3, 'name': '튀김', 'price': 3000},
    {'id': 4, 'name': '김밥', 'price': 3000},
    {'id': 5, 'name': '어묵', 'price': 1500}
] # 판매 메뉴 목록

cart = [] # 사용자가 주문한 상품을 담는 장바구니

while True:
    print('========== 파이썬 분식점 ==========')
    print('1. 메뉴 보기')
    print('2. 주문하기')
    print('3. 장바구니 보기')
    print('4. 주문 취소')
    print('5. 결제하기')
    print('0. 종료')
    menu = input('메뉴 선택 : ')

    if menu == '1':
        print('----- 판매 메뉴 -----')
        for menu in menus:
            print(menu['id'], menu['name'], menu['price'], '원')
        print('--------------------')

    elif menu == '2':
        print('----- 판매 메뉴 -----')
        for menu in menus:
            print(menu['id'], menu['name'], menu['price'], '원')
        print('--------------------')
        order_id = int(input('주문할 메뉴 선택 : '))
        selected_menu = None

        for item in menus:
            if item['id'] == order_id:
                selected_menu = item

        if selected_menu == None:
            print('없는 메뉴 입니다.')
        else:
            cart.append(selected_menu)
            print(selected_menu['name'], '주문 완료')

    elif menu == '3':
        if len(cart) == 0:
            print('장바구니가 비어 있습니다.')
        else:
            total = 0

            print('----- 장바구니 -----')

            for item in cart:
                print(item['name'], item['price'],'원')
                total += item['price']
            print('메뉴 선택 : ', len(cart),'개')
            print('총 금액 : ', total, '원')
            print('--------------------')

    elif menu == '4':
        print('----- 장바구니 -----')
        for item in cart:
            print(item['name'], item['price'], '원')
            total += item['price']
        print('--------------------')

        cancel_name = input('취소할 메뉴 이름 : ')
        cancel_item = None

        for item in cart:
            if item['name'] == cancel_name:
                cancel_item = item
                break

        if cancel_item == None:
            print('장바구니에 해당 메뉴가 없습니다.')
        else:
            cart.remove(cancel_item)
            print(cancel_name, '취소 완료 되었습니다.')

    elif menu == '5':
        if len(cart) == 0:
            print('결제할 상품이 없습니다.')
        else:
            total = 0

            for item in cart:
                total += item['price']

            print('총 결제 금액 : ', total, '원')
            print('결제가 완료되었습니다.')

    elif menu == '0':
        print('프로그램을 종료합니다.')
        break

    else:
        print('잘못된 메뉴입니다.')
'''

books = []

while True:
    print('-'*30)
    print('1. 책 목록 보기')
    print('2. 책 등록')
    print('3. 책 검색')
    print('4. 책 삭제')
    print('0. 종료')
    print('-' * 30)

    books_menu = input('독서 기록 관리 메뉴를 선택하세요 >>> ')

    if books_menu == '1':
        if len(books) == 0:
            print('등록된 책 정보가 없습니다.')
        else:
            for book in books:
                print('------------ 책 목록 ------------')
                print('책 이름 :',book['title'])
                print('책 저자 :',book['writer'])

    elif books_menu == '2':
        title = input('책 제목 : ')
        writer = input('책 저자 : ')

        book = {'title': title, 'writer': writer}
        books.append(book)

        print('책이 등록되었습니다.')

    elif books_menu == '3':
        select_book = input('책 이름 : ')
        found = False

        for book in books:
            if select_book in book['title']:
                print('-' * 30)
                print('책 이름 : ', book['title'])
                print('책 저자 : ', book['writer'])
                found = True

        if found == False:
            print('검색 결과가 없습니다.')

    elif books_menu == '4':
        delete_title = input('책 이름 : ')
        delete_book = None

        for book in books:
            if book['title'] == delete_title:
                delete_book = book
                break
        if delete_book == None:
            print('삭제할 책을 찾을 수 없습니다.')

        else:
            books.remove(delete_book)
            print('삭제하였습니다.')

    elif books_menu == '0':
        print('종료합니다.')
        break

    else:
        print('잘못 입력하셨습니다. 다시 입력하세요')