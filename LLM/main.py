from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv, find_dotenv
from langchain_huggingface import HuggingFaceEndpoint

load_dotenv(find_dotenv())
app = Flask(__name__)

# In-memory storage for chat messages
messages = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json

    repo_id = "deepseek-ai/DeepSeek-R1"
    task = "text-generation"

    llm = HuggingFaceEndpoint(repo_id=repo_id, task=task, temperature=0.9, model_kwargs={"max_length": 200})
    
    print(data['message'])
    response = llm.invoke(data['message'])
    print(f"\n\n\n\n{response}")
    
    message = data.get('message')
    if message:
        messages.append(message + "\n\n\n\n" + response)
        return jsonify({'status': 'success', 'message': message})
    return jsonify({'status': 'error', 'message': 'No message provided'})

@app.route('/messages')
def get_messages():
    # Return all messages as JSON
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")