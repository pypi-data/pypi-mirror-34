from django.db.models.query import QuerySet
from utility.exceptions import ValidationError


def is_value_unique(repository, field):
    """
    Checks if a value is unique
    """
    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.check_unique(instance, field):
                raise ValidationError('This value has alredy been used.', field=field)
            return True

    return _checker


def required_filed(repository, field):
    """
    Checks if a value is None
    """
    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.is_none(instance, field):
                raise ValidationError('Mandatory value was not provided.', field=field)
            return True

    return _checker


def max_length(repository, field, length):
    """
    Checks if the max length of a char field is exceeded
    """
    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.value_too_long(instance, field, length):
                raise ValidationError("Max length of {0} chars exceeded.".format(length),
                                      field=field)
            return True

    return _checker


def read_only_field(repository, field):
    """
    Ensures that read_only fields are not written to
    """
    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.contains_arg(instance, field):
                raise ValidationError('Attempt to write read only field.', field=field)
            return True

    return _checker


def validate_many(*validators):
    """
    Allows to apply multiple validators
    """
    def _checker(instance):
        return all(validator(instance) for validator in validators)

    return _checker
