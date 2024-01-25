# Django Rest Framework
from phonenumber_field.modelfields import PhoneNumberField


# Utils
from like_korean.utils.validators import validate_international_phonenumber


# Main section
class CustomPhoneNumberField(PhoneNumberField):
    default_validators = [validate_international_phonenumber]
