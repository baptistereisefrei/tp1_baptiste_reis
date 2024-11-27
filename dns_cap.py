from scapy.all import sniff, DNS, DNSQR, DNSRR

def process_packet(packet):
    """
    Fonction pour traiter chaque paquet capturé.
    Vérifie si le paquet est une requête et une réponse DNS.
    """
    if packet.haslayer(DNS) and packet[DNS].opcode == 0:  # Opcode 0 correspond à une requête standard
        # Si c'est une requête DNS pour efrei.fr
        if packet[DNS].qd and packet[DNS].qd.qname.decode() == "efrei.fr.":
            print(f"Requête DNS pour {packet[DNS].qd.qname.decode()} détectée.")
        # Si c'est une réponse DNS
        if packet[DNS].an:
            for i in range(packet[DNS].ancount):  # Parcours des réponses
                answer = packet[DNS].an[i]
                if answer.type == 1:  # Type 1 correspond à une réponse IPv4
                    print(f"Réponse DNS : Adresse IP de efrei.fr : {answer.rdata}")
                    return True  # Stopper après avoir capturé une réponse

def main():
    print("En attente d'une requête et d'une réponse DNS pour efrei.fr...")
    # Capture des paquets avec un filtre DNS
    sniff(filter="udp port 53", prn=process_packet, store=0, stop_filter=lambda x: x.haslayer(DNS) and x[DNS].an)

if __name__ == "__main__":
    main()
