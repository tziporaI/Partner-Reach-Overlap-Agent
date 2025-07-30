from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill
from agent_executor import AnalizeAgentExecutor
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.apps import A2AStarletteApplication
import uvicorn

analyze_media_performance_skill = AgentSkill(
    id="analyze_media_performance",
    name="Analyze Media Performance",
    description="Performs media analysis...",
    tags=["media", "analysis"],
    examples=["Analyze media performance for campaign XYZ..."]
)

root_agent_card = AgentCard(
    name="MediaPerformanceAnalyzerAgent",
    description="Main agent for analyzing media performance",
    url="http://localhost:8001",
    version="1.0.0",
    defaultInputModes=["text"],
    defaultOutputModes=["text"],
    capabilities=AgentCapabilities(streaming=True),
    skills=[analyze_media_performance_skill],
)

request_handler = DefaultRequestHandler(
    agent_executor=AnalizeAgentExecutor(),
    task_store=InMemoryTaskStore(),
)

server = A2AStarletteApplication(
    http_handler=request_handler,
    agent_card=root_agent_card,
).build()

if __name__ == "__main__":
    uvicorn.run(server, host="0.0.0.0", port=8001)
