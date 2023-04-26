"""
데코레이터를 만드는 실습
"""

from functools import wraps
from os import access


# 데코레이터 함수 정의
def decorator(func):

    @wraps(func)
    def inner_function(*args, **kwargs):  # 모든 종류의 인자를 다 받을 수 있게 만든다.
        # 데코레이터가 먼저 실행시킬 로직
        print("first print!")
        pass
        return func(*args, **kwargs)  # sum 이 호출됨

    return inner_function

# 데코레이터를 사용하여 함수 정의
@decorator
def sum(x: int, y: int) -> int:
    print("second print!", x + y)
    return x + y



"""
사용
"""
sum(3, 7)  # 데코레이터 적용


"""
실제 현업 사용 예시
"""
from flask import request

def login_required(f):

    @wraps
    def decorated_function(*args, **kwargs):
        access_token = request.headers.get('Authorization')
        if access_token is not None:
            try:
                payload = jwt.decode(access_token, current_app.config['JWT_SECRET_KEY'], 'HS256')
            except jwt.InvalidTokenError:
                payload = None

            if payload is None:
                return Response(status=401)

            user_id = payload['id']
            g.user_id = user_id
            g.user = get_user_info(user_id) if user_id else None
        else:
            return Response(status=401)

        return f(*args, **kwargs)

    return decorated_function