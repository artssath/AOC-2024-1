def read_data_list(file):
    input_data=open(file,'r').readlines()
    left_nums=[]
    right_nums=[]
    for line in input_data:
        line=line.split('\n')[0].strip()
        l, r = map(int, line.split())
        left_nums.append(int(l))
        right_nums.append(int(r))
    return left_nums,right_nums

def calculate_total_distance(left_dist, right_dist):
    # Check if both len are equal
    if left_dist == right_dist:
        print("The two lists doesn't contain the equal no of elements.")    
    # Sort the lists
    left_sorted = sorted(left_dist)
    right_sorted = sorted(right_dist)
    
    # Calculate total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    
    return total_distance

def calculate_total_similarity(left_dist, right_dist):
    total_similarity=0
    count_dict={}
    for r_num in right_dist:
        if r_num not in count_dict.keys():
            count_dict[r_num]=0
        count_dict[r_num] +=1

    for l_num in left_dist:
        if l_num in count_dict.keys():
            total_similarity += l_num * count_dict[l_num]
    return total_similarity

if __name__ == "__main__":
    left_dist,right_dist=read_data_list("input-1")
    result = calculate_total_distance(left_dist, right_dist)
    print(f"The total distance: {result}")
    result = calculate_total_similarity(left_dist, right_dist)
    print(f"The total similarity: {result}")