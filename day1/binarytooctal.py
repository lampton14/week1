def BinaryToOctal(number):
    unit = input("does you number have a decimal? ")
    if unit == "yes":
        [num_bef_dec, num_aft_dec] = number.split(".")
    if unit == "no":
        num_bef_dec = number
        num_aft_dec = ""
    output = ""

    if len(num_bef_dec) % 3 == 1:
        num_bef_dec = "00" + num_bef_dec
    if len(num_bef_dec) % 3 == 2:
        num_bef_dec = "0" + num_bef_dec

    for index in range(0, len(num_bef_dec), 3):
        cur_group = num_bef_dec[index: index+3]

        if cur_group == "000":
            output = output + "0"
        elif cur_group == "001":
            output = output + "1"
        elif cur_group == "010":
            output = output + "2"
        elif cur_group == "011":
            output = output + "3"
        elif cur_group == "100":
            output = output + "4"
        elif cur_group == "101":
            output = output + "5"
        elif cur_group == "110":
            output = output + "6"
        elif cur_group == "111":
            output = output + "7"

    if len(num_aft_dec) % 3 == 1:
        num_aft_dec = "00" + num_aft_dec
    if len(num_aft_dec) % 3 == 2:
        num_aft_dec = "0" + num_aft_dec
    output+= "."
    for index in range(0, len(num_aft_dec), 3):
        cur_group = num_aft_dec[index: index+3]

        if cur_group == "000":
            output = output + "0"
        elif cur_group == "001":
            output = output + "1"
        elif cur_group == "010":
            output = output + "2"
        elif cur_group == "011":
            output = output + "3"
        elif cur_group == "100":
            output = output + "4"
        elif cur_group == "101":
            output = output + "5"
        elif cur_group == "110":
            output = output + "6"
        elif cur_group == "111":
            output = output + "7"
    print(output)
number = input("please enter your binary number: ")
BinaryToOctal(number)
