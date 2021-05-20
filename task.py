def convert_dec_to_bin(number):
    # CITATION: See Brennan, Works Cited at end
    binaryString = ""

    result = number

    if number == 0:
        # If it's zero, we're done.
        binaryString = "0"
    elif number > 0:
        while result != 0:
            # CITATION: See Agrawal (Division Operators...), Works Cited at end
            newResult = result // 2
            remainder = result % 2
            result = newResult
            stringRemainder = ""

            if remainder == 0:
                stringRemainder = "0"
            else:
                stringRemainder = "1"

            # CITATION: See Byers, Works Cited at end
            binaryString = stringRemainder + binaryString

        # CITATION: See Wikipedia Contributors, Works Cited at end
        # Pad the nybble if needed
        while len(binaryString) % 4 != 0:
            binaryString = "0" + binaryString

    elif number < 0:

        # Get the positive version
        positiveNumber = 0 - number
        result = positiveNumber

        # Do the same calcs as above for the positive version
        while result != 0:
            # CITATION: See Agrawal (Division Operators...), Works Cited at end
            newResult = result // 2
            remainder = result % 2
            result = newResult
            stringRemainder = ""

            if remainder == 0:
                stringRemainder = "0"
            else:
                stringRemainder = "1"

            # CITATION: See Byers, Works Cited at end
            binaryString = stringRemainder + binaryString

        # CITATION: See Wikipedia Contributors, Works Cited at end
        # Pad the nybble if needed
        while len(binaryString) % 4 != 0:
            binaryString = "0" + binaryString

        # CITATION: See RapidTables.com Contributors, Works Cited at end
        # Now we just need to prepend the negative sign
        binaryString = "-" + binaryString

    return binaryString


def convert_bin_to_hex(number):
    # CITATION: See Brennan, RapidTables Contributors, Thakur,
    # Works Cited at end

    # CITATION: See Kumar, Mishra (Gullu), Works Cited at end
    bitDictionary = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
    }

    bitString = ""

    result = number

    if number == "0":
        return "00"

    if number[0] != "-":

        firstNybble = True

        while len(result) > 0:
            curNybble = result[len(result) - 4:(len(result) + 1)]

            # CITATION: See Wikipedia Contributors, Byers,
            # Mishra (Gullu) Works Cited
            hexadecimalDigit = bitDictionary.get(curNybble)

            # Slice this nybble off the result
            result = result[0:len(result) - 4]

            # CITATION: See PyCharm Contributors, Works Cited at end
            if firstNybble:
                firstNybble = False
                bitString = hexadecimalDigit + bitString
            elif not firstNybble and len(result) > 0:
                firstNybble = True
                bitString = " " + hexadecimalDigit + bitString
            else:
                bitString = hexadecimalDigit + bitString

            if len(result) == 0 and (len(bitString) % 3) - 2 != 0:
                # theNumber = len(bitString) % 3 - 2
                # We're at the last byte and need to pad
                bitString = "0" + bitString

    else:
        bitString = convert_bin_to_hex_negative(result)

    return bitString


def convert_bin_to_hex_negative(result):
    # CITATION: See Kumar, Mishra (Gullu), Works Cited at end
    bitDictionary = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
    }

    bitString = ""

    firstNybble = True
    # Slice off the negative sign
    result = result[1:len(result) + 1]

    while len(result) > 0:
        curNybble = result[len(result) - 4:(len(result) + 1)]

        # CITATION: See Wikipedia Contributors, Byers,
        # Mishra (Gullu) Works Cited
        hexadecimalDigit = bitDictionary.get(curNybble)

        # Slice this nybble off the result
        result = result[0:len(result) - 4]

        # CITATION: See PyCharm Contributors, Works Cited at end
        if firstNybble:
            firstNybble = False
            bitString = hexadecimalDigit + bitString
        elif not firstNybble and len(result) > 0:
            firstNybble = True
            bitString = " " + hexadecimalDigit + bitString
        else:
            bitString = hexadecimalDigit + bitString

        if len(result) == 0 and (len(bitString) % 3) - 2 != 0:
            # theNumber = len(bitString) % 3 - 2
            # We're at the last byte and need to pad
            bitString = "0" + bitString

    # Just need to prepend the negative sign now
    bitString = "-" + bitString

    return bitString


def conv_endian(num, endian="big"):

    num = convert_bin_to_hex(convert_dec_to_bin(num))

    # If it's big, we're done
    if endian == "big":
        return num
    elif endian == "little":
        result = num
        bitString = ""

        if result[0] != "-":

            while len(result) > 0:
                curNybble = result[0:2]
                bitString = curNybble + bitString
                result = result[3:len(result) + 1]

                if len(result) != 0:
                    bitString = " " + bitString
        else:
            # Slice off the negative sign
            result = result[1:len(result) + 1]

            while len(result) > 0:
                curNybble = result[0:2]
                bitString = curNybble + bitString
                result = result[3:len(result) + 1]

                if len(result) != 0:
                    bitString = " " + bitString

            # Just need to prepend the negative sign now
            bitString = "-" + bitString

        return bitString
    else:
        # CITATION: See OSU Course Contributors, Works Cited at end
        # Some invalid endianness was passed
        return None


def main():
    print(conv_endian(954786, "little"))
    # breakme = 1


# CITATION: See Shah, Works Cited at end
if __name__ == "__main__":
    main()

"""
WORKS CITED

Agrawal, Arpit. "Division Operators in Python." GeeksForGeeks,
https://www.geeksforgeeks.org/division-operator-in-python/.

Brennan, Eugene. "How to Convert Hex to Binary and Binary to Hexadecimal."
 Owlcation.com, https://owlcation.com/stem/
 How-to-Convert-Hex-to-Binary-and-Binary-to-Hexadecimal.

Brennan, Eugene. "How to Convert Decimal to Binary and Binary to Decimal."
 Owlcation.com, https://owlcation.com/stem/
 How-to-Convert-Decimal-to-Binary-and-Binary-to-Decimal.

Byers, Mark <StackOverflow username>. "inserting characters at the start
 and end of a string." StackOverflow,
 https://stackoverflow.com/questions/10059554/
 inserting-characters-at-the-start-and-end-of-a-string.

Mishra (Gullu), Shashank. "Switch Case in Python (Replacement)."
 GeeksForGeeks.com,
 https://www.geeksforgeeks.org/switch-case-in-python-replacement/.

Kumar, Prashant <StackOverflow username>. "What is the Python equivalent
 for a case/switch statement? [duplicate]." StackOverflow.com,
 https://stackoverflow.com/questions/11479816/
 what-is-the-python-equivalent-for-a-case-switch-statement.

OSU Course Contributors. "Group Project: Part 2." Canvas,
 https://oregonstate.instructure.com/courses/1810943/
 assignments/8334612?module_item_id=20728375.

PyCharm Contributors. "Show quick fixes." PyCharm Software Feature,
https://www.jetbrains.com/pycharm/.

RapidTables.com Contributors. "Decimal to Binary converter."
 RapidTables.com,
 https://www.rapidtables.com/convert/number/decimal-to-binary.html.

RapidTables.com Contributors. "How to convert binary to hex."
 Rapidtables.com,
 https://www.rapidtables.com/convert/number/how-binary-to-hex.html.

Shah, Nirmi. "What does the if __name__ == “__main__”: do?"
 GeeksForGeeks.com,
 https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/.

Thakur, Arjun. "How to Convert Binary to Hexadecimal?" TutorialsPoint.com,
https://www.tutorialspoint.com/how-to-convert-binary-to-hexadecimal.

Wikipedia Contributors. "Nibble." En.Wikipedia.org,
https://en.wikipedia.org/wiki/Nibble.

Wikipedia Contributors. "Hexadecimal." Simple.Wikipedia.org,
https://simple.wikipedia.org/wiki/Hexadecimal

"""
