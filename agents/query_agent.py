# agents/query_agent.py

from langchain.chains import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from utils.vector_utils import create_vectorstore

class QueryAgent:
    def __init__(self, transcript_text):
        self.vectorstore = create_vectorstore(transcript_text)
        self.llm = ChatOpenAI(temperature=0)
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self.chat_log = []  # Stores user questions in sequence

        self.chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.vectorstore.as_retriever(),
            memory=self.memory
        )

    def ask(self, question):
        self.chat_log.append(question)

        # Special handling for memory-related questions
        if "first question" in question.lower():
            return self.get_first_question()
        elif "do you remember" in question.lower():
            return "Yes, I remember everything from this session."

        response = self.chain.run(question)
        return response

    def get_first_question(self):
        return self.chat_log[0] if self.chat_log else "I don't remember your first question."