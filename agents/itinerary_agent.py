# agents/itinerary_agent.py

from langchain_core.messages import (
    HumanMessage,
    SystemMessage
)

from langchain_groq import ChatGroq

from config import GROQ_API_KEY
from state import TravelState


llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0
)


def itinerary_agent(
    state: TravelState
):

    prompt = f"""
Create a professional travel plan.

Destination:
{state["destination"]}

Duration:
{state["duration"]}

User Budget:
{state["budget"]}

Flights:
{state["flights"]}

Hotels:
{state["hotels"]}

Weather:
{state["weather"]}

Visa:
{state["visa"]}

Attractions:
{state["attractions"]}

Budget Summary:
{state["budget_summary"]}

Instructions:

1. Create a day-wise itinerary.
2. Mention recommended hotels.
3. Mention weather considerations.
4. Mention visa requirements.
5. Mention attractions.
6. Mention estimated budget.
7. Provide travel tips.
8. Format professionally.
9. ONLY use information provided.
10. NEVER invent hotels.
11. NEVER invent attractions.
12. If data is unavailable, explicitly say so.
13. Use retrieved sources whenever possible.
"""

    response = llm.invoke(
        [
            SystemMessage(
                content=
                "You are an expert travel planner."
            ),
            HumanMessage(
                content=prompt
            )
        ]
    )

    return {

        "itinerary":
            response.content,

        "llm_calls":
            state.get(
                "llm_calls",
                0
            ) + 1
    }

