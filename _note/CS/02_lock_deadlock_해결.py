"""
1. 세마포어(Semaphore)
프로세스간 공유 된 자원에 접근 시 문제 발생 가능성 -> 한 개의 프로세스만 접근 처리 고안 ( 경쟁상태 예방 )

2. 뮤텍스(Mutex)
공유된 자원의 데이터를 여러 스레드가 접근하는 것을 막는 것 -> 경쟁 상태 예방

3. Lock
상호 배제를 위한 잠금처리 -> 데이터 경쟁

4. DeadLock
프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상황 (교착 상태)

5. Thread Synchronization
스레드 동기화를 통해서 안정적으로 동작하게 처리한다. 동기화 메소드, 동기화 블럭

6. 세마포어와 뮤텍스 차이?
세마포어는 뮤텍스가 될 수 있지만, 뮤텍스는 세마포어가 될 ㅅ수 없다.

뮤텍스: 화장실 1개 (프로세스)에 여러명이 키(Lock) 를 가지고 있어야 순차적으로 들어갈 수 있다.
세마포어: 화장실 N개에 N개의 Lock(키)를 가지고 있으면 먼저나오는사람이 키를 주고받으며 순차적으로 들어갈 수 있다.

-> 세마포어와 뮤텍스 개체는 모두 병렬 프로그래밍 환경에서 상호배제를 위해 사용
-> 뮤텍스 개체는 단일 스레드가 리소스 또는 중요 섹션을 소비 허용
-> 세마포어는 리소스에 대한 제한된 수의 동시 액세스를 허용
"""

import logging
from concurrent.futures import ThreadPoolExecutor
import threading
import time

class FakeDataStore:
    # 공유 변수(value) 화장실
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    # 변수 업데이트 함수
    def update(self, n):
        logging.info(f"Thread {n} starting update")

        # # Lock 흭득 (방법1)
        # self._lock.acquire()
        # logging.info(f"Thread {n} has lock")

        # # 뮤텍스 & Lock 등 동기화 (스레드 동기화 필요)
        # local_copy = self.value
        # local_copy += 1
        # time.sleep(0.1)
        # self.value = local_copy

        # # Lock 해제 (방법1)
        # self._lock.release()
        # logging.info(f"Thread {n} release lock")

        # logging.info(f"Thread {n} finishing update")

        # Lock 흭득 (방법2)
        with self._lock:
            logging.info(f"Thread {n} has lock")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.info(f"Thread {n} release lock")

if __name__ == "__main__":
    # Logging Format
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main-Thread: before creating and running thread")

    # 클래스 인스턴스화
    store = FakeDataStore()

    logging.info(f"Testing update. Starting value is {store.value}")

    # With Context 시작
    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in [1, 2, 3, 4, 5]:
            executor.submit(store.update, n)

    logging.info(f"Testing update. Ending value is {store.value}")