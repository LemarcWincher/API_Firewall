from flask import Flask, request, jsonify
import logging
import json

# Creates server
app = Flask(__name__)

# Configure logging for user packets entered
logging.basicConfig(
    filename='user_packets.txt',  # log file 
    level=logging.INFO,
    format='%(message)s'  # just the message itself
    )
    
# Simple packet check
@app.route("/firewallcheck", methods=['POST'])
def check_packet():

    # Stores packet client sent
    packet = request.json

    # Check if this packet is user-entered
    user_packet = packet.get("user_packet", False)


    # Grabs attributes from packet
    src_ip = packet.get("src_ip")
    dest_ip = packet.get("dest_ip")
    src_port = packet.get("src_port")
    dest_port = packet.get("dest_port")
    protocol = packet.get("protocol")

    # Sets protocols for packet to follow, creating firewall
    blocked_ips = ["192.168.1.10", "10.0.0.5"] 
    
    if src_ip in blocked_ips: #No blocked IPs allowed
        if user_packet:
            packet_log = packet.copy()
            packet_log['status'] = "blocked"
            packet_log['reason'] = "Source IP is blocked"
            logging.info(json.dumps(packet_log))
        return jsonify({
            "status": "blocked",
            "reason": "Source IP is blocked"
        })

    if protocol != "TCP": #TCP ports only
        if user_packet:
            packet_log = packet.copy()
            packet_log['status'] = "blocked"
            packet_log['reason'] = "Only TCP allowed"
            logging.info(json.dumps(packet_log))
        return jsonify({
            "status": "blocked",
            "reason": "Only TCP allowed"
        })

    if dest_port == 22: #SSH port, gives remote access
        if user_packet:
            packet_log = packet.copy()
            packet_log['status'] = "blocked"
            packet_log['reason'] = "Destination Port is prohibited"
            logging.info(json.dumps(packet_log))
        return jsonify({
            "status": "blocked",
            "reason": "Destination Port is prohibited"
        })

    # If the packet is entered from a user, log it
    if user_packet: 
        packet_log = packet.copy()
        packet_log['status'] = "allowed"
        packet_log['reason'] = ""
        logging.info(json.dumps(packet_log))

    return jsonify({"status": "allowed"})


if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)   

    
