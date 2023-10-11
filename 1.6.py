def number_count (lists):
    lists=[]
    count_dict = dict()
    for i in lists:
        if i in count_dict:
                count_dict[i] +=1
        else:
                count_dict[i] = 1
    return(count_dict)
