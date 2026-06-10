# agents/attraction_agent.py

from state import TravelState

from tools.tavily_tool import (
    tavily_search
)


def attraction_agent(
    state: TravelState
):

    destination = state[
        "destination"
    ]

    attractions = tavily_search(
        f"""
        Top tourist attractions
        in {destination}

        Include:
        - famous places
        - food experiences
        - hidden gems
        """
    )

    return {

        "attractions":
            attractions,

        "llm_calls":
            state.get(
                "llm_calls",
                0
            ) + 1
    }

