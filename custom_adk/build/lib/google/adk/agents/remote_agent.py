from a2a.client import A2AClient
from a2a.types import AgentCard, Message, Role, Part, TextPart, SendMessageRequest, MessageSendParams
import httpx
import uuid

class RemoteA2aAgent:
    def __init__(self, agent_card: AgentCard):
        self.agent_card = agent_card

    async def execute(self, text: str):
        message = Message(
            role=Role.user,
            message_id=str(uuid.uuid4()),
            parts=[Part(root=TextPart(text=text))]
        )
        request = SendMessageRequest(
            id=str(uuid.uuid4()),
            params=MessageSendParams(message=message)
        )
        async with httpx.AsyncClient() as client:
            a2a_client = A2AClient(httpx_client=client, agent_card=self.agent_card)
            return await a2a_client.send_message(request)
