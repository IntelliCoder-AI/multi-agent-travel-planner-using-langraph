from tools.tavily_tool import (
    tavily_search
)


def get_visa_requirements(
    destination: str
):

    query = (
        f"Visa requirements for "
        f"Indian citizens travelling "
        f"to {destination}"
    )

    return tavily_search(query)

