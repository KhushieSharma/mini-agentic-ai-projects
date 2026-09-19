from langgraph.graph import StateGraph,START,END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver
load_dotenv()
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)
from langgraph.graph.message import add_messages
class chatst(TypedDict):
    message:Annotated[list[BaseMessage],add_messages]

def chatnode(state:chatst):
    message=state['message']
    response=llm.invoke(message)
    return {'message':[response]}

checkpoint=MemorySaver()
graph=StateGraph(chatst)

graph.add_node('chatnode',chatnode)
graph.add_edge(START,'chatnode')
graph.add_edge('chatnode',END)

chatbot=graph.compile(checkpointer=checkpoint)