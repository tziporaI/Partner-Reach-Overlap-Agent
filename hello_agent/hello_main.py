from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill
from hello_executor import HelloWorldExecutor
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.apps import A2AStarletteApplication
import uvicorn

hello_skill = AgentSkill(
    id="say_hello",
    name="Say Hello",
    description="Responds with a friendly greeting.",
    tags=["greeting"],
    examples=["Say hello"]
)

hello_card = AgentCard(
    name="HelloWorldAgent",
    description="Responds with hello.",
    url="http://localhost:8002",
    version="1.0.0",
    defaultInputModes=["text"],
    defaultOutputModes=["text"],
    capabilities=AgentCapabilities(streaming=True),
    skills=[hello_skill]
)

handler = DefaultRequestHandler(
    agent_executor=HelloWorldExecutor(),
    task_store=InMemoryTaskStore(),
)

server = A2AStarletteApplication(
    http_handler=handler,
    agent_card=hello_card,
).build()

if __name__ == "__main__":
    uvicorn.run(server, host="0.0.0.0", port=8002)
