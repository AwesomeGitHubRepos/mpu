#!/usr/bin/env python

# Third party
import hypothesis.strategies as st
import pytest
from hypothesis import given

# First party
import mpu.string


def test_str2bool_no_mapping():
    with pytest.raises(ValueError):
        mpu.string.str2bool("foobar")


@pytest.mark.parametrize("illegal_default", ["foobar", True])
def test_str2bool_illegal_default(illegal_default):
    with pytest.raises(ValueError):
        mpu.string.str2bool("yes", default=illegal_default)


@pytest.mark.parametrize("illegal_default", ["foobar", True])
def test_str2bool_or_none_illegal_default(illegal_default):
    with pytest.raises(ValueError):
        mpu.string.str2bool_or_none("yes", default=illegal_default)


def test_is_iban_not():
    assert mpu.string.is_iban("DE12") is False
    assert mpu.string.is_iban("") is False
    assert mpu.string.is_iban("ZZaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") is False
    assert mpu.string.is_iban("DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") is False


def test_is_iban():
    iban = "FR14 2004 1010 0505 0001 3M02 606"
    assert mpu.string.is_iban(iban)


@pytest.mark.parametrize("illegal_default", ["foobar", True])
def test_is_none_illegal_default(illegal_default):
    with pytest.raises(ValueError):
        mpu.string.is_none("none", default=illegal_default)


def test_is_none_not():
    with pytest.raises(ValueError):
        mpu.string.is_none("foobar")


@given(st.emails())
def test_is_email(email):
    assert mpu.string.is_email(email), f"is_email({email}) returned False"


@given(st.ip_addresses(v=4))
def test_is_ipv4(ip):
    assert mpu.string.is_ipv4(str(ip)), f"is_ipv4({ip}) returned False"
