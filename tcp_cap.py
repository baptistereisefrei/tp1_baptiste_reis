from scapy.all import sniff, TCP, IP

def process_packet(packet):
    """
    Fonction pour traiter chaque paquet capturé.
    Vérifie si le paquet est un TCP SYN-ACK.
    """
    if TCP in packet and packet[TCP].flags == 0x12:  # 0x12 correspond à SYN-ACK
        print("TCP SYN ACK reçu !")
        print(f"- Adresse IP src : {packet[IP].src}")
        print(f"- Adresse IP dst : {packet[IP].dst}")
        print(f"- Port TCP src : {packet[TCP].sport}")
        print(f"- Port TCP dst : {packet[TCP].dport}")
        return True  # Arrête la capture après avoir trouvé un SYN-ACK

def main():
    print("Attente d'un TCP SYN-ACK...")
    # Capture un paquet à la fois avec un filtre pour les paquets TCP
    sniff(filter="tcp", prn=process_packet, store=0, stop_filter=lambda x: TCP in x and x[TCP].flags == 0x12)

if __name__ == "__main__":
    main()
