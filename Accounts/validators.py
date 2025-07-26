from django.core.exceptions import ValidationError

def validate_email(value):
    if '@' not in value:
        raise ValidationError(
            'Please enter a valid email'
        )