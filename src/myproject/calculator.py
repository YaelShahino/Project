from typing import TypeVar, cast

from typing_extensions import assert_never

_TElem = TypeVar("_TElem", int, str)


def add(lst: list[_TElem], elem_type: type[_TElem], elem: int | str) -> list[_TElem]:
    if isinstance(elem, elem_type):
        lst.append(elem)
        return lst

    match elem:
        case str():
            int_lst = cast(list[int], lst)  # type:ignore[redundant-cast]
            int_lst.append(len(elem))
        case int():
            str_lst = cast(list[str], lst)  # type:ignore[redundant-cast]
            str_lst.append(str(elem))
        case _:
            assert_never(elem_type)

    return lst
