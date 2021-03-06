---
layout: single

header:
  teaser: /assets/images/logo/book.jpg
  overlay_image: /assets/images/logo/book.jpg
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "면접을 위한 CS 전공지식 노트 (1) - 디자인 패턴"
excerpt: "🚀 디자인 패턴과 프로그래밍 패러다임"

categories: book
tag: [cs]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

**[알림]** 책에 대한 정보는 [여기](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=292815727) 를 참고해주세요.🚀🚀
{: .notice--danger}



# 01. 디자인 패턴

<div class="notice--success">
  <ul>
    <li> 프로그램을 설계할때 발생했던 문제점들을 객체 간의 상호 관계 등을 이용하여 해결 할 수 있도록 하나의 규약 형태로 만들어 놓은 것 </li>
  </ul>
</div>



## 1.1 싱글톤 패턴

> 싱글톤 패턴(Singleton pattern)은 하나의 클래스에 오직 하나의 인스턴스만 가지는 패턴이다.
>
> 보통 데이터베이스 연결 모듈에 많이 사용

- 인스턴스를 생성할 때 드는 비용이 줄어드는 장점이 있다.
- 하지만 의존성이 높아진다는 단점이 있다.



### 구현

#### JS

```js
const obj = {
  a: 27
}

const obj2 = {
  a: 27
}

console.log(obj === obj2)
// false
```

위의 코드에서 볼 수 있듯이 `obj` 와 `obj2` 는 서로 다른 인스턴스를 가진다.

```js
class Singleton {
  
  constructor() {
    if (!Singleton.instance) {
      Singleton.instance = this
    }
    return Singleton.instance
  }
  
  getInstance() {
    return this.instance
  }
}

const a = new Singleton()
const b = new Singleton()
console.log(a === b) // true
```



앞의 코드는 `Singleton.instance` 라는 하나의 인스턴스를 가지는 Singleton 클래스를 구현한 모습

이를 통해 a와 b는 하나의 인스턴스를 가집니다.

#### Python

```python
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls,'instance'):
            print('create')
            cls.instance = super(Singleton, cls).__new__(cls)
        else:
            print('recycle')
        return cls.instance
 
s1 = Singleton() # create
s2 = Singleton() # recycle
print(s1 == s2) # true

```

#### Java

```java
class Singleton {
  private static class singleInstanceHolder {
    private static final Singleton INSTANCE = new Singleton();
  }
  
  public static synchronized Singleton getInstance() {
    return singleInstanceHolder.INSTANCE;
  }
}

public class HelloWorld {
  public static void main(String[] args) {
    Singleton a = Singleton.getInstance();
    Singleton b = Singleton.getInstance();
    System.out.println(a.hashCode());
    System.out.println(b.hashCode());
    
    if (a == b) {
      System.out.println(true);
    }
  }
}

// 705927765
// 705927765
// true
```



**데이터 베이스 연결 모듈**에 자주 쓰이는 패턴이다.



### 단점

싱글톤 패턴은 TDD 할 때 걸림돌이 된다. TDD를 할 때 단위 테스트를 주로 하는데, 단위 테스트는 테스트가 서로 독립적이어야 하며, 테스트를 어떤 순서로든 실행할 수 있어야 합니다.

하지만 싱글톤 패턴은 미리 생성된 하나의 인스턴스를 기반으로 구현하는 패턴이므로 각 테스트마다 `독립적인` 인스턴스를 만들기가 어렵습니다.



### 의존성 주입

- 싱글톤 패턴은 사용하기 쉽고, 굉장히 실용적
- 모듈간의 결합을 강하게 만드는 단점
- 의존성 주입(DI) 을 통해 모듈간의 결합을 느슨하게 만들어 해결 가능

메인 모듈이 직접 다른 하위 모듈에 대한 의존성을 주기보다는 중간에 의존성 주입자(dependency injector)가 이 부분을 가로채 메인 모듈이 간접적으로 의존성을 주입하는 방식



이를 통해 메인 모듈(상위 모듈)은 하위 모듈에 대한 의존성이 떨어지게 됩니다.참고로 이를 `디커플링` 이 된다. 라고도 합니다.



- DI 장점

  - 모듈들을 쉽게 교체할 수 있는 구조

  - 쉽게 테스팅 하기 쉽고 마이그레이션 하기도 수월

  - 구현할 때 추상화 레이러를 넣고 이를 기반으로 구현체를 넣어 주기 때문에 애플리케이션

    방향이 일관되고, 쉽게 추론

  - 모듈 간 관계들이 명확해진다.

- DI 단점

  - 모듈들이 더욱 분리
  - 클래스 수가 늘어나 복잡성 증가
  - 약간의 런타임 패널티

- DI 원칙

  - 상위 모듈은 하위 모듈에서 어떠한 것도 가져오지 않는다.
  - 둘 다 추상화에 의존해야 하며, 이때 추상화는 세부 사항에 의존하지 않는다.



## 1.2 팩토리 패턴

to be continue..



## 1.3 전략 패턴

to be continue..



## 1.4 옵저버 패턴

to be continue..



## 1.5 프록시 패턴과 프록시 서버

>  프록시 패턴은(Proxy pattern) 은 대상 객체(subject)에 접근하기 전 그 접근에 대한 흐름을 가로채
>
> 대상 객체 앞단의 인터페이스 역할을 하는 디자인 패턴이다.



- 프록시 서버에서의 캐싱

캐시 안에 정보를 담아두고, 캐시 안에 있는 정보를 요구하는 요청에 대해 다시 저 멀리 있는 원격 서버에 요청하지 않고,
캐시 안에 있는 데이터를 활용하는 것을 말한다. 이를 통해 불필요하게 외부와 연결하지 않기 때문에
**트래픽을 줄일 수 있는 장점이 있다.**



### 프록시 서버

프록시 서버는 서버와 클라이언트 사이에 클라이언트가 자신을 통해 다른 네트워크 서비스에 간접적으로 접속할 수 있게 해주는
컴퓨터 시스템이나 응용 프로그램을 가르킨다.

- Nginx
  - 비동기 이벤트 기반의 구조와 다수의 연결을 효과적으로 처리 가능한 웹 서버
  - 주로 Node.js, Django 등 서버 앞단의 프록시 서버로 활용됩니다.

![image-20220602022535598](/assets/images/posts/2022-05-12-csNoteForInterview01/image-20220602022535598.png)




- `버퍼 오버플로우`
  - 버퍼는 보통 데이터가 저장되는 메모리 공간
  - 메모리 공간을 벗어나는 경우 버퍼 오버플로우
- `gzip` 압축
  - LZ77과 Huffman 코딩의 조합인 Deflate 알고리즘을 기반으로 한 압축 기술
  - 데이터 전송량을 줄일 수 있다.
  - 하지만, 압축해제 시 서버에서의 CPU 오버헤드 발생 가능성 존재



### 프록시 서버로 쓰는 `CloudFlare`

`CloudFlare` 는 전 세계적으로 분산된 서버가 있고 이를 통해 어떠한 시스템의 콘텐츠 전달을 빠르게 할 수 있는 CDN 서비스이다.
{: .notice--danger}

CDN 말고도 CloudFlare 를 통해 누릴 수 있는 이점은 많다.

- DDOS 공격 방어
- HTTPS 구축 등
- 이 모든 것은 웹 서버 앞단에 두어 프록시 서버로 쓰기때문에 가능한 것



**`CDN` (Content Delivery Network)**

각 사용자가 인터넷에 접속하는 곳과 가까운 곳에서 콘텐츠를 캐싱 또는 배포하는 서버 네트워크를 말한다.
이를 통해 사용자가 웹 서버로부터 콘텐츠를 다운로드 하는 시간을 줄일 수 있다.



## 1.6 이터레이터 패턴

> 이터레이터 패턴은 이터레이터를 사용하여 컬렉션의 요소들에 접근하는 디자인 패턴이다.

## 1.7 노출모듈 패턴

> 노출모듈 패턴은 즉시 실행 함수를 통해 private, public 같은 접근 제어자를 만드는 패턴을 말한다.

- public
  - 클래스에 정의된 함수에서 접근 가능하며 자식 클래스와 외부 클래에스에서 접근 가능
- protected
  - 클래스에 정의된 함수에서 접근 가능, 자식 클래스에서 접근 가능하지만 외부 클래스에서 접근 불가능
- private
  - 클래스에 정의된 함수에서 접근 가능하지만, 자식 클래스와 외부 클래스에서 접근 불가능한 범위
- 즉시 실행 함수
  - 함수를 정의하자마자 바로 호출하는 함수, 초기화 코드, 라이브러리 내 전역 변수의 충돌 방지 등에 사용



## <span style="color: red;">1.8 MVC 패턴</span>

> 모델(Model), 뷰(View), 컨트롤러(Controller)로 이루어진 디자인 패턴

- 애플리케이션의 구성 요소를 세 가지 역할로 구분
- 개발 프로세스에서 각각의 구성 요소에만 집중해서 개발 가능
- 재사용성과 확장성이 용이하다는 장점
- 애플리케이션이 복잡해질수록 모델과 뷰 관곅 복잡해지는 단점



### 모델

- Model 은 애플리케이션의 데이터인 데이터베이스, 상수, 변수 등을 뜻한다.

### 뷰

-  View 는 사용자 인터페이스 요소를 나타낸다.
- 즉 모델을 기반으로 사용자가 볼 수 있는 화면을 뜻합니다.
- 최근에는 react, vue, svelte 와 같은 프론트 프레임워크로 구성된다.

### 컨트롤러

- 하나 이상의 모델과 하나 이상의 뷰를 잇는 다리 역할
- 이벤트 등 메인 로직을 담당한다. (비즈니스 로직이 담김)
- 모델과 뷰의 생명주기도 관리한다.



## 1.9 MVP 패턴

to be continue..



## MVVM 패턴

> MVVM 패턴은 MVC 의 C 에 해당하는 컨트롤러가 뷰모델(view model)로 바뀐 패턴이다.
>
> MVC -> MV(VM)

- 뷰모델은 뷰를 더 추상화한 계층
- MVC 패턴과는 다르게 커맨드와 데이터 바인딩을 가지는 특징이 있다.
- 뷰와 뷰모델 사이의 양방향 데이터 바인딩을 지원
- UI 를 별도의 코드 수정없이 재사용 할 수 있고 단위 테스팅하기 쉽다는 장점
- vue.js 가 대표적인 MVVM 패턴
  - watch, computed 등으로 쉽게 반응형적인 값들을 구축가능



**커맨드**

- 여러가지 요ㅗ에 대한 처리를 하나의 액션으로 처리할 수 있게 하는 기법이다.

**데이터 바인딩**

- 화면에 보이는 데이터와 웹 브라우저의 메모리 데이터를 일치시키는 기법으로, 
  뷰 모델을 변경하면 뷰가 변경된다.



