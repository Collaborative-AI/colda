from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
    Hashable,
    Iterator,
    Literal,
    Mapping,
    Optional,
    Protocol,
    Sequence,
    TypeVar,
    Union,
)

JSONType = Union[
    dict[str, Any],
    list[dict],
    list[Any]
]

DictKey = TypeVar('DictKey', bound=Hashable)
DictValue = TypeVar("DictValue", bound=Any)
Dict_Store_Type = Literal['append', 'one_access']

Train_Database_Type = Literal[
    'default_metadata',
    'train_sponsor_metadata',
    'train_assistor_metadata',
    'train_algorithm'
]

Test_Database_Type = Literal[
    'default_metadata'
    'test_sponsor_metadata',
    'test_assistor_metadata',
    'test_algorithm'
]

Role = Literal[
    'sponsor',
    'assistor',
]