# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator=","):
    participants_first_group_list = participants_first_group.split(separator)
    participants_second_group_list = participants_second_group.split(separator)
    in_both_groups_list = []
    for i in participants_first_group_list:
        if i in participants_second_group_list:
            in_both_groups_list.append(i)
    in_both_groups_list.sort()
    return in_both_groups_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
