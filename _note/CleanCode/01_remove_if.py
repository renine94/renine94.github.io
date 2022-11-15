# if 분기처리 를 없애보자.

# 기존 방식
def execute_payment(payment_type: str) -> str:
  if payment_type == 'KAKAO_PAYMENT':
    return '카카오 결제 처리'

  if payment_type == 'NAVER_PAYMENT':
    return '네이버 결제 처리'

  if payment_type == 'COUPANG_PAYMENT':
    return '쿠팡 결제 처리'

  if payment_type == 'PAYCO_PAYMENT':
    return '페이코 결제 처리'

  if payment_type == 'APPLE_PAYMENT':
    return '애플 결제 처리'


# 개선 방식
payment_map = {
  'KAKAO_PAYMENT': '카카오 결제 처리',
  'NAVER_PAYMENT': '네이버 결제 처리',
  'COUPANG_PAYMENT': '쿠팡 결제 처리',
  'PAYCO_PAYMENT': '페이코 결제 처리',
  'APPLE_PAYMENT': '애플 결제 처리',
}

def execute_payment(payment_type: str) -> str:
  return payment_map[payment_type]

result = execute_payment('KAKAO_PAYMENT')
print(result)


################################################################
def pay_on_kakao():
  print('kakao pay 처리중...1')
  print('kakao pay 처리중...2')
def pay_on_naver():
  print('naver pay 처리중...')
def pay_on_coupang():
  print('coupang pay 처리중...')
def pay_on_payco():
  print('payco pay 처리중...')
def send_log():
  return

payment_map = {
  'KAKAO_PAYMENT': pay_on_kakao,  # 함수 자체를 넣어야 한다. () 호출해서 넣으면 메모리에 올라갈때 값 고정됨
  'NAVER_PAYMENT': pay_on_naver,
  'COUPANG_PAYMENT': pay_on_coupang,
  'PAYCO_PAYMENT': pay_on_payco,
}

def execute_payment(payment_type: str) -> str:
  payment_map[payment_type]()

execute_payment('KAKAO_PAYMENT')
execute_payment('NAVER_PAYMENT')