from flask import Flask, request, jsonify
from SQLHelper import *

app = Flask(__name__)




@app.route("/AddMessage", methods=["POST"])
def add_message():
    try:
        data = request.get_json()

        # Validate required fields in the JSON data
        required_fields = ["application_id", "session_id", "message_id", "participants", "content"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        
        if get_messages_by_message_ids(data["message_id"]):
            return jsonify({"error": f"message id already exists"}), 400
        result_message = InsertMessage(data["application_id"], data["session_id"], data["message_id"], data["content"])
        for participant in data["participants"]:
            result_participant = InsertPostsParticipants([participant], data["message_id"])

        return jsonify({"message": "Message added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/GetMessage", methods=['GET'])
def get_message():
        application_id = request.args.get("applicationId")
        session_id = request.args.get("sessionId")
        message_id = request.args.get("messageId")

        # Check which parameter is provided and query the database accordingly
        if application_id:
            messages = get_messages_by_application_id(application_id)
            return jsonify(messages)

        elif session_id:
            messages = get_messages_by_session_id(session_id)
            return jsonify(messages)

        elif message_id:
            messages = get_messages_by_message_ids(message_id)
            return jsonify(messages)
        return jsonify({"error": "Message not found"}), 404

@app.route("/DeleteMessage", methods=['POST'])
def delete_message():
    application_id = request.args.get("applicationId")
    session_id = request.args.get("sessionId")
    message_id = request.args.get("messageId")

    # Check which parameter is provided and delete messages from the database accordingly
    if application_id:
        success = delete_messages_by_application_id(application_id)
        return jsonify({"success": success})

    elif session_id:
        success = delete_messages_by_session_id(session_id)
        return jsonify({"success": success})

    elif message_id:
        success = delete_messages_by_message_id(message_id)
        return jsonify({"success": success})
    return jsonify({"error": "Message not found"}), 404

if __name__ == "__main__":
    app.run()
