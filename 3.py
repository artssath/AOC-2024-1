import re

def extract_multiplications(input_string):
    # Find valid mul instructions
    mul_pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
    
    # Find all corrupted memory
    matches = re.findall(mul_pattern, input_string)
    
    # sum of valid mul
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return int(total_sum) if total_sum else 0

def read_corrupt_data(file):
    input_data=open(file,'r').readlines()
    data_merge=""
    do_pattern="^()"
    dont_pattern=r"^n't"
    result=0
    for line in input_data:
        data_merge+=line
    do_segment=data_merge.split('do')
    for do_line in do_segment:
            if not re.search(dont_pattern, do_line) and re.search(do_pattern, do_line):
                result += extract_multiplications(do_line)
    return result

if __name__ == "__main__":
    result = read_corrupt_data("input-3")
    print(f"The total sum of valid multiplications is: {result}")