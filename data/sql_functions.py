# Autogenerated file. ANY CHANGES WILL BE OVERWRITTEN
from to_python.core.types import FunctionType, \
    FunctionArgument, \
    FunctionArgumentValues, \
    FunctionReturnTypes, \
    FunctionSignature, \
    FunctionDoc, \
    FunctionOOP, \
    FunctionData, \
    CompoundFunctionData
    
DUMP_PARTIAL = [
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='dbConnect',
                return_types=FunctionReturnTypes(
                    return_types=[
                        FunctionType(
                                    names=['element'],
                                    is_optional=False,
                                )
                    ],
                    variable_length=False,
                ),
                arguments=FunctionArgumentValues(
                    arguments=[
                        [
                            FunctionArgument(
                                name='databaseType',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='host',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=False,
                                ),
                                default_value=None,
                            )
                        ],
                        [
                            FunctionArgument(
                                name='username',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=True,
                                ),
                                default_value='""',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='password',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=True,
                                ),
                                default_value='""',
                            )
                        ],
                        [
                            FunctionArgument(
                                name='options',
                                argument_type=FunctionType(
                                    names=['string'],
                                    is_optional=True,
                                ),
                                default_value='""',
                            )
                        ]
                    ],
                    variable_length=False,
                ),
            ),
            docs=FunctionDoc(
                description="""This function opens a connection to a database and returns an element that can be used with dbQuery. To disconnect use destroyElement. """,
                arguments={
                    "databaseType": """The type of database. This can be either sqlite or mysql """,
                    "host": """: Host address e.g. host=127.0.0.1 """,
                    "dbname": """: Name of the database to use e.g. dbname=test """,
                    "port": """: Host port e.g. port=1234 (optional, defaults to standard MySQL port if not used) """,
                    "unix_socket": """: Unix socket or named pipe to use (optional) """,
                    "charset": """: Communicate with the server using a character which is different from the default e.g. charset<nowiki>=</nowiki>utf8 (optional) """,
                    "username": """Usually required for MySQL, ignored by SQLite """,
                    "password": """Usually required for MySQL, ignored by SQLite """,
                    "options": """List of key=value pairs separated by semicolons. Supported keys are: """,
                    "share": """which can be set to 0 or 1. (Default value for SQLite is share=1, for MySQL is share=0). When set to 1, the connection is shared and will be used by other calls to dbConnect with the same host string. This is usually a good thing for SQLite connections, but not so good for MySQL unless care is taken. """,
                    "batch": """which can be set to 0 or 1. (Default is batch=1). When set to 1, queries called in the same frame are automatically batched together which can significantly speed up inserts/updates. The downside is you lose control of the feature that is used to achieve batching (For SQLite it is transactions, for MySQL it is autocommit mode). Therefore, if you use transactions, lock tables or control autocommit yourself, you may want to disable this feature. """,
                    "autoreconnect": """which can be set to 0 or 1. (Default value autoreconnect=1). When set to 1, dropped connections will automatically be reconnected. Note that session variables (incl. SET NAMES), user variables, table locks and temporary tables will be reset because of the reconnection. So if you use these fancy features, you will need to turn autoreconnect off and cope with dropped connections some other way. """,
                    "log": """which can be set to 0 or 1. (Default value log<nowiki>=</nowiki>1). When set to 0, activity from this connection will not be recorded in the Server_Commands#debugdb|database debug log file. """,
                    "tag": """(Default value tag<nowiki>=</nowiki>script). A string which helps identify activity from this connection in the Server_Commands#debugdb|database debug log file. """,
                    "suppress": """A comma separated list of error codes to ignore. (eg. suppress<nowiki>=</nowiki>1062,1169). """,
                    "multi_statements": """Enable multiple statements (separated by a semi-colon) in one query. Use dbPrepareString when building a multiple statement query to reduce SQL injection risks. """,
                    "queue": """Name of the queue to use. (Default value for SQLite is sqlite, for MySQL default is the host string from the host argument). Asynchronous database queries in the same queue are processed in order, one at a time. Any name can be used. """
                },
                result="""returns a database connection element unless there are problems, in which case it return false. """,
            ),
            oop=FunctionOOP(
                description=None,
                class_name='Connection',
                method_name=None,
                field=None,
                is_static=True,
            ),
            name='dbConnect',
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='dbExec',
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
            ),
            docs=FunctionDoc(
                description="""This function executes a database query using the supplied connection. No result is returned. """,
                arguments={
                    "databaseConnection": """A database connection element previously returned from dbConnect """,
                    "query": """An SQL query. Positions where parameter values will be inserted are marked with a ? """,
                    "paramX": """A variable number of parameters. These must be strings or numbers - it is important to make sure they are of the correct type. Also, the number of parameters passed must be equal to the number of ? characters in the query string.
String parameters are automatically quoted and escaped as required. (If you do not want a string quoted, use '''??''') Make sure that numbers are in number format as a string number is treated differently. """
                },
                result="""returns true unless the connection is incorrect, in which case it returns false. """,
            ),
            oop=FunctionOOP(
                description=None,
                class_name='connection',
                method_name="""exec""",
                field=None,
                is_static=False,
            ),
            name='dbExec',
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='dbFree',
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
            ),
            docs=FunctionDoc(
                description="""This function frees a database query handle. dbFree only needs to be used if a result has not been obtained with dbPoll """,
                arguments={
                    "queryHandle": """A query handle previously returned from dbQuery """
                },
                result="""returns true if the handle was successfully freed, false otherwise. """,
            ),
            oop=FunctionOOP(
                description=None,
                class_name='queryHandle',
                method_name="""free""",
                field=None,
                is_static=False,
            ),
            name='dbFree',
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='dbPoll',
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
            ),
            docs=FunctionDoc(
                description="""This function checks the progress of a database query. """,
                arguments={
                    "queryHandle": """A query handle previously returned from dbQuery """,
                    "timeout": """How many milliseconds to wait for a result. Use 0 for an instant response (which may return nil). Use -1 to wait until a result is ready. Note: A wait here will freeze the entire server just like executeSQLQuery """,
                    "multipleResults": """Set to true to enable the return values from multiple queries
|7972}} """
                },
                result="""*nil: returns nil if the query results are not yet ready. you should try again in a little while. (if you give up waiting for a result, be sure to call dbfree)
*false: returns false if the query string contained an error, the connection has been lost or the query handle is incorrect. this automatically frees the query handle, so you do not have to call dbfree.
** this also returns two extra values: (see the example on how the retrieve them)
***int: error code
***string error message
*table: returns a table with the result of the query when the query has successfully completed. this automatically frees the query handle, so you do not have to call dbfree. if multipleresults is set to true, it will first return a table pertaining to one query, followed by the results for that query and so on for the next queries.
** this also returns extra values (only when multipleresults is set to true):
***int: number of affected rows
***int: last insert id
the table is of the format:
<syntaxhighlight lang=lua>
{
{ colname1=value1, colname2=value2, ... },
{ colname1=value3, colname2=value4, ... },
...
}
</syntaxhighlight>
a subsequent table represents the next row. """,
            ),
            oop=FunctionOOP(
                description=None,
                class_name='queryHandle',
                method_name="""poll""",
                field=None,
                is_static=False,
            ),
            name='dbPoll',
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='dbPrepareString',
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
            ),
            docs=FunctionDoc(
                description="""This function escapes arguments in the same way as dbQuery, except dbPrepareString returns the query string instead of processing the query. This allows you to safely build complex query strings from component parts and help prevent (one class of) SQL injection.}} """,
                arguments={
                    "databaseConnection": """A database connection element previously returned from dbConnect """,
                    "query": """An SQL query. Positions where parameter values will be inserted are marked with a ? """,
                    "paramX": """A variable number of parameters. These must be strings or numbers - it is important to make sure they are of the correct type. Also, the number of parameters passed must be equal to the number of ? characters in the query string.
String parameters are automatically quoted and escaped as required. (If you do not want a string quoted, use '''??''') """
                },
                result="""returns a prepare sql query string, or false if an error occurred. """,
            ),
            oop=FunctionOOP(
                description=None,
                class_name='connection',
                method_name="""prepareString""",
                field=None,
                is_static=False,
            ),
            name='dbPrepareString',
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='dbQuery',
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
            ),
            docs=FunctionDoc(
                description="""This function starts a database query using the supplied connection. Use the returned query handle with dbPoll to get the result, or dbFree if you dont want the result. """,
                arguments={
                    "databaseConnection": """A database connection element previously returned from dbConnect """,
                    "query": """An SQL query. Positions where parameter values will be inserted are marked with a ? """,
                    "callbackFunction": """An optional function to be called when a result is ready. The function will only be called if the result has not already been read with dbPoll. The function is called with the query handle as the first argument. """,
                    "callbackArguments": """An optional table containing extra arguments to be sent to the callback function. """,
                    "paramX": """A variable number of parameters. These must be strings or numbers - it is important to make sure they are of the correct type. Also, the number of parameters passed must be equal to the number of ? characters in the query string.
String parameters are automatically quoted and escaped as required. (If you do not want a string quoted, use '''??''') """
                },
                result="""returns a query handle unless the connection is incorrect, in which case it return false. """,
            ),
            oop=FunctionOOP(
                description=None,
                class_name='connection',
                method_name="""query""",
                field=None,
                is_static=False,
            ),
            name='dbQuery',
        )
        ],
        client=[
            
        ],
    ),
    CompoundFunctionData(
        server=[
            FunctionData(
            signature=FunctionSignature(
                name='executeSQLQuery',
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
            ),
            docs=FunctionDoc(
                description="""This function executes an arbitrary SQL query and returns the result rows if there are any. It allows parameter binding for security (SQL injection is rendered impossible). """,
                arguments={
                    "query": """An SQL query. Positions where parameter values will be inserted are marked with a ?. """,
                    "paramX": """A variable number of parameters. These must be strings or numbers - it is important to make sure they are of the correct type. Also, the number of parameters passed must be equal to the number of ? characters in the query string.
String parameters are automatically escaped by adding a backslash (\) before ' and \ characters. """
                },
                result="""returns a table with the result of the query if it was a select query, or false if otherwise. in case of a select query the result table may be empty (if there are no result rows). the table is of the form:
<syntaxhighlight lang=lua>
{
{ colname1=value1, colname2=value2, ... },
{ colname1=value3, colname2=value4, ... },
...
}
</syntaxhighlight>
a subsequent table represents the next row. """,
            ),
            oop=None,
            name='executeSQLQuery',
        )
        ],
        client=[
            
        ],
    )
]
