"""
Section 2
Parallelism with Multiprocessing - multiprocessing(4) - Sharing state

Keyword - memory sharing, array, value

"""

from multiprocessing import Process, current_process, Value, Array
import random
import os

# 프로세스 메모리 공유 예제(공유 O)

# 프로세스 동기화 관련 참고
# https://docs.python.org/3/library/multiprocessing.html#synchronization-between-processes


# 실행 함수
def generate_update_number(v : int):
    for i in range(50):
        v.value += 1
    print(current_process().name, "data", v.value)

def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    # 출력
    print(f"Parent process ID {parent_process_id}")

    # 프로세스 리스트  선언
    processes = list()

    # 프로세스 메모리 공유 변수
    # from multiprocessing import shared_memory 사용 가능(파이썬 3.8)
    # from multiprocessing import Manager 사용 가능
    # https://docs.python.org/3/library/multiprocessing.html#sharing-state-between-processes(Manager 사용 가능)
    
    # share_numbers = Array('i', range(50)) # i, c 등 Flag 확인
    share_value = Value('i', 0)
    for _ in range(1,10):
        # 생성
        p = Process(target=generate_update_number, args=(share_value,))
        # 배열에 담기
        processes.append(p)
        # 실행
        p.start()
        
    # Join
    for p in processes:
        p.join()

    # 최종 프로세스 부모 변수 확인
    print("Final Data(share_value) in parent process",  share_value.value)

if __name__ == '__main__':
    main()