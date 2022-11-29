import redis

from .ranker import RedisRanker

# 레디스 클라이언트를 만듭니다. (사용하시는 레디스 접속정보로 바꿔주세요)
conn_redis = redis.Redis(
  host="127.0.0.1",
  port=6379,
  password="0000",
  decode_responses=True
)

movie_ranker = RedisRanker(conn_redis, 'kyle:movie')

for i in range(2000): # 2,000번 관람
    movie_ranker.plusOne("Avengers")

for i in range(1500): # 1,500번 관람
    movie_ranker.plusOne("Avatar")

for i in range(1000): # 1,000번 관람
    movie_ranker.plusOne("Titanic")

for i in range( 500): #   500번 관람
    movie_ranker.plusOne("Star Wars")


movie_ranker.getRank("Titanic")
# 3 => 타이타닉은 흥행 3위입니다

movie_ranker.getScore("Titanic")
# 1000 => 타이타닉은 1,000번 관람되었습니다

movie_ranker.getTops(3)
# ['Avengers', 'Avatar', 'Titanic'] => 1위는 어벤져스, 2위는 아바타, 3위는 타이타닉입니다