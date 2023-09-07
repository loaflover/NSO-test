import requests

api_url = 'http://127.0.0.1:5000'
post_url = api_url + '/AddMessage'
get_url = api_url + '/GetMessage'
delete_url = api_url + '/DeleteMessage'


def test_1():
    
   
    requests.post(delete_url + "?messageId=test1")
    #delete ^


    dataCreate = {
    "application_id": "testAppID",
    "session_id": "TestSeshID",
    "message_id": "test1",
    "participants": ["tedd", "jared"],
    "content": "sssss"
    }
    requests.post(post_url, json=dataCreate)
    #post^


    
    response = requests.get(get_url + "?messageId=test1")
   
 
   
    assert len(response.json()) == 1

def test_2():
    # Ensure that a message with messageId "test1" is not present by attempting to delete it
    requests.post(delete_url + "?messageId=test2")
    
    # Create a new message with the specified data
    dataCreate = {
        "application_id": "testAppID",
        "session_id": "TestSeshID",
        "message_id": "test2",
        "participants": ["tedd"],
        "content": "sssss"
    }
    requests.post(post_url, json=dataCreate)
    
    # Attempt to create a second message with the same messageId
    dataCreate2 = {
        "application_id": "testAppID",
        "session_id": "TestSeshID",
        "message_id": "test2",  # Same messageId as the first message
        "participants": ["alice", "bob"],
        "content": "another message"
    }
    response = requests.post(post_url, json=dataCreate2)
    
    # Check if the response status code is not 200 (indicating failure due to non-unique messageId)
    assert response.status_code != 200

def test_3():
  
    requests.post(delete_url + "?messageId=test2")
    
    
    dataCreate = {
        "application_id": "testAppID",
        "session_id": "TestSeshID",
        "message_id": "test2",
        "participants": ["tedd", "jared"],
        "content": "sssss"
    }
    requests.post(post_url, json=dataCreate)
    
    
    dataCreate2 = {
        "application_id": "testAppID",
        "session_id": "TestSeshID",
        "message_id": "test3",  # Different messageId
        "participants": ["alice", "bob"],
        "content": "another message"
    }
    requests.post(post_url, json=dataCreate2)
    
    
    dataCreate3 = {
        "application_id": "testAppID",
        "session_id": "TestSeshID2",  # Different session_id
        "message_id": "test4",  # Different messageId
        "participants": ["carol", "dave"],
        "content": "yet another message"
    }
    requests.post(post_url, json=dataCreate3)
    
 
    response_get1 = requests.get(get_url + "?messageId=test2")
    response_get2 = requests.get(get_url + "?messageId=test3")
    

    
    
    response_delete1 = requests.post(delete_url + "?messageId=test2")
    response_delete2 = requests.post(delete_url + "?messageId=test3")
    
    # Check if the delete operations were successful
    assert response_get1.status_code == 200 and response_get2.status_code == 200 and response_delete1.status_code == 200 and response_delete2.status_code == 200