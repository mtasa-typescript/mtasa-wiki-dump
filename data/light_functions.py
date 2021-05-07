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
                name='createLight',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['light'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='lightType',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='posX',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='posY',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='posZ',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
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
                                default_value='3',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='r',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=True,
                                ),
                                default_value='255',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='g',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=True,
                                ),
                                default_value='0',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='b',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=True,
                                ),
                                default_value='0',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='dirX',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value='0',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='dirY',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value='0',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='dirZ',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value='0',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='createsShadow',
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
            ),
            docs=FunctionDoc(
                description="""* The direction of the light only has any effect if the light type is spot light.
* One light will only apply illumination effects to Element/Ped|peds, Element/Player|players, wheels and number plates (like a emergency vehicle siren light does).
* Two or more lights will apply illumination effects to everything (excluding objects) that is in range of, at least, two of them. """,
                arguments={
                    "lightType": """An integer representing the type of light to create. """,
                    "posX": """A floating point number representing the X coordinate on the map. """,
                    "posY": """A floating point number representing the Y coordinate on the map. """,
                    "posZ": """A floating point number representing the Z coordinate on the map. """,
                    "radius": """A floating point number representing the radius of the light. """,
                    "r": """An integer number representing the amount of red to use in the colouring of the light (0 - 255). """,
                    "g": """An integer number representing the amount of green to use in the colouring of the light (0 - 255). """,
                    "b": """An integer number representing the amount of blue to use in the colouring of the light (0 - 255). """,
                    "dirX": """A floating point number representing the light directions X coordinate on the map. """,
                    "dirY": """A floating point number representing the light directions Y coordinate on the map. """,
                    "dirZ": """A floating point number representing the light directions Z coordinate on the map. """,
                    "createsShadow": """A boolean representing whether or not does the light cast shadows. """
                },
                result="""returns the element/light|light element if creation was successful, false otherwise. """,
            ),
            oop=FunctionOOP(
                description="""None """,
                class_name='Light',
                method_name='None',
                field='None',
                is_static=True,
            ),
            name='createLight',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getLightColor',
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
                                name='theLight',
                                argument_type=FunctionType(
                                    names=['light'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=False,
                ),
            ),
            docs=FunctionDoc(
                description="""This function returns the color for a Element/Light|light element. """,
                arguments={
                    "theLight": """The Element/Light|light that you wish to retrieve the color of. """
                },
                result="""returns three ints corresponding to the amount of red, green and blue (respectively) of the light, false if invalid arguments were passed. """,
            ),
            oop=FunctionOOP(
                description="""None """,
                class_name='light',
                method_name='getColor',
                field='color',
                is_static=False,
            ),
            name='getLightColor',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getLightDirection',
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
                                name='theLight',
                                argument_type=FunctionType(
                                    names=['light'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=False,
                ),
            ),
            docs=FunctionDoc(
                description="""This function returns the direction for a Element/Light|light element. """,
                arguments={
                    "theLight": """The Element/Light|light that you wish to retrieve the direction of. """
                },
                result="""returns three ints corresponding to the x, y and z coordinates (respectively) of the light direction, false if invalid arguments were passed. """,
            ),
            oop=FunctionOOP(
                description="""None """,
                class_name='light',
                method_name='getDirection',
                field='direction',
                is_static=False,
            ),
            name='getLightDirection',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getLightRadius',
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
                                name='theLight',
                                argument_type=FunctionType(
                                    names=['light'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=False,
                ),
            ),
            docs=FunctionDoc(
                description="""This function returns the radius for a Element/Light|light element. """,
                arguments={
                    "theLight": """The Element/Light|light that you wish to retrieve the radius of. """
                },
                result="""returns a float containing the radius of the specified light, false if invalid arguments were passed. """,
            ),
            oop=FunctionOOP(
                description="""None """,
                class_name='light',
                method_name='getRadius',
                field='radius',
                is_static=False,
            ),
            name='getLightRadius',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getLightType',
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
                        [
                            FunctionArgument(
                                name='theLight',
                                argument_type=FunctionType(
                                    names=['light'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=False,
                ),
            ),
            docs=FunctionDoc(
                description="""This function returns the type for a Element/Light|light element. """,
                arguments={
                    "theLight": """The Element/Light|light that you wish to retrieve the type of. """
                },
                result="""returns an int containing the type of the specified light, false if invalid arguments were passed. """,
            ),
            oop=FunctionOOP(
                description="""None """,
                class_name='light',
                method_name='getType',
                field='None',
                is_static=False,
            ),
            name='getLightType',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='setLightColor',
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
                                name='theLight',
                                argument_type=FunctionType(
                                    names=['light'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='r',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='g',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='b',
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
            ),
            docs=FunctionDoc(
                description="""This function sets the color for a Element/Light|light element. """,
                arguments={
                    "theLight": """The Element/Light|light that you wish to set the color of. """
                },
                result="""returns true if the function was successful, false otherwise. """,
            ),
            oop=FunctionOOP(
                description="""None """,
                class_name='light',
                method_name='setColor',
                field='color',
                is_static=False,
            ),
            name='setLightColor',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='setLightDirection',
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
                                name='theLight',
                                argument_type=FunctionType(
                                    names=['light'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
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
                        ]
                    ],
                    variable_length=False,
                ),
            ),
            docs=FunctionDoc(
                description="""This function sets the direction for a Element/Light|light element. """,
                arguments={
                    "theLight": """The Element/Light|light that you wish to set the direction of. """
                },
                result="""returns true if the function was successful, false otherwise. """,
            ),
            oop=FunctionOOP(
                description="""None """,
                class_name='light',
                method_name='setDirection',
                field='direction',
                is_static=False,
            ),
            name='setLightDirection',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='setLightRadius',
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
                                name='theLight',
                                argument_type=FunctionType(
                                    names=['light'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='radius',
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
            ),
            docs=FunctionDoc(
                description="""This function sets the radius for a Element/Light|light element. """,
                arguments={
                    "theLight": """The Element/Light|light that you wish to set the radius of. """
                },
                result="""returns true if the function was successful, false otherwise. """,
            ),
            oop=FunctionOOP(
                description="""None """,
                class_name='light',
                method_name='setRadius',
                field='radius',
                is_static=False,
            ),
            name='setLightRadius',
        )
        ],
    )
]
