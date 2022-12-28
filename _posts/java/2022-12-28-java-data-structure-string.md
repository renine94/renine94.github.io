---
layout: single

header:
  teaser: /assets/images/logo/java.jpeg
  overlay_image: /assets/images/logo/java.jpeg
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[Java] 기본 자료구조 - String"
excerpt: "🚀 Java, Data Structure, String, Method"

categories: java
tag: [java, data structure, string]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# String
> 자바에서 문자열을 나타내는 자료형
>
> [출처](https://wikidocs.net/205)

```java
// 리터럴 표기법
String a = "Hello, world!";
String b = "a";
String c = "123";

// 아래와 같이 표현할 수도 있다.
String a = new String("Hello, world!");
String b = new String("a");
String c = new String("123");
```

`new` 키워드는 객체를 만들 때 사용한다.
하지만 보통 문자열을 표현할 때는 가급적 첫번째 방식(리터럴 표기)을 사용하는 것이 좋다.
**첫 번째 처럼 사용하면 가독성에 이점이 있고 컴파일 시 최적화에 도움**을 주기 때문이다.

<br>

---



## 01. 원시(Primitive) 자료형

원시 자료형은 아래와 같이 있으며, 원시 자료형은 `new` 키워드로 그 값을 생성할 수 없다.
- int
- long
- double
- float
- boolean
- char

```java
boolean result = true;
char a = 'A';  // char 자료형은 홑따옴표 사용 ''
int i = 100000;
```
> 원시자료형은 위와 같이 리터럴(literal)로만 값을 세팅할 수 있다.
> String 은 "Happy Java" 와 같이 리터럴로 표기가 가능하지만, primitive자료형은 아니다.
> String은 리터럴 표현식을 사용할 수 있도록 자바에서 특별대우해주는 자료형이다.

## 02. 원시 자료형의 Wrapper 클래스



| 원시자료형 | Wrapper 클래스 |
| ---------- | -------------- |
| int        | Integer        |
| long       | Long           |
| double     | Double         |
| float      | Float          |
| boolean    | Boolean        |
| Char       | Char           |



앞으로 공부할 ArrayList, HashMap, HashSet 등은 데이터를 생성할때 원시 자료형 대신 그에 대응하는 Wrapper 클래스를 사용해야 한다. 원시 자료형 대신 Wrapper 클래스를 사용하면 값 대신 객체를 주고 받을 수 있어 코드를 객체 중심적으로 작성하는데 유리하다. 또한 멀티스레딩 환경에서 동기화를 지원하기 위해서도 Wrapper 클래스는 반드시 필요하다.





## 03. 문자열(String) 내장 메서드

> String built-in API 에 대해 알아보자

### equals

### indexOf

### contains

### charAt

### replaceAll

### substring

### toUpperCase

### split



**equals**

- 두 개의 문자열이 동일한지 비교하여 true/false 값을 리턴

```java
String a = "hello";
String b = "java";
String c = "hello";

System.out.println(a.equlas(b));  // false
System.out.println(a.equlas(c)); // true
```

문자열 a 와 b 는 "hello" 와 "java" 로 서로 같지 않다. 따라서 equals 메서드 호출 시 false 리턴



**문자열의 값을 비교할때는 반드시 `equals` 를 사용해야 한다. `==` 연산자를 사용할 경우 다음과 같은 경우가 발생할 수 있다.**

```java
String a = "hello";
String b = new String("hello");

System.out.println(a.equals(b)); // true
System.out.println(a == b); // false
```



문자열 a, b 는 모두 "hello" 로 값은 값을 가지지만, 

- equals 는 true
- == 연산자는 false

a 와 b는 값은 같지만 서로 다른 객체이다. `==` 은 **두개의 자료형이 동일한 객체인지를 판별**할 때 사용하는 연산자이기 때문에 false를 리턴한다.

> equals 는 값만 비교하는 반면,  == 연산자는 동일한 객체인지 판별, 즉. 메모리 주소값까지 같은지를 비교하는것 같다.
>
> python의 is 랑 비슷해보이는 느낌이다..

<br>

---



**indexOf**

- 문자열에서 특정 문자열이 시작되는 위치(인덱스) 리턴

```java
String a = "Hello Java";

int result = a.indexOf("Java");
System.out.println(result) // 6
```

<br>

---



**contains**

- 문자열에서 특정 문자열이 포함되어 있는지의 여부를 리턴

```java
String a = "Hello Java";
boolean result = a.contains("Java");

System.out.println(result); // true
```

문자열 a는 "Java" 라는 문자열을 포함하고 있기 때문에 true 를 리턴한다.

<br>

---

**replaceAll**

- 문자열 중 특정 문자열을 다른 문자열로 바꾸고자 할 때 사용

```java
String a = "Hello Java";
String result = a.replaceAll("Java", "World");

System.out.println(result);  // Hello World
```

"Hello Java" 문자열에서 "Java" 를 "World" 로 바꾸었다.

<br>

---

**subString**

- 문자열 중 특정 부분을 뽑아낼 경우 사용

```java
String a = "Hello Java";
String result = a.substring(0, 4);

System.out.println(result);  // Hell 출력
```

끝 위치 4 는 포함되지 않는다. (시작위치 <= a < 끝위치)



<br>

---

**toUpperCase**

- 문자열을 모두 대문자로 변경할 때 사용
- 소문자로 변경할 때는 `toLowerCase` 사용

```java
String a = "Hello Java";
System.out.println(a.toUpperCase());  // HELLO JAVA;
```

<br>

---

**split**

- 문자열을 특정 구분자로 나누어 문자열 배열로 리턴하는 메서드

```java
String a = "a:b:c:d";
String[] result = a.split(":");  // result = {"a", "b", "c", "d"}
```

`:` 로 나누어 문자열 배열을 만들 수 있다.

<br>

---

## 04. 문자열 포매팅



- 숫자 바로 대입

문자열 포매팅은 `String.format` 메서드를 사용한다.

```java
String result = String.format("I eat %d apples.", 3);  // %d = digit 문자열 포맷 코드
System.out.println(result)  // "I eat 3 apples."
```



- 문자열 바로 대입

```java
String result = String.format("I eat %s apples.", "five");
System.out.println(result);  // I eat five apples.
```





## 05. 문자열 포맷 코드



| 코드 |           설명            |
| :--: | :-----------------------: |
|  %s  |      문자열(String)       |
|  %c  |    문자 1개(character)    |
|  %d  |      정수 (Integer)       |
|  %f  | 부동소수 (floating-point) |
|  %o  |           8진수           |
|  %x  |          16진수           |
|  %%  | Literal % (문자 `%` 자체) |





