# sources ={"Alice": 50, "Bob": 75, "Charlie": 60}

# listing_item = list(sources.items())

# print("Before Sorting " , listing_item)

# listing_item.sort(reverse=True)

# print("After Sorting " ,listing_item)

def sort_dict_desc(original_dict):
    sorted_dict = {}

    while original_dict:
        max_key = max(original_dict, key=original_dict.get)
        

        sorted_dict[max_key] = original_dict.pop(max_key)
        
    return sorted_dict

original_dict = {"Alice": 50, "Bob": 75, "Charlie": 60}
print(" Original Dictionary ", original_dict)

sorted_dict = sort_dict_desc(original_dict.copy())
print(" Sorted Dictionary in Descending Order ", sorted_dict)
