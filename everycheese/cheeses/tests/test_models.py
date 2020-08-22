import pytest

# connects our tests to our database

pytestmark = pytest.mark.django_db

from ..models import Cheese

def test__str__():
    cheese = Cheese.objects.create(
        name='Stachhino',
        description='Semi-sweet cheese that goes will with starches',
        firmness=Cheese.Firmness.SOFT
    )

    assert cheese.__str__() == "Stachhino"
    assert str(cheese) == "Stachhino"