import re

def extract_multiplications(input_string):
    # Regular expression to find valid mul instructions
    mul_pattern = r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'
    
    # Find all matches in the corrupted memory
    matches = re.findall(mul_pattern, input_string)
    
    # Calculate the sum of multiplications
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return int(total_sum) if total_sum else 0

def read_corrupt_data(file):
    input_data=open(file,'r').readlines()
    result=0
    for line in input_data:
        result += extract_multiplications(line)
    return result

# Example usage
if __name__ == "__main__":
    result = read_corrupt_data("input-3")
    print(f"The total sum of valid multiplications is: {result}")