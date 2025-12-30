"""
카페 키오스크 시스템 예제 프로그램 작성 연습
( 조건문 필 활용 / 조건문만 활용 / 조건문 외 추가활용 나눠서 작성 )
프로그램 실행 순서도
    메뉴 선택
    사이즈 선택
    옵션 추가 ( 샷 추가, 휘핑 등 )
화면진행 예시
    #1
    [메뉴]
    1. 아메리카노 - 1500원
    2. 카페라때 - 2000원
    3. 바닐라라떼 - 2500원
    [사이즈]
    #2
    [사이즈]
    1. regular(기본)
    2. large(+500원)
    #3
    [옵션]
    1. 샷 추가 (+500원)
    2. 휘핑 추가 (+300원)
    3. 옵션 없음
    #4
    ==== 주문 내역 ====
    아메리카노 (large, 샷 추가) - 2500원
    ==================
    총 금액: 2500원
    감사합니다!
"""

# 메뉴변수
menu_1 = "아메리카노"
menu_2 = "카페라떼"
menu_3 = "바닐라라떼"
# 기본 가격 변수
price_1 = 1500
price_2 = 2000
price_3 = 2500
# 사이즈변수
size_1 = "regular(기본)"
size_2 = "large"
# 옵션 변수
option_1 = "샷 추가"
option_2 = "휘핑 추가"
option_3 = "옵션 없음"
# 추가 가격 변수
price_add_300 = 300
price_add_500 = 500

# 메뉴 입출력 변수
menu_input_num = 0
size_input_num = 0
option_input_num = 0
menu_input_var = ""
size_input_var = ""
option_input_var = ""
total_price = 0

# UI 화면출력
# 메뉴 선택 화면
print("메뉴")
print(f"1. {menu_1}")
print(f"2. {menu_2}")
print(f"3. {menu_3}")
# 메뉴 입력
menu_input_num = int(input("메뉴를 선택: "))

# 사이즈 선택 화면
print("사이즈")
print(f"1. {size_1}")
print(f"2. {size_2}")
# 사이즈 입력
size_input_num = int(input("사이즈를 선택: "))

# 옵션 선택 화면
print("옵션")
print(f"1. {option_1}")
print(f"2. {option_2}")
print(f"3. {option_3}")
print("")
# 옵션 입력
option_input_num = int(input("옵션 선택: "))

# 메뉴 입력값-문자열 변환 + 기본 가격 대입
if menu_input_num == 1:
    menu_input_var = menu_1
    total_price = price_1
elif menu_input_num == 2:
    menu_input_var = menu_2
    total_price = price_2
elif menu_input_num == 3:
    menu_input_var = menu_3
    total_price = price_3
else:
    print("잘못 입력")

# 사이즈 입력값-문자열 변환 + 추가가격 연산
if size_input_num == 1:
    size_input_var = size_1
elif size_input_num == 2:
    size_input_var = size_2
    total_price += price_add_500
else:
    print("잘못 입력")

# 옵션 입력값-문자열 변환 + 추가가격 연산
if option_input_num == 1:
    option_input_var = option_1
    total_price += price_add_500
elif option_input_num == 2:
    option_input_var = option_2
    total_price += price_add_300
elif option_input_num == 3:
    option_input_var = option_3
else:
    print("잘못 입력")

# 가격 출력 화면

print("=" * 40)
print("주문내역")
print("-" * 40)
print(f"{menu_input_var} ({size_input_var}, {option_input_var}) - {total_price} 원")
print("=" * 40)
print(f"총 금액: {total_price}")
print("감사합니다!")
