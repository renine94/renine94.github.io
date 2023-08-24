# Double Under(UNderscores)

# len
class Foo:
    def __len__(self):
        return 5

f = Foo()
result = len(f)
print(result)  # 5

print("================================")
# gt
a = 10
print(a > 11)
print(a.__gt__(11))


class A:
    def __init__(self, value):
        self.value = value

    def __gt__(self, value):
        print(f"{self.value} > {value}")
        return self.value > value

test = A(10)
print(test>5)
print("================================")
# contains ( in )
...
print("================================")
# format ( f"{value:something}")

class People:

    def __str__(self):
        return "i'm people str"

    def __repr__(self):
        return "i'm people repr"

    def __format__(self, _format_spec: str) -> str:
        if _format_spec == "something":
            return f"this is some~thing lol."
        return super().__format__(_format_spec)


p = People()

print(f"this is format: {p:something}")
print(f"this is format2: {p}")