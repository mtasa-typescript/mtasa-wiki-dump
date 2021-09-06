# 📦 MTASA Wiki Dump

Parsed and generated via 
[wiki-parser](https://github.com/mtasa-typescript/mtasa-wiki-parser)

Contains data about MTASA Server, Client and Shared Functions and events.

Used for generation TypeScript type definitions in 
[wiki-parser](https://github.com/mtasa-typescript/mtasa-wiki-parser).

**Do not edit dump files manually. Changes will be overwritten by code-generation**

## How to use

The entire dump list import:

```python
from to_python.dump import DUMP_FUNCTIONS
from to_python.dump import DUMP_EVENTS
from to_python.dump import DUMP_OOPS
```

URL List import:

```python
from to_python.dump.url_list import URL_LIST
from to_python.dump.url_list import URL_LIST_EVENT
```

## Data Structure

All data structures described in [mtasa-wiki-parser](https://github.com/mtasa-typescript/mtasa-wiki-parser)