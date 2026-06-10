def search_flights(
    origin: str,
    destination: str
):

    return [
        {
            "airline": "Air India",
            "route":
                f"{origin} -> {destination}",
            "price":
                "₹60,000 - ₹90,000"
        },
        {
            "airline": "Singapore Airlines",
            "route":
                f"{origin} -> {destination}",
            "price":
                "₹70,000 - ₹1,00,000"
        }
    ]


