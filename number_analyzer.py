
def analyze_numbers(num_array, threshold = 0, include_equal = False):

    if not isinstance(num_array, list):
        raise TypeError("Please enter list only")
    
    for num in num_array:
        if type(num) not in (int, float):
            raise TypeError("Please enter number in the list only")

    if not num_array:
        return {
                    "even_numbers": [],
                    "even_count": 0,
                    "odd_numbers": [],
                    "average": 0,
                    "largest_even": None,
                    "total": 0,
                    "odd_count": 0,
                    "sorted_numbers": [],
                    "smallest_number": None,
                    "above_threshold": []
               }

    even_numbers =  [num for num in num_array if num%2 == 0]
    odd_numbers = [num for num in num_array if num%2 != 0]
    if (include_equal):
      above_threshold = [num for num in num_array if num >= threshold]
    else:
       above_threshold = [num for num in num_array if num > threshold]   
            
    total = sum(num_array)
    average = total / len(num_array)
    even_count = len(even_numbers)
    odd_count = len(odd_numbers)
    sorted_numbers = sorted(num_array)
    smallest_number = min(num_array)
    
    if not even_numbers:
        largest_even = None
    else:
        largest_even = max(even_numbers)

    return {
                "even_numbers": even_numbers,
                "odd_numbers": odd_numbers,
                "average": average,
                "largest_even": largest_even, 
                "total": total,
                "even_count": even_count,
                "odd_count": odd_count,
                "sorted_numbers": sorted_numbers,
                "smallest_number": smallest_number,
                "above_threshold": above_threshold
            }

if __name__ == "__main__":
    print(analyze_numbers([10, 20, 30]))