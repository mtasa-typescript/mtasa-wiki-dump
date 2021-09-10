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
            FunctionOOP(
                description="""This OOP syntax is for [[Element/Weapon|custom weapons]] only.""",
                base_function_name="getWeaponProperty",
                class_name='Element/Weapon|weapon',
                method=FunctionData(
            signature=FunctionSignature(
                name='getProperty',
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
                                name='weaponID',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            ),
                FunctionArgument(
                                name='weaponName',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='weaponSkill',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='property',
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
                description='This function gets a weapon property of the specified Element/Weapon|custom weapon (clientside only) or specified Weapons|player-held weapon (both client and server).' ,
                arguments={
                    "weaponID or weaponName": """The ID or name of the weapon you want to get info of. Names can be: """,
                    "weaponSkill": """Either: pro, std or poor """,
                    "property": """The property you want to get the value of:
The following properties are get only: """
                },
                result='on success:\nint: the weapon property\non failure:\nbool: false if the passed arguments were invalid' ,
            ),
            url='getWeaponProperty',
        ),
                field=None,
                is_static=False,
            )
        ],
        client=[
            FunctionOOP(
                description="""This OOP syntax is for [[Element/Weapon|custom weapons]] only.""",
                base_function_name="getWeaponProperty",
                class_name='Element/Weapon|weapon',
                method=FunctionData(
            signature=FunctionSignature(
                name='getProperty',
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
                                name='weaponID',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            ),
                FunctionArgument(
                                name='weaponName',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='weaponSkill',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='property',
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
                description='This function gets a weapon property of the specified Element/Weapon|custom weapon (clientside only) or specified Weapons|player-held weapon (both client and server).' ,
                arguments={
                    "weaponID or weaponName": """The ID or name of the weapon you want to get info of. Names can be: """,
                    "weaponSkill": """Either: pro, std or poor """,
                    "property": """The property you want to get the value of:
The following properties are get only: """
                },
                result='on success:\nint: the weapon property\non failure:\nbool: false if the passed arguments were invalid' ,
            ),
            url='getWeaponProperty',
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
            FunctionOOP(
                description=None,
                base_function_name="setWeaponProperty",
                class_name='Element/Weapon|weapon',
                method=FunctionData(
            signature=FunctionSignature(
                name='setProperty',
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
                                name='theWeapon',
                                argument_type=FunctionType(
                                    names=['weapon'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='strProperty',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='theValue',
                                argument_type=FunctionType(
                                    names=['value'],
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
                description='<section name=Server class=server show=true>\nThis function sets the weapon property of the specified weapons specified weapon type. See lower down the page for documentation related to weapon creation.\n<syntaxhighlight lang=lua>bool setWeaponProperty ( int weaponID/string weaponName, string weaponSkill, string property, int/float theValue )</syntaxhighlight>\n*weaponID: The ID or name of the Weapons|weapon you want to set a property of. Names can be:\n*weaponSkill: Either: pro, std or poor. The player must have this skill level set to have the effect.\n*property: The property you want to set the value of:\n*theValue: The value to set the property to.\nOn success:\nbool: Returns true if the weapon property was successfully set\nOn failure:\nbool: Returns false if the weapon property was unable to be set\n</section>\n<section name=Client class=client show=true>\n<p>The client side function only applies to custom weapons created client sided.</p>\n<syntaxhighlight lang=lua>bool setWeaponProperty ( weapon theWeapon, string strProperty, value theValue )</syntaxhighlight>\n* theWeapon: the weapon to change the property of.\n* strProperty: the property to edit:\n* theValue: The value to set the property to.\nReturns true if the property was set.\n</section>' ,
                arguments={
                    "theWeapon": """the weapon to change the property of. """,
                    "strProperty": """the property to edit: """,
                    "theValue": """The value to set the property to. """
                },
                result='returns true if the property was set.' ,
            ),
            url='setWeaponProperty',
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
    )
]
