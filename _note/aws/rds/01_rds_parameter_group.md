# RDS 파라미터 그룹 설정

- 운영환경에 맞는 파라미터 설정하기
  - RDS 를 처음 생성하면 설정해야할 3가지
    - 타임존
    - Character Set
    - Max Connection

- 파라미터 그룹
- 파라미터 그룹 생성
  - 패밀리 지정 (mariadb10.2)
  - 그룹 이름 지정
  - 설명


- time_zone : Asia/Seoul
- Character_set_client : utf8mb4 (이모지 저장가능 mb4)
- Character_set_connection : utf8mb4 (이모지 저장가능 mb4)
- Character_set_database : utf8mb4 (이모지 저장가능 mb4)
- max_connections : 150


# 생성한 파라미터 그룹을 데이터베이스에 연결

- 데이터베이스 수정
- DB 파라미터 그룹 : default -> 위에서만든 파라미터 그룹
- 정상적용안되면 DB 재부팅