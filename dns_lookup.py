from scapy.all import Ether, IP, UDP, DNS, DNSQR, srp

def main():
    target_ip = "8.8.8.8"
    target_domain = "efrei.fr"
    eth = Ether()
    ip = IP(dst=target_ip)
    udp = UDP(sport=12345, dport=53)
    dns = DNS(rd=1, qd=DNSQR(qname=target_domain, qtype="A"))
    packet = eth / ip / udp / dns

    print(f"Envoi de la requête DNS pour {target_domain} vers {target_ip}...")

    response, _ = srp(packet, timeout=2, verbose=False)

    if response:
        for sent, received in response:
            if received.haslayer(DNS) and received[DNS].ancount > 0:
                for i in range(received[DNS].ancount):
                    answer = received[DNS].an[i]
                    if answer.type == 1:
                        print(f"Adresse IP pour {target_domain} : {answer.rdata}")
    else:
        print("Aucune réponse reçue.")

if __name__ == "__main__":
    main()
