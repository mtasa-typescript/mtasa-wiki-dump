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
            FunctionOOP(
                description=None,
                base_function_name="createWeapon",
                class_name='Element/Weapon|Weapon',
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
            FunctionOOP(
                description=None,
                base_function_name="fireWeapon",
                class_name='Element/Weapon|weapon',
                method=FunctionData(
            signature=FunctionSignature(
                name='fire',
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
                        ]
                    ],
                    variable_length=False,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description='Fires one shot from a Element/Weapon|custom weapon.' ,
                arguments={
                    "theWeapon": """The weapon to be fired. """
                },
                result='returns true if the shot weapon is valid and therefore the shot was fired, false otherwise.' ,
            ),
            url='fireWeapon',
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
            FunctionOOP(
                description=None,
                base_function_name="getWeaponAmmo",
                class_name='Element/Weapon|weapon',
                method=FunctionData(
            signature=FunctionSignature(
                name='getAmmo',
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
                                name='theWeapon',
                                argument_type=FunctionType(
                                    names=['weapon'],
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
                description='This function gets the total ammo a Element/Weapon|custom weapon has.' ,
                arguments={
                    "theWeapon": """: The weapon to get the ammo of. """
                },
                result='returns an int|integer containing how many ammo left has the weapon. returns false if an error occured.' ,
            ),
            url='getWeaponAmmo',
        ),
                field=FunctionOOPField(
                                name='ammo',
                                types=[
                                    FunctionType(
                                    names=['int'],
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
            FunctionOOP(
                description=None,
                base_function_name="getWeaponClipAmmo",
                class_name='Element/Weapon|weapon',
                method=FunctionData(
            signature=FunctionSignature(
                name='getClipAmmo',
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
                                name='theWeapon',
                                argument_type=FunctionType(
                                    names=['weapon'],
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
                description='This function gets the amount of ammo left in a Element/Weapon|custom weapons magazine/clip.' ,
                arguments={
                    "theWeapon": """the weapon to get the clip ammo of. """
                },
                result='returns the amount of ammo in the element/weapon|custom weapons clip, false if an error occured.' ,
            ),
            url='getWeaponClipAmmo',
        ),
                field=FunctionOOPField(
                                name='clipAmmo',
                                types=[
                                    FunctionType(
                                    names=['int'],
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
            FunctionOOP(
                description=None,
                base_function_name="getWeaponFiringRate",
                class_name='Element/Weapon|weapon',
                method=FunctionData(
            signature=FunctionSignature(
                name='getFiringRate',
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
                                name='theWeapon',
                                argument_type=FunctionType(
                                    names=['weapon'],
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
                description='This gets the firing rate to be used when a Element/Weapon|custom weapon opens fire.' ,
                arguments={
                    "theWeapon": """The weapon to modify the firing rate of. """
                },
                result='returns an integer with the firing rate of the custom weapon, false otherwise.' ,
            ),
            url='getWeaponFiringRate',
        ),
                field=FunctionOOPField(
                                name='firingRate',
                                types=[
                                    FunctionType(
                                    names=['int'],
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
            FunctionOOP(
                description=None,
                base_function_name="getWeaponFlags",
                class_name='Element/Weapon|weapon',
                method=FunctionData(
            signature=FunctionSignature(
                name='getFlags',
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
                                name='theFlag',
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
                description='This function gets the flags of a Element/Weapon|custom weapon.' ,
                arguments={
                    "theWeapon": """the weapon to get the flag of. """,
                    "theFlag": """the weapon flag to get: """,
                    "disable_model": """: makes the weapon and muzzle effect invisible or not. """,
                    "flags": """: returns the flags used to get where the gun shoots at. These flags are (by order): """,
                    "checkBuildings": """: allows the shoot to be blocked by GTAs internally placed buildings, i.e. the world map. """,
                    "checkCarTires": """: allows the shoot to be blocked by vehicle tires. """,
                    "checkDummies": """: allows the shoot to be blocked by GTAs internal dummies. These are not used in the current MTA version so this argument can be set to false. """,
                    "checkObjects": """: allows the shoot to be blocked by object|objects. """,
                    "checkPeds": """: allows the shoot to be blocked by ped|peds and player|players. """,
                    "checkVehicles": """: allows the shoot to be blocked by vehicle|vehicles. """,
                    "checkSeeThroughStuff": """: allows the shoot to be blocked by translucent game objects, e.g. glass. """,
                    "checkShootThroughStuff": """: allows the shoot to be blocked by things that can be shot through. """,
                    "instant_reload": """: if enabled, the weapon reloads instantly rather than waiting the reload time until shooting again. """,
                    "shoot_if_out_of_range": """: if enabled, the weapon still fires its target beyond the weapon range distance. """,
                    "shoot_if_blocked": """: if enabled, the weapon still fires its target even if its blocked by something. """
                },
                result='returns the true or false on success (flags flag returns 8 values) if the flag is enabled or not. returns false if the weapon element isnt valid or an error occured.' ,
            ),
            url='getWeaponFlags',
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
            FunctionOOP(
                description="""Pair is completely disabled at the moment (its value is ''[[nil]]'').""",
                base_function_name="getWeaponOwner",
                class_name='Element/Weapon|weapon',
                method=FunctionData(
            signature=FunctionSignature(
                name='getOwner',
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
                        ]
                    ],
                    variable_length=False,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description='This function gets the owner of a Element/Weapon|custom weapon. Weapon ownership system was, however, disabled, so this function always returns false. Please refer to setWeaponOwner for details.' ,
                arguments={
                    "theWeapon": """The weapon to get the owner of. """
                },
                result='this function was intended to return the player which owns the element/weapon|custom weapon, and false if an error occured. however, at the moment it always returns false.' ,
            ),
            url='getWeaponOwner',
        ),
                field=FunctionOOPField(
                                name='owner',
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
            FunctionOOP(
                description=None,
                base_function_name="getWeaponState",
                class_name='Element/Weapon|weapon',
                method=FunctionData(
            signature=FunctionSignature(
                name='getState',
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
                                name='theWeapon',
                                argument_type=FunctionType(
                                    names=['weapon'],
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
                description='This function gets the state of a Element/Weapon|custom weapon.' ,
                arguments={
                    "theWeapon": """the Element/Weapon|weapon to get the state of. """
                },
                result='* a string if the element/weapon|weapon is valid, indicating the weapon state, which can be:\n** reloading: the weapon is reloading.\n** firing: the weapon is constantly shooting (unless any shooting blocking flags are set) according to its assigned firing rate.\n** ready: the weapon is idle.\n* false if an error occured or the element/weapon|weapon is invalid.' ,
            ),
            url='getWeaponState',
        ),
                field=FunctionOOPField(
                                name='state',
                                types=[
                                    FunctionType(
                                    names=['string'],
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
            FunctionOOP(
                description="""Variable is read only.""",
                base_function_name="getWeaponTarget",
                class_name='Element/Weapon|weapon',
                method=FunctionData(
            signature=FunctionSignature(
                name='getTarget',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['nil', 'element', 'float'],
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
                        ]
                    ],
                    variable_length=False,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description='This functions gets the target of a Element/Weapon|custom weapon.' ,
                arguments={
                    "theWeapon": """The weapon to get the target of. """
                },
                result='* returns the target of the element/weapon|custom weapon, which can be:\n**nil if the weapon is in rotation based targeting.\n**3 float|floats if the weapon is firing at a fixed point.\n**an element if the weapon is firing an entity.\n* returns false if the weapon element is not valid.' ,
            ),
            url='getWeaponTarget',
        ),
                field=FunctionOOPField(
                                name='target',
                                types=[
                                    FunctionType(
                                    names=['nil', 'element', 'float'],
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
            FunctionOOP(
                description=None,
                base_function_name="resetWeaponFiringRate",
                class_name='Element/Weapon|weapon',
                method=FunctionData(
            signature=FunctionSignature(
                name='resetFiringRate',
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
                        ]
                    ],
                    variable_length=False,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description='This function resets the firing rate of a Element/Weapon|custom weapon to the default one.' ,
                arguments={
                    "theWeapon": """the weapon to reset the firing rate of. """
                },
                result='returns true on success, false otherwise.' ,
            ),
            url='resetWeaponFiringRate',
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
            FunctionOOP(
                description=None,
                base_function_name="setWeaponClipAmmo",
                class_name='Element/Weapon|weapon',
                method=FunctionData(
            signature=FunctionSignature(
                name='setClipAmmo',
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
                                name='clipAmmo',
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
                description='This function sets the ammo left in a Element/Weapon|custom weapons magazine/clip.' ,
                arguments={
                    "theWeapon": """The Element/Weapon|weapon to set the clip ammo of. """,
                    "clipAmmo": """The amount of ammo in the clip. """
                },
                result='this function returns true if the arguments are valid and the weapon clip ammo could be changed; false otherwise.' ,
            ),
            url='setWeaponClipAmmo',
        ),
                field=FunctionOOPField(
                                name='clipAmmo',
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
            FunctionOOP(
                description=None,
                base_function_name="setWeaponFiringRate",
                class_name='Element/Weapon|weapon',
                method=FunctionData(
            signature=FunctionSignature(
                name='setFiringRate',
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
                                name='firingRate',
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
                description='This function sets the firing rate to be used when a Element/Weapon|custom weapon is in firing state.' ,
                arguments={
                    "theWeapon": """The weapon to modify the firing rate of. """,
                    "firingRate": """The weapon firing rate. It seems to be a kind of frecuency value, so the lower the quicker the Element/Weapon|custom weapon will shoot. """
                },
                result='returns true on success, false otherwise.' ,
            ),
            url='setWeaponFiringRate',
        ),
                field=FunctionOOPField(
                                name='firingRate',
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
            FunctionOOP(
                description=None,
                base_function_name="setWeaponFlags",
                class_name='Element/Weapon|weapon',
                method=FunctionData(
            signature=FunctionSignature(
                name='setFlags',
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
                                name='theFlag',
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
                description='This function sets a Element/Weapon|custom weapon flags, used to change how it behaves or finds a possible target to shoot.' ,
                arguments={
                    "theWeapon": """the Element/Weapon|weapon element to set the flag of. """,
                    "theFlag": """the weapon flag to change (all of them can be true or false): """,
                    "disable_model": """: makes the weapon and muzzle effect invisible or not. """,
                    "flags": """: configures the flags used to get where the gun shoots at. They are based on processLineOfSights. You have to specify all the eight flags for the function to succeed. These flags are (by order): """,
                    "checkBuildings": """: allows the shoot to be blocked by GTAs internally placed buildings, i.e. the world map. """,
                    "checkCarTires": """: allows the shoot to be blocked by vehicle tires. """,
                    "checkDummies": """: allows the shoot to be blocked by GTAs internal dummies. These are not used in the current MTA version so this argument can be set to false. """,
                    "checkObjects": """: allows the shoot to be blocked by object|objects. """,
                    "checkPeds": """: allows the shoot to be blocked by ped|peds and player|players. """,
                    "checkVehicles": """: allows the shoot to be blocked by vehicle|vehicles. """,
                    "checkSeeThroughStuff": """: allows the shoot to be blocked by translucent game objects, e.g. glass. """,
                    "checkShootThroughStuff": """: allows the shoot to be blocked by things that can be shot through. """,
                    "instant_reload": """: if enabled, the weapon will reload instantly rather than waiting the reload time until shooting again. """,
                    "shoot_if_out_of_range": """: if enabled, the weapon will still fire its target beyond the weapon range distance. """,
                    "shoot_if_blocked": """: if enabled, the weapon will still fire its target even if its blocked by something. """,
                    "enable": """: whether to enable or disable the specified flag. """
                },
                result='returns true if all arguments are valid and the flags where changed; false otherwise.' ,
            ),
            url='setWeaponFlags',
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
            FunctionOOP(
                description=None,
                base_function_name="setWeaponState",
                class_name='Element/Weapon|weapon',
                method=FunctionData(
            signature=FunctionSignature(
                name='setState',
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
                                name='theState',
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
                description='This function sets a Element/Weapon|custom weapons state.' ,
                arguments={
                    "theWeapon": """: the weapon you wish to set the state of. """,
                    "theState": """: the state you wish to set: """,
                    "reloading": """: makes the weapon reload. """,
                    "firing": """: makes the weapon constantly fire its target (unless any shooting blocking flags are set) according to its assigned firing rate. """,
                    "ready": """: makes the weapon stop reloading or firing. """
                },
                result='returns true on success, false otherwise.' ,
            ),
            url='setWeaponState',
        ),
                field=FunctionOOPField(
                                name='state',
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
    )
]
