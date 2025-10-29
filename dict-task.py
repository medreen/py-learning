complex_dict = {
    "user": {
        "id": 101,
        "name": "Alice",
        "roles": ("admin", "editor"),
        "preferences": {
            "theme": "dark",
            "languages": ["Python", "Go", "Rust"],
            "notifications": {
                "email": True,
                "sms": False,
                "apps": ["Slack", "Discord"]
            }
        }
    },
    "projects": [
        {
            "title": "Project X",
            "contributors": ("Bob", "Charlie"),
            "tasks": [
                {"id": 1, "desc": "Setup repo", "done": True},
                {"id": 2, "desc": "Create API", "done": False},
                {"id": 3, "desc": "Write docs", "done": False}
            ],
            "tags": {"backend", "fastapi", "postgres"}
        },
        {
            "title": "UI Overhaul",
            "contributors": ["Diana"],
            "tasks": [],
            "tags": {"frontend", "react"}
        }
    ],
    "config": {
        "max_retries": 3,
        "features": {
            "beta": True,
            "experiments": [
                ("feature_flag", 0.75),
                ("new_login_flow", 0.2),
                ["dark_mode_v2", 0.05]
            ]
        },
        "limits": {
            "storage": {
                "free": 5 * 1024**3,
                "pro": float("inf")
            }
        }
    },
    "history": [
        {"action": "login", "timestamp": "2025-10-28T15:00:00Z"},
        {"action": "upload", "timestamp": "2025-10-28T15:05:10Z", "file": ("report.pdf", 1024 * 500)},
        {"action": "share", "timestamp": "2025-10-28T15:06:00Z", "to": ["Team A", "Team B"]}
    ],
    "misc": (
        {"nested_tuple_dict": {"numbers": (1, 2, 3)}},
        [True, False, None, {"key": "value"}],
        "end_of_world"
    )
}

#print report pdf
rpt = complex_dict["history"][1]['file'][0]
print(rpt)

#dark mode v2
dark = complex_dict["config"]["features"]["experiments"][2][0]
print(dark)

#postgres
postgres = list(complex_dict["projects"][0]["tags"])
postgres.sort()
print(postgres[2])

#numbers
numbers = complex_dict["misc"][0]['nested_tuple_dict']
print(numbers)

#user
user = complex_dict["user"].copy()
print(user)