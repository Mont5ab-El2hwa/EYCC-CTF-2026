# Infected Revenge

## Description

> ☠️ **Safety Warning:** This challenge involves a real C2 server and a real BTX miner. The files related to it are actual malware — do not run anything. Everything here is meant for static review only. You can visit the C2 with normal HTTP requests; just never execute what it serves.  
> **Link:** [Gofile](https://gofile.io/d/J2VI5Pfk)

Aurelia Systems, a mid-sized industrial-tech company, found suspicious outbound traffic during a routine audit. On 11 July 2026, an engineer in the Engineering VLAN clicked a link in what looked like an internal IT notice. It silently redirected through redacted.com to a remote server, which dropped a chain of scripts that installed a BitcoinTX miner. No alerts fired. The attached capture covers the full incident timeline.

`infected.pcap` is the company network capture from the incident. It contains only internal traffic: multiple VLANs (office, engineering, data center, CCTV, guest, IoT and more), plus some VPN and DMZ traffic. Nothing external is inside the capture, except the infected device with the requests to the C2 server.

- **Flag Format:** `EYCC{part1_part2_part3_part4_part5_part6}`

## Flag Parts

- **Part 1 — The Key:** the XOR key used to deobfuscate the C2 server's payload
- **Part 2 — The Wallet:** the BTX address used by the miner
- **Part 3 — First Payment:** the txid of that BTX address's first payout
- **Part 4 — The Operator:** the email that links the miner creator to the infrastructure
- **Part 5 — The Phone number:** the registrant phone of the mining pool domain

## Files

- [Infected-Revenge.pcap](files/Infected-Revenge.pcap)
