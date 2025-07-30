import httpx
from a2a.client import A2ACardResolver, A2AClient
from a2a.types import (
    AgentCard,
    Message,
    MessageSendParams,
    Part,
    Role,
    SendMessageRequest,
    TextPart
)
import uuid

PUBLIC_AGENT_CARD_PATH = "/.well-known/agent.json"
BASE_URL = "http://localhost:8001"

async def main()->None:
    async with httpx.AsyncClient() as httpx_client:
        resolver = A2ACardResolver(
            httpx_client=httpx_client,
            base_url=BASE_URL
        )

        final_agent_card_to_use: AgentCard | None

        try:
            print(
                f"fetching pablic agent card from {BASE_URL}{PUBLIC_AGENT_CARD_PATH}"
            )
            _public_card = await resolver.get_agent_card()
            print("fetched pablic agent card")
            print(_public_card.model_dump_json(indent=2))

            final_agent_card_to_use = _public_card
        except Exception as e:
            print(f"error feching public agent card: {e}")
            raise RuntimeError("failed to fetch public agent card")
        client = A2AClient(
            httpx_client=httpx_client,
            agent_card=final_agent_card_to_use,
        )
        print("a2aClient initialized")

        message_payload = Message(
            role = Role.user,
            message_id=str(uuid.uuid4()),
            parts=[Part(root=TextPart(text="analizing"))]
        )

        request = SendMessageRequest(
            id=str(uuid.uuid4()),
            params=MessageSendParams(
                message=message_payload,
            ),
        )
        print("sending message")

        response = await client.send_message(request)
        print("response:")
        print(response.model_dump_json(indent=2))
if __name__ =="__main__":
    import asyncio
    asyncio.run(main())