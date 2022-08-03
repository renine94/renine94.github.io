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

title: "[aws] CLI SDK IAM role policy (2) - EC2 Metadata"
excerpt: "🚀 EC2 Metadata, 169.254.169.254"

categories: aws
tag: [aws, cli, sdk, iam, metadata]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# AWS EC2 Instance Metadata

- 개발자들에게 아직 잘 알려지지는 않았지만, 매우 강력하며 좋은 기능이다.
- 이 기능은 EC2 인스턴스가 스스로 학습하도록 해서 그 목적으로 IAM 역할이 필요하지 않습니다.
- URL 은 `http://169.254.169.254/latest/meta-data` 이다.
  - 해당 아이피는 AWS의 내부 IP로 내컴퓨터에서는 접속이안되고, EC2 인스턴스에서만 실행됩니다.
- 메타데이터로부터 IAM Role 을 검색할수는 있지만, IAM policy 는 검색할 수 없다.
- Metadata = EC2 인스턴스에 관한 정보
- Userdata = EC2 인스턴스가 시작할때의 launch script 이다.



```shell
[ec2-user@ip-192.xxx.xxx.xxx]$ curl http://169.254.169.254
# 1.0
# 2007-01-19
# 2007-03-01
# ...
# 2018-03-28
# latest
[ec2-user@ip-192.xxx.xxx.xxx]$ curl http://169.254.169.254/latest/
# dynamic
# meta-data
# user-data
[ec2-user@ip-192.xxx.xxx.xxx]$ curl http://169.254.169.254/latest/meta-data/
# ami-id
# ami-launch-index
# ami-manifest-path
# hostname
# iam/
# instance-id
# ...
# security-groups
# services
[ec2-user@ip-192.xxx.xxx.xxx]$ curl http://169.254.169.254/latest/meta-data/instance-id
# i-05adcce6993809eda
[ec2-user@ip-192.xxx.xxx.xxx]$ curl http://169.254.169.254/latest/meta-data/local-ipv4
# 172.31.3.136

```



위의 코드에서 볼 수 있듯이, EC2 인스턴스 내에 직접 접속해서 (http://169.254.169.254/latest/meta-data)[http://169.254.169.254/latest/meta-data]  로 curl 요청을 보내면 해당 EC2 인스턴스의 다양한 설정들을 가져올 수 있고, 이것을 기반으로 많은 것들을 자동화 할 수 있게 된다.