"""
Section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(2) - threading vs asyncio vs multiprocessing


Keyword - I/O Bound, requests, asyncio

"""
# I/O-Bound Asyncio 예제(https://realpython.com/python-concurrency/#synchronous-version)
# threading 보다 높은 코드 복잡도 -> Async, Await 적절하게 코딩

import asyncio
import aiohttp
import time

# 실행함수1(다운로드)
async def request_site(session, url):

    # 세션 확인
    # print(session)
    # print(session.headers)
    
    async with session.get(url) as response:
        # status_code 동기화 문제
        print("Read Contents {0}, from {1}".format(response.content_length, url))

# 실행함수2
async def request_all_site(urls):
    async with aiohttp.ClientSession() as session:
        # 작업 목록
        tasks = []
        for url in urls:
            # 태스크 목록 생성
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)

        # 태스크 확인
        # print(*tasks)
        # print(tasks)
        
        # 태스크 완료 시 까지  태스크 사용
        await asyncio.gather(*tasks, return_exceptions=True)

def main():
    # 테스트 URLS
    urls = [
            "https://www.jython.org",
            "http://olympus.realpython.org/dice",
            "https://daum.net"
    ] * 3
    
    # 실행시간 측정
    start_time = time.time()

    # 실행1
    asyncio.get_event_loop().run_until_complete(request_all_site(urls))
    # 실행2(파이썬 3.7 이상)
    # asyncio.run(request_all_site(urls))

    # 실행 시간 종료
    duration = time.time() - start_time

    print()
    
    # 결과 출력
    print(f"Downloaded {len(urls)} sites in {duration} seconds")

if __name__ == "__main__":
    main()