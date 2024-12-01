from scapy.all import sniff, IP, ICMP

def process_packet(packet):

    if packet.haslayer(ICMP):
        icmp_layer = packet[ICMP]
        
        if icmp_layer.type == 8 and packet.haslayer(IP):
            data = bytes(icmp_layer.payload).decode(errors="ignore")
            if data.strip():
                print(f"Message reçu : {data}")

def start_sniffing():

    print("[*] En attente de messages ICMP contenant des données...")
    sniff(filter="icmp", prn=process_packet, store=False, iface='lo')

if __name__ == "__main__":
    try:
        start_sniffing()
    except KeyboardInterrupt:
        print("\n[!] Arrêt de la capture ICMP.")
