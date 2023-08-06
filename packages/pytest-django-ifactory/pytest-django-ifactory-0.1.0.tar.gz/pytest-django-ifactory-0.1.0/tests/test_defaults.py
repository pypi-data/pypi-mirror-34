"""Unit tests for pytest-django-ifactory's default value generators."""

import collections
import datetime

import pytest
from django.contrib.postgres import fields as postgres
from django.db import models
from django.utils.dateparse import parse_datetime, parse_time
from pytest import approx

from pytest_django_ifactory.defaults import generate_default_value


def test_default_default():
    assert generate_default_value(object()) is None


def test_default_unique_default():
    with pytest.raises(AssertionError):
        generate_default_value(object(), unique=True)


@pytest.mark.parametrize("field_type", [models.BooleanField, postgres.JSONField])
@pytest.mark.parametrize("field_is_unique", [True, False])
def test_unique_not_implemented(field_type, field_is_unique):
    field = field_type(unique=field_is_unique)
    with pytest.raises(AssertionError):
        generate_default_value(field, unique=not field_is_unique)


def test_boolean_field_default():
    field = models.BooleanField()
    assert generate_default_value(field) is True


@pytest.mark.parametrize(
    "field_type",
    [
        models.CharField,
        models.FileField,
        models.ImageField,
        models.SlugField,
        models.TextField,
    ],
)
class TestCharFieldDefault:
    def test_nonunique(self, field_type):
        field = field_type(max_length=9, unique=False)
        assert generate_default_value(field) == "abcd"

    @pytest.mark.parametrize("field_is_unique", [True, False])
    def test_unique(self, field_type, field_is_unique):
        field = field_type(max_length=9, unique=field_is_unique)
        default = generate_default_value(field, unique=not field_is_unique)
        assert isinstance(default, collections.Callable)
        assert default() == "abcd"
        assert default() == "abce"

    def test_short_max_length(self, field_type):
        field = field_type(max_length=3, unique=False)
        assert generate_default_value(field) == "abc"


class TestDateFieldDefault:
    def test_nonunique(self):
        field = models.DateField()
        assert generate_default_value(field) == datetime.date(1970, 1, 1)

    @pytest.mark.parametrize("field_is_unique", [True, False])
    def test_unique(self, field_is_unique):
        field = models.DateField(unique=field_is_unique)
        default = generate_default_value(field, unique=not field_is_unique)
        assert isinstance(default, collections.Callable)
        assert default() == datetime.date(1970, 1, 1)
        assert default() == datetime.date(1970, 1, 2)

    def test_auto_now(self):
        field = models.DateField(auto_now=True)
        assert generate_default_value(field) is None

    def test_auto_now_add(self):
        field = models.DateField(auto_now_add=True)
        assert generate_default_value(field) is None


class TestDateTimeFieldDefault:
    def test_nonunique(self):
        field = models.DateTimeField()
        default = generate_default_value(field)
        assert default == parse_datetime("1970-01-01T00:00Z")

    @pytest.mark.parametrize("field_is_unique", [True, False])
    def test_unique(self, field_is_unique):
        field = models.DateTimeField(unique=field_is_unique)
        default = generate_default_value(field, unique=not field_is_unique)
        assert isinstance(default, collections.Callable)
        assert default() == parse_datetime("1970-01-01T00:00Z")
        assert default() == parse_datetime("1970-01-01T01:00Z")

    def test_auto_now(self):
        field = models.DateTimeField(auto_now=True)
        assert generate_default_value(field) is None

    def test_auto_now_add(self):
        field = models.DateTimeField(auto_now_add=True)
        assert generate_default_value(field) is None


class TestFloatFieldDefault:
    def test_nonunique(self):
        field = models.FloatField()
        assert generate_default_value(field) == approx(0)

    @pytest.mark.parametrize("field_is_unique", [True, False])
    def test_unique(self, field_is_unique):
        field = models.FloatField(unique=field_is_unique)
        default = generate_default_value(field, unique=not field_is_unique)
        assert isinstance(default, collections.Callable)
        assert default() == approx(0)
        assert default() == approx(1)


@pytest.mark.parametrize(
    "field_type",
    [
        models.BigIntegerField,
        models.DecimalField,
        models.IntegerField,
        models.PositiveIntegerField,
        models.PositiveSmallIntegerField,
        models.SmallIntegerField,
    ],
)
class TestIntegerFieldDefault:
    def test_nonunique(self, field_type):
        field = field_type()
        assert generate_default_value(field) == 0

    @pytest.mark.parametrize("field_is_unique", [True, False])
    def test_unique(self, field_type, field_is_unique):
        field = field_type(unique=field_is_unique)
        default = generate_default_value(field, unique=not field_is_unique)
        assert isinstance(default, collections.Callable)
        assert default() == 0
        assert default() == 1


class TestTimeFieldDefault:
    def test_nonunique(self):
        field = models.TimeField()
        default = generate_default_value(field)
        assert default == parse_time("00:00Z")

    @pytest.mark.parametrize("field_is_unique", [True, False])
    def test_unique(self, field_is_unique):
        field = models.TimeField(unique=field_is_unique)
        default = generate_default_value(field, unique=not field_is_unique)
        assert isinstance(default, collections.Callable)
        assert default() == parse_time("00:00:00")
        assert default() == parse_time("00:00:01")

    def test_auto_now(self):
        field = models.TimeField(auto_now=True)
        assert generate_default_value(field) is None

    def test_auto_now_add(self):
        field = models.TimeField(auto_now_add=True)
        assert generate_default_value(field) is None


def test_json_field_default():
    field = postgres.JSONField()
    assert generate_default_value(field) == {}
