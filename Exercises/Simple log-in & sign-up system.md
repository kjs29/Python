## Make a simple log-in and sign-up system for the website that shows like these cases

## Let users type their own username and password.

<em>Case 1</em>
```
Create your account
Input username : admin
Input password : admin1
User 'admin' has been created successfully
Log in now
Input username : admin
Input password : admin1
User logged in successfully
```
<em>Case 2</em>
```
Create your account
Input username : admin
Input password : admin1
User 'admin' has been created successfully
Log in now
Input username : admin
Input password : admin2
Invalid credentials
```

<details>
  <summary>Answer</summary>
  
  ```py
  while True:
      print("Create your account")
      username = input("Input username : ")
      password = input("Input password : ")
      print(f"User '{username}' has been created successfully")
      print("Log in now")
      user_input_username = input("Input username : ")
      user_input_password = input("Input password : ")
      if username == user_input_username and password == user_input_password:
          print("User logged in successfully")
          break
      else:
          print("Invalid credentials")
          break
  ```
</details>

    
