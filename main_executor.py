# main_executor.py

from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCard, AgentCapabilities, AgentSkill
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.apps import A2AStarletteApplication
from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message
from google.adk.agents.remote_agent import RemoteA2aAgent

from a2a.types import AgentCard as A2ACard  # כדי שלא ידרוך על הקארד הראשי
import uvicorn
import uuid
import asyncio

# --------------------------
# Agent Executor (Main Logic)
# --------------------------

class MainExecutor(AgentExecutor):
    def __init__(self):
        # נגדיר את HelloWorldAgent
        hello_card = A2ACard(
            name="HelloWorldAgent",
            description="Says hello.",
            url="http://localhost:8002",
            version="1.0.0",
            defaultInputModes=["text"],
            defaultOutputModes=["text"],
            capabilities=AgentCapabilities(streaming=True),
            skills=[]
        )
        self.hello_agent = RemoteA2aAgent(agent_card=hello_card)

    async def execute(self, context: RequestContext, event_queue: EventQueue):
        try:
            await event_queue.enqueue_event(new_agent_text_message("🔄 מתחיל חישוב חפיפה..."))

        # קריאה לסוכן HelloWorld
            result = await self.hello_agent.execute("האם אתה חי?")
            print("📦 result:", result)

            if hasattr(result.root, "result"):
                text = result.root.result.parts[0].root.text
            else:
                text = "❌ לא נמצא שדה result"

            print(f"📡 תגובת Hello Agent: {text}")
            await event_queue.enqueue_event(new_agent_text_message(f"📡 תגובת Hello Agent: {text}"))

        except Exception as e:
            print("❌ שגיאה כללית ב־execute():", e)
            await event_queue.enqueue_event(new_agent_text_message(f"❌ שגיאה: {e}"))

    async def cancel(self, context: RequestContext, event_queue: EventQueue):
        raise NotImplementedError("Cancel not supported")

# --------------------------
# AgentCard ו־Skill
# --------------------------

reach_skill = AgentSkill(
    id="reach_overlap_analysis",
    name="Reach Overlap Analyzer",
    description="Analyzes reach and overlap between media sources.",
    tags=["media", "reach", "overlap"],
    examples=["Analyze reach overlap between Facebook and Google Ads"]
)

agent_card = AgentCard(
    name="ReachOverlapAgent",
    description="Main agent for analyzing media performance and overlap",
    url="http://localhost:8001",
    version="1.0.0",
    defaultInputModes=["text"],
    defaultOutputModes=["text"],
    capabilities=AgentCapabilities(streaming=True),
    skills=[reach_skill]
)

# --------------------------
# Server setup
# --------------------------

handler = DefaultRequestHandler(
    agent_executor=MainExecutor(),
    task_store=InMemoryTaskStore()
)

server = A2AStarletteApplication(
    http_handler=handler,
    agent_card=agent_card
).build()

if __name__ == "__main__":
    uvicorn.run(server, host="0.0.0.0", port=8001)
