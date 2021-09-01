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
            FunctionData(
            signature=FunctionSignature(
                name='loadMapData',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='node',
                                argument_type=FunctionType(
                                    names=['xmlnode'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='parent',
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
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description="""This function is intended to load data from a loaded XML file into the element tree. This could be used for loading an external map, or part of another map. """,
                arguments={
                    "node": """The node that you wish to load into the element tree. """,
                    "parent": """The node you wish to be the parent of the new map data. """
                },
                result="""returns an element object that corresponds to the root of the new data added, i.e. an element that represents the node xmlnode passed to the function. returns false if the arguments are invalid. """,
            ),
            name='loadMapData',
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='resetMapInfo',
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
                                name='thePlayer',
                                argument_type=FunctionType(
                                    names=['player'],
                                    is_optional=True,
                                ),
                                default_value='getRootElement()',
                            )
                        ]
                    ],
                    variable_length=False,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description="""This function is used to reset the state of a player.  It is intended to restore a player to his default state as if he had just joined the server, without any scripts affecting him. """,
                arguments={
                    "thePlayer": """The specific player you wish to restore the state of.  Not specifying this will result in all players map info being reset. """
                },
                result="""returns true if the map info was reset successfully, otherwise false. """,
            ),
            name='resetMapInfo',
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='saveMapData',
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
                                name='node',
                                argument_type=FunctionType(
                                    names=['xmlnode'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='baseElement',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='childrenOnly',
                                argument_type=FunctionType(
                                    names=['bool'],
                                    is_optional=True,
                                ),
                                default_value='false',
                            )
                        ]
                    ],
                    variable_length=False,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description="""This converts a set of elements in the element tree into XML. This is a format that can then be loaded as a map file. Each element represents a single XML node. """,
                arguments={
                    "node": """: An existing node that should contain the contents of baseElement """,
                    "baseElement": """: The first element to output to the XML tree. This element and all its children (and their children, etc) will be output. """,
                    "childrenOnly": """: Defines if you want to only save children of the specified element. """
                },
                result=""" """,
            ),
            name='saveMapData',
        )
        ],
        client=[
            
        ],
    )
]
