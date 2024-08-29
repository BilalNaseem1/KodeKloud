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
![alt text](image-5.png)

## How did the device get its IP Address
- Whenever a device connects to a router (Opera), the router gives it an IP Address
- Each of the numbers below can be between 0 and 255


![alt text](image-6.png)

- Mostly ip addresses start with `192.168.1.***`
- The way that opera tells us that each IP address is going to start with `192.168.1.***` is through a `Subnet Mask` 
- Purpose of subnet mask is to tell what IP's in our network start with.
- Each of the 4 numbers which are seperated by decimals are called octets.
- If the octet of the subnet mask is 255, then the corresponding octet of the IP address will remain the same in the same network 
- So in the below image `192.168.1` will always remain the same. These 3 numbers are known as the network portion of the IP Address.
- 0 in the subnet mask means the corresponding octet in the IP address can be any number it wants. This number is known as the Host portion of the IP Address. So for the below image a total of `256 - 3 = 253` IP Addresses are possible.
- `192.168.1.0` is known as the network address. `192.168.1.255` is the broadcast address (it contacts with everyone). These 2 and the Router IP are reserved and cannot be used.

![alt text](image-7.png)

![alt text](image-8.png)

- The network portion remains the same because other devices are in the same neighbourhood. Network portion is the neighbourhood name, and host part is the house address.
- If an IP is in a different neighbourhood (different network portion) - for ex. accessing netflix.com , then the router (default gateway) will be used for this.
- So every device looks at `IP Address -> Subet Mask`. If the IP is not in the network, it contacts default gateway
So when we have devices in a network, they all are known as hosts in the network (only have different hosts in the network)

---
[Basics of IP Address & Subnetting Part II](https://www.youtube.com/watch?v=tcae4TSSMo8&list=PLIhvC56v63IKrRHh3gvZZBAGvsvOhwrRF&index=2)

- There are 4.3 Billion (`0-255 . 0-255 . 0-255 . 0-255  ~= 2^32`) possible IP Addresses, and all of them are run out. 

![alt text](image-9.png)
---
- 2 computers are connected via switches
- The switch connects 2 computers by connecting to interfaces of hosts on each of the computers
- To see interfaces of the host - `iplink`
- We assign all systems/computers with the 

![alt text](image-3.png)
# DNS