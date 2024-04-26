<!-- https://gist.github.com/allieus/1f8fae7922f9daa60a0ccfada210fdf8 -->

- Decorators
```python
from django.middleware.cache import CacheMiddleware
from django.utils.cache import get_cache_key
from django.utils.decorators import decorator_from_middleware_with_args


class PostDeleterCacheMiddleware(CacheMiddleware):
    def process_request(self, request):
        if request.method == 'POST':
            # https://github.com/django/django/blob/3.0.9/django/middleware/cache.py#L137
            cache_key = get_cache_key(request, self.key_prefix, 'GET', cache=self.cache)
            self.cache.delete(cache_key)
        return super().process_request(request)


def post_deleter_cache_page(timeout, *, cache=None, key_prefix=None):
    return decorator_from_middleware_with_args(PostDeleterCacheMiddleware)(
        page_timeout=timeout, cache_alias=cache, key_prefix=key_prefix,
    )
```

- Views
```python
import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .decorators import post_deleter_cache_page


@csrf_exempt
@post_deleter_cache_page(60)
def index(request):
    return HttpResponse(f"Hello World : {datetime.datetime.now()}")
```
