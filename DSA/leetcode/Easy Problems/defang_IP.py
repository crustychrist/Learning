        address = ("1.0.1.0.1")
        # convert string into list of char
        char_list = list(address)

        # replacing '.' with desired output
        for x in range(0,len(char_list)):
            if char_list[x] =='.':
                char_list[x] = '[.]'

        # reconvert Char to string 
        result = ''.join(char_list)
        print(result)