from google.adk.agents.remote_agent import RemoteA2aAgent
from google.adk.tools.base_tool import BaseTool
from a2a.types import AgentCard, AgentCapabilities

class HelloA2ATool(BaseTool):
    def __init__(self):
        super().__init__(name="HelloWorldAgent", description="Calls HelloWorldAgent remotely.")

        hello_card = AgentCard(
            name="HelloWorldAgent",
            description="Responds with hello.",
            url="http://localhost:8002",
            version="1.0.0",
            defaultInputModes=["text"],
            defaultOutputModes=["text"],
            capabilities=AgentCapabilities(streaming=True),
            skills=[]
        )
        self.hello_agent = RemoteA2aAgent(agent_card=hello_card)

    async def __call__(self, input: str) -> str:
        result = await self.hello_agent.execute(input)
        return result.root.result.parts[0].root.text
