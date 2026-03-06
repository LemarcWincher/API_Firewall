import requests

# Defines packets to send to Firewall API (flask server)

packets = [
    {
        "src_ip": "192.168.1.5",
        "dest_ip": "10.0.0.1",
        "src_port": 4000,
        "dest_port": 80,
        "protocol": "TCP"
    },
    {
        "src_ip": "192.168.1.10",  #Blocked IP
        "dest_ip": "10.0.0.1",
        "src_port": 4001,
        "dest_port": 80,
        "protocol": "TCP"
    },
    {
        "src_ip": "192.168.1.15",
        "dest_ip": "10.0.0.1",
        "src_port": 4002,
        "dest_port": 22,  #Blocked port
        "protocol": "TCP"
    }
]

for packet in packets:
    response = requests.post("http://127.0.0.1:5000/firewallcheck", json=packet)
    print(packet)
    print(response.json())
    print("-----")

print("Thank you for checking these test packets with Lemarc's API Firewall! Soon you will be prompted to enter your own...")
