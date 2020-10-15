map_l = [0, 1, 1, 0], [0, 0, 1, 1], [0, 1, 1, 0], [0, 0, 1, 1], \
        [1, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 0, 1, 1], \
        [1, 1, 1, 0], [1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 1, 0], \
        [1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 2, 0]
# 0 - нет прохода  1 - проход  2 - закрытая дверь  3 - открытая дверь
room_type = ["сырой и темной", "темной и вонючей", "грязной,со скользким полом", "страшной и мрачной "]
item_list = ["Золотой ключ", 250], ["Топор", 0], ["Кольцо", 0], ["Бронзовый ключ", 3], ["Секира", 7], ["Коньяк", 15], [
    "медный ключ", 11], ["Молот", 20], ["Кольцо серебрянное", 14], ["Бронзовый меч", 9], ["Пила", 10], ["Водка", 250]

tmp_flag     = 0
room       = 15
item_check = 0
def door_and_exit (room):

    n = map_l[room][0]  # North
    w = map_l[room][1]  # West
    s = map_l[room][2]  # South
    e = map_l[room][3]  # East

    print ("Есть выходы:")
    if n == 1:
        print ('Север')
    if n == 2:
        print ('Север  дверь')
    if w == 1:
        print ('Запад')
    if w == 2:
        print ('Запад  дверь')
    if s == 1:
        print ('Юг')
    if s == 2:
        print ('Юг дверь')
    if e == 1:
        print ('Восток')
    if e == 2:
        print ('Восток дверь')
    return room

def item_in_room (item_check):
    tmp_flag = 0
    for i in range(0, len(item_list)):
        it = item_list[i][1]
        if it == room and tmp_flag == 0:
            tmp_flag = 1
            print(" На полу валяется:")
        if it == room and tmp_flag > 0:
            print(item_list[i][0])
    return item_check
def item_in_inv(item_check):
    tmp_flag = 0
    for i in range(0, len(item_list)):

        it = item_list[i][1]
        if it == 250 and tmp_flag == 0:
            tmp_flag = 1
            print(" В карманцах лежит:")
        if it == 250 and tmp_flag > 0:
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

    er = rooms_type(room)
    print("\n" * 30)
    print("Вы стоите в ", er, "комнате \n")

    er = item_in_room(item_check)   # Что на полу
    er = item_in_inv(item_check)  # Что в инвентаре
    er = door_and_exit(room)
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
    if m == "ю" and s == 2 and item_list [0][1] == 250 :
        map_l[room][s] == 1
        room += 4
        continue
    if m == "в" and e == 1:
        room -= 1
        continue
    print(" \n Тут нет выхода!")
print (map_l[15][2])
print("Вы проснулись!")
