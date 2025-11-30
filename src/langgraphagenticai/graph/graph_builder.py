from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State


class GraphBuilder:
    def __init__(self, model):
        self.llm=model
        self.graph_builder = StateGraph(State)


    def basic_chatbot_build_graph(self):
        """
            Builds a basic chatbot using LangGraph
            This method initiates a chatbot node using the 'BasicChatBotNode' class
            and integrates into a graph. The chatbot is set as both entry and exit point of the graph        
        """
        
        self.graph_builder.add_node("chatbot", "")
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        