map_l = [0, 1, 1, 0], [0, 0, 1, 1], [0, 1, 1, 0], [0, 0, 1, 1], \
        [1, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 0, 1, 1], \
        [1, 1, 1, 0], [1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 1, 0], \
        [1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 1, 0]

room_type = ["сырой и темной", "темной и вонючей", "грязной,со скользким полом", "страшной и мрачной "]
item_list = ["Золотой ключ", 0], ["Топор", 0], ["Кольцо", 0], ["Бронзовый ключ", 3], ["Секира", 7], ["Коньяк", 15], [
    "медный ключ", 11], ["Молот", 20], ["Кольцо серебрянное", 14], ["Бронзовый меч", 9], ["Пила", 10], ["Водка", 250]

flag_1     = 0
room       = 0
item_check = 0


def item_in_room(item_check):
    global flag_1
    flag_1 = 0
    for i in range(0, len(item_list)):
        it = item_list[i][1]
        if it == room and flag_1 == 0:
            flag_1 = 1
            print(" На полу валяется:")
        if it == room and flag_1 > 0:
            print(item_list[i][0])
    return item_check


def item_in_inv(item_check):
    global flag_1
    flag_1 = 0
    for i in range(0, len(item_list)):

        it = item_list[i][1]
        if it == 250 and flag_1 == 0:
            flag_1 = 1
            print(" В карманцах лежит:")
        if it == 250 and flag_1 > 0:
            print(item_list[i][0])

    return item_check


#  Логика item_in_room - Число в  item_list, после названия обозначает либо комнату где он лежит/оставлен
#  Логика item_in_inv - либо содержит число 250 означающее, что предмет лежит в карманах игрока

#  Чуть чуть улчшаем текст, добавляя  описание комнат
def rooms_type(room):
    if room >= 0 and room <= 3:
        b = room_type[0]
    if room >= 4 and room <= 7:
        b = room_type[1]
    if room >= 8 and room <= 11:
        b = room_type[2]
    if room >= 12 and room <= 15:
        b = room_type[3]
    return b


while room <= len(map_l) - 1:
    item_check = room
    n = map_l[room][0]  # North
    w = map_l[room][1]  # West
    s = map_l[room][2]  # South
    e = map_l[room][3]  # East

    b = rooms_type(room)
    print("\n" * 30)
    print("Вы стоите в ", b, "комнате \n")

    er = item_in_room(item_check)   # Что на полу
    er = item_in_inv(item_check)  # Что в инвентаре

    print(" \n Есть выходы на: ", end=" ")
    if n == 1:
        print("Север", end=" ")
    if w == 1:
        print("Запад", end=" ")
    if s == 1:
        print('Юг', end=" ")
    if e == 1:
        print("Восток")
    print('\n Куда пойдем?')
    m = input().lower()
    if m == "с" and n == 1:
        room -= 4
        continue
    if m == "з" and w == 1:
        room += 1
        continue
    if m == "ю" and s == 1:
        room += 4
        continue
    if m == "в" and e == 1:
        room -= 1
        continue
    print(" \n Тут нет выхода!")

print("Вы проснулись!")
