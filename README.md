# Data Parser (Python Profile)

|           |                                                                             |
| --------- | --------------------------------------------------------------------------- |
| Name      | Data Parser (Python Profile)                                                                  |
| Version   | v1.0.0                                                                      |
| DockerHub | [weevenetwork/python-parser](https://hub.docker.com/r/weevenetwork/python-parser) |
| Authors   | Paul Gaiduk                                                                 |

## Table of Contents

- [Data Parser (Python Profile)](#data-parser-python-profile)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Input](#input)
  - [Output](#output)

## Description

This module parses the input data using the provided parser profile code (in python) and sends the parsed data in uniform JSON to the next module, after validating it's correctness with the corresponding JSON schema from the data profile.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Environment Variables | type   | Description                                                                                                                                                                                                                                                                                             |
| --------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PARSER_CODE               | string | Code from the parser profile to parse the input data                                                                                                                                                                                                                                                 |
| JSON_SCHEMA            | string | Schema to validate the parsed data                                                                                                                                                                                                                                                                                   |

### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                                                                          |
| --------------------- | ------ | ---------------------------------------------------------------------------------------------------- |
| MODULE_NAME           | string | Name of the module                                                                                   |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)                                                       |
| EGRESS_URLS           | string | HTTP ReST endpoint for the next module                                                               |
| LOG_LEVEL             | string | Allowed log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL. Refer to `logging` package documentation. |

## Input

Example in CSV format:
```
"John,Doe,25\nJane,Smith,30\n"
```

## Output

Output of this module is a JSON with virtual addresses as lables followed by the bytes read from the LOGO! controller represented as integer numbers. Example:
```json
[
    {
        "first_name": "John",
        "last_name": "Doe",
        "age": "25"
    },
    {
        "first_name": "Jane",
        "last_name": "Smith",
        "age": "30"
    }
]
```
