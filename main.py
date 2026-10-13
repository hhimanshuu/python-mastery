from number_analyzer import analyze_numbers

lists_to_analyze = [
    [10, 20, 30], 
    [5, 12, 17, 24, 31]
]

for index, numbers in enumerate(lists_to_analyze, start=1):
    result = analyze_numbers(numbers)
    print(f"Dataset {index}")
    print(f"Numbers: {numbers}")
    print(f"Average: {result['average']:.2f}")
    print(f"Largest even: {result['largest_even']}")
    print(f"Sorted Numbers: {result['sorted_numbers']}")
    print("----------------------")