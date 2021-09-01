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
                name='createWeapon',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['weapon'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theType',
                                argument_type=FunctionType(
                                    names=['string'],
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
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description="""Creates a Element/Weapon|custom weapon that can fire bullets. Do not confuse this with player held weapons. """,
                arguments={
                    "theType": """The weapon type which can be: """,
                    "x": """The x position to create the weapon. """,
                    "y": """The y position to create the weapon. """,
                    "z": """The z position to create the weapon. """
                },
                result="""returns a element/weapon|custom weapon element, which represents a weapon floating at that position. """,
            ),
            name='createWeapon',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='fireWeapon',
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
                description="""Fires one shot from a Element/Weapon|custom weapon. """,
                arguments={
                    "theWeapon": """The weapon to be fired. """
                },
                result="""returns true if the shot weapon is valid and therefore the shot was fired, false otherwise. """,
            ),
            name='fireWeapon',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getWeaponAmmo',
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
                description="""This function gets the total ammo a Element/Weapon|custom weapon has. """,
                arguments={
                    "theWeapon": """: The weapon to get the ammo of. """
                },
                result="""returns an int|integer containing how many ammo left has the weapon. returns false if an error occured. """,
            ),
            name='getWeaponAmmo',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getWeaponClipAmmo',
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
                description="""This function gets the amount of ammo left in a Element/Weapon|custom weapons magazine/clip. """,
                arguments={
                    "theWeapon": """the weapon to get the clip ammo of. """
                },
                result="""returns the amount of ammo in the element/weapon|custom weapons clip, false if an error occured. """,
            ),
            name='getWeaponClipAmmo',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getWeaponFiringRate',
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
                description="""This gets the firing rate to be used when a Element/Weapon|custom weapon opens fire. """,
                arguments={
                    "theWeapon": """The weapon to modify the firing rate of. """
                },
                result="""returns an integer with the firing rate of the custom weapon, false otherwise. """,
            ),
            name='getWeaponFiringRate',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getWeaponFlags',
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
                description="""This function gets the flags of a Element/Weapon|custom weapon. """,
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
                result="""returns the true or false on success (flags flag returns 8 values) if the flag is enabled or not. returns false if the weapon element isnt valid or an error occured. """,
            ),
            name='getWeaponFlags',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getWeaponOwner',
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
                description="""This function gets the owner of a Element/Weapon|custom weapon. Weapon ownership system was, however, disabled, so this function always returns false. Please refer to setWeaponOwner for details. """,
                arguments={
                    "theWeapon": """The weapon to get the owner of. """
                },
                result="""this function was intended to return the player which owns the element/weapon|custom weapon, and false if an error occured. however, at the moment it always returns false. """,
            ),
            name='getWeaponOwner',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getWeaponState',
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
                description="""This function gets the state of a Element/Weapon|custom weapon. """,
                arguments={
                    "theWeapon": """the Element/Weapon|weapon to get the state of. """
                },
                result="""* a string if the element/weapon|weapon is valid, indicating the weapon state, which can be:
** reloading: the weapon is reloading.
** firing: the weapon is constantly shooting (unless any shooting blocking flags are set) according to its assigned firing rate.
** ready: the weapon is idle.
* false if an error occured or the element/weapon|weapon is invalid. """,
            ),
            name='getWeaponState',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='getWeaponTarget',
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
                description="""This functions gets the target of a Element/Weapon|custom weapon. """,
                arguments={
                    "theWeapon": """The weapon to get the target of. """
                },
                result="""* returns the target of the element/weapon|custom weapon, which can be:
**nil if the weapon is in rotation based targeting.
**3 float|floats if the weapon is firing at a fixed point.
**an element if the weapon is firing an entity.
* returns false if the weapon element is not valid. """,
            ),
            name='getWeaponTarget',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='resetWeaponFiringRate',
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
                description="""This function resets the firing rate of a Element/Weapon|custom weapon to the default one. """,
                arguments={
                    "theWeapon": """the weapon to reset the firing rate of. """
                },
                result="""returns true on success, false otherwise. """,
            ),
            name='resetWeaponFiringRate',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='setWeaponClipAmmo',
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
                description="""This function sets the ammo left in a Element/Weapon|custom weapons magazine/clip. """,
                arguments={
                    "theWeapon": """The Element/Weapon|weapon to set the clip ammo of. """,
                    "clipAmmo": """The amount of ammo in the clip. """
                },
                result="""this function returns true if the arguments are valid and the weapon clip ammo could be changed; false otherwise. """,
            ),
            name='setWeaponClipAmmo',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='setWeaponFiringRate',
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
                description="""This function sets the firing rate to be used when a Element/Weapon|custom weapon is in firing state. """,
                arguments={
                    "theWeapon": """The weapon to modify the firing rate of. """,
                    "firingRate": """The weapon firing rate. It seems to be a kind of frecuency value, so the lower the quicker the Element/Weapon|custom weapon will shoot. """
                },
                result="""returns true on success, false otherwise. """,
            ),
            name='setWeaponFiringRate',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='setWeaponFlags',
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
                description="""This function sets a Element/Weapon|custom weapon flags, used to change how it behaves or finds a possible target to shoot. """,
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
                result="""returns true if all arguments are valid and the flags where changed; false otherwise. """,
            ),
            name='setWeaponFlags',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='setWeaponState',
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
                description="""This function sets a Element/Weapon|custom weapons state. """,
                arguments={
                    "theWeapon": """: the weapon you wish to set the state of. """,
                    "theState": """: the state you wish to set: """,
                    "reloading": """: makes the weapon reload. """,
                    "firing": """: makes the weapon constantly fire its target (unless any shooting blocking flags are set) according to its assigned firing rate. """,
                    "ready": """: makes the weapon stop reloading or firing. """
                },
                result="""returns true on success, false otherwise. """,
            ),
            name='setWeaponState',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='setWeaponTarget',
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
                                name='theTarget',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='theComponent',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=True,
                                ),
                                default_value='255',
                            )
                        ]
                    ],
                    variable_length=False,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description="""This function sets the target of a Element/Weapon|custom weapon. There are 3 different targeting modes, which are explained below. """,
                arguments={
                    "theWeapon": """The weapon to clear the target of. """,
                    "theTarget": """The element to shoot at. It can be a player, ped, vehicle or object. """,
                    "theComponent": """The component of the target to shoot at. This argument is only relevant when used in the following element types: """,
                    "Vehicle|Vehicles": """: """,
                    "0": """: front left tire. """,
                    "1": """BONE_PELVIS1 position. """,
                    "2": """BONE_PELVIS position. """,
                    "3": """BONE_SPINE1 position. """,
                    "255": """: center of the ped (position returned by getElementPosition). """,
                    "Ped|Peds": """(players not included; see getPedBonePosition to know where is located each bone): """,
                    "4": """BONE_UPPERTORSO position. """,
                    "5": """BONE_NECK position. """,
                    "6": """BONE_HEAD2 position. """,
                    "7": """BONE_HEAD1 position. """,
                    "8": """BONE_HEAD position. """,
                    "21": """BONE_RIGHTUPPERTORSO position. """,
                    "22": """BONE_RIGHTSHOULDER position. """,
                    "23": """BONE_RIGHTELBOW position. """,
                    "24": """BONE_RIGHTWRIST position. """,
                    "25": """BONE_RIGHTHAND position. """,
                    "26": """BONE_RIGHTTHUMB position. """,
                    "31": """BONE_LEFTUPPERTORSO position. """,
                    "32": """BONE_LEFTSHOULDER position. """,
                    "33": """BONE_LEFTELBOW position. """,
                    "34": """BONE_LEFTWRIST position. """,
                    "35": """BONE_LEFTHAND position. """,
                    "36": """BONE_LEFTTHUMB position. """,
                    "41": """BONE_LEFTHIP position. """,
                    "42": """BONE_LEFTKNEE position. """,
                    "43": """BONE_LEFTANKLE position. """,
                    "44": """BONE_LEFTFOOT position. """,
                    "51": """BONE_RIGHTHIP position. """,
                    "52": """BONE_RIGHTKNEE position. """,
                    "53": """BONE_RIGHTANKLE position. """,
                    "54": """BONE_RIGHTFOOT position. """,
                    "targetX": """The target X. """,
                    "targetY": """The target Y. """,
                    "targetZ": """The target Z. """
                },
                result="""returns true on success, false otherwise.
returns true on success, false otherwise.
returns true on success, false otherwise. """,
            ),
            name='setWeaponTarget',
        )
        ],
    )
]
