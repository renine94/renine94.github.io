--------- Forwarded message ---------
보낸사람: Amazon Web Services <no-reply-aws@amazon.com>
Date: 2023년 1월 11일 (수) 오후 9:43
Subject: RE:[CASE 11735180201] 현재 사용하고 있는 RDS의 올바른 인스턴스 크기를 잘 모르겠습니다.
To: <dev@fitpet.co.kr>
Cc: <yongyeon.kim@fitpet.co.kr>, <jh.baek@fitpet.co.kr>, <jaeho.lee@fitpet.co.kr>


안녕하세요, Anton님

AWS Support에 문의해주셔서 감사합니다.
저는 고객님의 케이스를 담당하게 된 AWS Cloud Support Engineer 최진오입니다.

문의하신 내용을 제가 다음과 같이 정리하였습니다.
Aurora MySQL 클러스터 'fitpetmall-prod-db' 를 사용하시면서 메모리 사용량이 많은 것에 대해 문의하셨습니다.
또한 비용 문제를 고민하고 계셔 적정한 크기의 인스턴스 추천과 베스트 프랙티스에 대해 문의하셨습니다.
혹시 제가 고객님의 문의 사항을 잘못 이해한 부분이 있다면 정정해주시기를 바랍니다.

1. 첫 번째로 메모리 사용량에 대해서 확인해보겠습니다.
우선 사용하시는 인스턴스 db.r5.8xlarge 인스턴스의 HW 사양을 살펴보면 vCPU는 32개이고 256GiB(274.878GB) 메모리이며, 최대 세션 수는 5000개까지 사용이 가능합니다. [1][2]

그리고 각 인스턴스의 메모리 사용량을 살펴보겠습니다.
Aurora MySQL는 MySQL 기반으로 동작하기 때문에 MySQL의 메모리 사용방식과 동일하며, default 파라미터를 사용할 때 인스턴스 메모리의 80~90%가 할당됩니다. [2]
즉, 다음과 같이 메모리 사용량을 대략적으로 계산할 수 있습니다.
Maximum MySQL Memory Usage = innodb_buffer_pool_size + key_buffer_size + ((read_buffer_size + read_rnd_buffer_size + sort_buffer_size + join_buffer_size) X max_connections)

CloudWatch 상으로는 2주간의 데이터를 봤을 때 writer 인스턴스인 'application-autoscaling-ffe49211-5bb2-4c79-8612-9637ffcb503f'의 CPUUtilization은 최대 10.242%, 38638~39369MB 사이의 FreeableMemory를 나타내고 있으며, DatabaseConnections 수는 10~20대를 유지하고 있으나 최고 132까지 증가한 것을 확인하였습니다.
Reader 인스턴스 'application-autoscaling-ec12bee2-c56f-4ea7-aec9-2e3796c86850'의 CPUUtilization은 19.956%, 43332~43646MB 사이의 FreeableMemory를 유지하고 있으며, DatabaseConnections 수는 60~120을 유지하나 최대 432까지 증가한 것을 관찰할 수 있습니다.

* CloudWatch
https://ap-northeast-2.console.aws.amazon.com/cloudwatch/home?region=ap-northeast-2#metricsV2:graph=~(metrics~(~(~'AWS*2fRDS~'DatabaseConnections~'DBInstanceIdentifier~'application-autoscaling-ffe49211-5bb2-4c79-8612-9637ffcb503f~(label~'Writer*20DatabaseConnections))~(~'...~'application-autoscaling-ec12bee2-c56f-4ea7-aec9-2e3796c86850~(label~'Reader*20DatabaseConnections))~(~'.~'FreeableMemory~'.~'application-autoscaling-ffe49211-5bb2-4c79-8612-9637ffcb503f~(yAxis~'right~label~'Writer*20FreeableMemory))~(~'...~'application-autoscaling-ec12bee2-c56f-4ea7-aec9-2e3796c86850~(yAxis~'right~label~'Reader*20FreeableMemory))~(~'.~'CPUUtilization~'.~'.~(label~'Reader*20CPUUtilization~visible~false))~(~'...~'application-autoscaling-ffe49211-5bb2-4c79-8612-9637ffcb503f~(label~'Writer*20CPUUtilization~visible~false)))~view~'timeSeries~stacked~false~region~'ap-northeast-2~start~'-PT336H~end~'P0D~stat~'Average~period~60);query=~'*7bAWS*2fRDS*2cDBInstanceIdentifier*7d*20application-autoscaling-ffe49211-5bb2-4c79-8612-9637ffcb503f

즉, FreeableMemory를 제외하고 사용하는 메모리를 계산하면, Writer는 242837~242106MB / Reader는 238143~237829MB 로 추정되며, 이는 인스턴스 메모리의 약 80~90% 로 확인됩니다.

EM(Enhanced Monitoring) 상의 메모리 사용량을 살펴보기 전에 OS의 large page에 대해 설명을 드리겠습니다.
보통의 리눅스 OS는 page 단위(usually 4kb)로 메모리를 할당하나, mysql의 innodb와 관련한 메모리는 좀 더 큰 page 사이즈를 할당할 수 있는 large page(huge page) 기능을 사용하게 됩니다. [4]
관련 메모리 innodb buffer pool은 innodb_buffer_pool_size를 통해 지정되며, Aurora MySQL에서는 사용하는 인스턴스 메모리의 3/4를 할당하게 됩니다. [2]

EM에서 확인되는 huge page 크기는 Huge Pages Total*Huge Pages Size(KB)로 계산하며 192626MB가 할당되어 있습니다.
innodb buffer pool은 huge page를 사용하기 때문에, innodb_buffer_pool_size인 196608MB 와 huge page 크기가 유사한 것을 확인할 수 있습니다.

11 Jan 2023 09:19:43 UTC 기준의 'application-autoscaling-ffe49211-5bb2-4c79-8612-9637ffcb503f' writer 인스턴스의 EM OS memory 지표를 보면 다음과 같습니다. [5]
Active (KB)\t29169368
Free (KB)\t30377684
Buffers (KB)\t371468
Cached (KB)\t11530860
Dirty (KB)\t888
Inactive (KB)\t1933592
Slab (KB)\t1909528
Mapped (KB)\t434408
Writeback (KB)\t0
Huge Pages Size (KB)\t2048
Huge Pages Total\t96313

위에서 지표들을 Aurora MySQL이 사용하는 메모리와 정확히 매칭시킬 수 없지만, 대략 계산하면 CloudWatch에서 확인한 메모리 사용량과 유사한 것을 알 수가 있습니다.

2. 두 번째로 적정한 크기의 인스턴스 추천과 베스트 프랙티스에 대해 확인해보겠습니다.
Aurora MySQL는 EBS 볼륨을 사용하지 않고 단일 가상 볼륨인 클러스터 볼륨을 사용하기 때문에 스토리지 IOPS는 고려하지 않으셔도 됩니다.
즉, Auora MySQL의 성능은 (쿼리 성능을 고려하지 않는다면) 사용하는 인스턴스의 하드웨어(vCPU/memory/Max. bandwidth/Network performance)를 바탕으로 결정됩니다.

앞서 확인한 각 인스턴스들이 사용 중인 CPUUtiliazation과 DatabaseConnections 수 등을 고려하여, 서비스가 가능한 수준의 인스턴스로 교체해볼 수 있습니다.
예를 들어 한 인스턴스 당 최대 1000~2000명의 사용자 수를 추측하신다면 db.r5.large/db.r5.xlarge가 적합하나, vCPU가 2/4이기 때문에 CPU 사용량이 높아질 수 있습니다.
인스턴스 변경 이후에 실제 CPU 사용량이 얼마나 높아지는지는 직접 검증하셔야 하며, 필요하다면 SQL 최적화를 통해 리소스 사용량을 줄이는 것이 필요합니다.

또한 주기적으로 이벤트를 통해 스파이크성 트래픽이 들어오는 서비스라면, 해당 기간에 reader를 수동으로 추가하거나 혹은 Aurora Auto Scaling 기능을 통해 reader 인스턴스를 자동으로 늘려 트래픽을 대비할 수 있습니다. [6]

Aurora 사용간 베스트 프랙티스는 저희 공식 문서에 나온 모범 사례를 참조하는 것을 추천합니다. [+]


참조 문서:
[1] Aurora DB 인스턴스 클래스 - Aurora에 대한 DB 인스턴스 클래스의 하드웨어 사양 - https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html#Concepts.DBInstanceClass.Summary
[2] Amazon Aurora MySQL에 대한 성능 및 조정 관리 - Aurora MySQL DB 인스턴스에 대한 최대 연결 - https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Performance.html#AuroraMySQL.Managing.MaxConnections
[3] https://aws.amazon.com/ko/premiumsupport/knowledge-center/low-freeable-memory-rds-mysql-mariadb/?nc1=h_ls
[4] https://dev.mysql.com/doc/refman/8.0/en/large-page-support.html
[5] 향상된 모니터링의 OS 지표 - https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/AuroraUserGuide/USER_Monitoring-Available-OS-Metrics.html
[6] Aurora 복제본에 Amazon Aurora Auto Scaling 사용 - https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html
[7] Amazon Aurora MySQL 모범 사례 - https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.html


제공한 내용이 도움이 되었기를 바라며, 해당 이슈에 대해 궁금하신 내용이 더 있으면 언제든 편하게 연락해주시기를 바랍니다.

감사합니다.

We value your feedback. Please share your experience by rating this and other correspondences in the AWS Support Center. You can rate a correspondence by selecting the stars in the top right corner of the correspondence.

Best regards,
Jinoh C.
Amazon Web Services

===============================================================
To share your experience or contact us again about this case, please return to the AWS Support Center using the following URL: https://console.aws.amazon.com/support/home#/case/?displayId=11735180201&language=en

Note, this e-mail was sent from an address that cannot accept incoming e-mails. To respond to this case, please follow the link above to respond from your AWS Support Center.

===============================================================

Don’t miss messages from AWS Support when you need help! Update your contact information:
https://console.aws.amazon.com/billing/home#/account

If you receive an error message when visiting the contact information page, visit:
https://aws.amazon.com/premiumsupport/knowledge-center/iam-billing-access/

AWS Support:
https://aws.amazon.com/premiumsupport/knowledge-center/

AWS Documentation:
https://docs.aws.amazon.com/

AWS Cost Management:
https://aws.amazon.com/aws-cost-management/

AWS Training:
http://aws.amazon.com/training/

AWS Managed Services:
https://aws.amazon.com/managed-services/