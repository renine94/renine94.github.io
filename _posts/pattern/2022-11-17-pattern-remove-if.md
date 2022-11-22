---
layout: single

header:
  teaser: /assets/images/logo/pattern.jpeg
  overlay_image: /assets/images/logo/pattern.jpeg
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[pattern] if문을 사용하지않고 코드스타일 깔끔하게 정리해보기"
excerpt: "🚀 객체 리터럴을 활용한 if문 줄이는 방법을 알아보자."

categories: pattern
tag: [pattern, literal]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---
# 01. if문을 없애는방식으로 코딩하기

> 코드를 작성하다보면 if문이 많아져서 복잡해지는 문제를 해결해보자.
>
> 아래의 영상을 참고하여 Javascript 로 짜여진 코드를 Python으로 다시 작성하였습니다.

{% include video id="toUlXhTZZ8w" provider="youtube" %}



---



코드를 작성하다보면 아래와 같이 코드를 짜는 경우가 생기는데,

```python
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
```



이렇게 로직에 if문으로 처리를 하게되면, 나중에 결제 방식이 늘어날때마다 아래에 계속 추가가되어 가독성에 좋지않다.

이러한 코드를 아래처럼 바꾸게 되면 훨씬 코드가 간결해지는 효과를 볼 수 있다.



```python
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
```

<br><br>

---



# 02. 함수 자체를 저장시켜 호출하기

> 위에 방법을 조금 더 응용한 결과이다.



python 에서의 함수는 1급함수라는 특징이 있기 때문에 함수자체 또한 객체이므로 딕셔너리 value에 매핑시킬 수 있다.

```python
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

 # 함수 자체를 넣어야 한다. () 호출해서 넣으면 메모리에 올라갈때 값 고정됨
payment_map = {
  'KAKAO_PAYMENT': pay_on_kakao,  
  'NAVER_PAYMENT': pay_on_naver,
  'COUPANG_PAYMENT': pay_on_coupang,
  'PAYCO_PAYMENT': pay_on_payco,
}

def execute_payment(payment_type: str) -> str:
  payment_map[payment_type]()  # () 호출해주는것을 잊지말자.

execute_payment('KAKAO_PAYMENT')
execute_payment('NAVER_PAYMENT')
```

