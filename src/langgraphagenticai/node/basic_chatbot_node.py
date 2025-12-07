from src.langgraphagenticai.state.state import State

class BasicChatBotNodesBuilder:
    """
    Basic chatbot logic implementation
    """
    
    def ___init__(self, model):
        self.llm=model
    
    def process(self, state:State)->dict:
        return {"message":self.llm.invoke(state["message"])}
    