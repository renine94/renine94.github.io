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

title: "[aws] EC2 ELB - CLB & ALB"
excerpt: "🚀 Classic/Application Load Balancer"

categories: aws
tag: [aws, elb, clb, alb]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# Classic Load Balancers (v1)

---

> CLB 현재는 잘 사용되지 않는 로드밸런서로 2022년 8월 15일에 서비스 종료예정이다.

![image-20220608110656992](../../assets/images/posts/2022-06-08-AWS ELB (2) - CLB/image-20220608110656992.png)

이 로드밸런서는 TCP나 트래픽 아니면 HTTP와 HTTPS를 지원합니다.<br>**TCP는 4계층, HTTP/HTTPS 는 7계층**이며,<br>상태 확인(health check)은 TCP 또는 HTTP 기반으로 이루어집니다.<br>로드 밸런서, 즉 클래식 로드 밸런서로부터 고정 호스트 이름을 부여받습니다.<br>클라이언트가 HTTP 리스너를 통해 클래식 로드 밸런서에 연결된다.<br>내부에서는 CLB가 트래픽을 EC2 인스턴스로 다시 전송하게 된다.
{: .notice--success}

- 클라이언트(사용자)가 직접 EC2 에 바로 접근하는것보다 ELB 를 통해 접근하도록 보안그룹을 설정해야한다.
- EC2 의 보안그룹을 source ELB보안그룹으로부터 오는 트래픽만 허용하도록 설정한다.
- CLB 에 여러 대의 EC2 인스턴스를 등록하게되면 CLB 로 요청보낼 때 각각의 EC2 들로 트래픽을 분산

<br><br>

# Application Load Balancer (v2)

---

> ALB 는 마이크로 서비스(MSA) 또는 컨테이너 기반 애플리케이션(ECS, EKS) 에 가장 좋은 로드밸런서이다.
>
> 이후 다루게 될 도커와 Amazon ECS 의 경우 ALB 가 가장 적합한 로드 밸런서
>
> 왜냐하면 포트 매핑 기능이 있어 ECS 인스턴스의 동적 포트로서 리다이렉션을 가능하게 해주기 때문

- ALB 는 7계층, 즉 HTTP 전용 로드 밸런서
- 머신 간 다수 HTTP 애플리케이션의 라우팅에 사용이 된다.
  - 이러한 머신들은 Target Group(대상 그룹) 이라는 그룹으로 묶이게 된다.
- 동일 EC2 인스턴스 상의 여러 애플리케이션에 부하를 분산한다.
  - 컨테이너와 ECS 를 사용하게 된다.
- HTTP/2 와 WebSocket 을 지원
- 리다이렉트를 지원한다. (HTTP => HTTPS 할 경우 로드 밸런서 레벨에서 가능하다는 의미)



![image-20220608114730032](../../assets/images/posts/2022-06-08-AWS ELB (2) - CLB/image-20220608114730032.png)

- **경로 라우팅도 지원한다.**
  - 대상 그룹(Target Group)에 따른 라우팅
  - URL path에 기반한 라우팅을 가능
    -  example.com**/users** & exampe.com**/posts**
    - **서로 다른경로 이므로, 서로다른 Target Group에 Redirect 할 수 있게 한다.**
  - URL 호스트 이름에 기반한 라우팅도 가능
    - **one.example.com** & **other.example.com**
    - 로드밸런서가 위 2개 주소에 접근가능하다고 하면 두 개의 서로 다른 대상 그룹에 라우팅 가능
  - 쿼리 문자열과 헤더에 기반한 라우팅도 가능
    - example.com/users**?id=123&order=false** 
    - example.com 과 example.com/users**?id=123&order=false**
    - 위의 두 주소가 서로 다른 대상 그룹에 라우팅이 될 수있음을 의미한다.
- ALB 는 여러 Target Group 으로 라우팅할 수 있으며, Health Check는 Target Group 레벨에서 이뤄진다.

<br><br>

![image-20220608115847870](../../assets/images/posts/2022-06-08-AWS ELB (2) - CLB/image-20220608115847870.png)

## Target Group (대상 그룹)

> - EC2 인스턴스가 대상 그룹이 될 수 있다.
> - 이후에 다루게 될 ASG (오토 스케일링 그룹)에 의해 관리될 수 있다.
> - ECS 의 작업도 될 수가 있다. (ECS 때 다룰 예정)
> - 람다 함수도 될 수도 있지만, 잘 알려진 내용이 아니다.
>   - 람다(Lambda) 함수 앞에도 ALB 가 있을 수 있다.
> - IP Addresses (muse be private IPs)



## ALB - Good to Know

> ALB 에 대해 알아두면 좋을 내용

![image-20220608120358896](../../assets/images/posts/2022-06-08-AWS ELB (2) - CLB/image-20220608120358896.png)

- 고정된 호스트 이름이 부여된다. (CLB 와 동일)
- 애플리케이션 서버는 클라이언트의 IP를 직접 보지 못하며, client의 실제  ip는 `X-Forwarded-For` 헤더에 있다.
- 클라리언트의 IP인 12.34.56.78가 로드 밸런서와 직접 통신해 연결 종료라는 기능을 수행한다.
- 로드 밸런서가 EC2 인스턴스와 통신할 때는 사설IP 인 로드밸런서 IP를 사용해 EC2 인스턴스로 들어가게 된다.
- EC2 인스턴스가 클라리언트IP를 알기 위해서는 HTTP요청 헤더에 있는<br>`X-Forwarded-Port` 와 `X-Forwarded-Proto` 를 확인해야 한다.





### 실습

![image-20220608121010020](../../assets/images/posts/2022-06-08-AWS ELB (2) - CLB/image-20220608121010020.png)

- **internet-facing : 인터넷 경계 체계 (애플리케이션에 공공으로 액세스하기 때문에 사용)**
- internal : 개인 트래픽용



![image-20220608121329125](../../assets/images/posts/2022-06-08-AWS ELB (2) - CLB/image-20220608121329125.png)

- 네트워크 매핑에서는 실행할 VPC 를 지정
- 서브넷 개수와 실행할 AZ 도 지정
- 4개의 서브넷을 모두 선택 `ap-northest-2a ~ ap-northest-2d`
- 자동으로 올바른 서브넷에 할당된다.



![image-20220608121522281](../../assets/images/posts/2022-06-08-AWS ELB (2) - CLB/image-20220608121522281.png)

- 보안그룹도 설정해야 한다.



- **리스너와 라우팅을 지정해야 한다.**
  - 타겟 그룹이 있어야 한다. (없으면 생성)
  - **라우팅 규칙을 지정해야 한다.**
    - ![alb routing rule](../../assets/images/posts/2022-06-08-AWS ELB (2) - CLB/alb_real_auth_1-1024x411.png)





