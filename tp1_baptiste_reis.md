# TP 1
Baptiste Reis

## Setup topologie 1

### Commençons simple

```
pc1> sh ip

NAME        : pc1[1]
IP/MASK     : 10.3.1.1/24
GATEWAY     : 255.255.255.0
DNS         :
MAC         : 00:50:79:66:68:00
LPORT       : 20004
RHOST:PORT  : 127.0.0.1:20005
MTU         : 1500

```  
```
pc2> sh ip

NAME        : pc2[1]
IP/MASK     : 10.3.1.2/24
GATEWAY     : 255.255.255.0
DNS         :
MAC         : 00:50:79:66:68:01
LPORT       : 20006
RHOST:PORT  : 127.0.0.1:20007
MTU         : 1500
```  
```
pc1> ping 10.3.1.2

84 bytes from 10.3.1.2 icmp_seq=1 ttl=64 time=0.945 ms
84 bytes from 10.3.1.2 icmp_seq=2 ttl=64 time=1.168 ms
84 bytes from 10.3.1.2 icmp_seq=3 ttl=64 time=2.231 ms
84 bytes from 10.3.1.2 icmp_seq=4 ttl=64 time=1.178 ms
84 bytes from 10.3.1.2 icmp_seq=5 ttl=64 time=1.066 ms
``` 
```
sw1#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
   1    0050.7966.6800    DYNAMIC     Et0/0
   1    0050.7966.6801    DYNAMIC     Et0/1
Total Mac Addresses for this criterion: 2
```
## Setup topologie 2

### Adressage

```
pc3> sh ip

NAME        : pc3[1]
IP/MASK     : 10.3.1.3/24
GATEWAY     : 255.255.255.0
DNS         :
MAC         : 00:50:79:66:68:02
LPORT       : 20010
RHOST:PORT  : 127.0.0.1:20011
MTU         : 1500
```
```
pc3> ping 10.3.1.1

84 bytes from 10.3.1.1 icmp_seq=1 ttl=64 time=0.603 ms
84 bytes from 10.3.1.1 icmp_seq=2 ttl=64 time=1.328 ms
84 bytes from 10.3.1.1 icmp_seq=3 ttl=64 time=0.975 ms
84 bytes from 10.3.1.1 icmp_seq=4 ttl=64 time=0.798 ms
84 bytes from 10.3.1.1 icmp_seq=5 ttl=64 time=0.942 ms

pc3> ping 10.3.1.2

84 bytes from 10.3.1.2 icmp_seq=1 ttl=64 time=0.567 ms
84 bytes from 10.3.1.2 icmp_seq=2 ttl=64 time=1.044 ms
84 bytes from 10.3.1.2 icmp_seq=3 ttl=64 time=1.003 ms
84 bytes from 10.3.1.2 icmp_seq=4 ttl=64 time=0.662 ms
84 bytes from 10.3.1.2 icmp_seq=5 ttl=64 time=0.849 ms
```

### Configuration des VLANs

```
sw1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/3, Et1/0, Et1/1, Et1/2
                                                Et1/3, Et2/0, Et2/1, Et2/2
                                                Et2/3, Et3/0, Et3/1, Et3/2
                                                Et3/3
10   VLAN10                           active    Et0/0, Et0/1
20   VLAN20                           active    Et0/2
1002 fddi-default                     act/unsup
1003 token-ring-default               act/unsup
1004 fddinet-default                  act/unsup
1005 trnet-default                    act/unsup
```

```
pc1> ping 10.3.1.2

84 bytes from 10.3.1.2 icmp_seq=1 ttl=64 time=1.714 ms
84 bytes from 10.3.1.2 icmp_seq=2 ttl=64 time=1.298 ms
84 bytes from 10.3.1.2 icmp_seq=3 ttl=64 time=1.289 ms
84 bytes from 10.3.1.2 icmp_seq=4 ttl=64 time=1.369 ms
84 bytes from 10.3.1.2 icmp_seq=5 ttl=64 time=1.040 ms
```
```

pc3> ping 10.3.1.1

host (10.3.1.1) not reachable

pc3> ping 10.3.1.2

host (10.3.1.2) not reachable
```

### Vérif
