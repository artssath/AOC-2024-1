
def read_data_list(file):
    input_data=open(file,'r').readlines()
    data_lines=[]
    for line in input_data:
        line=line.split('\n')[0].strip()
        data_lines.append(line)
    return data_lines

def is_safe(levels):    
    
    if len(levels) < 2:
        return False 
    
    # Check increasing or all decreasing
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))

    # Check adjacent levels for diff  atleast 1 and at most 3
    valid_differences = all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))

    return (increasing or decreasing) and valid_differences

def can_be_safe_with_one_removal(levels):
    for i in range(len(levels)):
        # new list without the level
        new_levels = levels[:i] + levels[i + 1:]
        if is_safe(new_levels):
            return True
    return False

def analyze_report(reports):
    safe_list = []
    unsafe_list = []
    safe_list_change=[]
    unsafe_list_change=[]
    for report in reports:
        levels = list(map(int, report.split()))
        if is_safe(levels):
            safe_list.append(report)
        else:
            unsafe_list.append(report)
        if can_be_safe_with_one_removal(levels):
            safe_list_change.append(report)
        else:
            unsafe_list_change.append(report)
    return safe_list, unsafe_list, safe_list_change, unsafe_list_change



if __name__ == "__main__":
    reports = read_data_list("input-2")
    safe_list, unsafe_list, safe_list_change, unsafe_list_change = analyze_report(reports)

    print("Safe Reports     : " + str(len(safe_list)) )
    print("Unsafe Reports   : " + str(len(unsafe_list)))
    print("Safe Reports after change   : " + str(len(safe_list_change)))
    print("Unsafe Reports after change : " + str(len(unsafe_list_change)))
