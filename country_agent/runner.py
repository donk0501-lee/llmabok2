import dotenv
dotenv.load_dotenv()

from agent import root_agent

import asyncio
from google.adk.runners import InMemoryRunner
from google.genai.types import UserContent

async def main():
    runner = InMemoryRunner(agent=root_agent, app_name=root_agent.name)
    session = await runner.session_service.create_session(user_id="donk", session_id="session1", app_name=root_agent.name, state={"country": user_input})
    while(True):
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        for event in runner.run(user_id="donk", session_id=session.id, new_message=UserContent(user_input)):
            #print(event)
            if event.is_final_response():
                response = event.content.parts[0].text
        print(f"Agent: {response}")
        current_session = await runner.session_service.get_session(user_id="donk", session_id=session.id, app_name=root_agent.name)
        #print(current_session.events)

asyncio.run(main())