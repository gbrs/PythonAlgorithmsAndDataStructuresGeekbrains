'''3. Сформировать из введенного числа обратное по порядку входящих в него цифр
и вывести на экран. Например, если введено число 3486, надо вывести 6843
'''


number = int(input("Введите натуральное число: "))
new_number = 0

while number > 0:
    new_number = new_number * 10 + number % 10
    number //= 10

print(new_number)
