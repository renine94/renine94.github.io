---
layout: single

header:
  teaser: /assets/images/logo/django.png
  overlay_image: /assets/images/logo/django.png
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[Celery] 셀러리를 활용하여 백그라운드 태스크를 비동기 처리하기"
excerpt: "🚀 레디스, 셀러리, 장고를 활용하여 Django 에서 Background Task 처리하기"

categories: django
tag: [django, celery, redis, task, background]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# Celery
> 참조
> - [medium - Django + Celery](https://medium.com/gitconnected/django-celery-going-deeper-with-background-tasks-in-python-fa44958cf7cd)
> - [Django Celery Result Backend](https://dontrepeatyourself.org/post/django-celery-result-backend/)



미디엄 포스팅글 한글로 번역한 것이고, 까먹을 까봐 소장용으로 기입해둡니다.



# Celery + Redis + Django Checklist

![image](https://user-images.githubusercontent.com/34491412/178349618-372e12e5-d9e7-4a4d-b3ae-15b276f72711.png)

이 체크리스트를 사용하면 Celery, Redis 및 Django를 즉시 사용할 수 있습니다. 이 코드를 자유롭게 복사 붙여넣고 응용프로그램에 아낌없이 사용하십시오.

나는 코드 스니펫을 위해 GitHub에서 그것을 호스팅했고, 그래서 나는 지속적인 편집을 할 수 있다. 이 페이지에 영원히 액세스할 수 있습니다. 링크를 저장하거나 Giston GitHub을 시작하십시오!

체크리스트는 당신이 장고, 레디스, 셀러리에 익숙하다고 가정한다. 여기 코드는 이 Celery 튜토리얼을 기반으로 합니다. 여기서 이해할 수 없는 부분이 있으면 해당 기사를 참조하여 자세히 알아보십시오.

## 개요

이 체크리스트를 사용하여 구축할 아키텍처는 세 가지가 있습니다.

1. Django Web Server
1. Redis Message Queue
1. Celery worker server

작동 방식:

1. 장고는 태스크(파이썬 기능)를 생성하고 Celery에게 Queue에 추가하라고 말합니다.
2. Celery는 그 일을 Redis(Broker)에 맡긴다(장고가 다른 일을 계속하도록 자유롭게 한다).
3. 별도의 서버에서 Celery는 작업을 픽업할 수 있는 Worker를 실행합니다.
4. 그 Worker들은 Redis의 말을 듣고 새로운 Task가 도착하면 한 작업자가 그것을 집어들고 처리한다.



## Requirements

[Install Redis](https://redis.io/topics/quickstart) & start it up locally at port 6379

```bash
pip install django
```

```bash
pip install celery
```

```bash
pip install redis
```

## 1. Create Django app

```bash
django-admin startproject celery_tutorial  // Start the project

cd celery_tutorial/
python manage.py migrate  // Migrate the database

python manage.py runserver  // Start dev server to test it worked
```

Visit [http://localhost:8000] to see if it works!

## 2. Configure Celery

### 2.1 celery.py

In the directory where `settings.py` (should be `celery_tutorial/celery_tutorial/settings.py`), create a new file - `celery.py`

```python
# celery_tutorial/celery_tutorial/celery.py

from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_tutorial.settings')

app = Celery('celery_tutorial')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
```

### 2.2 __init__.py

In the same directory (as `settings.py` and `celery.py`), edit `__init__.py`:

```python
# celery_tutorial/celery_tutorial/__init__.py

from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)
```

### 2.3 settings.py

Open `settings.py` and add the following:

```python
CELERY_BROKER_URL = 'redis://localhost:6379'
```

## 3. Create a Celery task

For simplicity, I'm placing the example task in `celery.py`. You can also create new tasks in any app. Celery will auto-discover any file named `tasks.py`.

```python
# celery_tutorial/celery_tutorial/celery.py

# ... at the bottom of the file, add this debug task

@app.task(bind=True)
def debug_task(self):
    """Check Celery is working by just printing out the task context"""
    print('Request: {0!r}'.format(self.request))
```

## 4. Queue the task

We created the task definition, now we need to call it & queue the task. In production, you'd do this in code - somewhere like `views.py`.

In this case, we'll just manually queue the task from the command line. Make sure you're in the directory with `manage.py`, now:

```bash
python manage.py shell

>>> from celery_tutorial.celery import debug_task
>>> debug_task.delay()
<AsyncResult: fe261700-2160-4d6d-9d77-ea064a8a3727>
```

## 5. Start a worker

> Worker 를 실행할 때, 많은 [옵션](https://docs.celeryq.dev/en/stable/reference/cli.html#celery-worker) 들이 있습니다. 
>
> 8core cpu에서는 Concurrency=17 옵션을 준다. ( cpu_core_count * 2 + 1 )
>
> -pool 옵션 (prefork, eventlet, event, solo, processes, threads) 에 대해서도 공부필요.

We queued the task and it's waiting in Redis. Now, we need a worker to process it.

Start the worker server:

```bash
celery -A celery_tutorial.celery worker --loglevel=info
```

You should see Celery startup, receive the task, & print the result!

Celery is working in your application!

## Want to see a real application running Django + Celery?

Here's the source code of an application that uses Celery tasks to calculate Fibonacci numbers.

https://github.com/bennett39/celery39/tree/celery-fib/celery_tutorial

Make sure you're on the `celery-fib` branch.

Here's a video of the application and an explanation of how it works: https://youtu.be/yRClWC3pYMs