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
    CompoundEventData(
        server=[
            
        ],
        client=[
            EventData(
            name='onClientObjectBreak',
            docs=FunctionDoc(
                description='This event is fired before an object breaks.' ,
                arguments={
                    "attacker": """the vehicle/ped/player who is breaking the object """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='attacker',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=False,
                ),
        )
        ],
    ),
    CompoundEventData(
        server=[
            
        ],
        client=[
            EventData(
            name='onClientObjectDamage',
            docs=FunctionDoc(
                description='This event is fired before an object gets damaged.' ,
                arguments={
                    "loss": """the health loss caused by the damage. This parameter contains the theoretical loss, which could be less than 0, if you substract it of the current health. If you want to get the real loss, you have to substract the new health of the old health (use a timer for this). """,
                    "attacker": """the vehicle/ped/player who is damaging the object. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='loss',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='attacker',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=False,
                ),
        )
        ],
    ),
    CompoundEventData(
        server=[
            
        ],
        client=[
            EventData(
            name='onClientObjectMoveStart',
            docs=FunctionDoc(
                description='' ,
                arguments={
                    
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        
                    ],
                    variable_length=False,
                ),
        )
        ],
    ),
    CompoundEventData(
        server=[
            
        ],
        client=[
            EventData(
            name='onClientObjectMoveStop',
            docs=FunctionDoc(
                description='' ,
                arguments={
                    
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        
                    ],
                    variable_length=False,
                ),
        )
        ],
    )
]
