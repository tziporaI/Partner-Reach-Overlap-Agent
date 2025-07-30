from a2a.server.events.event_queue import EventQueue
from a2a.utils import new_agent_text_message
from a2a.server.agent_execution import AgentExecutor, RequestContext
from pydantic import BaseModel
from google.adk.agents.remote_agent import RemoteA2aAgent
from a2a.types import AgentCapabilities, AgentCard
import httpx
import asyncio

class AnalizingAgent(BaseModel):
    """analize agent that calc and return the analizing"""

    async def invoke(self)-> str:
        return "asdfghj"
    
class AnalizeAgentExecutor(AgentExecutor):
    def __init__(self):
        # מייצרים AgentCard ידנית (במקום להביא אותו עם A2aCardResolver)
        hello_agent_card = AgentCard(
            name="HelloWorldAgent",
            description="Responds with hello.",
            url="http://localhost:8002",
            version="1.0.0",
            defaultInputModes=["text"],
            defaultOutputModes=["text"],
            capabilities=AgentCapabilities(streaming=True),
            skills=[]  # אפשר להשאיר ריק אם לא דרוש
        )

        self.remote_agent = RemoteA2aAgent(
            name="hello_agent",
            agent_card=hello_agent_card
        )

    async def execute(self, context: RequestContext, event_queue: EventQueue):
        result = await self.remote_agent.execute("שלום")
        event_queue.enqueue_event(new_agent_text_message(result.message.text))

    async def cancel(self, context: RequestContext, event_queue: EventQueue):
        raise Exception("cancel not supported")