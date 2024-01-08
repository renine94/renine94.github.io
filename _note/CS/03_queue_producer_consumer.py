"""

Producer-Consumer  Pattern
1. 멀티스레드 디자인 패턴의 정석
2. 서버측 프로그래밍의 핵심
3. 주로 허리역할 중요

# Python Event 객체
1. Flag 초기값 0
2. set() -> 1, clear() -> 0, wait(1 -> 리턴, 0 -> 대기), isSet() -> 현 플래그 상태
event = threading.Event()
event.set()
event.clear()
event.wait()
event.is_set()
"""

import logging
import random
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import queue

# 생산자
def producer(queue, event):
    """네트워크ㅡ 대기 상태라 가정(서버)"""
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info(f'producer send message: {message}')
        queue.put(message)
    logging.info('producer send event exiting')

# 소비자
def consumer(queue: queue.Queue, event):
    """응답받고 소비하는 것으로 가정 or DB저장"""
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info(f'consumer received message: {message}, (size={queue.qsize()})')
    logging.info('consumer received event exiting')

if __name__ == "__main__":
    # Logging Format
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=10)

    event = threading.Event()

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)

        logging.info('Main: about to set event')

        event.set()
