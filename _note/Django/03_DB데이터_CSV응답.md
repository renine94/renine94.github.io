# Django 데이터를 csv 파일로 출력해주기
> 정산이나, 기타 다른 작업들을 할 때 유용하며, 서버에 파일을 저장하는게 아니라 바로 다운로드 받을 수 있게 해준다.


```python
def export_csv(request):
  qs = User.objects.values("username", "age")
  df = pd.DataFrame(data=qs)

  export_file = ByteIO()

  df.to_csv(export_file, index=False, encoding="utf-8-sig)

  response = HttpResponse(content=export_file.getvalue(), content_type="text/csv")
  response["Content-Disposition"] = "attachment; filename='유저정보.csv'"
  return response
```
