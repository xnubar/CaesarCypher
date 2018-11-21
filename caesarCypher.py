from tools import encode as encrypt, decode as decrypt, validation, fileoperations as file



while True:
    option = input('\n\ne - encode\nd - decode\nq - quit\nMake a choice: ')
    if option.lower()=='q':
        exit()
    elif option.lower()=='e' or option.lower()=='d':
        while True:
            shift_Value = input('The value of the shift: ')
            if validation.shift_isvalid(shift_Value):
                if option.lower() == 'e':
                    inputted_text = input('Text:  ')
                    file.save_to_file(encrypt.encode(int(shift_Value), inputted_text))
                elif option.lower() == 'd':
                    print('\nDecrypted text: ', decrypt.decode(int(shift_Value), file.read_from_file()))
            else:
               print('Shift value is invalid, you will be directed to the menu try again.')
            break
    else:
        print('Option is invalid!')









