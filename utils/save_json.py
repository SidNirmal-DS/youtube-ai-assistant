import json
import os

def save_to_json(user_input, bot_response, filename="qna.json"):
    qna_pair = {"question": user_input, "answer": bot_response}

    # Check if file exists and load existing content
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
    else:
        data = []

    # Append new Q&A and save back
    data.append(qna_pair)

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)