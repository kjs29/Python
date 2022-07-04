
"""
Project
Create a function called 'rotate' that takes two arguments called text, and key.

text is a string, for example, "abc"

key is an int, for example 5

basic english alphabets are like "abcdefghijklmnopqrstuvwxyz"

But in our project, because our key is 5, the last five digits are shifted back to the beginning of the alphabets. "vwxyzabcdefghijklmnopqrstu"

And because text is "abc", this function returns "fgh"

Make sure that text is case sensitive, spaces in text are counted, and so are symbols or punctuations.

"""


def rotate(text:str, key:int) -> str:
    
    plain = "abcdefghijklmnopqrstuvwxyz"
    
    shifted = plain[-key:] + plain[:len(plain)-key]
    print(f"shifted : {shifted}")
    

    #in case of text to be uppercase like "O M Geee", put the index number for the uppercase in the text into the cap_lst.
    #for example, when text = "O M Geee", then cap_lst = [0, 2, 4], because index for O is 0, M is 2, G is 4.
    cap_lst = []
    for a in range(len(text)):
        if text[a].isupper():
            cap_lst.append(a)
    print(f"this list holds the index for uppercase letter : {cap_lst}")


    #if text = "O M Geee", then text = "o m geee".
    text = text.lower()


    #if text = "o m geee", then text_lst = ['o', ' ', 'm', ' ', 'g', 'e', 'e', 'e'].
    text_lst = []
    for each in text:
        text_lst.append(each)
    print(f"text_lst : {text_lst}")

    
    #find index of the shifted for each element in text_lst, but space is copied, and anything else is also copied into index_lst.
    """
    for example, 
    
    when text_lst = ['o', ' ', 'm', ' ', 'g', 'e', 'e', 'e'], 
    
    when shifted = "vwxyzabcdefghijklmnopqrstu"

    index for 'o' in shifted is 19.
    
    index for 'm' in shifted is 17.

    index for 'g' in shifted is 11.

    index for 'e' in shifted is 9.
    """
    index_lst = []
    for each in text_lst:
        if each.isalpha():
            index_lst.append(shifted.find(each))
        elif each.isspace():
            index_lst.append(" ")
        
        #symbols, punctuations, digits
        else:
            index_lst.append(each)
    print(f"index list : {index_lst}")


    #using the index_lst and shifted, we will put them back into string, and put it in variable called 'result'
    result = ""
    for each in index_lst:
        if type(each)==int:
            result += plain[each]
        elif each.isspace():
            result += " "
        elif each.isdigit():
            result += each
        else:
            result += each
    print(f"result : {result}\nlength : {len(result)}")
    

    #for the element in a cap_lst, change it to uppercase
    answer = ""
    for i in range(len(text)):
        if i in cap_lst:
            print(f"this letter will be capital : {result[i]}")
            answer += result[i].upper()
        else:
            print(f"this letter is lowercase : {result[i]}")
            answer += result[i]
    print(f"\nanswer : {answer}\n")
    return answer
   
rotate("Hello from the other side", 13)
rotate("Uryyb sebz gur bgure fvqr", 13)
