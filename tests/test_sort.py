from src.sort import sort_numbers
def test_bubble_sort_empty_list():
    assert sort_numbers([]) == []

def test_bubble_sort_single_element():
    assert sort_numbers([1]) == [1]

def test_bubble_sort_sorted_list():
    assert sort_numbers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_reverse_sorted_list():
    assert sort_numbers([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bubble_sort_random_list():
    assert sort_numbers([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_bubble_sort_duplicate_elements():
    assert sort_numbers([2, 2, 1, 1, 3, 3]) == [1, 1, 2, 2, 3, 3]