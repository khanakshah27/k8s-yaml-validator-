import yaml
from jsonschema import validate, ValidationError

def validate_yaml(yaml_content):
    try:
        data = yaml.safe_load(yaml_content)
        # Simplified check: ensure basic K8s fields exist
        required_fields = ['apiVersion', 'kind', 'metadata']
        for field in required_fields:
            if field not in data:
                return False, f"Missing required field: {field}"
        return True, "Valid format"
    except yaml.YAMLError as e:
        return False, f"YAML Syntax Error: {e}"
