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
    'store_once',
    'store_multiple'
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

Mode = Literal[
    'auto', 
    'manual'
]

Task_Mode = Literal[
    'classification',
    'regression'
]

Model_Name = Literal[
    'linear',
    'decision_tree',
    'svm',
    'gradient_boosting',
    'mlp'
]

Metric_Name = Literal[
    'MAD',
    'RMSE',
    'R2',
    'Accuracy',
    'F1',
    'AUCROC'
]

Identifier_Type = Union[
    str,
    float,
    int
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

Stage = Literal[
    'train',
    'test'
]

Parse_Mode = Literal[
    'get',
    'store'
]