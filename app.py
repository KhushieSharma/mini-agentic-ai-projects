from agenticchatbot import chatbot
from langchain_core.messages import BaseMessage,HumanMessage
import streamlit as st
st.title("agentic chatbot with langgraph")

config={'configurable':{'thread_id':'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

#load conv history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input=st.chat_input("type here")
st.write('user:', user_input)

if user_input:
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)
    # response=chatbot.invoke({'message':[HumanMessage(content=user_input)]},config=config)
    # ai_message=response['message'][-1].content
    # st.session_state['message_history'].append({'role':'assistant','content':ai_message})
    # with st.chat_message('assistant'):
    #     st.text(ai_message)  stream chaiye
    #msg history
    with st.chat_message('assistant'):
        ai_message=st.write_stream(
            message_chunk.content 
            for message_chunk,metadata in chatbot.stream(
                {'message':[HumanMessage(content=user_input)]},
                config=config,
                stream_mode='messages'
            )
        )
    st.session_state['message_history'].append({'role':'assistant','content':ai_message})


