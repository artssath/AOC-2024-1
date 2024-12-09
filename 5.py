from collections import defaultdict, deque

def read_data_list(file):
    input_data=open(file,'r').read()
    return input_data


def parse_input(input_data):
    rules, updates = input_data.strip().split('\n\n')
    page_rules={}
    
    ordering_rules = [line.split('|') for line in rules.splitlines()]
    updates = [list(map(int, update.split(','))) for update in updates.splitlines()]
   
    for rule in ordering_rules:
        if int(rule[0]) not in page_rules.keys():
            page_rules[int(rule[0])] = []
        page_rules[int(rule[0])].append(int(rule[1]))
    return ordering_rules, updates,page_rules


def is_valide(update, page_rules):    
    for i in range(len(update)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if i == j : continue
            try:
                if update[j] in page_rules[update[i]]:
                    return False
            except KeyError:
                    pass
    return True

def fix_page_order(update, page_rules):
    updated=update
    while not is_valide(update,page_rules):
        for i in range(len(update)):
            flag=False
            if flag: break
            for j in range(i+1,len(update)):
                if i == j : continue
                try:
                    if  update[i] not in page_rules.keys() or update[j] not in page_rules[update[i]]:
                        tmp=update[j]
                        updated[j]=update[i]
                        updated[i]=tmp
                        flag=True
                        break
                except KeyError:
                    pass
        update=updated

    return update

def find_middle_page(update):
    mid_index = len(update) / 2
    return update[int(mid_index)]

def main(input_data):
    ordering_rules, updates, page_rules = parse_input(input_data)
    total_middle_sum = 0
    total_re_middle_sum = 0
    for update in updates:
        if is_valide(update, page_rules):
            middle_page = find_middle_page(update)
            total_middle_sum += int(middle_page)
        else:
            re_update = fix_page_order(update,page_rules)
            middle_page = find_middle_page(re_update)  
            total_re_middle_sum += int(middle_page)


    return total_middle_sum,total_re_middle_sum

# Example input
input_data = read_data_list("input-5")

# Run the main function
result, re_result = main(input_data)
print(f'The sum of the middle page numbers of correctly ordered updates is: {result}')
print(f'The sum of the middle page numbers of correctly ordered updates is: {re_result}')