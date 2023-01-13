# [AB180 | 핏펫] Braze Check-up

# 체크업 미팅 개요

<aside>
💁 **오늘 체크업 미팅의 목적은 무엇인가요?**

- Braze 솔루션 소개
- Braze에서 수집되는 데이터
- Braze의 캠페인 작동 원리
- Braze 캠페인 성과 확인 방법
- Braze User Guide 및 Developer Guide 활용
</aside>

# Braze 솔루션 소개

![Untitled](%5BAB180%20%E1%84%91%E1%85%B5%E1%86%BA%E1%84%91%E1%85%A6%E1%86%BA%5D%20Braze%20Check-up%20ff283a47e0464c49b8d9cc9517a1b571/Untitled.png)

# Braze에서 수집되는 데이터

[User search](https://dashboard-05.braze.com/users/user_search/61c3dc2936954d7e1e8240d7?query=626ba93c2d14230797354e9b&locale=en) (external_id : 606837, braze_id : 626ba93c2d14230797354e9b)

### Custom Attributes 이해

- 유저의 상태를 나타내는 속성 값
    - 이름, 핸드폰 번호
    - 마케팅 수신 동의 여부, 펫 정보, 회원가입 일자 등
- Braze에서 제공하는 data type
    - strings
    - numbers
        - ISO 8601 형식을 따를 수 있도록 주의
    - Time
    - arrays
    - booleans
        - string으로 데이터 전송하지 않도록 주의
    - object array
    
    <aside>
    💡 data type이 중요한 이유
    data type에 따라 Braze에서 활용할 수 있는 segment filter 연산자가 다름 ([상세 가이드](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#booleans))
    
    </aside>
    
    ![Untitled](%5BAB180%20%E1%84%91%E1%85%B5%E1%86%BA%E1%84%91%E1%85%A6%E1%86%BA%5D%20Braze%20Check-up%20ff283a47e0464c49b8d9cc9517a1b571/Untitled%201.png)
    

### Custom Event 및 Purchase Event

- 유저가 발생시킨 행동인 event 와 해당 event의 부가 정보를 담고있는 property로 구성
    
    ```json
    {
        "session_id": "E0A83598-B887-4541-8868-A2986229EC41",
        "data": {
          "n": "view_home_banner_main",
          "p": {
            "service": "common",
            "others_slug": "",
            "platform_detail": "ios_app",
            "eventsale_slug": "merits-petpermint",
            "banner_item_id": "QmFubmVyVHlwZToxMTk2",
            "banner_index": "11",
            "pet_type_mall": "DOG",
            "banner_item_name": "핏펫X메리츠 펫보험 제휴 이벤트"
          }
        },
        "name": "ce",
        "time": 1673437111.686
      }
    ```
    
- Braze에서 각 유저 당 총 이벤트 발생 횟수, 첫번째 이벤트 발생 시점, 마지막 이벤트 발생 시점을 추가로 저장
    
    ![Untitled](%5BAB180%20%E1%84%91%E1%85%B5%E1%86%BA%E1%84%91%E1%85%A6%E1%86%BA%5D%20Braze%20Check-up%20ff283a47e0464c49b8d9cc9517a1b571/Untitled%202.png)
    

### [Braze User profile lifecycle](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/)

- 익명 유저의 경우 Braze에서 device_id를 기준으로 braze_id를 부여
- [changeUser()](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles)를 통해 유저가 특정되는 시점에 external_id가 부여되고, 식별된 유저로 인식
    - changeUser()가 호출되면, 이전 braze_id에 쌓였던 데이터가 merge 됨
- 위와 같이 유저를 관리하는 이유는 여러 개의 기기를 사용하는 유저를 하나의 유저 프로필로 관리하기 위함

### Push 수신 동의 여부를 판별하는 방법

- Device단의 Push 수신 동의
    - 유효한 push token이 있는 상태
    - **`setPushNotificationSubscriptionType`** 메소드를 활용하여 로깅

![Untitled](%5BAB180%20%E1%84%91%E1%85%B5%E1%86%BA%E1%84%91%E1%85%A6%E1%86%BA%5D%20Braze%20Check-up%20ff283a47e0464c49b8d9cc9517a1b571/Untitled%203.png)

![Untitled](%5BAB180%20%E1%84%91%E1%85%B5%E1%86%BA%E1%84%91%E1%85%A6%E1%86%BA%5D%20Braze%20Check-up%20ff283a47e0464c49b8d9cc9517a1b571/Untitled%204.png)

- 유저가 마케팅 푸시 수신을 동의
    - 정보통신망법 제50조 규정을 준수
    - Custom attributes를 통해 로깅

![Untitled](%5BAB180%20%E1%84%91%E1%85%B5%E1%86%BA%E1%84%91%E1%85%A6%E1%86%BA%5D%20Braze%20Check-up%20ff283a47e0464c49b8d9cc9517a1b571/Untitled%205.png)

![Untitled](%5BAB180%20%E1%84%91%E1%85%B5%E1%86%BA%E1%84%91%E1%85%A6%E1%86%BA%5D%20Braze%20Check-up%20ff283a47e0464c49b8d9cc9517a1b571/Untitled%206.png)

### Developer Console

- Internal Groups : 내부 인원을 Internal Group으로 지정하여 캠페인 테스트 발송 및 User Log를 확인할 수 있도록 Internal Group을 지정하는 탭
    
    ![Untitled](%5BAB180%20%E1%84%91%E1%85%B5%E1%86%BA%E1%84%91%E1%85%A6%E1%86%BA%5D%20Braze%20Check-up%20ff283a47e0464c49b8d9cc9517a1b571/Untitled%207.png)
    

- Event User Log
    - Internal Groups에 등록된 유저가 발생시킨 Event Log를 확인하는 탭으로, SDK Integration QA, API 전송 QA, 트러블슈팅, Event 수집 현황 확인
    - 유저가 발생시킨 Session 정보, Event, Attribute 변동 log등을 확인
    
    ![Untitled](%5BAB180%20%E1%84%91%E1%85%B5%E1%86%BA%E1%84%91%E1%85%A6%E1%86%BA%5D%20Braze%20Check-up%20ff283a47e0464c49b8d9cc9517a1b571/Untitled%208.png)
    

# Braze의 캠페인 작동 원리

### Campaign 발송 option 및 Targeting

**발송 옵션**

1. Scheduled Delivery
2. Action-Based Delivery
3. API-Triggered Delivery

**Targeting**

Braze SDK 및 API를 통해 수집되는 custom attributes, custom event, purchase event, 세션등의 데이터를 활용하여 Campaign 수신 대상 유저 선별

### Push 캠페인 발송 원리 ([가이드](https://www.braze.com/docs/user_guide/message_building_by_channel/push/push_registration#what-does-this-look-like-on-a-broader-scale))

- Push Token : 어떤 기기에 푸시 메세지를 발송할지 식별할 수 있는 식별자로 push service providers(APNs, FCM)에서 발급

![분홍색 : Push Token Registration Steps
하늘색 : Messaging Steps](%5BAB180%20%E1%84%91%E1%85%B5%E1%86%BA%E1%84%91%E1%85%A6%E1%86%BA%5D%20Braze%20Check-up%20ff283a47e0464c49b8d9cc9517a1b571/Untitled%209.png)

분홍색 : Push Token Registration Steps
하늘색 : Messaging Steps

### In App Message 캠페인 발송 원리

![%5BAB180%20%E1%84%91%E1%85%B5%E1%86%BA%E1%84%91%E1%85%A6%E1%86%BA%5D%20Braze%20Check-up%20ff283a47e0464c49b8d9cc9517a1b571/Untitled%2010.png](%5BAB180%20%E1%84%91%E1%85%B5%E1%86%BA%E1%84%91%E1%85%A6%E1%86%BA%5D%20Braze%20Check-up%20ff283a47e0464c49b8d9cc9517a1b571/Untitled%2010.png)

1. **IAM Payloads를 SDK가 저장**
    
    고객이 서비스를 실행하여 SDK에서 세션 시작이 감지되면, IAM 캠페인의 Target User 조건을 따라 고객이 수신할 수 있는 모든 IAM를 Payload에 담아 SDK에 저장합니다.
    
    Braze의 SDK에 저장되는 IAM Payload 에는 아래 2가지 주요한 정보가 포함됩니다.
    
    - 인앱 메시지가 노출되어야 하는 Trigger Action
    - 인앱 메시지 정보
    
    ![Untitled](%5BAB180%20%E1%84%91%E1%85%B5%E1%86%BA%E1%84%91%E1%85%A6%E1%86%BA%5D%20Braze%20Check-up%20ff283a47e0464c49b8d9cc9517a1b571/Untitled%2011.png)
    
    ```json
    /payloads 예시
    "respond_with": {
        "triggers": true,
        "in_app_message": {
          "count": 0
        },
        "config": {
          "config_time": 1671045513
        },
        "feed": true
      },
      "response": {
        "feed": [],
        "triggers": [
          {
            "type": "inapp",
            "data": {
              "message": "",
              "click_action": "URI",
              "uri": "fitpet://fitpetmall/detail/events/hecto-safe-cash",
              "use_webview": null,
              "type": "MODAL",
              "message_close": "AUTO_DISMISS",
              "duration": 15000,
              "image_url": "https://braze-images.com/appboy/communication/marketing/slide_up/slide_up_message_parameters/images/63bd1cd5e2c6e7004d4c7c2e/f35f88981cf5d5c4e6e31aaa8a7baa235fb20c31/original.png?1673338072",
              "image_style": "GRAPHIC",
              "close_btn_color": 4294967295,
              "bg_color": 4294243575,
              "frame_color": 3207803699,
              "trigger_id": "NjNiZDFjZDVlMmM2ZTcwMDRkNGM3YzQ0XyRfbXY9NjNiZDFjZDVlMmM2ZTcwMDRkNGM3YzMyJnBpPWNtcA=="
            },
            "trigger_condition": [
              {
                "data": {
                  **"event_name": "view_playmain"**
                },
                "type": "custom_event"
              }
            ],
            "start_time": 1672848000,
            "end_time": 1674140100,
            "priority": 1000076000,
            "delay": 3,
            "id": "63bd1cd5e2c6e7004d4c7c44",
            "re_eligibility": 259200
          }
    ```
    
    1. **SDK에서 Trigger Action 감지**
        - 서비스 내에서 적절한 시점에 IAM를 고객에게 노출해야하기 때문에, 고객이 서비스 내에서 어떤 행동을 수행했을 때 그를 Trigger로 하여 IAM이 노출되는 `Action-based` 만을 지원
        - IAM payloads가 불려온 동일 세션에서만 IAM 노출 가능

### 그 외 Braze 캠페인 발송 옵션

- **Allow users to become re-eligible to receive campaign**
    - Braze에서 하나의 Campaign은 1번만 수신할 수 있는 것이 default 설정 입니다.
    - re-eligibility를 on으로 설정한다면 유저가 triggered된 campaign에 다시 참여할 수 있도록 함으로써 유저가 메시지를 두번 이상 수신 할 수 있습니다.
    
    ![스크린샷 2022-12-05 오후 7.05.42.png](%5BAB180%20%E1%84%91%E1%85%B5%E1%86%BA%E1%84%91%E1%85%A6%E1%86%BA%5D%20Braze%20Check-up%20ff283a47e0464c49b8d9cc9517a1b571/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-12-05_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_7.05.42.png)
    
- **Frequency Capping**
    
    유저에게 다양한 채널로 메시지를 보내는 것도 중요하지만 캠페인을 받는 유저의 입장에서 무분별한 전송, 스팸으로 느껴지면 문제가 될 수 있습니다. 따라서 메시지 전송 빈도에 대한 관리가 필요하며 Frequency Capping 설정이 이와 같은 역할을 하고 있습니다.
    
    Frequency Capping on/off 설정을 통하여 해당 설정에 영향을 받을 캠페인과 받지 않을 캠페인을 구분할 수 있습니다.
    
    Frequency Capping 설정은 Engagement탭의 Global Message Settings 카테고리에서 진행합니다. 
    
    ![스크린샷 2022-12-05 오후 7.43.22.png](%5BAB180%20%E1%84%91%E1%85%B5%E1%86%BA%E1%84%91%E1%85%A6%E1%86%BA%5D%20Braze%20Check-up%20ff283a47e0464c49b8d9cc9517a1b571/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-12-05_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_7.43.22.png)
    

- **A/B 테스팅**
    - A/B테스트를 위해 Control Group(메시지를 수신하지 않는 비교대조군)의 비율을 설정하거나, Compose 영역에서 생성한 Variant 집단의 비율을 조정할 수 있습니다. Control Group은 하단 옵션을 통해 제거 가능합니다.
    
    ![스크린샷 2022-12-05 오후 8.25.21.png](%5BAB180%20%E1%84%91%E1%85%B5%E1%86%BA%E1%84%91%E1%85%A6%E1%86%BA%5D%20Braze%20Check-up%20ff283a47e0464c49b8d9cc9517a1b571/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-12-05_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_8.25.21.png)
    

# Braze의 캠페인 성과 확인 방법

[[Public/AB180/Braze] Braze Report](https://www.notion.so/Public-AB180-Braze-All-About-Braze-Report-7253ee66b95d4b46be00cff6fe82eb50)

# Braze User Guide 및 Developer Guide 활용

- [User Guide](https://www.braze.com/docs/user_guide/introduction)
- [Developer Guide](https://www.braze.com/docs/developer_guide/home)
- [API 문서](https://www.braze.com/docs/api/home)
- [Braze swift SDK Github](https://github.com/braze-inc/braze-swift-sdk)
- [Braze Android SDK](https://appboy.github.io/appboy-android-sdk/kdoc/index.html)

<서포트랑 확인>

- intelligent selection : a 이후에 c,d 일 경우 어떻게 수신하게 될지
- 월별 데이터 포인트 소진량 확인 필요
- 전환 이벤트 변경 가능한지 서포트랑 확인 : 캠페인명(캠페인 id) 별로 변경한 이벤트 전달하면 변경 가능할지

<테스트>

- 90일 전에 구매를 했던 유저가 구매를 한 시점에 메세지를 발송하고자하는 경우