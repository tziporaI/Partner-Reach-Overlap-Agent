from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message

class HelloWorldExecutor(AgentExecutor):
    async def execute(self, context: RequestContext, event_queue: EventQueue):
        await event_queue.enqueue_event(new_agent_text_message("שלום עולם 👋"))
    async def cancel(self, context: RequestContext, event_queue: EventQueue):
        raise NotImplementedError("Cancel not supported")
