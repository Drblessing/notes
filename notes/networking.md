# Networking

## Ping server

```bash
ping <hostname>
```

Example:

```bash
~ 🐴 ping github.com
PING github.com (192.30.255.113): 56 data bytes
64 bytes from 192.30.255.113: icmp_seq=0 ttl=46 time=47.146 ms
64 bytes from 192.30.255.113: icmp_seq=1 ttl=46 time=46.927 ms
^C
--- github.com ping statistics ---
3 packets transmitted, 2 packets received, 33.3% packet loss
round-trip min/avg/max/stddev = 46.927/47.037/47.146/0.109 ms
```

## Find the IP address of a host

```bash
nslookup <hostname>
```

Example:

```bash
~ 🐴 nslookup github.com
Server:		2001:558:feed::1
Address:	2001:558:feed::1#53

Non-authoritative answer:
Name:	github.com
Address: 192.30.255.112
```

Note the address will change depending on your region.

## Find the hostname of an IP address

```bash
nslookup <ip address>
```

Example:

```bash
~ 🐴 nslookup 192.30.255.112
Server:		2001:558:feed::1
Address:	2001:558:feed::1#53

Non-authoritative answer:
112.255.30.192.in-addr.arpa	name = lb-192-30-255-112-sea.github.com.
```

## Find the hostname of a server

```bash
hostname
```

## Trace route to a server

```bash
traceroute <hostname or ip address>
```

Example:

```bash
~ 🐴 traceroute 192.30.255.112
traceroute to 192.30.255.112 (192.30.255.112), 64 hops max, 52 byte packets
 1  10.0.0.1 (10.0.0.1)  10.143 ms  10.700 ms  7.091 ms
 2  96.120.95.9 (96.120.95.9)  19.603 ms  17.976 ms  18.066 ms
 3  96.110.179.185 (96.110.179.185)  18.356 ms  18.007 ms  19.132 ms
 4  be-324-rar01.pleasanton.ca.sfba.comcast.net (162.151.79.133)  29.641 ms  20.450 ms  19.404 ms
 5  be-398-ar01.hayward.ca.sfba.comcast.net (162.151.87.225)  33.562 ms  31.839 ms  21.419 ms
 6  be-36311-cs01.9greatoaks.ca.ibone.comcast.net (68.86.93.129)  23.047 ms  21.548 ms
    be-36321-cs02.9greatoaks.ca.ibone.comcast.net (68.86.93.133)  20.917 ms
 7  be-2312-pe12.9greatoaks.ca.ibone.comcast.net (96.110.33.42)  25.669 ms
    be-2212-pe12.9greatoaks.ca.ibone.comcast.net (96.110.33.38)  24.968 ms
    be-2412-pe12.9greatoaks.ca.ibone.comcast.net (96.110.33.46)  23.357 ms
 8  ae7.cr3-sjc1.ip4.gtt.net (209.120.154.117)  25.012 ms  23.083 ms  82.593 ms
 9  ae21.cr4-sea2.ip4.gtt.net (89.149.130.78)  45.648 ms
    ae19.cr5-sea2.ip4.gtt.net (89.149.139.222)  41.291 ms  52.267 ms
10  ip4.gtt.net (208.116.132.190)  40.593 ms
    ip4.gtt.net (208.116.132.198)  43.245 ms
    ip4.gtt.net (208.116.132.190)  43.689 ms
11  * * *
12  * * *
13  * * *
```
