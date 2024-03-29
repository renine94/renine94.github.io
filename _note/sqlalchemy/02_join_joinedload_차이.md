# https://blog.hongminhee.org/2013/10/30/65522658529/

SQLAlchemy에서 쿼리할 때 조인을 직접 명시해야 하는 경우는 별로 없다
오랜만에 특정 라이브러리의 세부사항에 대해 얘기해본다.

SQLAlchemy ORM을 쓰는 경우 Query.join() 메서드를 직접 써야 하는 경우는 사실 별로 없다. 대부분은 기능을 다 알지 못해서 그렇게 쓰는 것이다.

참고로 이 글에서 다루는 내용은 원래 SQLAlchemy 공식 튜토리얼과 가이드 문서의 (API 레퍼런스 말고) 관계 로딩 테크닉 부분에서 훨씬 더 자세히 설명되어 있다.

로딩하면서 관계 객체들도 한번에 같이 가져오고 싶을 때
Query.join() 메서드를 잘못 사용하는 첫번째 케이스는 관계된 객체들까지 함께 eager loading하고 싶을 때이다.
```python
session.query(Post) \
       .join(User, Post.author_id == User.id)
```
하지만 위와 같이 써서는 원하는대로 작동하지 않는다. 실제로 Post.author 속성에 접근할 때 별도의 쿼리가 따로 나갈 것이다.

그 이전에 위 쿼리는 스타일 상으로도 문제가 있다. 모델 정의 시에 어차피 Post.author 관계 속성에 조인 조건을 명시하거나 자동으로 추론되는데, 해당 조건을 쿼리할 때 중복해서 다시 쓰는 것이다. 이렇게 되면 추후 관계 조건이 달라졌을 때 쿼리 코드를 뒤져가며 함께 고쳐줘야 하는 문제가 생긴다. (십중팔구는 까먹고 안 고쳤다가 논리적인 오류를 만난다.)

일단 중복 문제만 개선하자면 다음과 같이 고칠 수 있다.
```python
session.query(Post).join(Post.author)
```
보다시피 Query.join() 메서드는 관계 속성 자체를 인자로 받는다. 이렇게 하면 나중에 Post.author의 조건이 달라졌을 때도 의미가 변하지 않을 것이다


하지만 여전히 Post.author 속성에 접근했을 때 별도 쿼리가 생성되는 문제는 존재한다. 왜냐면 SQLAlchemy에서 쿼리 생성과 로딩 전략은 별도로 취급되기 때문이다. 조인된 Post.author를 메모리 상의 Post 객체를 만들 때 채워주고 싶다면 다음과 같이 Query.options() 메서드에 contains_eager()를 명시해야 한다.
```python
session.query(Post) \
       .join(Post.author) \
       .options(contains_eager(Post.author))
```
이제 Post.author 속성에도 이미 메모리 상에 로딩된 User 객체가 들어가 있을 것이다.

하지만 굳이 contains_eager()를 쓸 필요 없이, Query.join()과 contains_eager()를 함께 해주는 joinedload()를 쓰는 편이 낫다.
```python
session.query(Post).options(joinedload(Post.author))
```
조건 절에 조인된 테이블의 필드를 참조해야 하는 경우
Query.join() 메서드를 쓰는 또다른 경우는 조건 절에서 다른 관계된 테이블의 특정 컬럼을 참조해야 하는 경우이다.
```python
session.query(Post) \
       .join(User, User.id == Post.author_id) \
       .filter(~User.deleted) \
       .filter(User.last_login_time > now() - datetime.timedelta(days=1))
```
앞서 설명했듯 조인 조건을 굳이 중복해서 쓸 필요가 없으므로 위 쿼리도 다음과 같이 개선할 수 있다.

```python
session.query(Post) \
       .join(Post.author) \
       .filter(~User.deleted) \
       .filter(User.last_login_time > now() - datetime.timedelta(days=1))
```
Query.filter() 메서드 안에서 관계된 다른 모델의 속성을 참조해야 하는 경우, has-one 관계인 경우 .has() 메서드, has-many 관계인 경우 .any() 메서드를 써서 표현할 수 있다.

```python
session.query(Post) \
       .filter(Post.author.has(
           ~User.deleted |
           (User.last_login_time > now() - datetime.timedelta(days=1))
       ))
```
단순 == 연산만 필요한 경우에는 아예 키워드 인자로 넘겨버려도 된다. 가령 아래 두 쿼리는 같은 의미다.

```python
session.query(Post).filter(Post.author.has(~User.deleted))

session.query(Post).filter(Post.author.has(deleted=False))
```