from number_analyzer import analyze_numbers

assert analyze_numbers([10, 20, 30])["total"] == 60
assert analyze_numbers([10, 20, 30])["largest_even"] == 30
assert analyze_numbers([])["average"] == 0
assert analyze_numbers([1, 3, 5])["largest_even"] is None

assert analyze_numbers([10, 20, 30, 40], threshold=30)["above_threshold"] == [40]
assert analyze_numbers([10, 20, 30, 40], threshold=30, include_equal=True)["above_threshold"] == [30, 40]
assert analyze_numbers([1, 2, 3])["above_threshold"] == [1, 2, 3]