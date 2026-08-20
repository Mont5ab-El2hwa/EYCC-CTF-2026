# Infected

## Description

A sophisticated APT group known as 0n3Sh0t has been operating a custom infostealer dubbed Shad0wEXF (Shadow Exfiltration) across the MENA region, targeting finance, banking, software, retail, and healthcare sectors. Intelligence indicates they recently compromised GAB — Gulf Arab Bank, one of the region's most prestigious financial institutions. The SOC team at GAB discovered anomalous outbound traffic from an internal workstation sending HTTP POST requests to an unfamiliar external IP address. Investigation revealed the workstation was exfiltrating company databases to a remote Command-and-Control server hosted on AWS infrastructure. You have been provided with a network traffic capture from the GAB corporate network. The company operates across three internal department VLANs: 10.16.0.0/24 (Engineering), 10.32.0.0/24 (Finance), and 10.85.0.0/16 (General Staff). One workstation has been compromised and is exfiltrating data to an external malicious server. Upon examining the C2 server, a misconfigured nginx instance with directory listing enabled exposed the attacker's operational infrastructure: uploaded databases, encrypted operational logs, and email correspondence — all pointing to a darknet marketplace called GraveMirror, operated by a threat actor known as shayblaban, where stolen data is auctioned to buyers. Your mission: trace the exfiltration path in the capture, investigate the C2, crack the attacker's archives, locate the marketplace, and recover critical intelligence about the highest-value individual in the leaked GAB dataset.

- **Flag Format:** `EYCC{1st_2nd_3rd_4th_5th_6th}`

## Objectives & Flag Parts

- **1st Flag Part:** The internal IP address of the compromised workstation that is exfiltrating data to the C2 server.
- **2nd Flag Part:** The external IP address of the malicious C2 server receiving the exfiltrated databases.
- **3rd Flag Part:** The password used to encrypt the operational logs archive found on the C2 server.
- **4th Flag Part:** The Bitcoin wallet address belonging to the threat actor shayblaban, used for receiving marketplace commissions.
- **5th Flag Part:** The ISO 3166-1 alpha-2 country code of the wealthiest individual found in the GAB data leak.
- **6th Flag Part:** The phone number (including country code) of the same wealthiest individual from the GAB leak.

## Files

- [Infected.pcapng](files/Infected.pcapng)
