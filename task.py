def convert_dec_to_bin(number):
    # CITATION: See Brennan, Works Cited at end
    binaryString = ""

    result = number

    if number == 0:
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

        # CITATION: See RapidTables.com Contributors, Works Cited at end
        # Now we just need to prepend the negative sign
        binaryString = "-" + binaryString

    return binaryString


def main():
    print(convert_dec_to_bin(-29))
    breakme = 1


# CITATION: See Shah, Works Cited at end
if __name__ == "__main__":
    main()

"""
WORKS CITED

Agrawal, Arpit. "Division Operators in Python." GeeksForGeeks,
https://www.geeksforgeeks.org/division-operator-in-python/.

Brennan, Eugene. "How to Convert Decimal to Binary and Binary to Decimal."
 Owlcation.com, https://owlcation.com/stem/
 How-to-Convert-Decimal-to-Binary-and-Binary-to-Decimal.

Byers, Mark <StackOverflow username>. "inserting characters at the start
 and end of a string." StackOverflow,
 https://stackoverflow.com/questions/10059554/
 inserting-characters-at-the-start-and-end-of-a-string.

RapidTables.com Contributors. "Decimal to Binary converter." 
 RapidTables.com,
 https://www.rapidtables.com/convert/number/decimal-to-binary.html.

Shah, Nirmi. "What does the if __name__ == “__main__”: do?" GeeksForGeeks,
 https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/.

"""
