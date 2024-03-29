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
                name='createProjectile',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['projectile'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
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
                        ],
                        [
                            FunctionArgument(
                                name='weaponType',
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
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='posY',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='posZ',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='force',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value='1.0',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='target',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=True,
                                ),
                                default_value='nil',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='rotX',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='rotY',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='rotZ',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='velX',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='velY',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='velZ',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='model',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=True,
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
                description='This function creates a projectile of the specified type on the specified coordinates.\n*Model argument is not synchronized between clients. Clients differs from local player see always standard projectile model.\n*Target argument can only be defined as a player or another projectile.' ,
                arguments={
                    "creator": """The element representing creator of the projectile. In case you want the projectile to be synced for everybody creator must be the local player or his vehicle. """,
                    "weaponType": """int representing the projectile weaponType (characteristics). Valid IDs are: """,
                    "posX": """, posY, posZ: float starting coordinates for the projectile. They are coordinates of creator by default. """,
                    "force": """: float representing the starting force for throwable projectiles. """,
                    "target": """: element target used for heat seeking rockets. """,
                    "rotX": """, rotY, rotZ: float starting rotation for the projectile. """,
                    "velX": """, velY, velZ: float starting velocity for the projectile. """,
                    "model": """: Integer representing the projectiles model, uses default model for weaponType if not specified. """
                },
                result='returns a projectile element if projectile creation was successful. returns false if unable to create a projectile (wrong weapon id or projectiles limit was reached).' ,
            ),
            url='createProjectile',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='detonateSatchels',
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
                                name='Player',
                                argument_type=FunctionType(
                                    names=['player'],
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
                description='This function can be used to detonate a players satchels.' ,
                arguments={
                    
                },
                result='' ,
            ),
            url='detonateSatchels',
        )
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='detonateSatchels',
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
                description='This function can be used to detonate a players satchels.' ,
                arguments={
                    
                },
                result='' ,
            ),
            url='detonateSatchels',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getProjectileCounter',
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
                                name='projectile',
                                argument_type=FunctionType(
                                    names=['projectile'],
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
                description='Get the time left before a projectile detonates.' ,
                arguments={
                    "projectile": """: the projectile to get the timer of. """
                },
                result='returns the the time in milliseconds to detonation which depending on the projectile type will do different things:\n* grenades will explode when it hits 0\n* teargas may be a duration timer\n* both types of rockets will explode when it hits 0\n* satchels restarts so i do not think it does anything' ,
            ),
            url='getProjectileCounter',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getProjectileCreator',
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
                                name='theProjectile',
                                argument_type=FunctionType(
                                    names=['projectile'],
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
                description='This function returns the creator of the specified projectile.' ,
                arguments={
                    "theProjectile": """The projectiles| projectile element which creator you want to retrieve. """
                },
                result='returns the element which created the projectile if successful, false otherwise.' ,
            ),
            url='getProjectileCreator',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getProjectileForce',
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
                                name='theProjectile',
                                argument_type=FunctionType(
                                    names=['projectile'],
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
                description='This function returns the force of the specified projectile.' ,
                arguments={
                    "theProjectile": """The projectiles| projectile element which force you want to retrieve. """
                },
                result='returns a float if successful, false otherwise.' ,
            ),
            url='getProjectileForce',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getProjectileTarget',
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
                                name='theProjectile',
                                argument_type=FunctionType(
                                    names=['projectile'],
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
                description='This function returns the target of the specified projectile.' ,
                arguments={
                    "theProjectile": """The projectiles| projectile element which target you want to retrieve. """
                },
                result='returns the element which is the projectiles target if the projectile is valid and can have a target (like a heat-seeking rocket), false otherwise.' ,
            ),
            url='getProjectileTarget',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getProjectileType',
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
                                name='theProjectile',
                                argument_type=FunctionType(
                                    names=['projectile'],
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
                description='This function returns the type of the specified projectile.' ,
                arguments={
                    "theProjectile": """The Element/Projectile|projectile element which type you want to retrieve. """
                },
                result='returns an integer over the type of the projectile or false if invalid arguments were passed.' ,
            ),
            url='getProjectileType',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='setProjectileCounter',
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
                                name='projectile',
                                argument_type=FunctionType(
                                    names=['projectile'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='timeToDetonate',
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
                description='Will change the projectile counter timer which depending on the projectile type will do different things:\n* Rockets and Grenades will explode when it hits 0\n* Teargas may be a duration timer\n* Satchels restart (we currently assume it doesnt cause an effect)\n* Molotov will explode with search ground level when it hits 0' ,
                arguments={
                    "projectile": """The projectile to edit the timer of. """,
                    "timeToDetonate": """The time in milliseconds to detonation. """
                },
                result='returns true on success, false otherwise.' ,
            ),
            url='setProjectileCounter',
        )
        ],
    )
]
