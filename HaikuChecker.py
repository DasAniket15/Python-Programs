def is_haiku (sample_string):
    """
    Accepts an input string and checks if it is a Haiku or not and returns True or False boolean value
    """
    
    #Storing list of lines of haiku
    lines_list = sample_string.split("/")
    
    #Checking if there are 3 lines in the list of haiku
    if (len(lines_list) == 3):
        
        #Storing values of where all commas are
        line_1 = lines_list[0].split(',')
        line_2 = lines_list[1].split(',')
        line_3 = lines_list[2].split(',')
        
        #Checks if haiku has the correct amount of syllables in each line or not
        if (len(line_1) == 5 and len(line_2) == 7 and len(line_3) == 5):
            return True
        
        elif (len(line_1) == 5 and len(line_2) == 7 and len(line_3) != 5):
            print ("WARNING: The third line is not 5 syllables long.")
            return False
        
        elif(len(line_1) == 5 and len(line_2) != 7 and len(line_3) == 5):
            print ("WARNING: The second line is not 7 syllables long.")
            return False
        
        elif(len(line_1) == 5 and len(line_2) == 7 and len(line_3) == 5):
            print ("WARNING: The first line is not 5 syllables long.")
            return False

        else:
            print ("WARNING: This is not a haiku.")
            return False
    
    else:
        print ("WARNING: This does not have 3 lines.")
        return False


def haiku_string_parser(input_string):
    """
    Checks if haiku is based on its structure, and if it is then return reformatted easy-to-read string 
    """
    
    #Checks if haiku is correct or not
    haiku_check = is_haiku(input_string)

    if (haiku_check == False):
        return ""

    else:
        #Formats input string into easy-to-read strings
        formatted_string = input_string.replace(",", "")
        replaced_string = formatted_string.replace("/", "\n")

        return "".join(replaced_string)


def main():
    """#Running first function for a haiku that is correct
    haiku_string = "clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon "

    check_haiku = is_haiku(haiku_string)
    print (check_haiku)

    print ("\n")

    #Running program for a haiku that is incorrect
    haiku_string = "clouds , mur,mur ,dark,ly/it ,is ,a ,blin,ding, ha,bit/ga,zing"
    
    check_haiku = is_haiku(haiku_string)
    print (check_haiku)

    print ("\n")
    """
    
    #Running second function for a haiku that is correct
    haiku_string = "clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon "

    formatted_haiku = haiku_string_parser(haiku_string)
    print (formatted_haiku)

    print ("\n")

    #Running second function for a haiku that is incorrect
    haiku_string = "clouds , mur,mur ,dark,ly/it ,is ,a ,blin,ding, ha,bit/ga,zing"

    formatted_haiku = haiku_string_parser(haiku_string)
    print (formatted_haiku)


main()