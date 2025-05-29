
# Configure SSH Public Key Authentication on Cisco IOS

[Configure SSH on Routers and Switches](https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html)


[Using SSH public key authentication with Cisco](https://nsrc.org/workshops/2016/renu-nsrc-cns/raw-attachment/wiki/Agenda/Using-SSH-public-key-authentication-with-Cisco.htm)


#### Ensure router key gen is at least 2048 bit
`crypto key gen rsa mod 2048`

#### Wrap the key onto multiple lines
`fold -b -w 72 ~/.ssh/id_rsa.pub`

#### Add public key on the router

```
conf t
ip ssh pubkey-chain
username <username>
key-string
<< paste your multi-line public key here >>
exit
```

#### Verify
Cisco IOS uses MD5 for ssh key fingerprints

`show run | beg pubkey`
You should see a response like this:

```
r1#sh run | beg pubkey
ip ssh pubkey-chain
 username admin
  key-hash ssh-rsa 977D84C335D3C2A1114DDA07368A16CC
```

Compare against fingerprint from the original public key:
```
[rhel@Ridge ~]$ ssh-keygen -l -E MD5 -f ~/.ssh/id_rsa.pub
3072 MD5:97:7d:84:c3:35:d3:c2:a1:11:4d:da:07:36:8a:16:cc rhel@Ridge (RSA)
```

#### Optionally
Remove password

`username admin privilege 15`


Disable Password Authentication for SSH:

```
no ip ssh server authenticate user password
no ip ssh server authenticate user keyboard
```