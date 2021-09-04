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
            FunctionOOP(
                description=None,
                base_function_name="dbConnect",
                class_name='Connection',
                method=None,
                field=None,
                is_static=True,
            )
        ],
        client=[
            
        ],
    ),
    CompoundOOPData(
        server=[
            FunctionOOP(
                description=None,
                base_function_name="dbExec",
                class_name='connection',
                method=FunctionData(
            signature=FunctionSignature(
                name='exec',
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
                                name='databaseConnection',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='query',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='param1',
                                argument_type=FunctionType(
                                    names=['var'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='param2',
                                argument_type=FunctionType(
                                    names=['var'],
                                    is_optional=True,
                                ),
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
                description='This function executes a database query using the supplied connection. No result is returned.' ,
                arguments={
                    "databaseConnection": """A database connection element previously returned from dbConnect """,
                    "query": """An SQL query. Positions where parameter values will be inserted are marked with a ? """,
                    "paramX": """A variable number of parameters. These must be strings or numbers - it is important to make sure they are of the correct type. Also, the number of parameters passed must be equal to the number of ? characters in the query string.
String parameters are automatically quoted and escaped as required. (If you do not want a string quoted, use '''??''') Make sure that numbers are in number format as a string number is treated differently. """
                },
                result='returns true unless the connection is incorrect, in which case it returns false.' ,
            ),
            url='dbExec',
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
            FunctionOOP(
                description=None,
                base_function_name="dbFree",
                class_name='queryHandle',
                method=FunctionData(
            signature=FunctionSignature(
                name='free',
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
                                name='queryHandle',
                                argument_type=FunctionType(
                                    names=['handle'],
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
                description='This function frees a database query handle. dbFree only needs to be used if a result has not been obtained with dbPoll' ,
                arguments={
                    "queryHandle": """A query handle previously returned from dbQuery """
                },
                result='returns true if the handle was successfully freed, false otherwise.' ,
            ),
            url='dbFree',
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
            FunctionOOP(
                description=None,
                base_function_name="dbPoll",
                class_name='queryHandle',
                method=FunctionData(
            signature=FunctionSignature(
                name='poll',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['table'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='queryHandle',
                                argument_type=FunctionType(
                                    names=['handle'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='timeout',
                                argument_type=FunctionType(
                                    names=['int'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='multipleResults',
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
                description='This function checks the progress of a database query.' ,
                arguments={
                    "queryHandle": """A query handle previously returned from dbQuery """,
                    "timeout": """How many milliseconds to wait for a result. Use 0 for an instant response (which may return nil). Use -1 to wait until a result is ready. Note: A wait here will freeze the entire server just like executeSQLQuery """,
                    "multipleResults": """Set to true to enable the return values from multiple queries
|7972}} """
                },
                result='*nil: returns nil if the query results are not yet ready. you should try again in a little while. (if you give up waiting for a result, be sure to call dbfree)\n*false: returns false if the query string contained an error, the connection has been lost or the query handle is incorrect. this automatically frees the query handle, so you do not have to call dbfree.\n** this also returns two extra values: (see the example on how the retrieve them)\n***int: error code\n***string error message\n*table: returns a table with the result of the query when the query has successfully completed. this automatically frees the query handle, so you do not have to call dbfree. if multipleresults is set to true, it will first return a table pertaining to one query, followed by the results for that query and so on for the next queries.\n** this also returns extra values (only when multipleresults is set to true):\n***int: number of affected rows\n***int: last insert id\nthe table is of the format:\n<syntaxhighlight lang=lua>\n{\n{ colname1=value1, colname2=value2, ... },\n{ colname1=value3, colname2=value4, ... },\n...\n}\n</syntaxhighlight>\na subsequent table represents the next row.' ,
            ),
            url='dbPoll',
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
            FunctionOOP(
                description=None,
                base_function_name="dbPrepareString",
                class_name='connection',
                method=FunctionData(
            signature=FunctionSignature(
                name='prepareString',
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
                                name='databaseConnection',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='query',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='param1',
                                argument_type=FunctionType(
                                    names=['var'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='param2',
                                argument_type=FunctionType(
                                    names=['var'],
                                    is_optional=True,
                                ),
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
                description='This function escapes arguments in the same way as dbQuery, except dbPrepareString returns the query string instead of processing the query. This allows you to safely build complex query strings from component parts and help prevent (one class of) SQL injection.}}' ,
                arguments={
                    "databaseConnection": """A database connection element previously returned from dbConnect """,
                    "query": """An SQL query. Positions where parameter values will be inserted are marked with a ? """,
                    "paramX": """A variable number of parameters. These must be strings or numbers - it is important to make sure they are of the correct type. Also, the number of parameters passed must be equal to the number of ? characters in the query string.
String parameters are automatically quoted and escaped as required. (If you do not want a string quoted, use '''??''') """
                },
                result='returns a prepare sql query string, or false if an error occurred.' ,
            ),
            url='dbPrepareString',
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
            FunctionOOP(
                description=None,
                base_function_name="dbQuery",
                class_name='connection',
                method=FunctionData(
            signature=FunctionSignature(
                name='query',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['handle'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='callbackFunction',
                                argument_type=FunctionType(
                                    names=['function'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='callbackArguments',
                                argument_type=FunctionType(
                                    names=['table'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='databaseConnection',
                                argument_type=FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='query',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='param1',
                                argument_type=FunctionType(
                                    names=['var'],
                                    is_optional=True,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='param2',
                                argument_type=FunctionType(
                                    names=['var'],
                                    is_optional=True,
                                ),
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
                description='This function starts a database query using the supplied connection. Use the returned query handle with dbPoll to get the result, or dbFree if you dont want the result.' ,
                arguments={
                    "databaseConnection": """A database connection element previously returned from dbConnect """,
                    "query": """An SQL query. Positions where parameter values will be inserted are marked with a ? """,
                    "callbackFunction": """An optional function to be called when a result is ready. The function will only be called if the result has not already been read with dbPoll. The function is called with the query handle as the first argument. """,
                    "callbackArguments": """An optional table containing extra arguments to be sent to the callback function. """,
                    "paramX": """A variable number of parameters. These must be strings or numbers - it is important to make sure they are of the correct type. Also, the number of parameters passed must be equal to the number of ? characters in the query string.
String parameters are automatically quoted and escaped as required. (If you do not want a string quoted, use '''??''') """
                },
                result='returns a query handle unless the connection is incorrect, in which case it return false.' ,
            ),
            url='dbQuery',
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
    )
]