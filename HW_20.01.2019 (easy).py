# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print('Задача-1.Решение-1.')
def my_round(number, ndigits):
    mult = 10 ** ndigits
    x = mult * number
    x_main = int(x)
    x_remain = x - x_main
    if abs(x_remain)>= 0.5:
        if x_remain > 0:
            x_main += 1
        else:
            x_main -= 1
    return(x_main / mult)
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999997, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

print('Задача-2.Решение-1.')
def lucky_ticket(ticket_number):
    num_list = str(ticket_number)
    first_nums = 0
    last_nums = 0
    for i in range(3):
            first_nums += int(num_list[i])
            last_nums += int(num_list[-i-1])
    return first_nums == last_nums

print(lucky_ticket(123006))
print(lucky_ticket(120210))
print(lucky_ticket(436751))