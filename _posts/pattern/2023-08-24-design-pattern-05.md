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

title: "[pattern] 디자인패턴(5) - 빌더(Builder) 패턴"
excerpt: "🚀 디자인패턴 Builder"

categories: pattern
tag: [pattern, design, builder]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---
# 01. Builder Pattern

**Motivation** - 빌더 패턴을 사용하는 이유

- Some objects are simple and can be created in single initializer call
- Other objects require a lot of ceremony to create
- Having an object with 10 initializer arguments is not productive
- Instead, opt for piecewise construction
- Builder provides an API for constructing an object step-by-step



- 일부 객체는 간단하며 한 번의 이니셜라이저 호출로 생성할 수 있습니다.
- 다른 객체는 생성하는 데 많은 의식이 필요합니다.
- 이니셜라이저 인자가 10개인 객체를 갖는 것은 생산적이지 않습니다.
- 대신, 조각별로 구성하는 방법을 선택하세요.
- 빌더는 단계별로 객체를 구성하기 위한 API를 제공합니다.

빌더의 공식적인 정의
> When piecewise object construction is complicated, provide an API for doing it succinctly



```python
text = "hello"
parts = ["<p>", text, "</p>"]
print("".join(parts))

words = ["hello", "world"]
parts = ["<ul>"]
for w in words:
  parts.append(f"<li>{w}</l;i")
parts.append("</ul>")
print('\n'.join(parts))
```





```python
class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.text}")

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))

    def add_child_fluent(self, child_name, child_text):
        """Method 체이닝을 할 수 있게 됨"""
        self.__root.elements.append(HtmlElement(child_name, child_text))
        return self

    def __str__(self):
        return str(self.__root)


builder = HtmlElement.create("ul")
# builder = HtmlBuilder('ul')
# builder.add_child('li', 'hello')
# builder.add_child('li', 'world')
builder.add_child_fluent("li", "hello").add_child_fluent("li", "world")
print("Ordinary builder:")
print(builder)
```



다른 예시

```python
class Person:
    def __init__(self):
        # address
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return (
            f"Address: {self.street_address}, {self.postcode}, {self.city}"
            + f"Employed at {self.company_name} as a {self.position} earning {self.annual_income}"
        )


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person: Person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person: Person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


pb = PersonBuilder()
person = (
    pb
        .lives
            .at("123 London Road")
            .in_city("London")
            .with_postcode("SW12BC")
        .works
            .at("Fabrikam")
            .as_a("Engineer")
            .earning(123000)
        .build()
)

print(person)
```

> 개방형 폐쇄 원칙을 따른 상속을 통해 확장으로 만든 빌더패턴

```python
class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f"{self.name} born on {self.date_of_birth} " + f"works as {self.position}"

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


pb = PersonBirthDateBuilder()
me = pb\
    .called('Dmitri')\
    .works_as_a('Quant')\
    .born('1/1/1980')\
    .build()
print(me)
```



## 02. Builder Pattern 자바 예시

```java
public class Computer {

  // required parameters
  private String HDD;
  private String RAM;

  // optional parameters
  private boolean isGraphicsCardEnabled;
  private boolean isBluetoothEnabled;

  public String getHDD() {
    return HDD;
  }

  public String getRAM() {
    return RAM;
  }

  public boolean isGraphicsCardEnabled() {
    return isGraphicsCardEnabled;
  }

  public boolean isBluetoothEnabled() {
    return isBluetoothEnabled;
  }

  private Computer(ComputerBuilder builder) {
    this.HDD = builder.HDD;
    this.RAM = builder.RAM;
    this.isGraphicsCardEnabled = builder.isGraphicsCardEnabled;
    this.isBluetoothEnabled = builder.isBluetoothEnabled;
  }

  // Builder Class
  public static class ComputerBuilder {

    // required parameters
    private String HDD;
    private String RAM;

    // optional parameters
    private boolean isGraphicsCardEnabled;
    private boolean isBluetoothEnabled;

    public ComputerBuilder(String hdd, String ram) {
      this.HDD = hdd;
      this.RAM = ram;
    }

    public ComputerBuilder setGraphicsCardEnabled(boolean isGraphicsCardEnabled) {
      this.isGraphicsCardEnabled =  isGraphicsCardEnabled;
      return this;
    }

    public ComputerBuilder setBluetoothEnabled(boolean isBluetoothEnabled) {
      this.isBluetoothEnabled = isBluetoothEnabled;
      return this;
    }

    public Computer build() {
      return new Computer(this);
    }

  }
}
```

여기서 살펴볼 것은 Computer 클래스가 setter 메소드 없이 getter 메소드만 가진다는 것과 public 생성자가 없다는 것입니다. 그렇기 때문에 
**Computer 객체를 얻기 위해서는 오직 ComputerBuilder 클래스를 통해서만 가능합니다.**


```java
public class TestBuilderPattern {

  public static void main(String[] args) {
    Computer comp = new Computer.ComputerBuilder("500GB", "2GB")
                      .setBluetoothEnabled(true)
                      .setGraphiteEnabled(true)
                      .build();
  }
  
}
```