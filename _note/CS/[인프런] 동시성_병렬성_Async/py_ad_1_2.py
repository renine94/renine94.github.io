"""
Section 1
Multithreading - Python's GIL
Keyword - CPython, 메모리관리, Gil사용 이유

"""
"""

Gil(Global Interpreter Lock)
(1).CPython -> Python(bytecode) 실행 시 여러 thread 사용 할 경우
    단일 스레드만이 Python object에 접근 하게 제한하는 mutex
(2).CPython 메모리 관리가 취약하기 때문(즉, Thread-safe)
(3).단일 스레드도 충분히 빠르다.
(4).프로세스 사용 가능(Numpy/Scipy)등 Gil 외부 영역에서 효율적인 코딩 가능
(5).병렬 처리는 Multiprocessing, asyncio 선택지 다양함.
(6).thread 동시성 완벽 처리를 위해서 -> Jython, IronPython, Stackless Python 등이 존재

"""