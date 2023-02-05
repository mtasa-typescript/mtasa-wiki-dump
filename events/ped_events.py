# Autogenerated file. ANY CHANGES WILL BE OVERWRITTEN
from to_python.core.types import FunctionType, \
    FunctionArgument, \
    FunctionArgumentValues, \
    FunctionReturnTypes, \
    FunctionSignature, \
    FunctionDoc, \
    EventData, \
    CompoundEventData

DUMP_PARTIAL = [
    CompoundEventData(
        server=[
            
        ],
        client=[
            EventData(
            name='onClientPedDamage',
            docs=FunctionDoc(
                description='This event is triggered whenever a ped is damaged.' ,
                arguments={
                    "attacker": """: A player element representing the attacker or vehicle element (when a ped falls of a bike). """,
                    "weapon": """: An integer representing the Weapons|weapon ID the attacker used """,
                    "bodypart": """: An integer representing the bodypart the ped was damaged """,
                    "loss": """: A float representing the percentage of health the ped lost. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='attacker',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='weapon',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='bodypart',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='loss',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=False,
                ),
        )
        ],
    ),
    CompoundEventData(
        server=[
            
        ],
        client=[
            EventData(
            name='onClientPedHeliKilled',
            docs=FunctionDoc(
                description='This event is fired when a ped is killed due to the effect of a helicopter blades.' ,
                arguments={
                    "killer": """the vehicle (heli) responsible for causing the death. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='killer',
                                argument_type=FunctionType(
                                    names=['vehicle'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=False,
                ),
        )
        ],
    ),
    CompoundEventData(
        server=[
            
        ],
        client=[
            EventData(
            name='onClientPedHitByWaterCannon',
            docs=FunctionDoc(
                description='This event is fired when a ped is hit by a water cannon.' ,
                arguments={
                    "pedHit": """the ped which got shot by the water cannon """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='pedHit',
                                argument_type=FunctionType(
                                    names=['ped'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=False,
                ),
        )
        ],
    ),
    CompoundEventData(
        server=[
            
        ],
        client=[
            EventData(
            name='onClientPedStep',
            docs=FunctionDoc(
                description='This event is called when a peds foot has come on to the ground after jumping or taking a full step.' ,
                arguments={
                    "leftFoot": """:  a bool representing if it was the left foot that moved. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='leftFoot',
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
        )
        ],
    ),
    CompoundEventData(
        server=[
            
        ],
        client=[
            EventData(
            name='onClientPedVehicleEnter',
            docs=FunctionDoc(
                description='' ,
                arguments={
                    "theVehicle": """The vehicle that the ped entered. """,
                    "seat": """The seat that the ped now is on. Drivers seat = 0, higher numbers are passenger seats. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theVehicle',
                                argument_type=FunctionType(
                                    names=['vehicle'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='seat',
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
        )
        ],
    ),
    CompoundEventData(
        server=[
            
        ],
        client=[
            EventData(
            name='onClientPedVehicleExit',
            docs=FunctionDoc(
                description='' ,
                arguments={
                    "theVehicle": """The vehicle that the ped exited. """,
                    "seat": """The number of the seat that the ped was sitting on. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theVehicle',
                                argument_type=FunctionType(
                                    names=['vehicle'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='seat',
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
        )
        ],
    ),
    CompoundEventData(
        server=[
            
        ],
        client=[
            EventData(
            name='onClientPedWasted',
            docs=FunctionDoc(
                description='This event is triggered whenever a ped dies.' ,
                arguments={
                    "killer": """: A player, ped or vehicle element representing the killer. """,
                    "weapon": """: An int|integer representing the Weapons|killer weapon or the Damage Types|damage types. """,
                    "bodypart": """: An int|integer representing the bodypart the player was damaged. """,
                    "loss": """: A float representing the percentage of health the ped lost in the final hit. Note: Only for client-side created peds.
'''OR''' """,
                    "stealth": """: A boolean representing whether or not this was a stealth kill. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='killer',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='weapon',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='bodypart',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='loss',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            ),
                FunctionArgument(
                                name='stealth',
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
        )
        ],
    ),
    CompoundEventData(
        server=[
            
        ],
        client=[
            EventData(
            name='onClientPedWeaponFire',
            docs=FunctionDoc(
                description='This event is called when ped shoots a weapon.  This does not trigger for projectiles based, or melee weapons.' ,
                arguments={
                    "weapon": """:  an int representing weapons|weapon used for making a shot. """,
                    "ammo": """: an int ammount of ammo left for this weapon type. """,
                    "ammoInClip": """: an int ammount of ammo left for this weapon type in clip. """,
                    "hitX": """, hitY, hitZ: float world coordinates representing a hit point. """,
                    "hitElement": """: an element which was hit by a shot. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='weapon',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='ammo',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='ammoInClip',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='hitX',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='hitY',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='hitZ',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='hitElement',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=False,
                ),
        )
        ],
    ),
    CompoundEventData(
        server=[
            EventData(
            name='onPedDamage',
            docs=FunctionDoc(
                description='This event is triggered when a ped is damaged. For player damage, use onPlayerDamage instead.' ,
                arguments={
                    "loss": """: an int representing the percentage of health the ped lost. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='loss',
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
        )
        ],
        client=[
            
        ],
    ),
    CompoundEventData(
        server=[
            EventData(
            name='onPedVehicleEnter',
            docs=FunctionDoc(
                description='' ,
                arguments={
                    "theVehicle": """: A vehicle element representing the vehicle that was entered. """,
                    "seat": """: An int representing the seat in which the ped is entering. """,
                    "jacked": """: A player or ped element representing who has been jacked. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theVehicle',
                                argument_type=FunctionType(
                                    names=['vehicle'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='seat',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='jacked',
                                argument_type=FunctionType(
                                    names=['ped'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=False,
                ),
        )
        ],
        client=[
            
        ],
    ),
    CompoundEventData(
        server=[
            EventData(
            name='onPedVehicleExit',
            docs=FunctionDoc(
                description='' ,
                arguments={
                    "theVehicle": """: A vehicle element representing the vehicle in which the ped exited from. """,
                    "seat": """: An int representing the seat in which the ped was before exiting. """,
                    "jacker": """: A player or ped element representing who jacked the driver. """,
                    "forcedByScript": """A boolean representing whether the exit was forced using removePedFromVehicle or by the ped. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theVehicle',
                                argument_type=FunctionType(
                                    names=['vehicle'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='seat',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='jacker',
                                argument_type=FunctionType(
                                    names=['ped'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='forcedByScript',
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
        )
        ],
        client=[
            
        ],
    ),
    CompoundEventData(
        server=[
            EventData(
            name='onPedWasted',
            docs=FunctionDoc(
                description='This event is triggered when a ped is killed or dies. It is not triggered for players.' ,
                arguments={
                    "totalAmmo": """: an int representing the total ammo the victim had when he died. """,
                    "killer": """: an element representing the player, ped or vehicle who was the killer.  If there was no killer this is false. """,
                    "killerWeapon": """: an int representing the Weapons|killer weapon or the Damage Types|damage types. """,
                    "bodypart": """: an int representing the bodypart ID the victim was hit on when he died. """,
                    "stealth": """: a boolean representing whether or not this was a stealth kill. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='totalAmmo',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='killer',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='killerWeapon',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='bodypart',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='stealth',
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
        )
        ],
        client=[
            
        ],
    ),
    CompoundEventData(
        server=[
            EventData(
            name='onPedWeaponSwitch',
            docs=FunctionDoc(
                description='This event is triggered when a ped switches weapons.' ,
                arguments={
                    "previousWeaponID": """: an int representing the weapon that was switched from. """,
                    "currentWeaponID": """: an int representing the weapon that was switched to. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='previousWeaponID',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='currentWeaponID',
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
        )
        ],
        client=[
            
        ],
    )
]
