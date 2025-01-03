import re
from typing import Optional, Dict
import string
from ast import literal_eval
import json

def pre_process_the_json_response(response) -> str:
    try:
        response = "".join(char for char in response if char in string.printable)
    except Exception as e:
        raise Exception(
            f"Error filtering non-printable characters: {str(e)}"
        ) from e
    try:
        if response.startswith("```") and response.endswith("```"):
            response = "```".join(response.split("```")[1:-1])
            response = re.sub(
                r"\bjson\b", "", response
            )  # removing anything with a json in the beginning
        elif response.startswith("```json") and response.endswith("```"):
            response = "```json".join(response.split("```")[1:-1])
            response = re.sub(
                r"\bjson\b", "", response
            )  # removing anything with a json in the beginning
    except AttributeError as e:
        raise AttributeError(
            f"Error processing response format: {str(e)}"
        ) from e
    except re.error as e:
        raise Exception(f"Regex error: {str(e)}") from e
    except Exception as e:
        raise Exception(f"Unexpected error: {str(e)}") from e

    return response


def load_object_from_string(s) -> Optional[Dict]:
    try:
        return literal_eval(s)
    except (ValueError, SyntaxError):
        try:
            return json.loads(s)
        except json.JSONDecodeError as e:
            raise Exception(
                "Failed to parse string as both Python literal and JSON."
            ) from e
