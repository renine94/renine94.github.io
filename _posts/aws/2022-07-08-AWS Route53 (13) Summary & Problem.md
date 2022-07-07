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

title: "[aws] Route53 (13) - Summary & Problem"
excerpt: "🚀 Route53, Summary, Problem"

categories: aws
tag: [aws, route, summary, problem]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# Route53 정리 및 문제



1. 여러분은 Amazon Route 53 Registrar를 위해 mycoolcompany.com를 구매했으며, 이 도메인이 Elastic Load Balancer인 my-elb-1234567890.us-west-2.elb.amazonaws.com를 가리키게끔 하려 합니다. 이런 경우, 다음 중 어떤 Route 53 레코드 유형을 사용해야 할까요?

   - <i style="color: red;">Alias Records</i>

     

2. 새로운 Elastic Beanstalk 환경을 배포한 상태에서, 5%의 프로덕션 트래픽을 이 새로운 환경으로 다이렉트하려 합니다. 이를 통해 CloudWatch 지표를 모니터링하여, 새로운 환경에 있는 버그를 제거할 수 있게 됩니다. 이런 작업을 위해서는 다음 중 어떤 Route 53 레코드 유형을 사용해야 할까요?

   - <i style="color: red;">Weighted Records</i> - 가중치 기반

3. Route 53 레코드의 myapp.mydomain.com 값이 새로운 Elastic Load Balancer를 가리키도록 업데이트를 했는데도 불구하고, 사용자들은 여전히 기존의 ELB로 리다이렉트 되고 있는 상태입니다. 이런 경우, 가능성이 있는 원인은 무엇일까요?

   - <i style="color: red;">TTL</i>
   - 각 DNS 레코드는 클라이언트들이 이러한 값들을 캐시할 기간을 지정하고 DNS 요청으로 DNS 리졸버에 과부하를 일으키지 않도록 지시하는 TTL(타임 투 리브)을 갖습니다. TTL 값은 값을 캐시해야 하는 기간과 DNS 리졸버로 들어가야 하는 요청의 수 사이의 균형을 유지할 수 있도록 설정되어야 합니다.
     

4. 두 AWS 리전, `us-west-1` 및 `eu-west-2`에 호스팅 된 애플리케이션이 있습니다. 애플리케이션 서버의 사용자에 대한 응답 시간을 최소화하여, 사용자들에게 최상의 사용자 경험을 제공하려 합니다. 이 경우, 다음 중 어떤 Route 53 라우팅 정책을 사용해야 할까요?

   - <i style="color: red;">Latency Records</i> - 지연시간 레코드
   - 지연 시간 라우팅 정책은 사용자와 AWS 리전 사이에서 발생하는 지연 시간을 평가하여 지연 시간(예: 응답 시간)을 최소화할 수 있는 DNS 응답을 수신할 수 있게 해줍니다.
     

5. 프랑스를 제외한 국가에 있는 사람들이 여러분의 웹사이트로 액세스해서는 안 된다는 법적 요구 사항이 있습니다.<br>이 경우, 다음 중 어떤 Route 53 라우팅 정책을 사용해야 할까요?

   - <i style="color: red;">Geolocation Records</i> - 지리적위치 레코드

6. GoDaddy 에서 도메인을 구입하고, Route53 을 DNS서비스로 사용하려고 한다.<br>이를 위해서는 어떤 작업을 해야 하는가?

   - <i style="color: red;">공용 호스팅 영역을 생성하고, GoDaddy NS records를 업데이트 시킨다.</i>

7. 다음 중 유효하지 않은 Route53 Health Check를 고르시오.

   - <i style="color: red;">SQS 대기열을 모니터링하는 Health Check</i>
   - Endpoint 를 모니터링하는 Health Check
   - 다른 Health Check를 모니터링하는 Health Check
   - CloudWatch 경보를 모니터링하는 Health Check

