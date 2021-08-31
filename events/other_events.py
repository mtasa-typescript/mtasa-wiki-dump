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
            name='onClientChatMessage',
            docs=FunctionDoc(
                description="""This event is triggered when any text is output to chatbox, including MTAs internal messages. """,
                arguments={
                    "text": """The text that was output to chatbox. """,
                    "r": """The amount of red in the color of the text. """,
                    "g": """The amount of green in the color of the text. """,
                    "b": """The amount of blue in the color of the text. """,
                    "messageType": """The type of message as a number.
|20912}}
This function is used to change the loop option of the [[sound]] [[element]]. """
                },
                result=""" """,
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
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='g',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='b',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='messageType',
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
            name='onClientConsole',
            docs=FunctionDoc(
                description="""This event is triggered when the local player enters text in the console. Note that, if you want to add custom console commands, it is easier to use the addCommandHandler function. """,
                arguments={
                    "text": """the text line that was entered. """
                },
                result=""" """,
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
        )]),
    CompoundEventData(server=[], client=[EventData(
            name='onClientDebugMessage',
            docs=FunctionDoc(
                description="""This event is triggered when client-side debug messages (for instance errors or warnings) would appear in the debug window. This event doesnt require the debug window to be enabled to trigger, however.
Note: To prevent infinite loops, debug messages that occur inside the function that handles this event wont trigger this event, so you wont be able to rely on debug info to fix faulty code that is inside this function. Since build https://buildinfo.mtasa.com/index.php?Revision=14683 r14683 debug messages from outputDebugString and iprint will show up. """,
                arguments={
                    "message": """: The message which was outputted in the server console, without details like file, line etc """,
                    "level": """: The type of debug message which was outputted """,
                    "0": """Custom message """,
                    "1": """Error message """,
                    "2": """Warning message """,
                    "3": """Information message """,
                    "file": """: The file from which the debug message was outputted """,
                    "Note": """May return nil when the source could not be found """,
                    "line": """: The line in file file where the debug message was outputted """,
                    "r": """: Amount of red color (0-255) """,
                    "g": """: Amount of green color (0-255) """,
                    "b": """: Amount of blue color (0-255) """
                },
                result=""" """,
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
                        ],
                        [
                            FunctionArgument(
                                name='r',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='g',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='b',
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
            name='onClientExplosion',
            docs=FunctionDoc(
                description="""This event is triggered every time an explosion is created on the current clients scene (inside the streamer). """,
                arguments={
                    "x": """the X Coordinate of where the explosion was created """,
                    "y": """the Y Coordinate of where the explosion was created """,
                    "z": """the z Coordinate of where the explosion was created """,
                    "theType": """the type of explosion created, Values are: """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
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
                        ],
                        [
                            FunctionArgument(
                                name='theType',
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
            name='onClientFileDownloadComplete',
            docs=FunctionDoc(
                description="""This event is triggered when a file has been downloaded after downloadFile has been successfully called. """,
                arguments={
                    "fileName": """: the file downloaded. """,
                    "success": """: whether successful or not. """,
                    "requestResource": """: the resource that called downloadFile. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='fileName',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='success',
                                argument_type=FunctionType(
                                    names=['bool'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='requestResource',
                                argument_type=FunctionType(
                                    names=['resource'],
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
            name='onClientHUDRender',
            docs=FunctionDoc(
                description="""This event is triggered before GTA renders the HUD. This is particularly useful if you want to use dxUpdateScreenSource to capture the screen onto a texture without capturing the HUD, or to alter HUD textures using Element/Shader|shaders before they are drawn onto the screen. """,
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
            name='onClientMinimize',
            docs=FunctionDoc(
                description="""This event is triggered when the local player minimizes the game screen. """,
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
            name='onClientPedsProcessed',
            docs=FunctionDoc(
                description=""" """,
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
            name='onClientPlayerNetworkStatus',
            docs=FunctionDoc(
                description="""This event is triggered when the server network connection to a player is interrupted. See onPlayerNetworkStatus for detecting player to server interruptions. """,
                arguments={
                    "status": """: A number which is 0 if the interruption has begun, or 1 if the interruption is ending. """,
                    "ticks": """: Number of ticks since the interruption started. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='status',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='ticks',
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
            name='onClientPreRender',
            docs=FunctionDoc(
                description="""This event is triggered every time before GTA renders a new frame. """,
                arguments={
                    "timeSlice": """The interval between this frame and the previous one in milliseconds (delta time). """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='timeSlice',
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
        )]),
    CompoundEventData(server=[], client=[EventData(
            name='onClientRender',
            docs=FunctionDoc(
                description="""This event is triggered every time GTA renders a new frame. It is required for the DirectX drawing functions, and also useful for other clientside operations that have to be applied repeatedly with very short time differences between them. """,
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
            name='onClientRestore',
            docs=FunctionDoc(
                description="""This event is triggered when the local player restores the game screen from a previously minimized state. """,
                arguments={
                    "didClearRenderTargets": """A bool specifying whether all render targets have been cleared as part of the restore process. Generally, restoring in full screen mode will clear render targets. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='didClearRenderTargets',
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
            name='onClientTransferBoxProgressChange',
            docs=FunctionDoc(
                description=""" """,
                arguments={
                    "downloadedSizeTotal": """total progress in bytes """,
                    "downloadTotalBytes": """download total size in bytes """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='downloadedSizeTotal',
                                argument_type=FunctionType(
                                    names=['float'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='downloadTotalBytes',
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
        )]),
    CompoundEventData(server=[], client=[EventData(
            name='onClientTransferBoxVisibilityChange',
            docs=FunctionDoc(
                description=""" """,
                arguments={
                    "isVisible": """boolean, whether the transfer box is visible now """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='isVisible',
                                argument_type=FunctionType(
                                    names=['boolean'],
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
            name='onClientWorldSound',
            docs=FunctionDoc(
                description="""For example, you should only cancel player emitted sounds in this event, because when you cancel certain vehicle sounds, the game will try to play the same sound on the next frame.}} """,
                arguments={
                    "group": """An int|integer representing the World sound groups|world sound group """,
                    "index": """An int|integer representing an individual sound within the group """,
                    "x": """a floating point number representing the X coordinate on the map. """,
                    "y": """a floating point number representing the Y coordinate on the map. """,
                    "z": """a floating point number representing the Z coordinate on the map. """
                },
                result=""" """,
            ),
            arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='group',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='index',
                                argument_type=FunctionType(
                                    names=['int'],
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
        )])
]