def tree_intersection(bt1,bt2):

    hash_table = []
    common_values = []

    for value in bt1:
        hash_table.append(value)
      
    for value in bt2:
        if value in hash_table:
            common_values.append(value)

    return common_values
