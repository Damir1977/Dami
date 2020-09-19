
mnc = 1  #main_cycle (основной цикл)
while mnc > 0:
    i = 0  # (для чтения списка mem)
    chk = 0  # (контроль расхода краски)
    screw = 0  # (саморезы)
    sc = 1  # screw_cycle (цикл саморезов)
    mem = []  # memory (хранение списка покрашенного)
    
    print('---РАСЧЕТ КРАСКИ---')
    print('Остаток с прошлой смены')
    col_p = int(input())
    print('Взято со склада')
    col_s = int(input())
    print('Остаток краски на конец смены ')
    col_l = int(input())  
    col = (col_p + col_s) - col_l  # подсчет краски
    
    print ('\n ---РАСЧЕТ САМОРЕЗОВ---')
    print('Сколько покрашено саморезов по заявкам.\n Для завершения ввода введите 0')
    while sc != 0:
        sc = int(input())
        screw = screw + sc
        mem.append(sc)  # пока не введен 0 заносим в список покрашенное
    mem.pop()  # удаляем последнее введенное число (0)
    
    kf = col/screw  # коофициент расхода
    c = len(mem)
    print("Всего покрашено-", screw, "саморезов")
    print('Использованно-', col, 'краски')
    print('Расход на 1000шт.-', round(kf, 4),"\n")
    
    for i in range(c):
        a = mem[i]  
        ras = a * kf  # от английского the rashode -расход краски
        ras = round(ras)
        chk = chk + ras  # контроль точности расхода.
        if i == c-1:  # в последней итерации сверяем правильность расхода краски
            if chk < col:
                mod = col-chk
                mod = abs(mod)
                ras = mod + ras
            if chk > col:
                mod = chk-col
                mod = abs(mod)
                ras = ras-mod
        print("На ", a, " затрачено ", round(ras, 0), "краски \n ")
    print("\n Для нового ввода данных введите 1, для выхода 0")
    a = input()
    if a == "0":
        mnc=0
        print("Хорошего дня!")
