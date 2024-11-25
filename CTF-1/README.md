# CTF Problem Dev 1

## Problem Idea

I wanted to create a Crypto CTF problem that addressed concepts we
learned about in class, but were not directly implemented in homework
problems. Therefore, I decided on making a problem involving the OFB
block cipher mode. The idea of the problem is that users are able to
receive an encrypted key, and can also provide plaintext that will be
encrypted and returned as ciphertext. Given this functionality, they
must retrieve the flag.

## Solution Approach

First, one needs to know what OFB is and how it works. OFB is a block
cipher mode that uses an initialization vector and a key to create a
bistream. This bitstream is then XOR'd with the plaintext to create the
ciphertext. OFB is vulnerable when reusing the same IV, since then the
bistream that is created only depends on the key and the IV. This is
effectively a two-time pad if the attacker is able to provide plaintexts
to be encrypted.

To get the flag, the attacker must first receive the encrypted flag,
and then provide a plaintext of sufficient length to be encrypted. 
Then, the attacker can XOR the ciphertext and the encrypted flag, and
since this is a two-time pad, the result will be the same as the XOR
of the flag and the plaintext they provided. So, the attacker can then
XOR the result with the plaintext they provided to get the flag.

