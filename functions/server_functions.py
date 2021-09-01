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
                name='getMaxPlayers',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['int'],
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
                description='This function returns the maximum number of player slots on the server.' ,
                arguments={
                    
                },
                result='returns the maximum number of players allowed on the server.' ,
            )
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='getServerHttpPort',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['int'],
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
                description='This function retrieves the servers HTTP port.' ,
                arguments={
                    
                },
                result='an integer corresponding to the servers http port.' ,
            )
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='getServerName',
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
                description='This function retrieves the servers name.' ,
                arguments={
                    
                },
                result='a string containing the servers name.' ,
            )
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='getServerPassword',
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
                description='This function returns the current password required to join the server.' ,
                arguments={
                    
                },
                result='returns the current server password as a string if it has a password, if not it returns nil.' ,
            )
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='getServerPort',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['int'],
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
                description='This function retrieves the servers port.' ,
                arguments={
                    
                },
                result='an integer corresponding to the servers port.' ,
            )
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='isGlitchEnabled',
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
                                name='glitchName',
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
                description='This function retrieves whether San Andreas game glitches are enabled or not, set by using setGlitchEnabled' ,
                arguments={
                    "glitchName": """the name of the property to set. Possible values are: """
                },
                result='returns true if if the glitch was enabled, or false if it is disabled.' ,
            )
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='isTransferBoxVisible',
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
                        
                    ],
                    variable_length=False,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description='' ,
                arguments={
                    
                },
                result='on server this returns a boolean, whether the transfer box should be visible during downloads or not.\non client this returns a boolean, whether the transfer box should be visible or not at the time of invocation.' ,
            )
        )
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='isTransferBoxVisible',
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
                        
                    ],
                    variable_length=False,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description='' ,
                arguments={
                    
                },
                result='on server this returns a boolean, whether the transfer box should be visible during downloads or not.\non client this returns a boolean, whether the transfer box should be visible or not at the time of invocation.' ,
            )
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='setGlitchEnabled',
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
                                name='glitchName',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='enable',
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
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description='This function enables or disables glitches that are found in the original Single Player game that can be used to gain an advantage in multiplayer.\nUsers of the fastmove glitch may additionally want to install https://community.mtasa.com/index.php?p=resources&s=details&id=13368 this resource to disable crouchsliding.' ,
                arguments={
                    "glitchName": """the name of the property to set. Possible values are: """,
                    "enable": """whether or not to enable the glitch. """
                },
                result='returns true if successful, false otherwise.' ,
            )
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='setMaxPlayers',
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
                                name='slots',
                                argument_type=FunctionType(
                                    names=['int'],
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
                description='This function sets the maximum number of player slots on the server.' ,
                arguments={
                    "slots": """Maximum number of player slots on the server. """
                },
                result='returns true if number of player slots was successfully changed, false or nil otherwise.' ,
            )
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='setServerPassword',
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
                                name='thePassword',
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
                description='This function changes the password required to join the server to the given string.' ,
                arguments={
                    "thePassword": """The new server password you want. Pass nil or an empty string to remove the password. """
                },
                result='returns true if the password was successfully changed or removed, false or nil otherwise.' ,
            )
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='setTransferBoxVisible',
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
                                name='visible',
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
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description='' ,
                arguments={
                    "visible": """The new visibility state. """
                },
                result='returns true if the visibility was set successfully, false otherwise.' ,
            )
        )
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='setTransferBoxVisible',
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
                                name='visible',
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
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description='' ,
                arguments={
                    "visible": """The new visibility state. """
                },
                result='returns true if the visibility was set successfully, false otherwise.' ,
            )
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='shutdown',
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
                                name='reason',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=True,
                                ),
                                default_value='"Noreasonspecified"',
                            )
                        ]
                    ],
                    variable_length=False,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description='This function shuts down the server.\nMake sure your server ACL setup has function.shutdown object protected.' ,
                arguments={
                    "reason": """the reason why the server has been shutdown. """,
                    "exitCode": """the server application exit code to be returned on shutdown.
|20915}} """
                },
                result='returns false if it was not possible to shut down the server.' ,
            )
        )
        ],
        client=[
            
        ],
    )
]
