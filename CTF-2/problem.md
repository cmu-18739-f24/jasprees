# CTF-2

- Namespace: jasprees
- ID: CTF-2
- Type: custom
- Category: Crypto

## Description

Can you find the flag?

## Details

Connect to the program with netcat:

`$ nc {{server}} {{port}}`

The program's source code can be downloaded {{url_for("challenge.py", "here")}}.

## Hints

- What is CFB mode?
- What is "segment size"?

## Challenge Options

```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Attributes

- author: Jaspreet Singh
