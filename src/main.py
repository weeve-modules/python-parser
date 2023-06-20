from weeve_modules import send, add_graceful_termination, weeve_logger, listener
from os import getenv
import json
import jsonschema

log = weeve_logger("main")


CONFIG = {
    "PARSER_CODE": getenv("PARSER_CODE"),
    "JSON_SCHEMA": getenv("JSON_SCHEMA"),
}


def parse_incoming_data(incoming_data):
    """
    Implements module's main logic for parsing incoming data.
    Function description should not be modified.
    """
    log.debug("Received data: %s", incoming_data)
    exec(CONFIG["PARSER_CODE"])  # execute parser code, transforming incoming data into parsed_data
    if not parsed_data:
        log.error("Parser code did not produce any output.")
        return

    # check if parsed_data is valid according to JSON schema
    if CONFIG["JSON_SCHEMA"]:
        try:
            jsonschema.validate(parsed_data, json.loads(CONFIG["JSON_SCHEMA"]))
        except jsonschema.exceptions.ValidationError as err:
            print("JSON object is not valid against the schema. Error: ", err)
            return

    # send parsed data to the next module in the pipeline
    send_error = send(parsed_data)

    if send_error:
        log.error(send_error)
    else:
        log.debug("Data sent sucessfully.")


if __name__ == "__main__":
    add_graceful_termination()

    # set up a listener to receive data from other modules within the weeve ecosystem
    listener(callback_function=parse_incoming_data)
