# agents/visa_agent.py

from state import TravelState

from tools.visa_tool import (
    get_visa_requirements
)


def visa_agent(
    state: TravelState
):

    visa = get_visa_requirements(
        state["destination"]
    )

    return {

        "visa":
            visa,

        "llm_calls":
            state.get(
                "llm_calls",
                0
            ) + 1
    }

