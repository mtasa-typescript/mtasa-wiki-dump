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
            FunctionData(
            signature=FunctionSignature(
                name='clearChatBox',
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
                                name='clearFor',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=True,
                                ),
                                default_value='getRootElement()',
                            )
                        ]
                    ],
                    variable_length=False,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description=""" """,
                arguments={
                    "clearFor": """The player whose chat is to be cleared. By default, this is set to the root element, which will affect all players. """
                },
                result="""returns true if the players chat was cleared successfully, false otherwise. """,
            ),
            name='clearChatBox',
        )
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='clearChatBox',
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
                description=""" """,
                arguments={
                    
                },
                result="""returns true if the players chat was cleared successfully, false otherwise. """,
            ),
            name='clearChatBox',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='clearDebugBox',
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
                description=""" """,
                arguments={
                    
                },
                result="""always returns true. """,
            ),
            name='clearDebugBox',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='isChatVisible',
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
                description="""This function checks if players chat is visible. """,
                arguments={
                    
                },
                result="""returns true if the chat is visible, false otherwise. """,
            ),
            name='isChatVisible',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='outputChatBox',
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
                                name='text',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='visibleTo',
                                argument_type=FunctionType(
                                    names=['table', 'element'],
                                    is_optional=True,
                                ),
                                default_value='root',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='r',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=True,
                                ),
                                default_value='231',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='g',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=True,
                                ),
                                default_value='217',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='b',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=True,
                                ),
                                default_value='176',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='colorCoded',
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
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description="""This outputs the specified text string to the chatbox. It can be specified as a message to certain player(s) or all players.
It can optionally allow you to embed color changes into the string by setting the colorCoded boolean to true. This allows:
<syntaxhighlight lang=lua>
outputChatBox ( #FF0000Hello #00FF00World, root, 255, 255, 255, true )
</syntaxhighlight>
This will display as: <span style=color:red;>Hello</span> <span style=color:green>World</span> """,
                arguments={
                    "text": """The text string that you wish to send to the chat window. If more than 256 characters it will not be showed in chat. """,
                    "visibleTo": """Can also be a table of players or team.}} """,
                    "r": """The amount of red in the color of the text. Default value is 231. """,
                    "g": """The amount of green in the color of the text. Default value is 217. """,
                    "b": """The amount of blue in the color of the text. Default value is 176. """,
                    "colorCoded": """A boolean value determining whether or not #RRGGBB tags should be used.
Note: The #RRGGBB format must contain capital letters a-f is not acceptable but A-F is. Default RGB values in this format are: '#E7D9B0'. """
                },
                result=""" """,
            ),
            name='outputChatBox',
        )
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='outputChatBox',
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
                                name='text',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='r',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=True,
                                ),
                                default_value='231',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='g',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=True,
                                ),
                                default_value='217',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='b',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=True,
                                ),
                                default_value='176',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='colorCoded',
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
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description="""This outputs the specified text string to the chatbox. It can be specified as a message to certain player(s) or all players.
It can optionally allow you to embed color changes into the string by setting the colorCoded boolean to true. This allows:
<syntaxhighlight lang=lua>
outputChatBox ( #FF0000Hello #00FF00World, root, 255, 255, 255, true )
</syntaxhighlight>
This will display as: <span style=color:red;>Hello</span> <span style=color:green>World</span> """,
                arguments={
                    "text": """The text string that you wish to send to the chat window. If more than 256 characters it will not be showed in chat. """,
                    "r": """The amount of red in the color of the text. Default value is 231. """,
                    "g": """The amount of green in the color of the text. Default value is 217. """,
                    "b": """The amount of blue in the color of the text. Default value is 176. """,
                    "colorCoded": """A boolean value determining whether or not #RRGGBB tags should be used.
Note: The #RRGGBB format must contain capital letters a-f is not acceptable but A-F is. Default RGB values in this format are: '#E7D9B0'. """
                },
                result=""" """,
            ),
            name='outputChatBox',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='outputConsole',
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
                                name='text',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='visibleTo',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=True,
                                ),
                                default_value='getRootElement()',
                            )
                        ]
                    ],
                    variable_length=False,
                ),
                generic_types=[
                    
                ],
            ),
            docs=FunctionDoc(
                description="""This outputs the specified text string to the console window (accessed with F8 or ~ key). It can be specified as a message to certain player(s) or all players. """,
                arguments={
                    "text": """The text string that you wish to send to the console window """,
                    "visibleTo": """This specifies who the chat is visible to. Any players in this element will see the chat message. See visibility. """
                },
                result=""" """,
            ),
            name='outputConsole',
        )
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='outputConsole',
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
                                name='text',
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
                description="""This outputs the specified text string to the console window (accessed with F8 or ~ key). It can be specified as a message to certain player(s) or all players. """,
                arguments={
                    "text": """The text string that you wish to send to the console window """
                },
                result=""" """,
            ),
            name='outputConsole',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='outputDebugString',
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
                                name='text',
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
                                    is_optional=True,
                                ),
                                default_value='3',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='red',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=True,
                                ),
                                default_value='255',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='green',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=True,
                                ),
                                default_value='255',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='blue',
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
                description="""This function outputs scripting debug messages, which can be read by enabling the debug textbox. The debug display level can then be set so that info or warning messages get filtered out. """,
                arguments={
                    "text": """the text to be output to the debug box. """,
                    "level": """the debug message level. Possible values are: """,
                    "0": """Custom message """,
                    "1": """Error message """,
                    "2": """Warning message """,
                    "3": """Information message (default) """,
                    "4": """Custom message (omits file path and line number)}} """,
                    "red": """The amount of red in the color of the text. Default value is 255. """,
                    "green": """The amount of green in the color of the text. Default value is 255. """,
                    "blue": """The amount of blue in the color of the text. Default value is 255. """
                },
                result="""returns true if the debug message was successfully output, false if invalid arguments are specified. """,
            ),
            name='outputDebugString',
        )
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='outputDebugString',
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
                                name='text',
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
                                    is_optional=True,
                                ),
                                default_value='3',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='red',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=True,
                                ),
                                default_value='255',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='green',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=True,
                                ),
                                default_value='255',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='blue',
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
                description="""This function outputs scripting debug messages, which can be read by enabling the debug textbox. The debug display level can then be set so that info or warning messages get filtered out. """,
                arguments={
                    "text": """the text to be output to the debug box. """,
                    "level": """the debug message level. Possible values are: """,
                    "0": """Custom message """,
                    "1": """Error message """,
                    "2": """Warning message """,
                    "3": """Information message (default) """,
                    "4": """Custom message (omits file path and line number)}} """,
                    "red": """The amount of red in the color of the text. Default value is 255. """,
                    "green": """The amount of green in the color of the text. Default value is 255. """,
                    "blue": """The amount of blue in the color of the text. Default value is 255. """
                },
                result="""returns true if the debug message was successfully output, false if invalid arguments are specified. """,
            ),
            name='outputDebugString',
        )
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='outputServerLog',
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
                                name='text',
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
                description="""This outputs a line of text to the servers log. This could be useful for debugging. """,
                arguments={
                    "text": """The text to be output to the log. """
                },
                result="""returns true if successful, false otherwise. """,
            ),
            name='outputServerLog',
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='showChat',
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
                                name='thePlayer',
                                argument_type=FunctionType(
                                    names=['player'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='show',
                                argument_type=FunctionType(
                                    names=['bool'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='inputBlocked',
                                argument_type=FunctionType(
                                    names=['bool'],
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
                description="""This function is used to show or hide the players chat. """,
                arguments={
                    "thePlayer": """The player whose chat is to be hidden or shown. """,
                    "show": """A boolean value determining whether to show (true) or hide (false) the chat. """,
                    "inputBlocked": """A boolean value determining whether chat input is blocked/hidden, regardless of chat visibility. If unset, this will keep the default behaviour prior to r20898 (true when chat is hidden, false when chat is visible). """
                },
                result="""returns true if the players chat was shown or hidden successfully, false otherwise. """,
            ),
            name='showChat',
        )
        ],
        client=[
            FunctionData(
            signature=FunctionSignature(
                name='showChat',
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
                                name='show',
                                argument_type=FunctionType(
                                    names=['bool'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='inputBlocked',
                                argument_type=FunctionType(
                                    names=['bool'],
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
                description="""This function is used to show or hide the players chat. """,
                arguments={
                    "show": """A boolean value determining whether to show (true) or hide (false) the chat. """,
                    "inputBlocked": """A boolean value determining whether chat input is blocked/hidden, regardless of chat visibility. If unset, this will keep the default behaviour prior to r20898 (true when chat is hidden, false when chat is visible). """
                },
                result="""returns true if the players chat was shown or hidden successfully, false otherwise. """,
            ),
            name='showChat',
        )
        ],
    )
]
