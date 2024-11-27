from scapy.all import *

ping = ICMP(type=8)
packet = IP(src="10.2.1.114", dst="10.2.1.51")
frame = Ether(src="08:00:27:ad:25:87", dst="00:50:79:66:68:00")
final_frame = frame/packet/ping
answers, unanswered_packets = srp(final_frame, timeout=10)
print(f"Pong reçu : {answers[0]}")