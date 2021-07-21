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
    CompoundEventData(server=[], client=[EventData(
            name='onClientTrailerAttach',
            docs=FunctionDoc(
                description="""This event is triggered by a trailer when it gets attached to a towing vehicle. """,
                arguments={
                    "towedBy": """the vehicle that is now towing the trailer. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='towedBy',
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
        )]),
    CompoundEventData(server=[], client=[EventData(
            name='onClientTrailerDetach',
            docs=FunctionDoc(
                description="""This event is triggered when a trailer gets detached from its towing vehicle. """,
                arguments={
                    "towedBy": """the vehicle that was towing the trailer. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='towedBy',
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
        )]),
    CompoundEventData(server=[], client=[EventData(
            name='onClientVehicleCollision',
            docs=FunctionDoc(
                description="""This event is triggered when a vehicle collides with an element or a world object.
Note that the collision reported by this event doesnt always damage the vehicle by default (this event triggers when hitting lamp posts, but the vehicle isnt damaged by them automatically, for example). If you want to deal with real damage, please refer to onClientVehicleDamage. """,
                arguments={
                    "theHitElement": """the other entity, or nil if the vehicle collided with the world """,
                    "damageImpulseMag": """the impact magnitude (Note: this is NOT the damage it is a force value which is then multiplied by the vehicles collision damage multiplier. for an example of this see below) """,
                    "bodyPart": """the bodypart that hit the other element """,
                    "collisionX/Y/Z": """the position the collision took place """,
                    "normalX/Y/Z": """the surface normal of the hit object """,
                    "hitElementforce": """0 for non vehicles or the force of the other vehicle """,
                    "model": """model of the hit element (useful to detect building collisions as hitElement will be nil) """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theHitElement',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='damageImpulseMag',
                                argument_type=FunctionType(
                                    names=['float'],
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
                                name='collisionX',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='collisionY',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='collisionZ',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='normalX',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='normalY',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='normalZ',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='hitElementForce',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='model',
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
        )]),
    CompoundEventData(server=[], client=[EventData(
            name='onClientVehicleDamage',
            docs=FunctionDoc(
                description="""This event is triggered when a vehicle is damaged. """,
                arguments={
                    "theAttacker": """: An element if there was an attacker. """,
                    "theWeapon": """: An integer specifying the Weapons|weapon ID if a weapon was used. Otherwise Damage Types|Damage Type ID is used. """,
                    "loss": """: A float representing the amount of damage taken. """,
                    "damagePosX": """: A float representing the X co-ordinate of where the damage took place. """,
                    "damagePosY": """: A float representing the Y co-ordinate of where the damage took place. """,
                    "damagePosZ": """: A float representing the Z co-ordinate of where the damage took place. """,
                    "tireID": """: A number representing the tire which took damage, if there is one. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theAttacker',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='theWeapon',
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
                            )
                        ],
                        [
                            FunctionArgument(
                                name='damagePosX',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='damagePosY',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='damagePosZ',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='tireID',
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
        )]),
    CompoundEventData(server=[], client=[EventData(
            name='onClientVehicleEnter',
            docs=FunctionDoc(
                description="""This event gets fired when a player or ped enters a vehicle. """,
                arguments={
                    "thePed": """the player or ped that entered the vehicle """,
                    "seat": """the number of the seat that the ped is now sitting on. 0 = driver, higher numbers are passenger seats. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='thePed',
                                argument_type=FunctionType(
                                    names=['ped'],
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
        )]),
    CompoundEventData(server=[], client=[EventData(
            name='onClientVehicleExit',
            docs=FunctionDoc(
                description="""This event gets fired when a ped or player gets out of a vehicle. """,
                arguments={
                    "thePed": """the player or ped element that exited the vehicle """,
                    "seat": """the number of the seat that the player was sitting on. 0 = driver, higher numbers are passenger seats. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='thePed',
                                argument_type=FunctionType(
                                    names=['ped'],
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
        )]),
    CompoundEventData(server=[], client=[EventData(
            name='onClientVehicleExplode',
            docs=FunctionDoc(
                description="""This event is triggered when a vehicle explodes. """,
                arguments={
                    
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        
                    ],
                    variable_length=False,
                ),
        )]),
    CompoundEventData(server=[], client=[EventData(
            name='onClientVehicleNitroStateChange',
            docs=FunctionDoc(
                description="""This event gets triggered when nitro state is changing. """,
                arguments={
                    "state": """current state of nitro """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='state',
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
        )]),
    CompoundEventData(server=[], client=[EventData(
            name='onClientVehicleRespawn',
            docs=FunctionDoc(
                description="""This event is triggered when a vehicle respawns. """,
                arguments={
                    
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        
                    ],
                    variable_length=False,
                ),
        )]),
    CompoundEventData(server=[], client=[EventData(
            name='onClientVehicleStartEnter',
            docs=FunctionDoc(
                description="""This event is triggered when a ped or player starts entering a vehicle. Once the entering animation completes, onClientVehicleEnter is triggered. """,
                arguments={
                    "thePed": """the ped that just started entering a vehicle. """,
                    "seat": """the number of the seat he is going to sit on. """,
                    "door": """An integer of which door the ped used (0-3). 0 is driver side door, 1 is front passenger, 2 is back left, 3 is back right. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='thePed',
                                argument_type=FunctionType(
                                    names=['ped'],
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
                                name='door',
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
        )]),
    CompoundEventData(server=[], client=[EventData(
            name='onClientVehicleStartExit',
            docs=FunctionDoc(
                description="""This event is triggered when a ped or player starts exiting a vehicle. Once the exiting animation completes, onClientVehicleExit is triggered. """,
                arguments={
                    "thePed": """the ped who started exiting the vehicle. """,
                    "seat": """the number of the seat that the ped was sitting on. """,
                    "door": """the number of the door that the ped is using to leave. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='thePed',
                                argument_type=FunctionType(
                                    names=['ped'],
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
                                name='door',
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
        )]),
    CompoundEventData(server=[EventData(
            name='onTrailerAttach',
            docs=FunctionDoc(
                description="""This event is triggered when a trailer is attached to a truck or when a tow truck hooks on to a vehicle. """,
                arguments={
                    "theTruck": """: the truck vehicle that got attached to this trailer. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theTruck',
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
        )], client=[]),
    CompoundEventData(server=[EventData(
            name='onTrailerDetach',
            docs=FunctionDoc(
                description="""This event is triggered when a trailer is detached from a truck. """,
                arguments={
                    "theTruck": """: the truck vehicle that this trailer got detached from. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theTruck',
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
        )], client=[]),
    CompoundEventData(server=[EventData(
            name='onVehicleDamage',
            docs=FunctionDoc(
                description="""This event is triggered when a vehicle is damaged. If you want to get the attacker you can use onClientVehicleDamage. """,
                arguments={
                    "loss": """: a float representing the amount of health the vehicle lost. """
                },
                result=""" """,
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
        )], client=[]),
    CompoundEventData(server=[EventData(
            name='onVehicleEnter',
            docs=FunctionDoc(
                description="""This event is triggered when a player or ped enters a vehicle. """,
                arguments={
                    "thePed": """: a player or ped element who is entering the vehicle. """,
                    "seat": """: an int representing the seat in which the ped is entering. Seat 0 is the drivers seat. """,
                    "jacked": """: a player or ped element representing who has been jacked. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='thePed',
                                argument_type=FunctionType(
                                    names=['ped'],
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
                                    names=['player'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=False,
                ),
        )], client=[]),
    CompoundEventData(server=[EventData(
            name='onVehicleExit',
            docs=FunctionDoc(
                description="""This event is triggered when a player or ped leaves a vehicle. """,
                arguments={
                    "thePed": """: a player or ped element who exited the vehicle. """,
                    "seat": """: an int representing the seat in which the ped exited from. """,
                    "jacker": """: a player or ped element who jacked the driver. """,
                    "forcedByScript": """a boolean representing whether the exit was forced using removePedFromVehicle or by the ped/player. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='thePed',
                                argument_type=FunctionType(
                                    names=['ped'],
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
        )], client=[]),
    CompoundEventData(server=[EventData(
            name='onVehicleExplode',
            docs=FunctionDoc(
                description="""This event is triggered when a vehicle explodes. """,
                arguments={
                    
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        
                    ],
                    variable_length=False,
                ),
        )], client=[]),
    CompoundEventData(server=[EventData(
            name='onVehicleRespawn',
            docs=FunctionDoc(
                description="""This event is triggered when a vehicle is respawned due. See toggleVehicleRespawn. """,
                arguments={
                    "exploded": """: true if this vehicle respawned because it exploded, false if it respawned due to being deserted. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='exploded',
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
        )], client=[]),
    CompoundEventData(server=[EventData(
            name='onVehicleStartEnter',
            docs=FunctionDoc(
                description="""This event is triggered when a player or ped starts to enter a vehicle. This event can be used to cancel entry, if necessary. """,
                arguments={
                    "enteringPed": """: a player or ped element who is starting to enter a vehicle. """,
                    "seat": """: an int representing the seat in which the ped is entering. """,
                    "jacked": """: a player or ped element representing who is going to be jacked. """,
                    "door": """: an int of which door is being used (0-3). 0 is driver side door, 1 is front passenger, 2 is back left, 3 is back right. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='enteringPed',
                                argument_type=FunctionType(
                                    names=['ped'],
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
        )], client=[]),
    CompoundEventData(server=[EventData(
            name='onVehicleStartExit',
            docs=FunctionDoc(
                description="""This event is triggered when a player or ped starts to exit a vehicle. This event can be used to cancel exit, if necessary. """,
                arguments={
                    "exitingPed": """: a player or ped element who is starting to exit a vehicle. """,
                    "seat": """: an int representing the seat in which the ped is exiting from. """,
                    "jacked": """: a player or ped element representing who is jacking. """,
                    "door": """: an int representing the door that the ped is using to leave. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='exitingPed',
                                argument_type=FunctionType(
                                    names=['ped'],
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
                        ],
                        [
                            FunctionArgument(
                                name='door',
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
        )], client=[])
]
