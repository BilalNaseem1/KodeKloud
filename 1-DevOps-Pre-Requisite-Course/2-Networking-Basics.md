# Networking Basics

[Basics of IP Address & Subnetting Part 1](https://www.youtube.com/watch?v=5WfiTHiU4x8&list=PLIhvC56v63IKrRHh3gvZZBAGvsvOhwrRF)

- Every computer device has an IP Address (it's just like a phone number)
- IP Addresses also give the ability to connect to the internet
- To check current IP Address:
```bash
# windows
ipconfig

#linux
curl ifconfig.me

sudo apt-get install net-tools
ifconfig
```
![alt text](images/image-5.png)

## How did the device get its IP Address
- Whenever a device connects to a router (Opera), the router gives it an IP Address
- Each of the numbers below can be between 0 and 255


![alt text](images/image-6.png)

- Mostly ip addresses start with `192.168.1.***`
- The way that opera tells us that each IP address is going to start with `192.168.1.***` is through a `Subnet Mask` 
- Purpose of subnet mask is to tell what IP's in our network start with.
- Each of the 4 numbers which are seperated by decimals are called octets.
- If the octet of the subnet mask is 255, then the corresponding octet of the IP address will remain the same in the same network 
- So in the below images/image `192.168.1` will always remain the same. These 3 numbers are known as the network portion of the IP Address.
- 0 in the subnet mask means the corresponding octet in the IP address can be any number it wants. This number is known as the Host portion of the IP Address. So for the below images/image a total of `256 - 3 = 253` IP Addresses are possible.
- `192.168.1.0` is known as the network address. `192.168.1.255` is the broadcast address (it contacts with everyone). These 2 and the Router IP are reserved and cannot be used.

![alt text](images/image-7.png)

![alt text](images/image-8.png)

- The network portion remains the same because other devices are in the same neighbourhood. Network portion is the neighbourhood name, and host part is the house address.
- If an IP is in a different neighbourhood (different network portion) - for ex. accessing netflix.com , then the router (default gateway) will be used for this.
- So every device looks at `IP Address -> Subet Mask`. If the IP is not in the network, it contacts default gateway
So when we have devices in a network, they all are known as hosts in the network (only have different hosts in the network)

---
[Basics of IP Address & Subnetting Part II](https://www.youtube.com/watch?v=tcae4TSSMo8&list=PLIhvC56v63IKrRHh3gvZZBAGvsvOhwrRF&index=2)

- There are 4.3 Billion (`0-255 . 0-255 . 0-255 . 0-255  ~= 2^32`) possible IP Addresses, and all of them are run out. 
- There are 5 groups of IP addresses A to E
- Classes A, B and C each have their own default subnet mask (It determines how big the network is / which numbers in our IP address remain the same and which change)
- In class A only the first octet is static, rest can change - so overall 16 million IP addresses are possible in 1 network.
- Big companies have category A IP addresses - each has 16 million IP addresses (hosts) - There are only 126 class A networks.
- IANA is responsible for giving away IP addresses
- Big companies break it into smaller networks
- IP addresses which have subnet mask of `255.255.255.0` are called classless network.
- In class B 65k ip addresses are possible and 16k networks are possible.
- In class C 254 IP addresses are possible and 2M networks are possible.
```
Class C gives us the most networks and smaller number of hosts per network.
Class A gives us v high # of hosts per network but only 126 networks. 
```
- Class D and E networks are untouchable (reserved).

![alt text](images/image-9.png)

### Missing IP Addresses
- Between class A and B, there are 16 million IP addresses.
- These are known as loop back addresses and are used in our devices.
- `ping` means are you alive and awake?
```
Loopback addresses are special IP addresses used by a computer to refer to itself. The most common loopback address is 127.0.0.1, which is used for testing and troubleshooting network configurations. It allows a device to send and receive data to itself without accessing the network, ensuring the network stack is functioning correctly.
```
Our computer has 16 million IP addresses ready to respond to itself.
```
ping 127.0.0.1 
ping 127.145.145.8
```

![alt text](images/image-10.png)
---
## Private IP Addresses
[Basics of IP Address & Subnetting Part III](https://www.youtube.com/watch?v=8bhvn9tQk8o&list=PLIhvC56v63IKrRHh3gvZZBAGvsvOhwrRF&index=3)

- In 1996 we were about to run out of IP addresses, but this was solved by `RFC1918` (Private IP addresses)
- Class A, B and C of IP addresses are now referred to as public IP addresses - meaning IP addresses which can be reached on the internet.
- The internet can be thought of as a big network
- So to connect to the internet we need a public IP address but it needs to be unique.
### Private IP addresses

![alt text](images/image-11.png)

- Most common private IP addresses home routers use is class C ip address range.
- Private IP adresses dont connect to you to the internet (they are not publically routable on the internet - cant talk to them from the internet)
- NAT is responsible for connecting to the internet. 
### NAT
- NAT (Network address translation) is performed by the router.
- NAT is responsible for translating private IP address to a public one when it leaves the router
- The router assigns private IP addresses (not unique and millions can have the same)
- The ISP (internet service provider) gives 1 public IP address to the router.
- So every device in the home network, when it accesses anything on the internet, their identity is the same public IP address
`google what is my ip?`

![alt text](images/image-12.png)

- But we still run out of IPv addresses, and to solve that we came up with `IPv6` addresses.

![alt text](images/image-13.png)

- Every device which exists can have a public IPv6 address and connect to the internet.
- All phones connected via cellular networks have `IPv6` address.

---
## Decimal to Binary Conversion of IP Addresses
[Basics of IP Address & Subnetting Part IV](https://www.youtube.com/watch?v=2-i5x8KCfII&list=PLIhvC56v63IKrRHh3gvZZBAGvsvOhwrRF&index=4)

- The computer interprets the IP addresses like the images/image below - its in binary (the language of the computer) 
- bits is the bottom.
- In the IP address there are 32 numbers (bits)  
- 8 bits make up 1 byte.

![alt text](images/image-14.png)

#### How big is an IP address in bits?
- 32 bits
- Each octet is 8 bits. oct means 8 which is why octets.
#### How big is an IP address in bytes?
- 32/8 = 4 bytes
#### Binary to Decimal
- All numbers are 2^n

![alt text](images/image-15.png)

#### Decimal to Binary
- For `172.16.34.3`, ans is `1 0 1 0 1 1 0 0`

![alt text](images/image-16.png)

---
## The Subnet Mask
[Basics of IP Address & Subnetting Part V](https://www.youtube.com/watch?v=oZGZRtaGyG8&list=PLIhvC56v63IKrRHh3gvZZBAGvsvOhwrRF&index=5)

- Every IP address has a subnet mask, and it tells us all the secrets of the network (some of them).

#### Converting the subnet mask into binary

![alt text](images/image-17.png)

The Subnet mask converted into binary:

![alt text](images/image-18.png)

- Network bits - are part of IP address that dont change, tell us on which network we are on.
- The 0s tell us which part of the IP address are host bits.
- 2^8 (8 0s in host) - number of possible hosts/ip addresses in this network. But 2 are reserved.
#### But what if we need more than 256 addresses in our network?
- We use Subnet masks

## What are Subnet Masks
Every IP address in the world has a subnet mask
The job of the subnet mask is to tell:
- Tell how big the network is. Can also tell if the octet is frozen or not.

![alt text](images/image-19.png)
- When subnet mask is 255, every bit is on. And adding all numbers = 255.
- Where we have all 1s those are network bits and where all 0s those are host bits
- Host bits also tell us how many possible hosts are there in the network
- 2^# of zeros = number of possible hosts. 2^8 = 256 possible hosts.
- If we need more than 256 IP addresses we need to add more 0s (more host bits) in our binary IP address. **This is Subnetting**
- Subnetting means changing the subnet mask to suit our needs.

![alt text](images/image-20.png)

- in subnet mask the numbers are contiguous, meaning the 1s will always be in a row.

![alt text](images/image-21.png)
---
## The Subnet Mask
[Basics of IP Address & Subnetting Part VI](https://www.youtube.com/watch?v=mJ_5qeqGOaI&list=PLIhvC56v63IKrRHh3gvZZBAGvsvOhwrRF&index=6)

#### Breaking a network into 4 networks
When we need more networks we need to hack the **network** bits. When we need more networks we need more 1s
- And when we need more hosts we need more 0s

#### We want to create 17 new networks
![alt text](images/image-22.png)

To create 17 networks we need 5 bits

![alt text](images/image-24.png)

**To create 4 new networks we need 4 bits**

![alt text](images/image-25.png)

So now we converted a single network to 4 networks
- Now to convert to decimal

![alt text](images/image-26.png)

the /26 part (CIDR notation) comes from the number of (ON) network bits. In this case we had 11111111.11111111.11111111.11000000 
If you count the number of ones (1) you will get 8+8+8+2 = 26.

---

- 2 computers are connected via switches
- The switch connects 2 computers by connecting to interfaces of hosts on each of the computers
- To see interfaces of the host - `iplink`

To view kernel IP routing rable:
```bash
route
```
- We assign all systems/computers with the 

![alt text](images/image-3.png)

### Assigning systems with ip addresses on the same network
```bash
ip addr add 192.168.1.0/24 dev eth0
ip addr add 192.168.1.11/24 dev eth0
```

Once the links are up and the ip addresses are assigned, the computers can now communicate with each other through the switch

```bash
ping 192.168.1.11
```

- The switch can only enable communication within a network, which means it can recieve packets from host on the network and deliver it to other systems within the same network.
- For communication of devices on other networks - **Routers** are used for this.

![alt text](images/image-30.png)

- Since the router connects 2 seperate networks, It gets 2 IPs assigned. One on each network.
- There is a gateway configured on the system, i.e. the network needs to know where the door is to go to the router.

```bash
route
```
- route command helps in seeing the existing routing configuration on the system - it displays the kernel's routing table.

#### Configuring a Gateway

- Below we are configuring the gateway (door) to be 192.168.1.1
```bash
ip route add 192.168.2.0/24 via 192.168.1.1
ip route add 192.168.1.0/24 via 192.168.2.1

# For any network we dont know a route to, use this router as the default gateway
ip route add default via 198.168.2.1
# This way any request to any network outside of the existing network goes through this particular router
```

# DNS
![alt text](images/image-31.png)

Telling system A that when I say db, i mean IP 192.168.1.11
```bash
sudo nano /etc/hosts
#or
cat >> /etc/hosts
192.168.1.11 db
```
Whatever we put in the etc host file is the source of truth for host A.

### DNS Server
All hosts are pointed to lookup that server if they need to resolve a host name to an IP address istead of of its own.
- Every host has a DNS resolution configuration file at `/etc/resolv.conf`

#### Priority Order:

- `/etc/hosts file:` The system first checks the /etc/hosts file for any matching hostname. If a match is found, it uses the IP address specified in this file.
- `DNS server:` If the hostname is not found in /etc/hosts, the system then queries the DNS server to resolve the IP address.

Which of the following command is used to query a hostname from a DNS server? - `nslookup`