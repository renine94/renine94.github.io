---
layout: single

header:
  teaser: /assets/images/logo/pattern.jpeg
  overlay_image: /assets/images/logo/pattern.jpeg
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[pattern] 디자인패턴(2) - 단일책임 원칙"
excerpt: "🚀 디자인패턴 & SOLID 원칙"

categories: pattern
tag: [pattern, design, solid]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---
# 01. SRP (Single Responsibility Principle)
> 관심사의 분리 SOC (separation of concerns) 랑 뭔가 비슷한 느낌.

- 클래스가 있는 경우, 클래스는 무엇을 하려는지 간에 주된 책임이 있어야 한다.
- `Journal` 클래스에 저장기능까지 추가하면 책임이 너무 많아지므로, `PersistenceManager` 와 같은 클래스로 파일 입출력에 대한 기능을 따로 나누는것이 좋다.


```python
class Journal:

  def __init__(self):
    self.entries = []
    self.count = 0

  def add_entry(self, text):
    self.count += 1
    self.entries.append(f"{self.count}: {text}")

  def remove_entry(self, pos):
    del self.entries[pos]
  
  def __str__(self):
    return "\n".join(self.entries)

  # def save(self, filename):
  #   file = open(filename, "w")
  #   file.write(str(self))
  #   file.close()
  
  # def load(self, filename):
  #   ...
  
  # def low_from_web(self, url):
  #   ...


class PersistenceManager:
  
  @staticmethod
  def save_to_file(journal, filename):
    file = open(filename, "w")
    file.write(str(journal))
    file.close()

j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}")

file = r'c:\temp\journal.txt'
PersistenceManger.save_to_file(j, file)

```
