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
            name='onClientElementColShapeHit',
            docs=FunctionDoc(
                description='This event is triggered when an element (like a player or vehicle) enters a collision shape.' ,
                arguments={
                    "theShape": """the colshape that the element entered. """,
                    "matchingDimension": """true if the element is in the same dimension as the colshape, false otherwise. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theShape',
                                argument_type=FunctionType(
                                    names=['colshape'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='matchingDimension',
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
            name='onClientElementColShapeLeave',
            docs=FunctionDoc(
                description='This event is triggered when an element (like a player or vehicle) leaves a collision shape.' ,
                arguments={
                    "theShape": """the colshape that the element left. """,
                    "matchingDimension": """true if the element is in the same dimension as the colshape, false otherwise. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theShape',
                                argument_type=FunctionType(
                                    names=['colshape'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='matchingDimension',
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
            name='onClientElementDataChange',
            docs=FunctionDoc(
                description='This event is triggered after an elements element data|data entry is changed. Such changes can be made on the client or the server using setElementData.' ,
                arguments={
                    "theKey": """: The name of the element data entry that has changed. """,
                    "oldValue": """: The old value of this entry before it changed. See element data for a list of possible datatypes. """,
                    "newValue": """: the new value of this entry after it changed. This will be equivalent to getElementData(source, theKey). """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theKey',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='oldValue',
                                argument_type=FunctionType(
                                    names=['var'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='newValue',
                                argument_type=FunctionType(
                                    names=['var'],
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
            name='onClientElementDestroy',
            docs=FunctionDoc(
                description='This event is triggered when an element gets destroyed by destroyElement or when the creator resource is stopping. It is also triggered when a children element of this element is destroyed. It is not triggered on a player when they quit.' ,
                arguments={
                    
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        
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
            name='onClientElementDimensionChange',
            docs=FunctionDoc(
                description='' ,
                arguments={
                    "oldDimension": """: An int representing the dimension the element was in before. """,
                    "newDimension": """: An int representing the dimension the element is in now. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='oldDimension',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='newDimension',
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
            name='onClientElementInteriorChange',
            docs=FunctionDoc(
                description='' ,
                arguments={
                    "oldInterior": """: An int representing the interior the element was in before. """,
                    "newInterior": """: An int representing the interior the element is in now. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='oldInterior',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='newInterior',
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
            name='onClientElementModelChange',
            docs=FunctionDoc(
                description='' ,
                arguments={
                    "oldModel": """an int representing the model of the element before the change occurred. """,
                    "newModel": """an int representing the new model of the element. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='oldModel',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='newModel',
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
            name='onClientElementStreamIn',
            docs=FunctionDoc(
                description='This event is triggered whenever a physical element is streamed in. This is triggered for all elements that are streamable, such as players, peds, vehicles, objects and markers. When this event is triggered, that element is guaranteed to be physically created as a GTA object.\nBe aware that this event triggers for local player (as itself being the element that got streamed in) when said local player spawns, as this is the creation of entity local ped.' ,
                arguments={
                    
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        
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
            name='onClientElementStreamOut',
            docs=FunctionDoc(
                description='This event is triggered whenever a physical element is streamed out. This is triggered for all elements that are streamable, such as players, peds, vehicles, objects and markers when the local player is leaving the element. When this event is triggered, that element is no longer physical and is now virtualized by MTA.' ,
                arguments={
                    
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        
                    ],
                    variable_length=False,
                ),
        )
        ],
    ),
    CompoundEventData(
        server=[
            EventData(
            name='onElementClicked',
            docs=FunctionDoc(
                description='This event is triggered when an element is clicked on by the client. These events can only trigger when the client has its cursor enabled. It triggers for all three mousebuttons in both their up and down states.' ,
                arguments={
                    "mouseButton": """: a string representing the mouse button that was clicked. This might be left, middle or right. """,
                    "buttonState": """: a string representing what state the button clicked is in. This might be up or down. """,
                    "playerWhoClicked": """: the player that clicked on the element. """,
                    "clickPosX": """: the X position in the world the player clicked at. """,
                    "clickPosY": """: the Y position in the world the player clicked at. """,
                    "clickPosZ": """: the Z position in the world the player clicked at. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='mouseButton',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='buttonState',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='playerWhoClicked',
                                argument_type=FunctionType(
                                    names=['player'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='clickPosX',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='clickPosY',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='clickPosZ',
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
            name='onElementColShapeHit',
            docs=FunctionDoc(
                description='This event is triggered when an player or vehicle element collides with a colshape.' ,
                arguments={
                    "theColShape": """: the colshape that this element collided with. """,
                    "matchingDimension": """: a boolean representing if the element and the colshape are in the same dimension. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theColShape',
                                argument_type=FunctionType(
                                    names=['colshape'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='matchingDimension',
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
            name='onElementColShapeLeave',
            docs=FunctionDoc(
                description='This event is triggered when an player or vehicle element leaves the area of a colshape.' ,
                arguments={
                    "theColShape": """: the colshape that this element left the area of. """,
                    "matchingDimension": """: a boolean representing if the element and the colshape are in the same dimension. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theColShape',
                                argument_type=FunctionType(
                                    names=['colshape'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='matchingDimension',
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
            name='onElementDataChange',
            docs=FunctionDoc(
                description='This event is triggered after an elements element data|data entry is changed. Such changes can be made on the client or the server using setElementData.' ,
                arguments={
                    "theKey": """: The name of the element data entry that has changed. """,
                    "oldValue": """: The old value of this entry before it changed. See element data for a list of possible datatypes. """,
                    "newValue": """: the new value of this entry after it changed. This will be equivalent to getElementData(source, theKey). """,
                    "source": """: The event system#Event source|source of this event is the element whose element data changed. """,
                    "client": """: The event system#Event client|client global variable is set to the client that called setElementData, or nil if it was called on the server. """,
                    "sourceResource": """: The resource which changed the element data. (Only works in versions above 1.3.4-5937) """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theKey',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='oldValue',
                                argument_type=FunctionType(
                                    names=['var'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='newValue',
                                argument_type=FunctionType(
                                    names=['var'],
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
            name='onElementDestroy',
            docs=FunctionDoc(
                description='This event is triggered when an element gets destroyed by destroyElement or when the creator resource is stopping. It is also triggered when a parent element of this element is destroyed.' ,
                arguments={
                    
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        
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
            name='onElementDimensionChange',
            docs=FunctionDoc(
                description='' ,
                arguments={
                    "oldDimension": """: An int representing the dimension the element was in before. """,
                    "newDimension": """: An int representing the dimension the element is in now. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='oldDimension',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='newDimension',
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
    ),
    CompoundEventData(
        server=[
            EventData(
            name='onElementInteriorChange',
            docs=FunctionDoc(
                description='' ,
                arguments={
                    "oldInterior": """: an int representing the interior the element was in before. """,
                    "newInterior": """: an int representing the interior the element is in now. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='oldInterior',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='newInterior',
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
    ),
    CompoundEventData(
        server=[
            EventData(
            name='onElementModelChange',
            docs=FunctionDoc(
                description='This event is triggered when the model of an element is changed using setElementModel.' ,
                arguments={
                    "oldModel": """an int representing the model of the element before the change occurred. """,
                    "newModel": """an int representing the new model of the element. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='oldModel',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='newModel',
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
    ),
    CompoundEventData(
        server=[
            EventData(
            name='onElementStartSync',
            docs=FunctionDoc(
                description='This event is triggered when an element becomes synced by a player.' ,
                arguments={
                    "newSyncer": """: a player element representing the player who is now syncing the element. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='newSyncer',
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
        )
        ],
        client=[
            
        ],
    ),
    CompoundEventData(
        server=[
            EventData(
            name='onElementStopSync',
            docs=FunctionDoc(
                description='This event is triggered when an element is no longer synced by a player.' ,
                arguments={
                    "oldSyncer": """: a player element representing the last player who was syncing the element. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='oldSyncer',
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
        )
        ],
        client=[
            
        ],
    )
]
