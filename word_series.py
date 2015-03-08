def Character_to_number():
    """ This function converts a given (User Defined) Character to Number\
    as per the given Pattern (2*(Previous Character) + counter) """
    nb = input('please enter the character: ')
    nb = nb.upper()
    count = 1    
    sum = 0
    for s in range(65,ord(nb)+1):
        sum = sum*2+count
        count = count+1
    print ('The Value of ',chr(s),':',sum,' \n')

def String_to_number():
    """ This function converts a given (User Defined) String to Number\
    as per the given Pattern (2*(Previous Character) + counter)\
    This function calculates the individual value of the letters of the String\
    and then gives us the Sum of all the letters, which is the Numeric Value of the String. """
    alpha = input('Please enter a word: ')
    alpha = alpha.upper()
    final_sum = 0
    for s in alpha:
        count = 1        
        sum = 0
        for i in  range(65,ord(s)+1):
            sum = sum*2 + count
            count = count+1
        print('for',s,'value is',sum)    
        final_sum = final_sum+sum
    print('The sum of given words is: ', final_sum,' \n')
        
def Digit_to_string():
    """This function Converts a given Number into String :/
    with character value calculated as per the given pattern (2*(Previous Character) + counter) """
    numb = int(input('Enter the number: '))
    temp = numb
    while (temp >= 1):
            sum = 0
            i = 1
            prev_char = ''
            prev = 0
            l=0
            while (temp >= sum):
                prev = sum
                if (prev == 0):
                    prev_char = ''
                elif(prev ==1):
                    prev_char= 'A'
                else:
                    l= i-2
                    prev_char = chr(ord('A') + l)
                sum = sum *2 + i
                i=i+1
            if (temp==numb):
                word = prev_char
            else:
               word = word + prev_char
            temp = temp -prev
    print('The Word is: ',word, ' \n') 

 
if __name__=='__main__':
    Character_to_number()
    String_to_number()
    Digit_to_string()
    
