from functools import wraps

from flask import abort, request


def json_required(invalid_content_type_code: int=406):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if not request.is_json:
                abort(invalid_content_type_code)

            return fn(*args, **kwargs)
        return wrapper
    return decorator


def validate_keys(required_keys, key_missing_code: int=400):
    def _validate_keys(src, keys):
        for key in keys:
            if key not in src:
                abort(key_missing_code)

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if required_keys:
                _validate_keys(request.json, required_keys)

            return fn(*args, **kwargs)
        return wrapper
    return decorator


def validate_common(key_type_mapping: dict, key_missing_code: int=400, invalid_type_code: int=400):
    def validate_key_and_type(src, mapping):
        for key, typ in mapping.items():
            if key not in src:
                abort(key_missing_code)

            if type(src[key]) is not typ:
                abort(invalid_type_code)

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if key_type_mapping:
                validate_key_and_type(request.json, key_type_mapping)

            return fn(*args, **kwargs)
        return wrapper
    return decorator


def validate_with_fields(key_field_mapping: dict, key_missing_code: int=400, validation_failure_code: int=400):
    def _validate_with_fields(src, mapping):
        for key, field in mapping:
            if field.required and key not in src:
                abort(key_missing_code)

            if key in src:
                value = src[key]

                if field.enum is not None and value not in field.enum:
                    abort(validation_failure_code)
                if not field.allow_null and value is None:
                    abort(validation_failure_code)
                if field.validator_function is not None and not field.validator_function(value):
                    abort(validation_failure_code)

                if not field.validate(value):
                    abort(validation_failure_code)

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if key_field_mapping:
                _validate_with_fields(request.json, key_field_mapping)

            return fn(*args, **kwargs)
        return wrapper
    return decorator
