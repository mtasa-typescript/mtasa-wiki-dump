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
            name='onClientProjectileCreation',
            docs=FunctionDoc(
                description='This event is triggered when a projectile is created.' ,
                arguments={
                    "creator": """the element that created the projectile. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='creator',
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
    )
]
