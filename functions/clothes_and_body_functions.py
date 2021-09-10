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
                name='getBodyPartName',
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
                                name='bodyPartID',
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
                description='This function is used to get the name of a body part on a player.' ,
                arguments={
                    "bodyPartID": """: An integer representing the body part ID you wish to retrieve the name of. """
                },
                result='this function returns a string containing the body part name if the id is valid, false otherwise.' ,
            ),
            url='getBodyPartName',
        )
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getBodyPartName',
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
                                name='bodyPartID',
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
                description='This function is used to get the name of a body part on a player.' ,
                arguments={
                    "bodyPartID": """: An integer representing the body part ID you wish to retrieve the name of. """
                },
                result='this function returns a string containing the body part name if the id is valid, false otherwise.' ,
            ),
            url='getBodyPartName',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='getClothesByTypeIndex',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
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
                                name='clothesType',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='clothesIndex',
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
                description='This function is used to get the texture and model of clothes by the clothes type and index.\n(Scans through the list of clothes for the specific type).' ,
                arguments={
                    "clothesType": """: An integer representing the clothes slot/type to scan through. """,
                    "clothesIndex": """: An integer representing the index (0 based) set of clothes in the list you wish to retrieve. Each type has a different number of valid indexes. """
                },
                result='this function returns 2 strings, a texture and model respectively, false if invalid arguments were passed to the function.' ,
            ),
            url='getClothesByTypeIndex',
        )
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getClothesByTypeIndex',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
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
                                name='clothesType',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='clothesIndex',
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
                description='This function is used to get the texture and model of clothes by the clothes type and index.\n(Scans through the list of clothes for the specific type).' ,
                arguments={
                    "clothesType": """: An integer representing the clothes slot/type to scan through. """,
                    "clothesIndex": """: An integer representing the index (0 based) set of clothes in the list you wish to retrieve. Each type has a different number of valid indexes. """
                },
                result='this function returns 2 strings, a texture and model respectively, false if invalid arguments were passed to the function.' ,
            ),
            url='getClothesByTypeIndex',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='getClothesTypeName',
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
                                name='clothesType',
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
                description='This function is used to get the name of a certain clothes type.' ,
                arguments={
                    "clothesType": """: An integer determining the type of clothes you want to get the clothes of. """
                },
                result='this function returns a string (the name of the clothes type) if found, false otherwise.' ,
            ),
            url='getClothesTypeName',
        )
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getClothesTypeName',
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
                                name='clothesType',
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
                description='This function is used to get the name of a certain clothes type.' ,
                arguments={
                    "clothesType": """: An integer determining the type of clothes you want to get the clothes of. """
                },
                result='this function returns a string (the name of the clothes type) if found, false otherwise.' ,
            ),
            url='getClothesTypeName',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='getTypeIndexFromClothes',
                return_types=FunctionReturnTypes(
                    return_types=[
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
                                name='clothesTexture',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='clothesModel',
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
                description='This function is used to get the clothes type and index from the texture and model.\n(Scans through the list of clothes for the specific type).' ,
                arguments={
                    "clothesTexture": """: A string determining the clothes texture that you wish to retrieve the type and index from. See the CJ Clothes|clothes catalog. """,
                    "clothesModel": """: A string determining the corresponding clothes model that you wish to retrieve the type and index from. See the CJ Clothes|clothes catalog. """
                },
                result='this function returns two integers, type and index respectively, false if invalid arguments were passed to the function.' ,
            ),
            url='getTypeIndexFromClothes',
        )
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getTypeIndexFromClothes',
                return_types=FunctionReturnTypes(
                    return_types=[
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
                                name='clothesTexture',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='clothesModel',
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
                description='This function is used to get the clothes type and index from the texture and model.\n(Scans through the list of clothes for the specific type).' ,
                arguments={
                    "clothesTexture": """: A string determining the clothes texture that you wish to retrieve the type and index from. See the CJ Clothes|clothes catalog. """,
                    "clothesModel": """: A string determining the corresponding clothes model that you wish to retrieve the type and index from. See the CJ Clothes|clothes catalog. """
                },
                result='this function returns two integers, type and index respectively, false if invalid arguments were passed to the function.' ,
            ),
            url='getTypeIndexFromClothes',
        )
        ],
    )
]
