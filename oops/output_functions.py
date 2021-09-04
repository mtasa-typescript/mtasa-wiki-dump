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
            FunctionOOP(
                description=None,
                base_function_name="outputChatBox",
                class_name='player',
                method=FunctionData(
            signature=FunctionSignature(
                name='outputChat',
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
                description='This outputs the specified text string to the chatbox. It can be specified as a message to certain player(s) or all players.\nIt can optionally allow you to embed color changes into the string by setting the colorCoded boolean to true. This allows:\n<syntaxhighlight lang=lua>\noutputChatBox ( #FF0000Hello #00FF00World, root, 255, 255, 255, true )\n</syntaxhighlight>\nThis will display as: <span style=color:red;>Hello</span> <span style=color:green>World</span>' ,
                arguments={
                    "text": """The text string that you wish to send to the chat window. If more than 256 characters it will not be showed in chat. """,
                    "visibleTo": """Can also be a table of players or team.}} """,
                    "r": """The amount of red in the color of the text. Default value is 231. """,
                    "g": """The amount of green in the color of the text. Default value is 217. """,
                    "b": """The amount of blue in the color of the text. Default value is 176. """,
                    "colorCoded": """A boolean value determining whether or not #RRGGBB tags should be used.
Note: The #RRGGBB format must contain capital letters a-f is not acceptable but A-F is. Default RGB values in this format are: '#E7D9B0'. """
                },
                result='' ,
            ),
            url='outputChatBox',
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
    )
]
