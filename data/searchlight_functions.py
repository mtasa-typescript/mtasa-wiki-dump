# Autogenerated file. ANY CHANGES WILL BE OVERWRITTEN
from to_python.core.types import FunctionType, \
    FunctionArgument, \
    FunctionArgumentValues, \
    FunctionReturnTypes, \
    FunctionSignature, \
    FunctionDoc, \
    FunctionOOP, \
    FunctionData, \
    CompoundFunctionData
    
DUMP_PARTIAL = [
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='createSearchLight',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['searchlight'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='startX',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='startY',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='startZ',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='endX',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='endY',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='endZ',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='startRadius',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='endRadius',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='renderSpot',
                                argument_type=FunctionType(
                                    names=['bool'],
                                    is_optional=True,
                                ),
                                default_value='true',
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
                    "startX": """: the X coordinate where the searchlight light cone will start. """,
                    "startY": """: the Y coordinate where the searchlight light cone will start. """,
                    "startZ": """: the Z coordinate where the searchlight light cone will start. """,
                    "endX": """: the X coordinate of the direction where the searchlight will point to. """,
                    "endY": """: the Y coordinate of the direction where the searchlight will point to. """,
                    "endZ": """: the Z coordinate of the direction where the searchlight will point to. """,
                    "startRadius": """: the radius of the searchlights light cone in its beginning. """,
                    "endRadius": """: the radius of the searchlights light cone in its end. """,
                    "renderSpot": """: if true, the searchlight will lighten the surface where it ends. """
                },
                result="""if every argument is correct and the limit of 1000 searchlights has not been reached, this function returns a element/searchlight|searchlight element. otherwise, it returns false. """,
            ),
            oop=FunctionOOP(
                description=None,
                class_name='Element/Searchlight|SearchLight',
                method_name=None,
                field=None,
                is_static=True,
            ),
            name='createSearchLight',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getSearchLightEndPosition',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                    FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                    FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theSearchLight',
                                argument_type=FunctionType(
                                    names=['searchlight'],
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
                description="""This function gets the end position of a Element/Searchlight|searchlight element. """,
                arguments={
                    "theSearchLight": """: the searchlight to get the position where the searchlights light cone ends. """
                },
                result="""if the specified searchlight element is valid, this function will return three float, which are the three coordinates of searchlights end position. if not, it will return false plus an error message. """,
            ),
            oop=FunctionOOP(
                description=None,
                class_name='Element/Searchlight|searchLight',
                method_name="""getEndPosition""",
                field="""endPosition""",
                is_static=False,
            ),
            name='getSearchLightEndPosition',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getSearchLightEndRadius',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theSearchLight',
                                argument_type=FunctionType(
                                    names=['searchlight'],
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
                description="""This function gets the end radius of a Element/Searchlight|searchlight element. """,
                arguments={
                    "theSearchLight": """: the searchlight to get the radius of the searchlights light cone in its end. """
                },
                result="""if the specified searchlight element is valid, this function will return one float, which is the searchlights end radius. if not, it will return false plus an error message. """,
            ),
            oop=FunctionOOP(
                description=None,
                class_name='Element/Searchlight|searchLight',
                method_name="""getEndRadius""",
                field="""endRadius""",
                is_static=False,
            ),
            name='getSearchLightEndRadius',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getSearchLightStartPosition',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                    FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                    FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theSearchLight',
                                argument_type=FunctionType(
                                    names=['searchlight'],
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
                description="""This function gets the start position of a Element/Searchlight|searchlight element. """,
                arguments={
                    "theSearchLight": """: the searchlight to get the position where the searchlights light cone starts. """
                },
                result="""if the specified searchlight element is valid, this function will return three float, which are the three coordinates of searchlights start position. if not, it will return false plus an error message. """,
            ),
            oop=FunctionOOP(
                description=None,
                class_name='Element/Searchlight|searchLight',
                method_name="""getStartPosition""",
                field="""startPosition""",
                is_static=False,
            ),
            name='getSearchLightStartPosition',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getSearchLightStartRadius',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theSearchLight',
                                argument_type=FunctionType(
                                    names=['searchlight'],
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
                description="""This function gets the start radius of a Element/Searchlight|searchlight element. """,
                arguments={
                    "theSearchLight": """: the searchlight to get the radius of the searchlights light cone in its beginning. """
                },
                result="""if the specified searchlight element is valid, this function will return one float, which is the searchlights start radius. if not, it will return false plus an error message. """,
            ),
            oop=FunctionOOP(
                description=None,
                class_name='Element/Searchlight|searchLight',
                method_name="""getStartRadius""",
                field="""startRadius""",
                is_static=False,
            ),
            name='getSearchLightStartRadius',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='setSearchLightEndPosition',
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
                                name='theSearchLight',
                                argument_type=FunctionType(
                                    names=['searchlight'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='endX',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='endY',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='endZ',
                                argument_type=FunctionType(
                                    names=['float'],
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
                description=""" """,
                arguments={
                    "theSearchLight": """: the searchlight to modify the property of. """,
                    "endX": """: the X coordinate where the searchlight light cone will end. """,
                    "endY": """: the Y coordinate where the searchlight light cone will end. """,
                    "endZ": """: the Z coordinate where the searchlight light cone will end. """
                },
                result="""if every argument is correct, this function returns true. if not, it will return false plus an error message. """,
            ),
            oop=FunctionOOP(
                description=None,
                class_name='Element/Searchlight|searchLight',
                method_name="""setEndPosition""",
                field="""endPosition""",
                is_static=False,
            ),
            name='setSearchLightEndPosition',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='setSearchLightEndRadius',
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
                                name='theSearchlight',
                                argument_type=FunctionType(
                                    names=['searchlight'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='endRadius',
                                argument_type=FunctionType(
                                    names=['float'],
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
                description="""This function sets the end radius of a Element/Searchlight|searchlight element. """,
                arguments={
                    "theSearchLight": """: the searchlight to modify the property of. """,
                    "endRadius": """: the radius of the searchlights light cone in its end. """
                },
                result="""if every argument is correct, this function returns true. if not, it will return false plus an error message. """,
            ),
            oop=FunctionOOP(
                description=None,
                class_name='Element/Searchlight|searchLight',
                method_name="""setEndRadius""",
                field="""endRadius""",
                is_static=False,
            ),
            name='setSearchLightEndRadius',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='setSearchLightStartPosition',
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
                                name='theSearchLight',
                                argument_type=FunctionType(
                                    names=['searchlight'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='startX',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='startY',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='startZ',
                                argument_type=FunctionType(
                                    names=['float'],
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
                description="""This function sets the start position of a Element/Searchlight|searchlight element. """,
                arguments={
                    "theSearchLight": """: the searchlight to modify the property of. """,
                    "startX": """: the X coordinate where the searchlight light cone will start. """,
                    "startY": """: the Y coordinate where the searchlight light cone will start. """,
                    "startZ": """: the Z coordinate where the searchlight light cone will start. """
                },
                result="""if every argument is correct, this function returns true. if not, it will return false plus an error message. """,
            ),
            oop=FunctionOOP(
                description=None,
                class_name='Element/Searchlight|searchLight',
                method_name="""setStartPosition""",
                field="""startPosition""",
                is_static=False,
            ),
            name='setSearchLightStartPosition',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='setSearchLightStartRadius',
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
                                name='theSearchlight',
                                argument_type=FunctionType(
                                    names=['searchlight'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='startRadius',
                                argument_type=FunctionType(
                                    names=['float'],
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
                description="""This function sets the start radius of a Element/Searchlight|searchlight element. """,
                arguments={
                    "theSearchLight": """: the searchlight to modify the property of. """,
                    "startRadius": """: the radius of the searchlights light cone in its beginning. """
                },
                result="""if every argument is correct, this function returns true. if not, it will return false plus an error message. """,
            ),
            oop=FunctionOOP(
                description=None,
                class_name='Element/Searchlight|searchLight',
                method_name="""setStartRadius""",
                field="""startRadius""",
                is_static=False,
            ),
            name='setSearchLightStartRadius',
        )
        ],
    )
]
