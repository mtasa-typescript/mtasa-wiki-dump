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
            EventData(
            name='onBan',
            docs=FunctionDoc(
                description='This event is triggered when an IP address or serial is banned from the server.' ,
                arguments={
                    "theBan": """: the ban which was added. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theBan',
                                argument_type=FunctionType(
                                    names=['ban'],
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
            name='onChatMessage',
            docs=FunctionDoc(
                description='This event is triggered when any message is output to chat using outputChatBox server-side (also when a player uses say, teamsay or me successfully).' ,
                arguments={
                    "theMessage": """A string representing the text that was output to the chatbox. """,
                    "theElement": """A resource if it was done via outputChatBox or a player element if it was done via say, teamsay or me. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theMessage',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='theElement',
                                argument_type=FunctionType(
                                    names=['resource', 'element'],
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
            name='onDebugMessage',
            docs=FunctionDoc(
                description='This event is triggered when debug messages (for instance errors or warnings) appear in the server console.\nNote: To prevent infinite loops, debug messages that occur inside the function that handles this event wont trigger this event, so you wont be able to rely on debug info to fix faulty code that is inside this function. Since build https://buildinfo.mtasa.com/index.php?Revision=14683 r14683 debug messages from outputDebugString and iprint will show up.' ,
                arguments={
                    "message": """: the message which was outputted in the server console, without details like file, line etc. """,
                    "level": """: the type of debug message which was outputted. """,
                    "0": """Custom message. """,
                    "1": """Error message. """,
                    "2": """Warning message. """,
                    "3": """Information message. """,
                    "file": """: the file from which the debug message was outputted. """,
                    "Note": """may return nil when the source could not be found. """,
                    "line": """: the line in file file where the debug message was outputted. """,
                    "r": """: an int representing the amount of red color (0-255). """,
                    "g": """: an int representing the amount of green color (0-255). """,
                    "b": """: an int representing the amount of blue color (0-255). """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='message',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='level',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='file',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='line',
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
            name='onSettingChange',
            docs=FunctionDoc(
                description='This event is triggered when resource setting has been changed. For instance, this event would trigger if you would edit the settings of the Race resource through the Admin panel.' ,
                arguments={
                    "setting": """: The setting which was changed. For instance: *race.ghostmode """,
                    "oldValue": """: The previous value. Please note that this value is in JSON. To get a normal Lua value, use fromJSON """,
                    "newValue": """: The new value. Also in JSON """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='setting',
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
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='newValue',
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
        )
        ],
        client=[
            
        ],
    ),
    CompoundEventData(
        server=[
            EventData(
            name='onUnban',
            docs=FunctionDoc(
                description='This event is triggered when a ban is removed from the server.\nif the ban was removed using function removeBan, and the responsibleElement was not specifying, the event will return nil.' ,
                arguments={
                    "theBan": """: the ban that will be removed. """,
                    "responsibleElement": """: the player who removed the ban, otherwise returns nil. """
                },
                result='' ,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='theBan',
                                argument_type=FunctionType(
                                    names=['ban'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='responsibleElement',
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
