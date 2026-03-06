import requests

# URL of running Flask firewall(API)
FIREWALL_URL = "http://127.0.0.1:5000/firewallcheck"

print("=== User Packet Sender ==")
print("Please enter packet info to send to Lemarc's API Firewall.\n")

while True:
    # Gets 5-tuple info from user
    src_ip = input("Enter source IP: ").strip()
    dest_ip = input("Enter destination IP: ").strip()

    # Validate port inputs
    try:
        src_port = int(input("Enter source port: ").strip())
        dest_port = int(input("Enter destination port: ").strip())
    except ValueError: #ensures input is integer
        print("Ports must be numbers. Try again.\n")
        continue

    protocol = input("Enter protocol (TCP/UDP): ").strip().upper()
    if protocol not in ["TCP", "UDP"]: #ensures input is TCP or UDP
        print("Protocol must be TCP or UDP. Try again.\n")
        continue

    # Build packet with logging flag
    user_packet = {
        "src_ip": src_ip,
        "dest_ip": dest_ip,
        "src_port": src_port,
        "dest_port": dest_port,
        "protocol": protocol,
        "user_packet": True  # ensures Flask logs it
    }

      # Sends packet to firewall
    try:
        response = requests.post(FIREWALL_URL, json=user_packet)
        resp_json = response.json()
        print(f"\nFirewall Response: {resp_json}\n")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to firewall: {e}\n")

    # Ask if user wants to send another packet
    cont = input("Send another packet? (y/n): ").strip().lower()
    if cont != "y":
        print("Exiting User Packet Sender. Thank you for using my Lemarc's API Firewall!")
        break
