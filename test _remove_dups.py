import pytest

def remove_dups(your_list):
  new_set = set(your_list)
  new_list = list(new_set)
  return(new_list)  


@pytest.mark.parametrize("[list],[list]"[("blue", "green", "blue"),("blue", "green")])

def test_remove_dups(test_input, expected):
    assert remove_dups(test_input) == expected