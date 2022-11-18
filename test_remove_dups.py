import pytest
from main import remove_dups
 
@pytest.mark.parametrize("list_with_dups, cleaned_list", [
    (["blue"], ["blue"]),
    (['blue', 'green', 'blue'], ['blue', 'green']),
    ([], [])
    ("string", "" )
])

def test_remove_dups(list_with_dups, cleaned_list):
    assert remove_dups(list_with_dups) == cleaned_list