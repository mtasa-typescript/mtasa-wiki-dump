# MTASA Wiki Dump

Parsed and generated via 
[wiki-parser-python](https://github.com/mtasa-typescript/mtasa-wiki-parser)

Contains data about MTASA Server, Client and Shared Functions.

Used for generation TypeScript type definitions in 
[wiki-parser](https://github.com/mtasa-typescript/mtasa-wiki-parser).

**Please, minimize manual dump editing. Changes can be overwritten by code-generation**

## File Structure

`client.py` contains list of client functions

`server.py` contains list of server functions

`shared.py` contains list of shared functions

## Data Structure

Every file contains list of commands. Sorted by categories (like on [MTASA Wiki](https://wiki.multitheftauto.com/wiki/Main_Page) pages)

`CompoundFunctionData` contains `FunctionData` or `None` about server and client function

`FunctionData` contains `FunctionType`, `FunctionDoc`, `FunctionOOP` and `FunctionUrl`.

- `FunctionType` contains information about function signature:
  
  -  `name` is the function name
  - `return_types` contains list of strings -- name of types returned by the function
  - `arguments` contains list of `FunctionArgument`:
    
    - Each `FunctionArgument` contains `name` of argument
    - `argument_type` name
    - `default_value` or `None`
    - Is the argument `optional`
    
- `FunctionDoc` contains the function documentation

  - `description` of the function
  - information about `arguments`: `Dict[argument name -> description]`
  - `result` information
    
- `FunctionOOP` contains the function OOP information:

  - Target `class_name`
  - Target `method_name`
  - Target `field` if exists, otherwise `None`
  
- `FunctionUrl` contains information about the function URL in MTASA Wiki

## How to use

To import dataset use `from dump.shared import DATA as SHARED_DATA`. 
The import is useless without [wiki-parser](https://github.com/mtasa-typescript/mtasa-wiki-parser), because all types definitions are defined there.