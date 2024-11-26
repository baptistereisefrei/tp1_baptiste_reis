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