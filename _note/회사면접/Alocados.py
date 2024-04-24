# Coding Test


class Item:

    def __init__(self, key: int, value: str):
        if key < 0:
            raise ValueError("key 는 0이상의 정수")
        self.key = key
        self.value = value

    def __repr__(self):
        return f"<Item key={self.key}, value={self.value}>"


class HashMap:
    def __init__(self, size: int = None):
        self.size = size

        if size is None:
            # 동적으로 늘어나는 배열의 크기일때 처리를 어떻게 할 지 생각
            self.items = []
        else:
            self.items = [None] * size

    def set(self, item: Item) -> None:
        index = self.hash_func(item.key)
        self.items[index] = item

    def get(self, key: int) -> Item | None:
        index = self.hash_func(key)

        # TODO 해쉬 충돌 상황일 때 해결 코드
        # TODO self.items[index] 에서 indexOutOfArray 발생 try except 처리
        if item := self.items[index]:
            if item.key == key:
                return self.items[index]
            else:
                return None
        return None

    def hash_func(self, key: int) -> int:
        """Key에 hash_func 을 적용하여 unique한 값을 받아온다."""
        idx = key % self.size
        return idx


# Test Case
hash_map = HashMap(size=10)  # size는 입력을 받아도 되고, 받지 않아도 무방

apple = Item(key=1, value="apple")
banana = Item(key=3, value="banana")
tomato = Item(key=13, value="tomato")

hash_map.set(apple)
hash_map.set(banana)

assert hash_map.get(1).value == "apple"
assert hash_map.get(3).value == "banana"
assert hash_map.get(13) is None

hash_map.set(tomato)
assert hash_map.get(13).value == "tomato"

print("Clear!")
