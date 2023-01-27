# buffer_pool_size
> - 버퍼풀은 mySQL 의 Storage Engine 인 InnoDB 가 액세스할 때 테이블 및 인덱스 데이터를 캐시하는 메인 메모리 영역
> - 버퍼풀은 자주 사용하는 데이터를 메모리에서 직접 처리할 수 있게하여 처리속도를 높인다.
> - 전용 서버에서 실제 메모리의 최대 75% 정도가 버퍼풀에 할당된다.
> - 버퍼 풀을 활용하여 자주 액세스하는 데이터를 메모리에 유지하는 노하우(기술)은 MySQL 튜닝의 중요한 측면

## 01. 버퍼 풀의 크기 (innodb_buffer_pool_size)

버퍼 풀은 두 가지 역할을 담당한다.
- 데이터 파일과 로그 파일이 기록되는 순서를 조정하는 역할
- 디스크 액세스를 줄이기 위한 캐시의 역할
시스템(OS)에서 파일 캐시의 크기가 클수록 성능에 유리하듯이, Database 에서도 마찬가지로 버퍼 풀의 크기가 클수록 성능에 유리하다.

특히 조회 처리를 위한 캐시 효과가 크기 마련인데, 이는 읽으려는 데이터가 메모리에 올라와 있으므로 Disk I/O 를 발생시키지 않기 때문이다.이론적으로는 다른 버퍼에 할당하는 메모리를 제외하고는 대부분의 메모리를 버퍼 풀에 할당하는 것이 좋다.

인덱스 설계가 잘 되어 있는데도 슬로우 쿼리가 해결되지 않는다면? innodb_buffer_pool_size 파라메터를 의심해봐야 한다. (이름이 의미하듯이 InnoDB 스토리지 엔진에만 해당한다.) 해당 파라메터의 크기가 클수록 쿼리 실행시 디스크보다 메모리를 사용하게 되어 빠른 결과를 얻을 수 있다.

버퍼 풀 메모리가 충분히 큰 양으로 할당되어 있다면 innodb는 in-memory 데이터베이스처럼 동작한다.

Access를 위한 select 데이터 뿐 아니라, Insert 및 Update 작업에도 도움이 되는 캐싱을 하기 때문에 적절하게 조정하여 사용하는 것이 핵심이다.

버퍼 풀 메모리는 내부적으로 LRU 알고리즘을 사용하는 리스트의 형태이다.

> innodb_buffer_pool_size = innodb_buffer_pool_instance * innodb_buffer_pool_chunk_size

1048576B = 1024KB = 1MB

- InnoDB 버퍼풀 크기 온라인 설정
  - SET 문을 사용하여 innodb_buffer_pool_size 구성 옵션을 동적으로 설정하여 서버를 다시 시작하지 않고도 버퍼 풀의 크기를 조정할 수 있습니다. 예를 들면 다음과 같습니다.
  - `mysql >> SET GLOBAL innodb_buffer_pool_size=402653184;`



- **AWS RDS 8XL (32vCPU, 256GB 기준)**

```mysql
SHOW VARIABLES;

SELECT @@innodb_buffer_pool_size/1024/1024/1024 as 'innodb_buffer_pool_size(GB)'
	, @@innodb_buffer_pool_chunk_size/1024/1024/1024 as 'innodb_buffer_pool_chunk_size(GB)'
	, @@innodb_buffer_pool_instances as innodb_buffer_pool_instances;
```

| innodb_buffer_pool_size(GB) | innodb_buffer_pool_chunk_size(GB) | innodb_buffer_pool_instances |
| --------------------------- | --------------------------------- | ---------------------------- |
| 183.129                     | 5.722                             | 32                           |





# 참고 블로그
  - [블로그1](https://omty.tistory.com/65)
  - [블로그2](https://owlyr.tistory.com/23)
  - [블로그3](https://myinfrabox.tistory.com/50)