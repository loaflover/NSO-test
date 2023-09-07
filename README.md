
# flask api app - nir flatau

flask api app, made by nir flatau as a test/first job interview for NSO.
this app contains 3 files and 1 folder (except of course for auto generated ones)

Main.py - main python script, includes the majority of the code. also includes all of the flask side of the project.

SQLHelper.py - the file containing all of the work with the sqlite database.

test_api.py (under automation folder) - all of the pytests testcases

# usage and explination
## all commands are done from the project root folder
to use this app, you first run the following command:
> flask --app Main.py run
this command initiates the flask server, running it on http://127.0.0.1:5000. the api has 3 commands built in, them being:

AddMessage (post) - accepts json input

GetMessage (get) - accepts query parameters

DeleteMessage (post) - accepts query parameters

to run these, connect with your favorite method (for example: curl, postman, requests (python) etc). choose the correct method (post or get), type the correct url (it being http://127.0.0.1:5000/[command you want to use]), type the correct inputs and send. if it returns 200 or 201 you have done everything successfully. here are 3 examples of valid requests, generated with the help of postman.

http://127.0.0.1:5000/GetMessage?messageId=tesst1 (get)
http://127.0.0.1:5000/DeleteMessage?messageId=test1 (post)
http://127.0.0.1:5000/AddMessage {
        "application_id": 2,
    "session_id": "aaaac",
    "message_id": "bbdsbbc",
    "participants": ["daniel beck", "moomoo"],
    "content": "Hi, how are you today?"
}

(post, curly brackets signifying json input)


to test the api with pytest, make sure the flask api is up and running, and execute the following command:
> pytest .\automation\test_api.py 
you should then see either success or failure, depending on if the test succeded or not (you will most likely get success as i have tested it on my machine with success)

# requirements

### for main flask app you will need the following python libraries:
flask, sqlite3

### for the pytest script you will also need:
requests, pytest