
while True:
    check_paint_consumption = 0  
    screw = 0  
    screw_mem = []  
    #   Выясняем остаток краски на начало смены, сколько потрачено и  остаток в конце смены
    print ('---РАСЧЕТ КРАСКИ---')
    print ('Остаток с прошлой смены')
    paint_p = int(input())
    print ('Взято со склада')
    paint_s = int(input())
    print ('Остаток краски на конец смены ')
    paint_l = int(input())
    full_paint_consumption = (paint_p + paint_s) - paint_l  # сколько потрачено краски за смену
    #   расчет покрашеных саморезов
    print ('\n ---РАСЧЕТ САМОРЕЗОВ---')
    print ('Сколько покрашено саморезов по заявкам? \n Для завершения  введите 0')
    while True:
        screw_input = int(input())
        if screw_input <= 0:
            break
        screw = screw + screw_input
        screw_mem.append(screw_input)
    coeff_consumption = full_paint_consumption / screw  # выясняем коэфициент расхода краски
    print ('Всего покрашено-', screw, 'саморезов')
    print ('Использованно-', full_paint_consumption, 'краски')
    print ('Расход на 1000шт.-', round(coeff_consumption, 4),'\n')
    j = len(screw_mem)
    for i in range(j):
        tmp = screw_mem[i]
        paint_consumption = int(tmp * coeff_consumption)  # расход краски по заданию
        if i == j-1:  # в последней итерации сверяем правильность расхода краски
            if check_paint_consumption + paint_consumption  != full_paint_consumption:
                paint_consumption = (full_paint_consumption - check_paint_consumption)
        check_paint_consumption = check_paint_consumption + paint_consumption  # контроль точности расхода.
        print ('На ', tmp, 'саморезов  затрачено ', int (paint_consumption), 'краски \n ')
    print ('\n Для нового ввода данных введите 1, для выхода 0')
    a = input()
    if a == "0":
        print('Хорошего дня!')
        break
