# agents/supervisor_agent.py

import json
import re

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


def supervisor_agent(
    state: TravelState
):

    prompt = f"""
Extract travel information from the user request.

User Request:
{state["user_query"]}

Return ONLY JSON.

Required format:

{{
    "destination": "",
    "duration": 0,
    "budget": "",
    "origin_country": ""
}}

Rules:
1. Return only JSON.
2. Do not add explanations.
3. Do not use markdown.
4. Do not wrap in ```json.
5. If budget is not specified, return "Not specified".
6. If origin country is not specified, infer if obvious.
"""

    response = llm.invoke(
        [
            SystemMessage(
                content="""
You are a JSON extraction engine.

Return ONLY valid JSON.

Never use markdown.
Never use ```json.
Never provide explanations.
"""
            ),
            HumanMessage(
                content=prompt
            )
        ]
    )

    raw_content = response.content.strip()

    print("\nRAW RESPONSE:")
    print(raw_content)

    try:

        # Remove markdown fences if model still adds them
        raw_content = re.sub(
            r"^```json\s*",
            "",
            raw_content
        )

        raw_content = re.sub(
            r"^```\s*",
            "",
            raw_content
        )

        raw_content = re.sub(
            r"\s*```$",
            "",
            raw_content
        )

        print("\nCLEANED RESPONSE:")
        print(raw_content)

        data = json.loads(
            raw_content
        )

    except Exception as e:

        print("\nJSON ERROR:")
        print(e)

        data = {
            "destination": "Unknown",
            "duration": 7,
            "budget": "Not specified",
            "origin_country": "India"
        }

    return {

        "destination":
            data.get(
                "destination",
                "Unknown"
            ),

        "duration":
            data.get(
                "duration",
                7
            ),

        "budget":
            data.get(
                "budget",
                "Not specified"
            ),

        "llm_calls":
            state.get(
                "llm_calls",
                0
            ) + 1
    }
