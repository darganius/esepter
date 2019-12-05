from pyzt import inputi, inputf, inputs


def input_digit():
    print('Hex system starts From 0x')
    print('Octal system starts From 0c')
    print('Binary system starts From 0b')
    print('Decimal system starts from 0d')
    x = input('Input your number: ')
    tekseru(x)
    return x


def tekseru(x):
    hexa = set('0123456789AaBbCcDdEeFf')
    octa = set('01234567')
    deci = set('0123456789')
    binary = set('01')
    san = x
    x = set(x)
    while True:
        if '0' and 'b' in x:
            print('Choose 1) 2 --> 10')
            print('Choose 2) 2 --> 16')
            print('Choose 3) 2 --> 8')
            print('Choose 4) To Enter another digit')
            print('Choose 5) To Exit')
            a = inputi('Input your choice: ')
            while True:
                if a == 1:
                    l = []
                    a = 1
                    sum = 0

                    for i in san:
                        l.append(i)
                    l.pop(0)
                    l.pop(0)
                    a1 = len(l)
                    for i in l:
                        sd = int(i) * (2 ** (a1 - a))
                        a1 -= 1
                        if a1 == -1:
                            break
                        sum += sd
                    print('Your decimal numbers is:', sum)
                    break
                elif a == 2:
                    l = []
                    a = 1
                    sum = 0

                    for i in san:
                        l.append(i)
                    l.pop(0)
                    l.pop(0)
                    a1 = len(l)
                    for i in l:
                        sd = int(i) * (2 ** (a1 - a))
                        a1 -= 1
                        if a1 == -1:
                            break
                        sum += sd
                    lis = []
                    while True:
                        a = sum // 16
                        b = sum % 16
                        sum = a
                        if b == 10:
                            lis.append('A')
                        elif b == 11:
                            lis.append('B')
                        elif b == 12:
                            lis.append('C')
                        elif b == 13:
                            lis.append('D')
                        elif b == 14:
                            lis.append('E')
                        elif b == 15:
                            lis.append('F')
                        elif 0 <= b <= 9:
                            lis.append(str(b))
                            break
                        else:
                            break
                    lis.reverse()
                    if lis[0] == '0':
                        lis.pop(0)
                        list = "".join(lis)
                        print(list)
                    else:
                        myStri = ''.join(lis)
                        print(myStri)
                    break
                elif a == 4:
                    input_digit()
                elif a == 3:
                    l = []
                    a = 1
                    sum = 0

                    for i in san:
                        l.append(i)
                    l.pop(0)
                    l.pop(0)
                    a1 = len(l)
                    for i in l:
                        sd = int(i) * (2 ** (a1 - a))
                        a1 -= 1
                        if a1 == -1:
                            break
                        sum += sd
                    s = ''
                    while sum > 0:
                        t = sum // 8
                        s = str(sum % 8) + s
                        sum = t
                    print(s)
                elif a == 5:
                    exit(0)

        elif '0' and 'x' in x:
            while True:
                print('Choose 1) 16 --> 10')
                print('Choose 2) 16 --> 2')
                print('Choose 3) 16 --> 8')
                print('Choose 4) To Enter another digit')
                print('Choose 5) To Exit')
                while True:
                    a = inputi('Input your choice: ')

                    if a == 1:
                        l = []
                        a = 1
                        sum = 0

                        for i in san:
                            l.append(i)
                        l.pop(0)
                        l.pop(0)
                        a1 = len(l)
                        for i in l:
                            if i == 'A' or 'a':
                                i = '10'
                            elif i == 'B' or 'b':
                                i = '11'
                            elif i == 'C' or 'c':
                                i = '12'
                            elif i == 'D' or 'd':
                                i = '13'
                            elif i == 'E' or 'e':
                                i = '14'
                            elif i == 'F' or 'f':
                                i = '15'
                            sd = int(i) * (16 ** (a1 - a))
                            a1 -= 1
                            if a1 == -1:
                                break
                            sum += sd
                        print('Your decimal numbers is:', sum)
                        break
                    elif a == 2:
                        l = []
                        a = 1
                        sum = 0

                        for i in san:
                            l.append(i)
                        l.pop(0)
                        l.pop(0)
                        a1 = len(l)
                        for i in l:
                            if i == 'A' or 'a':
                                i = '10'
                            elif i == 'B' or 'b':
                                i = '11'
                            elif i == 'C' or 'c':
                                i = '12'
                            elif i == 'D' or 'd':
                                i = '13'
                            elif i == 'E' or 'e':
                                i = '14'
                            elif i == 'F' or 'f':
                                i = '15'
                            sd = int(i) * (16 ** (a1 - a))
                            a1 -= 1
                            if a1 == -1:
                                break
                            sum += sd
                        s = ''
                        while sum > 0:
                            t = sum // 2
                            s = str(sum % 2) + s
                            sum = t
                        print('Your decimal number: ', s)

                    elif a == 3:
                        l = []
                        a = 1
                        sum = 0

                        for i in san:
                            l.append(i)
                        l.pop(0)
                        l.pop(0)
                        a1 = len(l)
                        for i in l:
                            if i == 'A' or 'a':
                                i = '10'
                            elif i == 'B' or 'b':
                                i = '11'
                            elif i == 'C' or 'c':
                                i = '12'
                            elif i == 'D' or 'd':
                                i = '13'
                            elif i == 'E' or 'e':
                                i = '14'
                            elif i == 'F' or 'f':
                                i = '15'
                            sd = int(i) * (16 ** (a1 - a))
                            a1 -= 1
                            if a1 == -1:
                                break
                            sum += sd
                        s = ''
                        while sum > 0:
                            t = sum // 8
                            s = str(sum % 8) + s
                            sum = t
                        print('Your octal number: ', s)
                    elif a == 4:
                        input_digit()
                    elif a == 5:
                        exit(0)
        elif '0' and 'c' in x:
            while True:
                print('Choose 1) 8 --> 10')
                print('Choose 2) 8 --> 16')
                print('Choose 3) 8 --> 2')
                print('Choose 4) To Enter another digit')
                print('Choose 5) To Exit')
                while True:
                    a = inputi('Input your choice: ')
                    if a == 1:
                        l = []
                        a = 1
                        sum = 0

                        for i in san:
                            l.append(i)
                        l.pop(0)
                        l.pop(0)
                        a1 = len(l)
                        for i in l:
                            sd = int(i) * (8 ** (a1 - a))
                            a1 -= 1
                            if a1 == -1:
                                break
                            sum += sd
                        print('Your decimal numbers is:', sum)
                        break
                    elif a == 2:
                        l = []
                        a = 1
                        sum = 0

                        for i in san:
                            l.append(i)
                        l.pop(0)
                        l.pop(0)
                        a1 = len(l)
                        for i in l:
                            sd = int(i) * (8 ** (a1 - a))
                            a1 -= 1
                            if a1 == -1:
                                break
                            sum += sd
                        lis = []
                        while True:
                            a = sum // 16
                            b = sum % 16
                            sum = a
                            if b == 10:
                                lis.append('A')
                            elif b == 11:
                                lis.append('B')
                            elif b == 12:
                                lis.append('C')
                            elif b == 13:
                                lis.append('D')
                            elif b == 14:
                                lis.append('E')
                            elif b == 15:
                                lis.append('F')
                            elif 0 <= b <= 9:
                                lis.append(str(b))
                                break
                            else:
                                break
                        lis.reverse()
                        if lis[0] == '0':
                            lis.pop(0)
                            list = "".join(lis)
                            print('Your hex number is: ', list)
                        else:
                            myStri = ''.join(lis)
                            print(myStri)
                        break
                    elif a == 3:
                        l = []
                        a = 1
                        sum = 0

                        for i in san:
                            l.append(i)
                        l.pop(0)
                        l.pop(0)
                        a1 = len(l)
                        for i in l:
                            sd = int(i) * (8 ** (a1 - a))
                            a1 -= 1
                            if a1 == -1:
                                break
                            sum += sd
                        s = ''
                        while sum > 0:
                            t = sum // 2
                            s = str(sum % 2) + s
                            sum = t
                        print('Your binary number: ', s)
                    elif a == 4:
                        input_digit()
        elif '0' and 'd' in x:
            while True:
                print('Choose 1) 10 --> 2')
                print('Choose 2) 10 --> 8')
                print('Choose 3) 10 --> 16')
                print('Choose 4) To Enter another digit')
                print('Choose 5) To Exit')
                while True:
                    a = inputi('Input your choice: ')
                    if a == 1:
                        l = []
                        a = 1
                        sum = 0
                        for i in san:
                            l.append(i)
                        l.pop(0)
                        l.pop(0)
                        myStri = ''.join(l)
                        lis = []
                        sum = int(myStri)
                        s = ''
                        while sum > 0:
                            t = sum // 2
                            s = str(sum % 2) + s
                            sum = t
                        print('Your binary number: ', s)
                    elif a == 2:
                        l = []
                        a = 1
                        sum = 0
                        for i in san:
                            l.append(i)
                        l.pop(0)
                        l.pop(0)
                        myStri = ''.join(l)
                        lis = []
                        sum = int(myStri)
                        s = ''
                        while sum > 0:
                            t = sum // 8
                            s = str(sum % 8) + s
                            sum = t
                        print('Your octal number: ', s)
                    elif a == 3:
                        l = []
                        a = 1
                        sum = 0
                        for i in san:
                            l.append(i)
                        l.pop(0)
                        l.pop(0)
                        myStri = ''.join(l)
                        lis = []
                        sum = int(myStri)
                        while True:
                            a = sum // 16
                            b = sum % 16
                            sum = a
                            if b == 10:
                                lis.append('A')
                            elif b == 11:
                                lis.append('B')
                            elif b == 12:
                                lis.append('C')
                            elif b == 13:
                                lis.append('D')
                            elif b == 14:
                                lis.append('E')
                            elif b == 15:
                                lis.append('F')
                            elif 0 <= b <= 9:
                                lis.append(str(b))
                                break
                            else:
                                break
                        lis.reverse()
                        if lis[0] == '0':
                            lis.pop(0)
                            listt = "".join(lis)
                            print('Your hex number is: ', listt)
                        else:
                            myStri = ''.join(lis)
                            print('Your hex number is', myStri)
                        break
                    elif a==4:
                        input_digit()
                    elif a==5:
                        exit(0)
        else:
            print("Wrong! Try again!")
            input_digit()


input_digit()
