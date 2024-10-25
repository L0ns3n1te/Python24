def count_letters(the_str):
    letters_list = []
    for i in the_str:
        if not i.islower():
            the_str = the_str.replace(i, i.lower())
    letters_dict = {}
    for i in the_str:
        if i.isalpha():
            letters_list.append(i)
    return letters_list


def calculate_frequency(the_str, letters_dict):
    n = 0
    for i in the_str:
        if i.isalpha():
            n += 1
    frequency_dict = {}
    for i in letters_dict:
        if letters_dict.count(i) / n >= 0.005:
            frequency_dict[i] = round(letters_dict.count(i) / n, 2)
        else:
            frequency_dict[i] = "0.00"
    return frequency_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
for i in calculate_frequency(main_str, count_letters(main_str)):
    print(f"{i}: {calculate_frequency(main_str, count_letters(main_str))[i]}")

