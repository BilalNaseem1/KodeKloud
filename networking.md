# Networking Crash course
- Protocol: Rule which defined how is data being sent is known as protocol
- TCP: Transmission control protocol - it will ensure that the data will reach its destination and will not be corrupted on the way
- UDP: User Datagram protocol not all data is reached e.g. vdeo calling
- HTTP: Hyper-text Transfer protocol. Used by web browsers. defines the format of the data which is being websites - clients and servers 

- Files are always sent in chunks (packets)
- Servers are identified using IP addresses

```bash
curl ifconfig.me -s
```
## Ports
- Ports are 16 bit numbers - so total port numbers which are possible are 2^16.
- Web pages use http. All http stuff happens at port `80`.
- Port for mongodb is 27017.
- ports 0 to 1023 are reserved ports
- ports 1024 to 49152 are registered for applications like mongodb and mysql etc.
- 1 MBPS means 1 mega bits per second.

## Types of Networks
**_LAN:_** For a small house / office. Network adapter is used or wifi

**_MAN:_** Metropolitan area network across a city

**_WAN:_**  Wide area network across countries using optical fibre cables.

- Internet is a collection of all 3 above.
- A lot of LANs are connected to each other using MAN, which are connected to each other using WANs.

1. SONET - synchronous optical networking. carries data using optical fibre cables, hence can cover larger distances.
2. Frame Relay - connect LAN to WAN

## Modem & Router
- Modem is used to convert digital signals into analogue (electrical) signals and vv.
- 


OSI MODEL 

ALL             - APPLICATION LAYER
PEOPLE     - PRESENTATION LAYER
SHOULD    - SESSION LAYER
TRY            - TRANSPORT LAYER
NEW           - NETWORK LAYER
DOMINOS  -  DATALINK
PIZZA         - PHYSICAL LAYER