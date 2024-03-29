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
                name='getGameType',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        
                    ],
                    variable_length=False,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description='This function retrieves the current gametype as set by setGameType. The game type is displayed in the server browser next to the servers name.' ,
                arguments={
                    
                },
                result='returns the gametype as a string. if no gametype is set it returns nil.' ,
            ),
            url='getGameType',
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='getMapName',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        
                    ],
                    variable_length=False,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description='This function retrieves the current mapname as set by setMapName.' ,
                arguments={
                    
                },
                result='returns the mapname as a string. if no mapname is set it returns nil.' ,
            ),
            url='getMapName',
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='getRuleValue',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='key',
                                argument_type=FunctionType(
                                    names=['string'],
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
                description='This function gets a rule value. A rule value is a string that can be viewed by server browsers and used for filtering the server list.' ,
                arguments={
                    "key": """The name of the rule """
                },
                result='returns a string containing the value set for the specified key, false if invalid arguments were specified.' ,
            ),
            url='getRuleValue',
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='removeRuleValue',
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
                                name='key',
                                argument_type=FunctionType(
                                    names=['string'],
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
                description='This function removes a set rule value that can be viewed by server browsers.' ,
                arguments={
                    "key": """The name of the rule you wish to remove """
                },
                result='returns true if the rule value was removed, false if it failed.' ,
            ),
            url='removeRuleValue',
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='setGameType',
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
                                name='gameType',
                                argument_type=FunctionType(
                                    names=['string'],
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
                description='This function sets a string containing a name for the game type. This should be the game-mode that is active, for example Capture The Flag or Deathmatch. This is then displayed in the server browser and external server browsers.\nIt should be noted that mapmanager handles this automatically for gamemodes that utilise the map/gamemode system.' ,
                arguments={
                    "gameType": """A string containing a name for the game mode, or false to clear it. """
                },
                result='returns true if the game type was set, false if an invalid argument was passed to the function.' ,
            ),
            url='setGameType',
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='setMapName',
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
                                name='mapName',
                                argument_type=FunctionType(
                                    names=['string'],
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
                description='This function is used to set a map name that will be visible in the server browser. In practice you should generally rely on the mapmanager to do this for you.' ,
                arguments={
                    "mapName": """The name you wish the server browser to show. """
                },
                result='returns true if map name was set successfully, false otherwise.' ,
            ),
            url='setMapName',
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='setRuleValue',
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
                                name='key',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='value',
                                argument_type=FunctionType(
                                    names=['string'],
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
                description='This function sets a rule value that can be viewed by server browsers.' ,
                arguments={
                    "key": """The name of the rule """,
                    "value": """The value you wish to set for the rule """
                },
                result='returns true if the rule value was set, false if invalid arguments were specified.' ,
            ),
            url='setRuleValue',
        )
        ],
        client=[
            
        ],
    )
]
