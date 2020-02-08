from gfxhat import lcd, backlight

try:
    fontsTxt = open('font3.txt', 'r')

    # This function creates a dictionary with characters as keys and its respective matrix list representation as value.
    def generateDictionary (txtFile):
        fonts = dict()
        for line in txtFile:
            row = line.split(",")
            character = row[1][:-1]
            codeNumber = row[0][2:]
            matrixList = [list(bin(int('0x'+(codeNumber[i:i+2]),16))[2:].zfill(8)) for i in range(0, len(codeNumber), 2)] 
            fonts[character] = matrixList
        return fonts

    # This function displays an object on the GFX HAT from a matrix list.
    def displayObject(obj, startX=0, startY=0):
        if(startY + len(obj) > 63):
            startY = 64 - len(obj)
        if(startX + len(obj[0]) > 127):
            startX = 128 - len(obj[0])

        for y in range(0,len(obj)):
            for x in range(0,len(obj[y])):
                lcd.set_pixel(x+startX,y+startY,int(obj[y][x]))
        lcd.show()

    fonts = generateDictionary(fontsTxt)

    # This function asks the user which character to display and where to display it on the GFX HAT.
    def menu():
        backlight.set_all(255,255,255)
        backlight.show()
        choice = input("Enter number:    1. Draw character   2. Exit   >>> ")
        if (choice == "1"):
            characterChoice = input("Which character do you want to print? > ")
            if characterChoice in fonts.keys():
                x = int(input("Inform start position in axis X  >>> "))
                y = int(input("Inform start position in axis Y  >>> "))
                displayObject(fonts[characterChoice],x,y)
                input("Press enter to erase and go back.")
                lcd.clear()
                lcd.show()
                menu()
            else:
                print("Character not in list.")
                menu()
        if (choice == "2"):
            lcd.clear()
            backlight.set_all(0,0,0)
            lcd.show()
            backlight.show()
            print("Goodbye!")
        else:
            print("Invalid choice.")
            menu()

    menu()

except:
    print("File .txt wasn't found. Check the source of the file on line 4.")  


