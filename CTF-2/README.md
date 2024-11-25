# CTF Problem Dev 2

## Problem Idea

After I created the first Crypto CTF problem, I wanted to create
another Crypto CTF problem, but this time with a solve that was more 
difficult to execute. So I created a problem that was conceptually
similar, but required more effort to retrieve the flag.

This time, I decided on making a problem involving the CFB block
cipher mode. The idea of the problem is the same: users are able to
receive an encrypted key, and can also provide plaintext that will
be encrypted and returned as ciphertext. Given this functionality,
they must retrieve the flag.

## Solution Approach

To solve this, one needs to know what CFB is and how it works. CFB
is a block cipher mode that uses an initialization vector and a key,
and creates a bitstream. Notably, the bitstream is also dependent on
the plaintext that is being encrypted. CFB is vulnerable when reusing
the same IV. This is because in CFB, encrypting and decrypting are
extremely similar processes, and if the same IV is used, this results
in a two-time pad. By using the received ciphertext, an attacker can
carefully reconstruct the plaintext one segment at a time.

To get the flag, the attacker must first receive the encrypted flag.
They can then use this encrypted flag to recover the flag one byte
at a time (since the default segment size for CFB is 1 byte). To do
this, the attacker must create a two-time pad for each of the bytes.

To recover byte i of the flag, the attacker must already know bytes
1 to i-1 of the flag. This is necessary so that the cipher's bitstream
will become a two-time pad. In such a case, if the attacker encrypts
a chosen plaintext that consists of bytes 1 to i-1 of the flag followed
by byte i of the encrypted flag, byte i of the resulting ciphertext
will be byte i of the flag.

Therefore, the attacker should perform an iterative process to get
all of the bytes of the flag, starting from byte 1. The only reason
byte 1 can be recovered is because the IV was reused, resulting in a
two-time pad.
