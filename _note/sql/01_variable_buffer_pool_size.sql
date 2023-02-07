-- DB 환경변수 확인하기 (파라미터 그룹으로 설정가능)
SHOW VARIABLES ;

-- buffer_pool_size 확인하기 (GB 단위로)
SELECT @@innodb_buffer_pool_size/1024/1024/1024 as 'innodb_buffer_pool_size(GB)'
	, @@innodb_buffer_pool_chunk_size/1024/1024/1024 as 'innodb_buffer_pool_chunk_size(GB)'
	, @@innodb_buffer_pool_instances as innodb_buffer_pool_instances;