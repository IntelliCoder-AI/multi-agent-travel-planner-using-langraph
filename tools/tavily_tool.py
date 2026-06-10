from tavily import TavilyClient

from config import TAVILY_API_KEY

client = TavilyClient(
    api_key=TAVILY_API_KEY
)


def tavily_search(
    query: str,
    max_results: int = 5
):

    try:

        response = client.search(
            query=query,
            max_results=max_results
        )

        results = []

        for item in response.get(
            "results",
            []
        ):

            results.append(
                {
                    "title":
                        item.get(
                            "title"
                        ),

                    "url":
                        item.get(
                            "url"
                        ),

                    "content":
                        item.get(
                            "content",
                            ""
                        )[:300]
                }
            )

        return results

    except Exception as e:

        return [
            {
                "error":
                    str(e)
            }
        ]
