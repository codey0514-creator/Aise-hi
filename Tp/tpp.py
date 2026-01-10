import mediapipe as mp
# Python 3.12+ only
from typing import Self
class Counter:
    def __init__(self, value: int = 0):
        self.value = value

    def increment(self) -> Self:
        self.value += 1
        return self

c = Counter()
c.increment().increment()
print(c.value)
import sys
print(sys.executable)

