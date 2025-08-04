from django.core.exceptions import ValidationError


def validate_phone_number(value):
    if len(str(value)) < 8:
        raise ValidationError(
            'Please enter a valid phone number.'
        )