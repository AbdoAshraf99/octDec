#sheet1 Q12

def octDec(num):
    if 'o' in num:
        x=num.split('o')
        number=int(x[1])
        decimal_value = 0
        base = 1
        while (number):
            last_digit = number % 10
            number = int(number / 10)
            decimal_value += last_digit * base
            base = base * 8
        print("decimal number= ", decimal_value)
    else:
        print("octal number=",oct(int(num)))


octDec('0o170')