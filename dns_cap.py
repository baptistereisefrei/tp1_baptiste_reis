from scapy.all import sniff, DNS, DNSQR, DNSRR

def process_packet(packet):

    if packet.haslayer(DNS) and packet[DNS].opcode == 0:
        if packet[DNS].qd and packet[DNS].qd.qname.decode() == "efrei.fr.":
            print(f"Requête DNS pour {packet[DNS].qd.qname.decode()} détectée.")
        if packet[DNS].an:
            for i in range(packet[DNS].ancount):
                answer = packet[DNS].an[i]
                if answer.type == 1:
                    print(f"Réponse DNS : Adresse IP de efrei.fr : {answer.rdata}")
                    return True

def main():
    print("En attente d'une requête et d'une réponse DNS pour efrei.fr...")
    sniff(filter="udp port 53", prn=process_packet, store=0, stop_filter=lambda x: x.haslayer(DNS) and x[DNS].an)

if __name__ == "__main__":
    main()
