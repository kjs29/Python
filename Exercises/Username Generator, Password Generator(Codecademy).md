# Tried on 6/18(o), 7/11(o)

You want to make a program that determines your username based on your first and last name.
You want to make a program that generates your password based on  your username.
If their first name is less than three letters and their last name is less than four letters it should use their entire names.


the username generator takes two input `firstname`, and `lastname`.

It takes first three letter in the first name, and first four letters in the lastname and puts it together.

The password generator takes the username and shift all letters to the right by one index position.

For example, if my username is `GeoKim` this password generator will turn it into `mGeoKi`


<details>
    <summary>answer</summary>
    
    ```py
    #make username generator

    def username_generator(firstname,lastname):

        #we will return this username at the end of the program
        username = ""

        if len(firstname) < 3 and len(lastname) < 4:
            username = firstname + lastname
            return username
        else:
          username = firstname[:3] + lastname[:4]
          return username


    #make password generator
    def password_generator(username):

        #we will return this password
        password = ""

        #we have to rearrange the password because we should shift all letters by one to the right.
        for a in range(0, len(username)):

            #every iteration in for loop, we will assign username[a-1] to password. 
            #originally username[0] will turn into username[-1], and this will be stored in a password variable.
            password = password + username[a-1]

    return password
    ```
    
</details>

<details>
    <summary>answer2</summary>
    
    ```py
    def username(first, last):
        if len(first) < 3 or len(last) < 4:
            return first+last
        else:
            return first[:3]+last[:4]
    
    def password(user):
        return user[-1:] + user[:-1]
    ```
</details>
