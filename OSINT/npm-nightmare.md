# NPM NIGHTMARE

## Description

A few months ago, one of the world's most popular JavaScript libraries became the victim of a sophisticated software supply chain attack.

The affected package was downloaded over **100 million times every week** through the npm ecosystem and was trusted by developers, companies, universities, and countless open-source projects. Instead of attacking users directly, the attackers compromised the software supply chain itself by publishing malicious package updates that silently delivered malware to anyone who installed the affected versions.

The malicious releases remained available long enough to place thousands of systems at risk before they were discovered and removed. During the investigation, security researchers uncovered malicious dependencies, attacker-controlled infrastructure, command-and-control servers, multiple malware families, and evidence linking the operation to a much larger campaign.

Your task is to retrace the investigation using only publicly available information.

You will begin with the original software supply chain attack and gradually follow the evidence into a second investigation involving the same threat group. Along the way, you will examine public incident reports, malware analysis blogs, infrastructure records, and other OSINT sources to recover seven pieces of information.

Each part of this challenge represents one stage of the investigation. Every answer you recover becomes one component of the final flag.

---

## Part 1 — Following the First Clue

Every supply chain attack leaves traces behind.

The compromised package communicated with an attacker-controlled domain as part of its malicious activity. Your first objective is to identify the **registration email address** associated with that domain.

**Flag format**

```text
{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxxx@xxxxxxxxxxxxxxxxxx.xxx}
```

---

## Part 2 — Following the Threat Group

The investigation into the supply chain attack eventually led researchers to attribute the operation to a specific North Korean threat group.

Later research describing the same group introduced two custom data-stealing tools used during a separate (CryptoCurrency & AI Deep fake Social Engineering) campaign.

Identify **the first** of these two tools.

**Flag format**

```text
{XXXXXXXXXX}
```

---

## Part 3 — Breaking the Operating System's Defenses

The first data-stealing tool avoids requesting user permissions through normal operating system prompts.

Instead, it modifies one protected permissions database before extracting credentials from another database.

Recover both database names.

**Flag format**

```text
{PermissionDatabase:CredentialDatabase}

{XXX.xx:xxxxx.xxxxxxxx-xx}
```

---

## Part 4 — A Second Data Stealer

Researchers also documented another custom tool deployed during the same campaign.

Unlike the previous tool, this one focuses on Chromium-based browsers and quietly collects sensitive browser information.

Recover the name assigned to this second tool.

**Flag format**

```text
{XXXXXXXXXX}
```

---

## Part 5 — Browser Persistence

To survive reboots, the browser-focused malware installs itself in a location used by Chromium browsers and registers a trusted browser extension to communicate with it.

Recover:

* the **exact installation path** (including every space),
* the browser extension origin allowed to communicate with it.

**Important:** Copy the installation path exactly as it appears in the report.

**Flag format**

```text
{ExactInstallationPath:chrome-extension://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/}

{%XXXX%/Xxxxxxx/Xxxxxxxxxxx Xxxxxxx/Xxxxxx/Xxxxxx/XxxxxxXxxxxxxxxXxxxx/Xxxxxx Xxxxxx Xxxx:chrome-extension://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/}
```

---

## Part 6 — Temporary Staging

Before sending stolen information to its remote server, the malware stores the collected data using several predefined filename patterns.

Recover:

* the screenshot filename pattern,
* the keylogging filename pattern,
* the upload server,
* the creation date of the upload server's domain.

**Flag format**

```text
{ScreenshotPattern:KeyloggingPattern:UploadServer:YYYY-MM-DD}

{XXXXXXXXxxxxxx.dat:XXXXXXXXxxxxxx.dat:xxxxxxx[.]xxx:NN/xxxxxx:YYYY-MM-DD}
```

---

## Part 7 — The Initial Downloader

Finally, researchers identified another C++ program associated with the same threat group.

Its purpose was to contact remote infrastructure, download additional malware, and execute it on compromised systems.

Recover the two command-and-control servers used by this downloader.

**Flag format**

```text
{domain[.]tld:port_domain[.]tld:port}

{xxxxxxxxxx[.]xxx:NNN_xxxxxxxx[.]xxx:NNN}
```

---

# Final Flag

After collecting all seven flag components, visit the CyberChef recipe below:

**<https://gchq.github.io/CyberChef/#recipe=HMAC(%7B'option':'Hex','string':'0x2face'%7D,'Whirlpool-T')&input=e3h4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4Lnh4eHh4eHhAeHh4eHh4eHh4eHh4eHh4eHh4Lnh4eH0Ke1hYWFhYWFhYWFh9CntYWFgueHg6eHh4eHgueHh4eHh4eHgteHh9CntYWFhYWFhYWFhYfQp7JVhYWFglL1h4eHh4eHgvWHh4eHh4eHh4eHggWHh4eHh4eC9YeHh4eHgvWHh4eHh4L1h4eHh4eFh4eHh4eHh4eFh4eHh4L1h4eHh4eCBYeHh4eHggWHh4eDpjaHJvbWUtZXh0ZW5zaW9uOi8veHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHgvfQp7WFhYWFhYWFh4eHh4eHguZGF0OlhYWFhYWFhYeHh4eHh4LmRhdDp4eHh4eHh4Wy5deHh4Ok5OL3h4eHh4eDpZWVlZLU1NLUREfQp7eHh4eHh4eHh4eFsuXXh4eDpOTk5feHh4eHh4eHhbLl14eHg6Tk5OfQ>**

Replace each placeholder with the value you recovered during your investigation.

If every value is correct, the recipe will generate a hexadecimal digest.

Submit the final flag as:

```text
EYCC{generated_hash}
```

Good luck, and enjoy uncovering the story behind one of the most significant npm supply chain compromises in recent years.

Some notes from 0x2face white face :

1st note : you are lucky i have whiteface :)

2nd note : reread 1st note again so you dont forget.

3rd note : flag is case sensitive , the x and X means lower & uppercase , also the final flag should be EYCC{9f19xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx5d4a} , also the NN is the exact port number from the report. , for dates flag parts , the DD or MM , if it is single number like 6 or 7 , you will use 06 , 07 , so it will be 0X where x is the day or month if it is single.

good luck and happy investigation guys <3 .
