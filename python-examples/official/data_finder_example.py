# This code will get you historical EPS (periods TTM, TTM-1 and TTM-2) for Apple Inc (SimFin ID 111052)

import requests

data = {
    "search": [
        {
            "indicatorId": "4-12",
            "meta": [
                {
                    "id": 6,
                    "value": "TTM",
                    "operator": "eq"
                },
            ],
        },
        {
            "indicatorId": "4-12",
            "meta": [
                {
                    "id": 6,
                    "value": "TTM-1",
                    "operator": "eq"
                },
            ],
        },
        {
            "indicatorId": "4-12",
            "meta": [
                {
                    "id": 6,
                    "value": "TTM-2",
                    "operator": "eq"
                },
            ],
        }
    ],
    "simIdList": [
        111052
    ]
}

r = requests.post('https://simfin.com/api/v1/finder?api-key=YOUR_API_KEY', json=data)
print(r.content)