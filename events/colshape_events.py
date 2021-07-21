# Autogenerated file. ANY CHANGES WILL BE OVERWRITTEN
from to_python.core.types import FunctionType, \
    FunctionArgument, \
    FunctionArgumentValues, \
    FunctionReturnTypes, \
    FunctionSignature, \
    FunctionDoc, \
    EventData, \
    CompoundEventData
    
DUMP_PARTIAL = [
    CompoundEventData(server=[], client=[EventData(
            name='onClientColShapeHit',
            docs=FunctionDoc(
                description="""This event is triggered when a physical element hits a colshape. """,
                arguments={
                    "theElement": """the element that entered the colshape. """,
                    "matchingDimension": """a boolean referring to whether the hit collision shape was in the same dimension as the element. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theElement',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='matchingDimension',
                                argument_type=FunctionType(
                                    names=['bool'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=False,
                ),
        )]),
    CompoundEventData(server=[], client=[EventData(
            name='onClientColShapeLeave',
            docs=FunctionDoc(
                description="""This event is triggered when a physical element leaves a colshape. """,
                arguments={
                    "theElement": """the element that left the colshape. """,
                    "matchingDimension": """a boolean referring to whether the collision shape was in the same dimension as the element. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theElement',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='matchingDimension',
                                argument_type=FunctionType(
                                    names=['bool'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=False,
                ),
        )]),
    CompoundEventData(server=[EventData(
            name='onColShapeHit',
            docs=FunctionDoc(
                description="""This event is triggered when a physical element hits a colshape. """,
                arguments={
                    "hitElement": """: the element that entered the colshape. """,
                    "matchingDimension": """: a boolean referring to whether the hit collision shape was in the same dimension as the element. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='hitElement',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='matchingDimension',
                                argument_type=FunctionType(
                                    names=['bool'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=False,
                ),
        )], client=[]),
    CompoundEventData(server=[EventData(
            name='onColShapeLeave',
            docs=FunctionDoc(
                description="""This event is triggered when a player or a vehicle leaves a collision shape. """,
                arguments={
                    "leaveElement": """: The element that who exited the col shape. This can be a player or a vehicle. """,
                    "matchingDimension": """: a boolean referring to whether the collision shape was in the same dimension as the element. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='leaveElement',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='matchingDimension',
                                argument_type=FunctionType(
                                    names=['bool'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=False,
                ),
        )], client=[])
]
