---
layout: single

header:
  teaser: /assets/images/logo/aws.png
  overlay_image: /assets/images/logo/aws.png
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[aws] S3 Advanced (7) - Performance"
excerpt: "🚀 S3 Performance, Byte-Range Fetches, Multi-Part 성능을 높이는 방법을 알아보자"

categories: aws
tag: [aws, s3, performance, quotas, kms, acceleration]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"



---

# S3 - Baseline Performance

> S3의 기준 성능에 대해 알아보자

- S3 는 자동으로 아주 많은 수의 요청을 처리하도록 스케일링이 가능하며, 첫 바이트를 얻기까지 100-200ms<br>정도로 지연 시간이 굉장히 짧다.
- 초당 가능한 요청으로 환산하면 접두어 및 초당 3,500개의 PUT/ COPY/ POST/ DELETE 요청을 처리하며 접두어 및 초당 5,500개의 GET/ HEAD 요청을 버킷 내에서 처리하는 속도이다.
- 아주 고성능이라는 의미이다.
- 버킷 내의 접두어의 개수에는 제한이 없다.



- 예시 (object path --> prefix)
  - `file` 이라는 이름의 객체 4개를 예시로 들어 해당 객체의 접두어를 분석해보자
    1. `bucket/folder1/sub1/file` --> `/folder1/sub1/`
    2. `bucket/folder1/sub2/file` --> `/folder2/sub2/`
    3. `bucket/1/file` --> `/1/`
    4. `bucket/2/file` --> `/2/`
  - 접두어는 bucket 과 file 사이의 뭐든 될 수 있다.



첫번째 파일에 대해서 이 접두어(`/folder1/sub1/`)는 초당 3,500개의 PUT과 5,500개의 GET을 얻을 수 있다.<br>그리고 다른 파일은 `folder1/sub2` 에 있다고 하면 bucket과 file 사이의 뭐든 접두어가 될 수 있으니<br>접두어는 `/folder1/sub2` 가 된다. 이 역시 3,500개의 PUT과 5,500개의 GET을 한 접두부에 대해 얻을 수 있다.

이렇게 1과 2가 있으면 서로 접두어가 다르다. 이렇듯, 버킷 내의 접두어 및 초당 3,500개의 PUT과 5,500개의 GET을 얻는다는 규칙이 이해가 될 것이다.

다시말해, **이 4개의 접두어에 읽기 작업을 균일하게 분산시키면 초당 22,000개의 HEAD와 GET 요청을 수행하는 셈이니 성능이 아주 좋다고 볼 수 있다.**



접두어 (prefix) - 버킷이름과 파일명 사이의 모든 경로라고 이해



## 1. S3 - KMS Limitation

> S3 성능 제한인 KMS에 대해 알아보자

![image-20220813021214294](../../assets/images/posts/2022-08-11-AWS S3 advanced (7) - Performance/image-20220813021214294.png)

- 만약 SSE-KMS를 사용해 객체를 암호화 하는 경우 KMS 제한에 의해 영향을 받을 수 있다.
- 파일을 업로드하면 KMS Limitation(제한)이 우리를 대신해서 S3에서 `GenerateDateKey` KMS API를 호출
- SSE-KMS 를 통해 S3에서 파일을 다운로드 하는 경우에는 `Decrypt KMS-API` 를 호출하게 된다.
- 그리고 이 두 가지 요청은 KMS 할당량에 집계가 된다.
  - 예를 들어 유저들이 S3 버킷에 연결하고 SSE-KMS 암호화를 사용해 파일을 업로드/다운로드 하려는 상황이면, S3 버킷이 API를 호출하고 키를 생성하거나 KMS키로 해독해 그로부터 결과를 가지고 온다.
  - 그래서 KMS는 기본적으로 초당 요청에 대한 할당량을 가지고 있다.
  - Region에 따라 요청이 초당 5,500개 또는 10,000개 or 30,000개일 수도 있다.
- 이보다 많은 양의 요청이 필요한 경우에는 서비스 할당량 콘솔을 통해 할당량 증가를 요청할 수 있다.
  - 서비스 할당량 콘솔 (Service Quotas Console)
  - 즉, 서울 리전에서는 초당 5,500개의 요청을 지원하는곳인데, 10,000개의 요청이 발생하면 요청이 지나치게 많아진다.

S3 버킷을 많이 쓰는 경우를 대비해서 알아두면 좋을 지식이다.





## 2. S3 Performance

> S3 성능에 대해 알아보자

![image-20220813021620782](../../assets/images/posts/2022-08-11-AWS S3 advanced (7) - Performance/image-20220813021620782.png)

- 최적화를 위한 첫 번째 방법은 분할 업로드(Multi-Part Upload) 이다.
  - 100MB가 넘는 파일은 분할 업로드 권장
  - 5GB가 넘는다면 분할업로드 필수

분할 업로드는 병렬화를 통해 전송 속도를 높이고 대역폭을 극대화한다. S3 에 업로드할 큰 파일이 있으면 이 파일을 작은 덩어리의 여러 파트로 나눠서 각 파일을 S3에 병렬로 업로드한다. S3 에서는 모든 파트가 업로드되면 이들을 다시 모아 큰 파일로 합쳐 주게 된다.



![image-20220813021643123](../../assets/images/posts/2022-08-11-AWS S3 advanced (7) - Performance/image-20220813021643123.png)

- S3 Transfer Acceleration은 업로드/다운로드를 위한 기능? 서비스이다.
- 파일을 AWS의 Edge Location으로 파일을 전송함으로써 전송 속도를 높인다.
- 엣지 로케이션에서는 데이터를 대상 Region에 S3 버킷으로 보내준다.
- 리전보다 엣지로케이션의 수가 더 많다.
  - 200개가 넘고 계속 늘고 있다.
- 이 기능은 분할업로드(Multi-Part) 기능과 호환이 된다.



파일이 미국에 있는 상태에서 호주에 있는 S3 버킷에 이 파일을 업로드하려한다. 이 때 파일을 미국에 있는 엣지로케이션에 업로드한다. 공용 인터넷을 사용해 아주 빠르게 처리한다. 그러면 해당 엣지로케이션에서 호주의 S3 버킷으로 고속 사설 AWS 네트워크를 통해 파일이 전송된다.

Transfer Acceleration이라고 불리는 이유는 공용 인터넷을 최소한으로 거치면서 사설 AWS 네트워크 사용을 최대화 하기 때문이다. Transfer Acceleration를 사용하면 전송속도를 높일 수 있다.

그렇다면 파일을 다운받는 경우에는 어떻게 할까? 파일을 가장 효율적으로 읽는 방법은 뭘까? 아래의 S3 byte range fetches 을 이용하면 된다. 파일의 특정 바이트 범위를 얻어 GET을 마비시키는 방식이다. 바이트 범위를 얻는 데 실패한 경우에도 작은 바이트 범위를 얻는 작업을 다시 시도함으로써 실패에 대한 복원성을 가지게 된다.

이 방법은 다운로드 속도를 높이는 데에 사용된다.



## 3. S3 Performance - S3 Byte-Range Fetches

![image-20220813022710542](../../assets/images/posts/2022-08-11-AWS S3 advanced (7) - Performance/image-20220813022710542.png)

- 특정 byte 범위 요청을 통한 병렬 GET요청
- 바이트 범위를 얻는 데 실패한 경우에도 작은 바이트 범위를 얻는 작업을 다시 시도함으로써 실패에 대한 복원성을 가지게 된다.
- 이 방식은 다운로드의 속도를 높이는 데에 사용된다.



S3 에 아주 큰 파일이 있고, 파일의 첫 몇 바이트에 해당하는 Part1 을 요청한다. 그리고 두번째 파트에 이어 마지막 파트까지 있을 것이다. 이 모든 파트들을 특정 Byte Range Fetches 기능을 요청한다. 바이트 범위라고 불리는 건 파일의 특정 범위만을 요청할 것이기 때문이다. 그리고 이 요청은 전부 **병렬**적으로 이루어진다. 즉 GET 를 병렬화해서 다운로드를 가속화시키는 원리이다.

<br><br>

두 번째 사용 사례는 파일의 일부를 회수하는 경우이다.

만약 S3에 있는 파일의 첫 50바이트가 파일에 대한 정보를 제공하는 헤더라는 사실을 알고 있다면 헤더 요청을 바로 보낸다. 헤더에 해당하는 첫 50바이트를 바이트 범위 요청으로 전송함으로써 해당 정보를 빠르게 얻을 수 있을 것이다.



## Summary

> 이번 포스팅에서는 S3 성능과 업로드/다운로드 가속화 방법 및 기준 성능과 KMS 제한에 대해 알아보았다.

- 기준 성능
  - prefix 당 3,500개 PUT, 5,500개 GET
- KMS Limitation
  - SSE-KMS 암호화 사용하면 KMS 집계에 할당됨
  - 리전에 따라 요청수가 다름
  - 요청수가 부족하면 서비스 할당량 콘솔 이용해서 늘리기
- 성능
  - 분할 업로드
    - 100MB 이상 권장
    - 5GB 이상 필수
  - 전송 가속화 (transfer Accelerate)
    - 미국 --> 엣지 로케이션 --> 호주버킷
- 바이트 범위 요청
  - 큰 파일을 병렬 GET요청으로 부분적으로 다운받음
  - 첫 부분 헤더만 가져옴

