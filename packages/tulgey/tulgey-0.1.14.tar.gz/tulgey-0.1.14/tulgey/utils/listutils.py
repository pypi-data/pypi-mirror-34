from typing import TypeVar, List

T = TypeVar('T')
def chunks(list: List[T], n: int) -> List[List[T]]:
    for i in range(0, len(list), n):
        yield list[i:i + n]

