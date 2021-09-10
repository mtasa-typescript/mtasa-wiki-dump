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
            
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            FunctionOOP(
                description=None,
                base_function_name="triggerClientEvent",
                class_name='player',
                method=FunctionData(
            signature=FunctionSignature(
                name='triggerEvent',
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
                                name='sendTo',
                                argument_type=FunctionType(
                                    names=['table', 'element'],
                                    is_optional=True,
                                ),
                                default_value='getRootElement()',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='name',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='sourceElement',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='arguments',
                                argument_type=None,
                                default_value=None,
                            )
                        ]
                    ],
                    variable_length=True,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description='This function triggers an event previously registered on a client. This is the primary means of passing information between the server and the client. Clients have a similar triggerServerEvent function that can do the reverse. You can treat this function as if it was an asynchronous function call, using triggerServerEvent to pass back any returned information if necessary.\nAlmost any data types can be passed as expected, including elements and complex nested tables. Non-element MTA data types like xmlNodes or resource pointers will not be able to be passed as they do not necessarily have a valid representation on the client.\nEvents are sent reliably, so clients will receive them, but there may be (but shouldnt be) a significant delay before they are received. You should take this into account when using them.\nKeep in mind the bandwidth issues when using events - dont pass a large list of arguments unless you really need to. It is marginally more efficient to pass one large event than two smaller ones.' ,
                arguments={
                    "name": """The name of the event to trigger client side. You should register this event with addEvent and add at least one event handler using addEventHandler. """,
                    "sourceElement": """The element that is the Event system#Event handlers|source of the event. """,
                    "sendTo": """The event will be sent to all players that are children of the specified element. By default this is the root element, and hence the event is sent to all players. If you specify a single player it will just be sent to that player. This argument can also be a table of player elements. """,
                    "arguments...": """A list of arguments to trigger with the event. You can pass any lua data type (except functions). You can also pass elements. """
                },
                result='returns true if the event trigger has been sent, false if invalid arguments were specified.' ,
            ),
            url='triggerClientEvent',
        ),
                field=None,
                is_static=False,
            )
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
