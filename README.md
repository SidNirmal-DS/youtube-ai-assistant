# Contextual AI Agent: Your Smart YouTube Video Assistant

Welcome to the **Contextual AI Agent** — a web application designed to revolutionize how you interact with YouTube video content. No more scrubbing through long videos to find specific information or manually summarizing lengthy discussions. With this tool, simply provide a YouTube URL, and our AI agent will do the heavy lifting for you.

---

## 🚀 Project Overview

The Contextual AI Agent is a powerful and intuitive web application that allows you to extract insights from YouTube videos. It leverages advanced Artificial Intelligence models to:

- Fetch full video transcripts
- Generate concise summaries
- Answer natural language questions about the content

Built with **Flask** for the backend and a modern **HTML/CSS/JS** frontend, this project provides a seamless, intelligent user experience.

---

## 🔑 Key Features

- **YouTube Transcript Extraction**: Fetch and display transcripts of any public YouTube video.
- **Intelligent Video Summarization**: Generate brief, meaningful summaries of video content.
- **Natural Language Q&A**: Ask questions about the video in plain English and receive smart answers.
- **Conversational Memory**: Multi-turn conversations with context memory within your session.
- **Responsive UI**: Mobile-friendly interface with smooth interactions.
- **Dark Mode Support**: Toggle between light and dark themes.
- **Shimmer Loading Effects**: Visual cues during processing for enhanced UX.

---

## 🛠 Tech Stack

### Backend
- **Flask**: Handles routing and server logic.
- **LangChain**: Orchestrates AI agent behavior and memory.
- **OpenAI Chat Model**: Powers summaries and Q&A generation.
- **ConversationBufferMemory**: Maintains session context during interactions.
- **youtube-transcript-api**: Retrieves transcripts programmatically.
- **Vector Stores** (FAISS, ChromaDB - conceptual): For semantic search and question matching.

### Frontend
- **HTML5**: Web structure.
- **Tailwind CSS**: For responsive, clean UI with built-in dark mode support.
- **Vanilla JavaScript**: For API communication and UI logic.
- **Font Awesome**: Iconography.

---

## ⚙️ How It Works

1. **User Input**: Paste a YouTube URL and click **Extract Transcript**.
2. **Transcript Fetching**:
   - Frontend sends a request to Flask.
   - Flask retrieves the transcript using `youtube-transcript-api`.
   - Transcript is returned and displayed.
3. **Vectorization**:
   - Transcript is converted into vector format on the backend.
4. **Summary Generation**:
   - Click "Summarize Transcript".
   - Transcript is sent to OpenAI via LangChain for summarization.
   - Result is returned and shown on the UI.
5. **Conversational Q&A**:
   - Type a question about the video.
   - LangChain agent processes it using context and vector store.
   - Answer is returned and displayed in chat-like format.

---

## 💻 How to Run Locally

### Clone the Repository
```bash
git clone https://github.com/your-username/contextual-ai-agent.git
cd contextual-ai-agent


### Set Up a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # For Windows: .venv\Scripts\activate

### Install Requirements
```bash
pip install -r requirements.txt

### Add OpenAI Key in .env File
OPENAI_API_KEY=your_api_key_here

### Run the Flask App
```bash
flask run

### Open in Browser

🔮 Future Enhancements
	•	Advanced AI Models: Switch to Llama, Mistral, or Mixtral for better flexibility.
	•	Long Video Support: Use chunking and dynamic memory strategies.
	•	Multilingual Support: Process non-English videos.
	•	Embedded Video Player: Play and highlight transcript sections inline.
	•	User Accounts: Save summaries and chats across sessions.
	•	Usage Monitoring: Track token usage and API costs.
	•	Public Deployment: Host using GCP, Azure, or AWS.
	•	Enhanced Feedback Handling: Improved UX for errors, loading, and feedback.
	•	Smarter Memory Management: Persistent memory using vector DBs or external store.

⸻

🧠 Sample Use Cases
	•	Students: Summarize lectures, ask clarification questions.
	•	Content Creators: Analyze competitor videos, ideate from popular content.
	•	Researchers: Extract insights from long talks without full viewing.
	•	Journalists: Review interviews or briefings and extract quotes or facts.
	•	L&D Teams: Generate summaries and quizzes from internal training videos.
	•	Busy Professionals: Get video highlights in seconds.

⸻

🤝 Contributing

We welcome ideas, improvements, and feedback. Fork the repo, raise issues, or submit pull requests.

