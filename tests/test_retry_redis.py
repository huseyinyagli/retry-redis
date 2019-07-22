"""
:author: Gatsby Lee
:since: 2019-04-10
"""
import pytest

from retry_redis import Redis

def test_object_creation_with_default_value():
    """
    Test that Redis instance could be created with
    default value argument.
    """
    Redis()


def test_simple_positive_op():
    """
    Test that simple operation still works
    """
    res = Redis().lpush('list:test', 1)
    assert res
