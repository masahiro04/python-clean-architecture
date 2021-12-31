import pytest
import uuid
from unittest import mock

from domain.room import Room
from use_cases.room_list import room_list_use_case


@pytest.fixture
def domain_rooms():
    room1 = Room(
        code=uuid.uuid4(),
        size=200,
        price=10,
        longitude=-0.09998975,
        latitude=51.75436293
    )

    room2 = Room(
        code=uuid.uuid4(),
        size=405,
        price=65,
        longitude=0.18228006,
        latitude=51.74640997
    )

    room3 = Room(
        code=uuid.uuid4(),
        size=56,
        price=60,
        longitude=0.27891577,
        latitude=51.45994069
    )
    room4 = Room(
        code=uuid.uuid4(),
        size=93,
        price=48,
        longitude=0.33894476,
        latitude=51.39916678
    )

    return [room1, room2, room3, room4]


def test_room_list_without_parameteres(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms

    result = room_list_use_case(repo)

    repo.list.assert_called_with()
    assert result == domain_rooms
