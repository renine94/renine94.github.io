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

title: "[aws] All Storage Services Summary & Quiz"
excerpt: "🚀 Storage, S3, Glacier, EFS, FSx, EBS, Instance Store, Storage Gateway, Snowball, Database"

categories: aws
tag: [aws, storage, s3, quiz, summary, fsx]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# Storage Comparison

> AWS 에서 제공하는 Storage Services 들의 특징을 비교해보자

1. **S3**: Object Storage
   - 객체 스토리이지며, 서버리스
   - 용량을 미리 프로비저닝 할 필요 없다.
   - 많은 데이터베이스 서비스와 긴밀하게 통합됨
2. **Glacier**: Object Archival
   - 객체 아카이브를 위한 곳
   - 객체를 오래동안 저장하고 싶고 회수할 일은 매우 드물 때 사용
   - 객체를 회수할때는 다시 가져오기까지 많은 시간이 걸린다. (객체가 아카이브 되기 때문)
3. **EFS**: Network File System for Linux instances, POSIX file system
   - 일래스틱 파일 시스템으로 Linux 인스턴스용의 네트워크 파일 시스템
   - POSIX 파일시스템이니 다시 Linux용이라는 말
   - 모든 EC2 인스턴스에서 동시에 액세스 가능하며, AZ 전반에 걸쳐 공유됨
4. **FSx for Windows**: Network File System for Windows servers
   - EFS 와 같지만 Window를 위한 것
   - Window 서버를 위한 네트워크 파일 시스템이다.
5. **FSx for Lustre**: High Performance Computing Linux file system
   - Linux와 클러스터로 고성능 컴퓨팅이 가능한 Linux 파일 시스템
   - HPC가 실행된다. 상상 이상으로 IOPS가 높고 용량도 엄청나다.
   - 백엔드에서 S3와 통합된다.
6. **EBS volumes**: Network storage for one EC2 instance at a time
   - 네트워크 스토리지로 한 번에 EC2 인스턴스 하나만 액세스 된다.
   - 생성된 특정 가용 영역 내부에 바인딩 된다.
   - AZ를 변경하고 싶다면 스냅샷을 생성해서 해당 스냅샷을 이동시키고 거기에서 볼륨을 만들어야 한다.
7. **Instance Storage**: Physical storage for your EC2 instance (high IOPS)
   - EC2 인스턴스의 물리적 스토리지이다.
   - 하드웨어에 연결되어 있기 때문에 EBS보다 훨씬 높은 IOPS를 가진다.
   - EBS볼륨은 최대 16,000 IOPS, io1 에선 최대 64,000 IOPS 
   - EC2 인스턴스와 물리적으로 연결되기 때문에 수백만 IOPS도 가능해 매우 높다.
   - 인스턴스가 중단되면 해당 스토리지가 영구적으로 손실된 위험이 있다.
8. **Storage Gateway**: File Gateway, Volume Gateway (cache & stored), Tape Gateway
   - 온프레미스에서 AWS로 파일을 전송
   - 여기엔 FileGateway, 캐시 및 저장을 위한 VolumeGateway, TypeGateway가 있다.
   - 각각 사용 사례가 다르다.
9. **Snowball / Snowmobile**: to move large amount of data to the cloud, physically
   - 대용량 데이터를 S3의 클라우드로 물리적으로 옮깁니다.
10. **Database**: for specific workloads, usually with indexing and querying
    - 데이터를 저장하는 방법
    - 보다 특정한 워크로드에 사용된다.
    - 일반적으로 인덱싱 및 쿼리와 함께 사용된다.





# Storage Quiz

1. 수백 TB의 데이터를 Amazon S3로 이전한 후, EC2 인스턴스 플릿을 사용해 처리해야 합니다. 광대역은 1Gbit/초입니다. 여러분은 데이터를 더 빠르게 이전하고, 가능하면 전송 중에 데이터를 처리했으면 합니다. 어떤 방법을 추천할 수 있을까요?
   - 자체 네트워크 사용하기
   - Snowcone 사용하기
   - AWS 데이터 이전 사용하기
   - <span style="color: red;">Snowball Edge 사용하기</span>
     - Snowball Edge는 컴퓨팅 능력을 갖추고 있으며, 데이터가 Snowball로 이동하는 동안 데이터를 사전에 처리할 수 있도록 해주므로 정답입니다.
2. 테이프 백업에 가상 인피니트 스토리지를 노출하려고 합니다. 여러분은 사용 중인 것과 동일한 소프트웨어를 유지하고, iSCSI와 호환 가능한 인터페이스를 사용하려 합니다. 어떤 방법을 사용해야 할까요?
   - AWS Snowball
   - AWS Storage Gateway - Tape
   - <span style="color: red;">AWS Storage Gateway - Volume</span>
   - AWS Storage Gateway - File
3. 여러분의 EC2 Windows 서버는 Windows의 보안 메커니즘을 준수하며, Microsoft Active Directory와 통합된 네트워크 파일 시스템을 마운트하여 일부 데이터를 공유해야 합니다. 어떤 방법을 추천할 수 있을까요?
   - <span style="color: red;">Window용 Amazon FSx(File Server)</span>
   - Amazon EFS
   - Lustre용 Amazon FSx
   - 파일 게이트웨이를 지닌 Amazon S3
4. 여러분은 수백 TB의 데이터를 AWS S3로 최대한 빨리 이전시켜야 합니다. 여러분의 네트워크 대역폭을 사용해보려 했으나, 업로드 프로세스가 완료되기까지 약 3주가 소요됩니다. 이런 경우 어떤 접근법이 권장될까요?
   - AWS Storage Gateway
   - S3 멀티파트 업로드
   - <span style="color: red;">AWS Snowball 엣지</span>
   - AWS 데이터 이전 서비스
5. S3에 대규모의 데이터셋이 저장되어 있습니다. 여러분은 NFS, 혹은 SMB 프로토콜을 사용해 온프레미스 서버를 통해 이 데이터셋에 액세스하려 합니다. 또한, 온프레미스 Microsoft AD를 통해 이러한 파일에 대한 액세스를 인증하고자 합니다. 무엇을 사용해야 할까요?
   - AWS Storage Gateway - Volume
   - <span style="color: red;">AWS Storage Gateway - File</span>
   - AWS Storage Gateway - Type
   - AWS 데이터 이전 서비스
6. 기업의 인프라를 온프레미스에서 AWS Cloud로 이전시킬 계획을 가지고 있습니다. 여러분은 이전시키려는 온프레미스 Microsoft Windows 파일 서버를 갖고 있습니다. 어떤 AWS 서비스를 사용하는 것이 가장 적절할까요?
   - <span style="color: red;">Window용 Amazon FSx(파일 서버)</span>
   - AWS Storage Gateway - 파일 게이트웨이
   - AWS가 관리하는 Microsoft AD
7. 고성능 컴퓨팅(HPC)과 전산 유전학 연구를 수행하기 위해 IOPS를 최대화해 줄 분산 POSIX 준수 파일 시스템이 필요한 상황입니다. 이 파일 시스템은 수백만 개의 IOPS로 손쉽게 스케일링할 수 있어야 합니다. 어떤 방법을 추천할 수 있을까요?
   - Max를 가진 EFS IO 활성화
   - <span style="color: red;">Lustre용 Amazon FSxLustre용 Amazon FSx</span>
   - EC2 인스턴스 상에 마운팅된 Amazon S3
   - EC2 인스턴스 스토어
8. FSx 파일 시스템에 있는 다음 배포 옵션 중에서 AZ 내에 복사된 장기 스토리지를 제공하는 것은 무엇인가요?
   - 스크래치 파일 시스템
   - <span style="color: red;">영구 파일 시스템</span>
     - 이는 데이터가 동일한 AZ 내에서 복제되는 장기 스토리지를 제공합니다. 실패한 파일들은 수 분 내로 교체됩니다.
9. 다음 중 AWS 전송 제품군이 지원하지 "않는" 프로토콜은 무엇인가요?
   - 파일 전송 프로토콜 (FTP)
   - SSL을 통한 파일 전송 프로토콜 (FTP)
   - <span style="color: red;">전송층 보안 (TLS)</span>
     - AWS 전송 제품군은 FTP 프로토콜을 사용해 S3, 혹은 EFS 내부/외부로 파일을 전송하는 관리 서비스입니다. 따라서 TLS를 지원하지 않습니다.
   - qhdks vkdlf wjsthd vmfhxhzhf (FTP)





