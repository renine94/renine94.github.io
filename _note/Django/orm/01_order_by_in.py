"""
Django ORM 사용해서 in 으로 id 필터링 조회할때 데이터 순서 바뀌는 현상
"""
from django.db.models import Case, When

id_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 이 순서 그대로 가져오고 싶음
preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(id_list)])

user_queryset = User.objects.filter(id__in=id_list).order_by(preserved)