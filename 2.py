
def read_data_list(file):
    input_data=open(file,'r').readlines()
    data_lines=[]
    for line in input_data:
        line=line.split('\n')[0].strip()
        data_lines.append(line)
    return data_lines

def is_safe(report):
    levels = list(map(int, report.split()))
    
    if len(levels) < 2:
        return False  # A report with fewer than 2 levels can't be evaluated
    
    # Check if levels are all increasing or all decreasing
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))

    # Check adjacent levels differ by at least 1 and at most 3
    valid_differences = all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))

    return (increasing or decreasing) and valid_differences

def analyze_report(reports):
    safe_list = []
    unsafe_list = []
    for report in reports:
        if is_safe(report):
            safe_list.append(report)
        else:
            unsafe_list.append(report)

    return safe_list, unsafe_list

# Example usage
if __name__ == "__main__":
    # Example report data
    reports = read_data_list("input-2")
    safe_list, unsafe_list = analyze_report(reports)

    print("Safe Reports:")
    print(str(len(safe_list)))

    print("\nUnsafe Reports:")
    print(str(len(unsafe_list)))