import json
from typing import List, Optional, Union, Dict, Any
from jsonschema import Draft7Validator, ValidationError

class JsonValidator:
    def __init__(self):
        pass

    def validate_schema(
        self,
        json_file: str,
        schema_file: str,
    ) -> bool:
        """
        Validates a JSON file against a given schema file.
        
        :param json_file: Path to the JSON file for validation
        :type json_file: str
        :param schema_file: Path to the schema file for validation
        :type schema_file: str
        :return: True if validation succeeds, False otherwise
        :rtype: bool
        """
        try:
            
            with open(json_file, "r") as json_data:
                json_content = json.load(json_data)

            with open(schema_file, "r") as schema_data:
                schema_content = json.load(schema_data)

            validator = Draft7Validator(schema_content)
            errors = list(validator.iter_errors(json_content))

            if not errors:
                return True
            else:
                for error in errors:
                    print(f"Validation Error: {error.message}")
                return False
        except (ValidationError, FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Validation Error: {str(e)}")
            return False


if __name__ == "__main__":
    
    json_file_path = "C:\\Users\\tanma\\OneDrive\\Desktop\\data.json"
    schema_file_path = "C:\\Users\\tanma\\OneDrive\\Desktop\\schema.json"
    
    validator = JsonValidator()

    is_valid = validator.validate_schema(json_file_path, schema_file_path)

    if is_valid:
        print("Validation succeeded!")
    else:
        print("Validation failed.")
