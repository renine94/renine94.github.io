"""
Section 2
Parallelism with Multiprocessing - multiprocessing(2) - Naming 

Keyword - Naming, parallel processing

"""

from multiprocessing import Process, current_process
import os
import random
import time


# 실행 방법
def square(n):
    # 랜덤 sleep
    time.sleep(random.randint(1, 3))
    process_id = os.getpid()
    process_name = current_process().name
    # 제곱
    result = n * n
    # 정보 출력
    print(f"Process ID: {process_id}, Process Name: {process_name}")
    print(f"Result of {n} square : {result}")


if __name__ == "__main__":
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    # 출력
    print(f"Parent process ID {parent_process_id}")

    # 프로세스 리스트  선언
    processes = list()

    # 프로세스 생성 및 실행
    for i in range(1, 10): # 1 ~ 100 적절히 조절
        # 생성
        t = Process(name=str(i), target=square, args=(i,))

        # 배열에 담기
        processes.append(t)

        # 시작
        t.start()

    # Join
    for process in processes:
        process.join()

    # 종료
    print("Main-Processing Done!")