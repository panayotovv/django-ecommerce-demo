from django.core.exceptions import ValidationError


def validate_phone_number(value):
    if len(value) < 8:
        raise ValidationError(
            'Please enter a valid phone number.'
        )