import asyncio
from custom_adk.google.adk.agents.remote_agent import RemoteA2aAgent
from a2a.types import AgentCard, AgentCapabilities

hello_agent_card = AgentCard(
    name="hello_agent",
    description="Simple hello agent",
    url="http://localhost:8002",
    version="1.0.0",
    defaultInputModes=["text"],
    defaultOutputModes=["text"],
    capabilities=AgentCapabilities(streaming=True),
    skills=[]
)

hello_agent = RemoteA2aAgent(agent_card=hello_agent_card)

async def main():
    print("⏳ שולח בקשה ל־Hello Agent...")
    result = await hello_agent.execute("תגיד שלום")

    try:
        text = result.root.result.parts[0].root.text
        print("✅ תשובה:", text)
    except Exception as e:
        print("❌ שגיאה:", e)
        print("🔍 תגובה מלאה:", result)

if __name__ == "__main__":
    asyncio.run(main())
