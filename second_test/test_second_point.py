from second_point import reorganize

def test_reorganize():
    acc = ['']
    item = 1
    expected_result = ['1']
    assert reorganize(acc, item) == expected_result

    acc = ['']
    item = 0
    expected_result = ['', 'X']
    assert reorganize(acc, item) == expected_result

    acc = ['1']
    item = 3
    expected_result = ['13']
    assert reorganize(acc, item) == expected_result

    acc = ['13']
    item = 2
    expected_result = ['123']
    assert reorganize(acc, item) == expected_result

    acc = ['123']
    item = 0
    expected_result = ['123', 'X']
    assert reorganize(acc, item) == expected_result

    acc = ['123', '']
    item = 7
    expected_result = ['123', '7']
    assert reorganize(acc, item) == expected_result

    acc = ['1237']
    item = 8
    expected_result = ['12378']
    assert reorganize(acc, item) == expected_result

    acc = ['12378']
    item = 1
    expected_result = ['112378']
    assert reorganize(acc, item) == expected_result

    acc = ['1237813', '']
    item = 0
    expected_result = ['1237813', '', 'X']
    assert reorganize(acc, item) == expected_result

    acc = ['1237813', 'X']
    item = 6
    expected_result = ['1237813', '6']
    assert reorganize(acc, item) == expected_result

test_reorganize()