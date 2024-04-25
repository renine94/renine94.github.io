# https://www.inflearn.com/course/lecture?courseSlug=%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EC%9B%B9%EC%84%9C%EB%B9%84%EC%8A%A4-with%EB%A6%AC%EC%95%A1%ED%8A%B8&unitId=197652&tab=curriculum
# Django DB 데이터 엑셀로 응답


```python
from io import ByteIO
import pandas as pd
from django.http import HttpResponseBadRequest

def export(request: HttpRequest, format: Literal["csv", "xlsx"]) -> HttpResponse:
  queryset: QuerySet = User.objects.all()
  queryset = queryset.value()
  df = pd.DataFrame(data=queryset)

  export_file = ByteIO()

  if format == "csv":
    content_type = 'text/csv'
    filename = 'user.csv'
    df_to_csv(path_or_buf=export_file, index=False, encoding='utf-8-sig')
  elif format == "xlsx":
    content_type = 'application/vnd.ms-excel'
    filename = 'user.xlsx'
    df_to_excel(path_or_buf=export_file, index=False, engine="openpyxl)
  else:
    return HttpResponseBadRequest(f"invalid format: {format}")
  
  response = HttpResponse(content=export_file.getvalue(), content_type=content_type)
  response['Content-Disposition'] = 'attachment; filename*=utf-8''{}"'.format(filename)

  return response

```
