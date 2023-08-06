"""Test options."""

from simpleconf2 import Section, Option, exceptions
from pytest import raises


def test_existing():
    """Test existing options."""
    value = 'testing'

    class Config(Section):
        title = 'Test'
        test = Option(value, title='Testing')

    c = Config()
    c.test = Option(value, title='&Testing')
    assert c['test'] == value
    value *= 2
    c['test'] = value
    assert c['test'] == value


def test_nonexisting():
    """Test an option which doesn't exist."""
    c = Section()
    with raises(exceptions.NoOptionError):
        c['nothing'] = 4


def test___str__():
    name = 'Testing'
    o = Option('whatever', title=name)
    assert o.get_title() == name
