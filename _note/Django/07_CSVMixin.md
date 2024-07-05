# Django

## CSV 모델 데이터 반환하기

```python
from django.http import StreamingHttpResponse
from django.db import models
from rest_framework.decorators import action
import csv
import io

class CSVStreamingMixin:
    @action(detail=False, methods=["GET"], url_path="stream_csv")
    def stream_csv(self, request):
        queryset = self.get_queryset().order_by('id')
        fields = self.get_csv_fields()

        def stream_csv():
            buffer = io.StringIO()
            writer = csv.writer(buffer)

            # Write CSV header
            writer.writerow(fields)
            yield buffer.getvalue()
            buffer.seek(0)
            buffer.truncate(0)

            # Process data in chunks
            chunk_size = 1000
            for obj in queryset.iterator(chunk_size=chunk_size):
                row = [getattr(obj, field) for field in fields]
                writer.writerow(row)
                yield buffer.getvalue()
                buffer.seek(0)
                buffer.truncate(0)

        response = StreamingHttpResponse(stream_csv(), content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{self.get_csv_filename()}"'
        return response

    def get_csv_fields(self):
        return [field.name for field in self.get_queryset().model._meta.fields]

    def get_csv_filename(self):
        return f"{self.get_queryset().model._meta.model_name}_data.csv"

class CouponExtensionViewSet(CSVStreamingMixin, viewsets.ModelViewSet):
    queryset = CouponExtension.objects.all()
    # ... 기타 ViewSet 설정 ...

    def get_csv_fields(self):
        return ['sno', 'other_field1', 'other_field2']  # 원하는 필드 지정
```
