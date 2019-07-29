# SSH config

Located in `~/.ssh/config`. Insert proper paths to privatet key files.

```
ServerAliveInterval 60
ServerAliveCountMax 120

Host *
	ControlMaster auto
	ControlPath ~/.ssh/%C
	Compression yes
	VisualHostKey yes
	HashKnownHosts yes
	IdentityFile ~/.ssh/id_ed25519_<something>

Host github.com
	User git
	IdentityFile ~/.ssh/id_ed25519_<something>
	VerifyHostKeyDNS yes
```
