name = str(input())
price = int(input())
wght = float(input())
cash = int(input())
cost = price * wght
chng = cash - cost
print (" Чек", name, "\n", wght, "кг", "\n" , price, "руб/кг", "\n", "Итого:", cost, "руб", "\n", "Внесено:", cash, "руб", "\n", "Сдача:", int(chng), "руб")