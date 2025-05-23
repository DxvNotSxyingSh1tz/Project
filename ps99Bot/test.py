import requests

res = requests.post("http://127.0.0.1:5000/verify", json={
    "code": "088554",
    "roblox_name": "WSpolii"
})

print(res.status_code)
print(res.json())
