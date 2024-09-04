def main():
    total_length = 0
    for x in range(1,1001):
        # Convert to string for easy manipulation
        x = str(x)
        # Calculate the length of the string
        length = len(x)
        # Provide the length of the single digit string
        string_length = single(x[-1])
        # If the string contains mulitple digits
        if length > 1:
            # And if the second digit is equal to 1
            if x[-2] == "1":
                # Replace string length with teens version
                string_length = teens(x[-2:])
            # Otherwise, append the length of the tens place
            else:
                string_length += tens(x[-2])
        # If we are in the hundreds, and the hundreds value is not zero
        if length > 2 and x[-3] != "0":
            # Append the hundreds digit length, and the length of "hundred"
            string_length += (single(x[-3]) + 7)
            # If the lower digits are not zero
            if x[-2] != "0" or x[-1] != "0":
                # Add 3 to string length (for "and")
                string_length += 3
        # If lengh is greater than three
        if length > 3:
            # Add the thousands digit length, and the length of "hundred"
            string_length += (single(x[-4]) + 8)

        # We do not currently have something to consider 
        # how to deal with the "and" case.
        #  It was not required for the program, 
        # but it might be difficult 


        total_length += string_length
    print(total_length)


def single(x):
    match x:
        case "0":
            return 0
        case "1" | "2" | "6":
            return 3
        case "3" | "8" | "7":
            return 5
        case "4" | "5" | "9":
            return 4


def teens(x):
    match x:
        case "10":
            return 3
        case "11" | "12":
            return 6
        case "13" | "14" | "18" | "19":
            return 8
        case "15" | "16":
            return 7
        case "17":
            return 9


def tens(x):
    match x:
        case "0":
            return 0
        case "2" | "3" | "8"| "9":
            return 6
        case "4" | "5" | "6":
            return 5
        case "7":
            return 7


if __name__ == "__main__":
    main()

