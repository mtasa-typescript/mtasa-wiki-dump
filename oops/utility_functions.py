# Autogenerated file. ANY CHANGES WILL BE OVERWRITTEN
from to_python.core.types import FunctionType, \
    FunctionArgument, \
    FunctionArgumentValues, \
    FunctionReturnTypes, \
    FunctionSignature, \
    FunctionDoc, \
    FunctionOOP, \
    FunctionOOPField, \
    CompoundOOPData, \
    FunctionData, \
    CompoundFunctionData

DUMP_PARTIAL = [
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            FunctionOOP(
                description=None,
                base_function_name="getTimerDetails",
                class_name='timer',
                method=FunctionData(
            signature=FunctionSignature(
                name='getDetails',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                    FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                    FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theTimer',
                                argument_type=FunctionType(
                                    names=['timer'],
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
                description='This function is for getting the details of a running timer.' ,
                arguments={
                    "theTimer": """A timer element. """
                },
                result='* integer one represents the time left in miliseconds (1000th of a second) of the current time left in the loop.\n* integer two represents the amount of times the timer has left to execute.\n* integer three represents the time interval of timer.\n* returns false if the timer doesnt exist or stopped running. also, debugscript will say bad argument @ gettimerdetails. to prevent this, you can check if the timer exists with istimer().' ,
            ),
            url='getTimerDetails',
        ),
                field=None,
                is_static=False,
            )
        ],
        client=[
            FunctionOOP(
                description=None,
                base_function_name="getTimerDetails",
                class_name='timer',
                method=FunctionData(
            signature=FunctionSignature(
                name='getDetails',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                    FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                    FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theTimer',
                                argument_type=FunctionType(
                                    names=['timer'],
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
                description='This function is for getting the details of a running timer.' ,
                arguments={
                    "theTimer": """A timer element. """
                },
                result='* integer one represents the time left in miliseconds (1000th of a second) of the current time left in the loop.\n* integer two represents the amount of times the timer has left to execute.\n* integer three represents the time interval of timer.\n* returns false if the timer doesnt exist or stopped running. also, debugscript will say bad argument @ gettimerdetails. to prevent this, you can check if the timer exists with istimer().' ,
            ),
            url='getTimerDetails',
        ),
                field=None,
                is_static=False,
            )
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            FunctionOOP(
                description=None,
                base_function_name="isTimer",
                class_name='timer',
                method=FunctionData(
            signature=FunctionSignature(
                name='isValid',
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
                                name='theTimer',
                                argument_type=FunctionType(
                                    names=['timer'],
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
                description='This function checks if a variable is a timer.' ,
                arguments={
                    "theTimer": """: The variable that we want to check. """
                },
                result='returns true if the passed value is a timer, false otherwise.' ,
            ),
            url='isTimer',
        ),
                field=FunctionOOPField(
                                name='valid',
                                types=[
                                    FunctionType(
                                    names=['bool'],
                                    is_optional=False,
                                )
                                ],
                            ),
                is_static=False,
            )
        ],
        client=[
            FunctionOOP(
                description=None,
                base_function_name="isTimer",
                class_name='timer',
                method=FunctionData(
            signature=FunctionSignature(
                name='isValid',
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
                                name='theTimer',
                                argument_type=FunctionType(
                                    names=['timer'],
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
                description='This function checks if a variable is a timer.' ,
                arguments={
                    "theTimer": """: The variable that we want to check. """
                },
                result='returns true if the passed value is a timer, false otherwise.' ,
            ),
            url='isTimer',
        ),
                field=FunctionOOPField(
                                name='valid',
                                types=[
                                    FunctionType(
                                    names=['bool'],
                                    is_optional=False,
                                )
                                ],
                            ),
                is_static=False,
            )
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            FunctionOOP(
                description=None,
                base_function_name="killTimer",
                class_name='timer',
                method=FunctionData(
            signature=FunctionSignature(
                name='destroy',
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
                                name='theTimer',
                                argument_type=FunctionType(
                                    names=['timer'],
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
                description='This function allows you to kill/halt existing timers.' ,
                arguments={
                    "theTimer": """The timer you wish to halt. """
                },
                result='returns true if the timer was successfully killed, false if no such timer existed.' ,
            ),
            url='killTimer',
        ),
                field=None,
                is_static=False,
            )
        ],
        client=[
            FunctionOOP(
                description=None,
                base_function_name="killTimer",
                class_name='timer',
                method=FunctionData(
            signature=FunctionSignature(
                name='destroy',
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
                                name='theTimer',
                                argument_type=FunctionType(
                                    names=['timer'],
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
                description='This function allows you to kill/halt existing timers.' ,
                arguments={
                    "theTimer": """The timer you wish to halt. """
                },
                result='returns true if the timer was successfully killed, false if no such timer existed.' ,
            ),
            url='killTimer',
        ),
                field=None,
                is_static=False,
            )
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            FunctionOOP(
                description=None,
                base_function_name="resetTimer",
                class_name='timer',
                method=FunctionData(
            signature=FunctionSignature(
                name='reset',
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
                                name='theTimer',
                                argument_type=FunctionType(
                                    names=['timer'],
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
                description='This function allows you to reset the elapsed time in existing timers to zero. The function does not reset the times to execute count on timers which have a limited amout of repetitions.' ,
                arguments={
                    "theTimer": """The timer whose elapsed time you wish to reset. """
                },
                result='returns true if the timer was successfully reset, false otherwise.' ,
            ),
            url='resetTimer',
        ),
                field=None,
                is_static=False,
            )
        ],
        client=[
            FunctionOOP(
                description=None,
                base_function_name="resetTimer",
                class_name='timer',
                method=FunctionData(
            signature=FunctionSignature(
                name='reset',
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
                                name='theTimer',
                                argument_type=FunctionType(
                                    names=['timer'],
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
                description='This function allows you to reset the elapsed time in existing timers to zero. The function does not reset the times to execute count on timers which have a limited amout of repetitions.' ,
                arguments={
                    "theTimer": """The timer whose elapsed time you wish to reset. """
                },
                result='returns true if the timer was successfully reset, false otherwise.' ,
            ),
            url='resetTimer',
        ),
                field=None,
                is_static=False,
            )
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            FunctionOOP(
                description=None,
                base_function_name="setTimer",
                class_name='Timer',
                method=None,
                field=None,
                is_static=True,
            )
        ],
        client=[
            FunctionOOP(
                description=None,
                base_function_name="setTimer",
                class_name='Timer',
                method=None,
                field=None,
                is_static=True,
            )
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            
        ],
        client=[
            
        ],
    )
]
