import sqlite3

conn = sqlite3.connect('ChatAppAPI.db')
c = conn.cursor()


c.execute(""" CREATE TABLE IF NOT EXISTS posts (
          application_id TEXT,
          session_id TEXT,
          message_id TEXT,
          content TEXT
          
          )
          """)

c.execute(""" CREATE TABLE IF NOT EXISTS PostsParticipants (
          ParticipantName TEXT,
          postID TEXT,
          FOREIGN KEY(postID) REFERENCES posts(message_id)
          )
          """)





conn.commit()
conn.close()
def InsertMessage(application_id, session_id, message_id, content):
    try:
        conn = sqlite3.connect('ChatAppAPI.db')
        c = conn.cursor()

        # Generate a unique UID for the message (you can use UUID or any other method)
        # For simplicity, we'll generate a random integer here
       

        # Insert the message into the 'posts' table
        c.execute("INSERT INTO posts (application_id, session_id, message_id, content) VALUES (?, ?, ?, ?)",
                  (application_id, session_id, message_id, content))





       





        conn.commit()
        conn.close()
        return True  # Success
    except Exception as e:
        return str(e)  # Return the error message if an exception occurs
def InsertPostsParticipants(participant_names, post_id):
    try:
        conn = sqlite3.connect('ChatAppAPI.db')
        c = conn.cursor()

        # Insert each participant name along with the post UID
        for participant_name in participant_names:
            c.execute("INSERT INTO PostsParticipants (ParticipantName, postID) VALUES (?, ?)",
                      (participant_name, post_id))







       



        conn.commit()
        conn.close()
        return True  # Success
    except Exception as e:
        return str(e)  # Return the error message if an exception occurs



def get_messages_by_application_id(application_id):
    try:
        conn = sqlite3.connect('ChatAppAPI.db')
        c = conn.cursor()

        
        c.execute("SELECT * FROM posts WHERE application_id = ?", (application_id,))
        messages = c.fetchall()

       
        messages_with_participants = []
        for message in messages:
            c.execute("SELECT ParticipantName FROM PostsParticipants WHERE postID = ?", (message[2],))
            participants = [participant[0] for participant in c.fetchall()]
            messages_with_participants.append({"message": message, "participants": participants})

        conn.close()
        return messages_with_participants
    except Exception as e:
        return str(e)
def get_messages_by_session_id(session_id):
    try:
        conn = sqlite3.connect('ChatAppAPI.db')
        c = conn.cursor()

        
        c.execute("SELECT * FROM posts WHERE session_id = ?", (session_id,))
        messages = c.fetchall()

        
        messages_with_participants = []
        for message in messages:
            c.execute("SELECT ParticipantName FROM PostsParticipants WHERE postID = ?", (message[2],))
            participants = [participant[0] for participant in c.fetchall()]
            messages_with_participants.append({"message": message, "participants": participants})

        conn.close()
        return messages_with_participants
    except Exception as e:
        return str(e)
def get_messages_by_message_ids(message_id):
    try:
        conn = sqlite3.connect('ChatAppAPI.db')
        c = conn.cursor()

        
        c.execute("SELECT * FROM posts WHERE message_id = ?", (message_id,))
        messages = c.fetchall()

        
        messages_with_participants = []
        for message in messages:
            c.execute("SELECT ParticipantName FROM PostsParticipants WHERE postID = ?", (message_id,))
            participants = [participant[0] for participant in c.fetchall()]
            messages_with_participants.append({"message": message, "participants": participants})

        conn.close()
        return messages_with_participants
    except Exception as e:
        return str(e)



def delete_messages_by_message_id(message_id):
    try:
        conn = sqlite3.connect('ChatAppAPI.db')
        c = conn.cursor()

        # Delete messages with the specified message_id from 'posts' table
        c.execute("DELETE FROM posts WHERE message_id = ?", (message_id,))
        
        # Delete associated participants from 'PostsParticipants' table
        c.execute("DELETE FROM PostsParticipants WHERE postID = ?", (message_id,))
        
        conn.commit()
        conn.close()
        return True  # Success
    except Exception as e:
        return str(e)
def delete_messages_by_session_id(session_id):
    try:
        conn = sqlite3.connect('ChatAppAPI.db')
        c = conn.cursor()

        # Delete messages with the specified session_id from 'posts' table
        c.execute("DELETE FROM posts WHERE session_id = ?", (session_id,))
        
        # Delete associated participants from 'PostsParticipants' table
        c.execute("DELETE FROM PostsParticipants WHERE postID IN (SELECT message_id FROM posts WHERE session_id = ?)", (session_id,))
        
        conn.commit()
        conn.close()
        return True  # Success
    except Exception as e:
        return str(e)
def delete_messages_by_application_id(application_id):
    try:
        conn = sqlite3.connect('ChatAppAPI.db')
        c = conn.cursor()

        # Delete messages with the specified application_id from 'posts' table
        c.execute("DELETE FROM posts WHERE application_id = ?", (application_id,))
        
        # Delete associated participants from 'PostsParticipants' table
        c.execute("DELETE FROM PostsParticipants WHERE postID IN (SELECT message_id FROM posts WHERE application_id = ?)", (application_id,))
        
        conn.commit()
        conn.close()
        return True  # Success
    except Exception as e:
        return str(e)
