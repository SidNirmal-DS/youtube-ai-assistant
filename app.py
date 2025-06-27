from flask import Flask, render_template, request, jsonify
from agents.transcript_agent import TranscriptAgent
from agents.summary_agent import SummaryAgent
from agents.query_agent import QueryAgent

app = Flask(__name__)

# Simple in-memory store (valid until app restart)
agent_memory_store = {}

@app.route("/transcript", methods=["POST"])
def get_transcript():
    data = request.get_json()
    url = data.get("url")
    transcript_agent = TranscriptAgent(url)
    transcript = transcript_agent.transcribe()
    return jsonify({"transcript": transcript})

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    transcript = data.get("transcript", "")
    summary_agent = SummaryAgent(transcript)
    summary = summary_agent.summarize()
    return jsonify({"summary": summary})

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.get_json()
    question = data.get("question")
    transcript = data.get("transcript")

    # Use first 100 chars of transcript to avoid full-text key bloat
    session_key = transcript[:100]

    if session_key not in agent_memory_store:
        agent_memory_store[session_key] = QueryAgent(transcript)

    query_agent = agent_memory_store[session_key]
    answer = query_agent.ask(question)
    return jsonify({"answer": answer})

@app.route("/")
def index():
    return render_template("index.html")