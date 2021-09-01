# Autogenerated file. ANY CHANGES WILL BE OVERWRITTEN
from to_python.core.types import FunctionType, \
    FunctionArgument, \
    FunctionArgumentValues, \
    FunctionReturnTypes, \
    FunctionSignature, \
    FunctionDoc, \
    FunctionData, \
    CompoundFunctionData
    
DUMP_PARTIAL = [
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='createFire',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['bool'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='x',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='y',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='z',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='size',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value='1.8',
                            )
                        ]
                    ],
                    variable_length=False,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description="""Creates a patch of fire that will spread a bit and die out after a while. Because its a client side only function, other players wont see it, so custom events or custom objects will be needed to make a fire visible to some players. """,
                arguments={
                    "x, y, z": """the coordinates when the initial patch of fire will be created. """,
                    "size": """a float value indicating the size of the initial patch of fire. It will also make the fire to stay alive more or less time. """
                },
                result="""returns true if successful, false if bad arguments were passed or the limit of active fires was reached. there can be a maximum of 60 active fires. """,
            ),
            name='createFire',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='extinguishFire',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['bool'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='x',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='y',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='z',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='radius',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value='1.0',
                            )
                        ]
                    ],
                    variable_length=False,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description=""" """,
                arguments={
                    "x, y, z": """the coordinates at which any fire will be extinguished. """,
                    "radius": """a float value indicating the radius in which to extinguish fire. """
                },
                result="""returns true if successful, false otherwise. """,
            ),
            name='extinguishFire',
        )
        ],
    )
]
