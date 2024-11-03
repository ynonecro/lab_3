def find_common_participants(participants1, participants2, sep=','):
    set_first_group = set(participants1.split(sep))
    list_second_group = set(participants2.split(sep))

    common_set = set_first_group.intersection(list_second_group)
    common_list = list(common_set)
    common_list.sort()
    return common_list
