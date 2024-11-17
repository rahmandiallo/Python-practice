def set_covering(universal_set , set_of_subsets):

    # second_rule
    set_of_subsets.sort(reverse=True,key=len)
    # Third list : Mandatory list : Contains the sublists with unique elements (Second Rule)
    mand_subsets = []
    # Second_list : Removes any sublists that are elements in a larger sublist (First Rule)
    updated_subsets = []
    # General List : Used to append all the sublists into one whole list.
    all_subsets = []

    # second_rule
    
    # This for loop appends each sublist value to a single list all_subsets
    for i in range(0,len(set_of_subsets)):
        single_subset = set_of_subsets[i] 
        for j in range(0,len(single_subset)):
            all_subsets.append(single_subset[j])

    # This for loop checks if the "all_subsets" list contains any unique elements.
    for z in range(0,len(all_subsets)):
        if all_subsets.count(all_subsets[z]) == 1:
            unique_value = all_subsets[z]


    # Finds the sublists that contains the unique values and appends these to the "mand_subsets" list
    for x in range(0,len(set_of_subsets)):
        if unique_value in set_of_subsets[x]:
            unique_set = set_of_subsets[x]
            mand_subsets.append(unique_set)

    

    # make a copy of the set of subsets 
    updated_subsets = set_of_subsets

    # first rule
    # checks if a sublist contains elements of a larger sublist
    # used a nested for loop to compare each sublist with each other e.g [1,2,3,4,5,6] --> [1,2,3,4,5] , [1,2,3,4,5,6] --> [0,1,2,3]
    for a in range(0,len(set_of_subsets)):
        # sublist we want comparisons with 
        main_element = set_of_subsets[a]
        for b in range(a+1,len(set_of_subsets)):
            # compare with main_sublist
            current_element = updated_subsets[b]
            # if main sublist has all the elements of current sublist , remove the current sublists from updated _sublists
            if all(v in main_element for v in current_element):
                # code not working right now, giving an index error , Next Step : Fix it ;)
                updated_subsets.remove(current_element)
                
        
    

    return updated_subsets
        





print(set_covering([0,1, 2, 3, 4, 5, 6, 7, 8] , [[1, 2, 3, 4, 5], [0, 1, 2, 3], [4, 5, 6, 8], [1, 2, 3, 4, 5, 6], [4, 5, 6, 7], [4, 5, 6, 7, 8]]))

