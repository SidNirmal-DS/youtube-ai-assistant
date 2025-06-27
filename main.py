from agents.transcript_agent import TranscriptAgent
from agents.summary_agent import SummaryAgent
from agents.query_agent import QueryAgent
from langchain_openai import OpenAIEmbeddings
from utils.save_json import save_to_json

if __name__ == "__main__":
    video_url = input("Enter YouTube URL: ")
    
    # Transcript
    agent = TranscriptAgent(video_url)
    transcript = agent.transcribe()  # ✅ Updated method name here
    print("\n—— Transcript (first 1000 chars) ——\n")
    print(transcript[:1000])

    # Summary
    summary_agent = SummaryAgent(transcript)
    summary = summary_agent.summarize()
    print("\n—— Summary ——\n")
    print(summary)

    # Query Agent
    query_agent = QueryAgent(transcript)

    print("\n—— Ask anything about this video ——\n")
    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit", "q"]:
            print("Exiting chat.")
            break
        answer = query_agent.ask(question)
        print("Bot:", answer)
        save_to_json(question, answer)
        