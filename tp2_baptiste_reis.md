# TP 2
Baptiste Reis

## Setup topologie

### Le routeur doit pouvoir joindre internet

```
R1(config)#interface fastEthernet 0/0
R1(config-if)#ip address dhcp
R1(config-if)#no shut
R1(config-if)#exit
*Nov 26 10:28:30.879: %DHCP-6-ADDRESS_ASSIGN: Interface FastEthernet0/0 assig DHCP address 192.168.122.167, mask 255.255.255.0, hostname R1
```

```
R1#ping 8.8.8.8

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 60/72/92 ms
```
### Configuration d'un NAT simpliste

```
PC1> ping 8.8.8.8

84 bytes from 8.8.8.8 icmp_seq=1 ttl=114 time=40.458 ms
84 bytes from 8.8.8.8 icmp_seq=2 ttl=114 time=34.807 ms
84 bytes from 8.8.8.8 icmp_seq=3 ttl=114 time=38.737 ms
84 bytes from 8.8.8.8 icmp_seq=4 ttl=114 time=35.747 ms
84 bytes from 8.8.8.8 icmp_seq=5 ttl=114 time=42.884 ms

```
### Proof !

```
PC4> dhcp
DORA IP 10.2.1.102/24 GW 10.2.1.254

```

```
PC4> ping 10.2.1.51

84 bytes from 10.2.1.51 icmp_seq=1 ttl=64 time=3.041 ms
84 bytes from 10.2.1.51 icmp_seq=2 ttl=64 time=1.229 ms
84 bytes from 10.2.1.51 icmp_seq=3 ttl=64 time=1.992 ms
84 bytes from 10.2.1.51 icmp_seq=4 ttl=64 time=1.806 ms
84 bytes from 10.2.1.51 icmp_seq=5 ttl=64 time=1.681 ms

```

```
PC4> ping 8.8.8.8

84 bytes from 8.8.8.8 icmp_seq=1 ttl=114 time=40.391 ms
84 bytes from 8.8.8.8 icmp_seq=2 ttl=114 time=36.481 ms
84 bytes from 8.8.8.8 icmp_seq=3 ttl=114 time=37.653 ms
84 bytes from 8.8.8.8 icmp_seq=4 ttl=114 time=52.866 ms
84 bytes from 8.8.8.8 icmp_seq=5 ttl=114 time=44.632 ms

```
### ARP (attaque 1)

#### Poisoning

```
PC1> arp

08:00:27:ad:25:87  10.2.1.114 expires in 90 seconds
aa:bb:cc:dd:ee:ff  10.2.1.14 expires in 113 seconds

```

#### Spoofing

```

PC1> arp

08:00:27:ad:25:87  10.2.1.114 expires in 48 seconds
08:00:27:ad:25:87  10.2.1.52 expires in 120 seconds

PC1> ping 10.2.1.52

84 bytes from 10.2.1.52 icmp_seq=1 ttl=63 time=9.679 ms
84 bytes from 10.2.1.52 icmp_seq=2 ttl=63 time=6.372 ms
84 bytes from 10.2.1.52 icmp_seq=3 ttl=63 time=6.688 ms
84 bytes from 10.2.1.52 icmp_seq=4 ttl=63 time=7.906 ms
84 bytes from 10.2.1.52 icmp_seq=5 ttl=63 time=7.871 ms
```
### Man in the middle

```
PC1> arp

08:00:27:ad:25:87  10.2.1.114 expires in 31 seconds
08:00:27:ad:25:87  10.2.1.254 expires in 120 seconds
```
```
R1#show arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.2.1.11              25   0800.2789.6765  ARPA   FastEthernet1/0
Internet  192.168.122.1           0   5254.00d1.e503  ARPA   FastEthernet0/0
Internet  10.2.1.51               0   0800.27ad.2587  ARPA   FastEthernet1/0
Internet  192.168.122.81          -   ca01.0534.0000  ARPA   FastEthernet0/0
Internet  10.2.1.114              1   0800.27ad.2587  ARPA   FastEthernet1/0
Internet  10.2.1.254              -   ca01.0534.001c  ARPA   FastEthernet1/0
```
### Remediation

#### Fixez les adresses IP et MAC importantes (passerelle, serveurs critiques) directement dans les tables ARP des machines :

- sudo arp -s <ip_address> <mac_address>

#### Activer Dynamic ARP Inspection (DAI) :

Configurez cette fonctionnalité sur les switches gérés :

Exemple Cisco :

- ip arp inspection vlan <vlan_id>
- ip dhcp snooping

#### Utiliser HTTPS et SSL/TLS

Chiffrez les communications réseau pour empêcher le vol d'informations sensibles, même en cas d'interception :

- Implémentez HTTPS pour les sites web et HSTS pour forcer son utilisation.
- Assurez-vous que les connexions à distance utilisent SSH, VPN ou TLS.

### ICMP (attaque 2)

```
sudo python icmp_basic_exfiltr.py 127.0.0.1 'hello data'
[sudo] password for kali: 
[*] Envoi de la chaîne 'hello data' dans des pings vers 127.0.0.1
[*] Paquet envoyé : hello data
```
```
sudo python icmp_basic_receiver.py
[*] En attente de messages ICMP contenant des données...
Message reçu : Hello, ICMP exfiltration
Message reçu : Hello, ICMP exfiltration
```

