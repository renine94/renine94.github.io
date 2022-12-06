# What is "Context" in develop
> 개발에서 말하는 'context' 란 무엇인가?
> 참조
> - [orbit-blog](https://orbit-orbit.tistory.com/65)
> - [여씨개발이야기](https://yeoossi.tistory.com/54)





**TL; DR**

개발에서 말하는 **Context** 의 주된 뜻은 이벤트가 일어나는 조건, 환경 등이 된다.

A라는 사람이 인터넷을 통해 물건을 구매하려고 한다.<br>쇼핑몰은 A의 이름, 전화번호, 주소 등의 개인 정보와 결제를 위한 정보 등을 필요로 할 것이다<br>이 때, **A의 정보**들이 **물건을 구매하기 위해 필요한 Context 개체** 라고 부를 수 있다.

Context의 종류

- 필수 Context
  - 물건 금액, 카드번호, 결제정보, 받는주소, 받는사람 정보
- 선택 Context
  - 성별, 집전화번호, 배송메시지, 등





## 01. Example



```w
Let's say you go to the dentist to have a tooth pulled out.

When the receptionist asks you for your name, that's information they need in order to begin the appointment. In this example, your name is contextual information. So in the context of visiting the dentist, you need to provide your name to get your tooth pulled.

Now let's say you walk over to the bank.

At the bank, you ask to withdraw $100. The teller needs to establish your identity before giving you money, so you'll probably have to show them a driver's license or swipe your ATM card and enter your PIN number. Either way, what you're providing is context. The teller uses this information to move the transaction forward. They may then ask you which account you'd like to withdraw from. When you answer, "My savings account", that's even more context.

The more context you give, the more knowledge the other party has to help deal with your request. Sometimes context is optional (like typing more and more words into your Google search to get better results) and sometimes it's required (like providing your PIN number at the ATM). Either way, it's information that usually helps to get stuff done.

Now let's say you take your $100 and buy a plane ticket to fly somewhere warm while your mouth heals.

You arrive at a nice sunny destination, but your bag doesn't make it. It's lost somewhere in the airport system. So, you take your "baggage claim ticket" (that sticker with the barcode on it) to the "Lost Baggage office". The first thing the person behind the desk will ask for is that ticket with your baggage number on it. That's an example of some required context.

But then the baggage person asks you for more information about your bag like so they can find it more easily. They ask, "What color is it? What size is it? Does it have wheels? Is it hard or soft? While they don't necessarily need those pieces of information, it helps narrow things down if you provide them. It reduces the problem area. It makes the search much faster. That's optional context.

Here's the interesting part: for a lot of software and APIs, the required context usually ends up as actual parameters in a method signature, and optional context goes somewhere else, like a flexible key-value map that can contain anything (and may be empty) or into thread-local storage where it can be accessed if needed.

The examples above are from real life, but you can easily map them to areas within computer science. For example, HTTP headers contain contextual information. Each header relates to information about the request being made. Or when you're sending along a global transaction ID as part of a two-phase commit process, that transaction ID is context. It helps the transaction manager coordinate the work because it's information about the overall task at hand.

Hope that helps.

```





```wiki
여러분이 치과에 가서 이를 뽑았다고 가정해 봅시다.

안내원이 당신에게 이름을 물었을 때, 그것은 그들이 약속을 시작하기 위해 필요한 정보입니다. 이 예에서는 사용자의 이름이 상황별 정보입니다. 그래서 치과를 방문하는 맥락에서, 당신은 이를 뽑으려면 당신의 이름을 제공할 필요가 있다.

이제 당신이 은행으로 걸어간다고 가정해보자.

은행에서 당신은 100달러를 인출해 달라고 요청합니다. 창구 직원이 돈을 주기 전에 신원을 확인해야 하기 때문에 운전면허증을 보여주거나 현금인출기 카드를 찍고 비밀번호를 입력해야 할 것입니다. 어느 쪽이든, 당신이 제공하는 것은 맥락입니다. 출납원은 거래를 진전시키기 위해 이 정보를 사용한다. 그런 다음 어떤 계정에서 탈퇴할 것인지 물어볼 수 있습니다. "내 저축 계좌"라고 대답하는 것은 훨씬 더 맥락이 있습니다.

사용자가 더 많은 컨텍스트를 제공할수록 상대방은 사용자의 요청을 처리하는 데 도움이 되는 더 많은 지식을 보유하게 됩니다. 컨텍스트가 선택적인 경우(예: 더 나은 결과를 얻기 위해 Google 검색에 점점 더 많은 단어를 입력하는 경우)도 있고 필요한 경우(예: ATM에서 PIN 번호 제공)도 있습니다. 어느 쪽이든, 그것은 보통 일을 하는데 도움이 되는 정보이다.

이제 여러분이 100달러를 가지고 입이 치유되는 동안 따뜻한 곳으로 날아가기 위해 비행기 표를 산다고 가정해봅시다.

당신은 화창한 목적지에 도착하지만, 당신의 가방은 도착하지 않는다. 그것은 공항 시스템 어딘가에서 분실되었다. 그래서, 당신은 당신의 "짐 찾는 표"(바코드가 붙어있는 스티커)를 "짐 찾는 사무실"로 가져갑니다. 책상 뒤에 있는 사람이 제일 먼저 요청할 것은 당신의 수화물 번호가 적힌 표입니다. 그것은 몇 가지 필수적인 맥락의 예이다.

하지만 수하물 담당자는 당신의 가방에 대한 더 많은 정보를 그들이 더 쉽게 찾을 수 있도록 당신에게 요청합니다. 그들은 묻습니다. "무슨 색이죠?" 사이즈가 어떻게 되죠? 바퀴가 있나요? 딱딱해요, 부드러워요? 이러한 정보가 반드시 필요한 것은 아니지만, 제공하면 정보 범위를 좁히는 데 도움이 됩니다. 그것은 문제 영역을 줄여줍니다. 검색 속도가 훨씬 빨라집니다. 그것은 선택적인 맥락입니다.

여기 흥미로운 부분이 있습니다. 많은 소프트웨어와 API의 경우 필요한 컨텍스트는 대개 메서드 시그니처의 실제 매개 변수로 끝나며, 옵션 컨텍스트는 무엇이든 포함할 수 있는 유연한 키 값 맵과 같이 다른 곳으로 이동하거나 필요할 때 액세스할 수 있는 스레드 로컬 스토리지로 이동합니다.

위의 예들은 실생활에서 나온 것들이지만, 당신은 그것들을 컴퓨터 과학 내의 영역들에 쉽게 매핑할 수 있다. 예를 들어 HTTP 헤더에는 상황별 정보가 포함되어 있습니다. 각 헤더는 수행 중인 요청에 대한 정보와 관련이 있다. 또는 2단계 커밋 프로세스의 일부로 글로벌 트랜잭션 ID를 함께 보낼 때 해당 트랜잭션 ID는 컨텍스트입니다. 이것은 당면한 전체 작업에 대한 정보이기 때문에 트랜잭션 관리자가 작업을 조정하는 데 도움이 됩니다.

그게 도움이 됐으면 좋겠네요.
```

