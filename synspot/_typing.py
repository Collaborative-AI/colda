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
    List,
    Dict
)

JSONType = Union[
    Dict[str, Any],
    List[Any]
]

DictKey = TypeVar('DictKey', List[Hashable], Hashable)
DictValue = TypeVar("DictValue", bound=Any)
Dict_Store_Type = Literal[
    'append', 
    'one_access',
    'multiple_access'
]

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

Default_Mode = Literal[
    'auto', 
    'manual'
]

Serializable_Datatype = Union[
    dict,
    list,
    tuple,
    str,
    int,
    float,
    bool,
    None,
]

Stage = [
    'train',
    'test'
]
