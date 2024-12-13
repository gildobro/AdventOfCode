
leftlist = [3, 4, 2, 1, 3, 3]
rightlist = [4, 3, 5, 3, 9, 3]
new_list = []


def difference(num1, num2):
    return abs(num1 - num2)

def distance(leftlist, rightlist):
    #take right list, compare it to the left list. Find the smallest number in the right list, find smallest number in the left list.
    #Find the diff between smallright and small left, append to new list. Add all numbers in new list
    # for i in leftlist:
    #     for j in leftlist:
    #         print(i, j)
    print(min(leftlist), min(rightlist))

    #find difference between smallest numebrs in the list
    min_diff = difference(min(leftlist), min(rightlist))

    #append difference to new list
    new_list.append(min_diff)
    
    #Remove the smallest number from each list
    leftlist.remove(min(leftlist))
    rightlist.remove(min(rightlist))

    print(new_list, leftlist, rightlist)

    #TODO--> do this same process by iterating through the entire lists



distance(leftlist, rightlist)