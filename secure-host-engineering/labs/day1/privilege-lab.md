# Privilege Lab Report

## 1. Permission
Permissions control what users can do with files.
Types: **Read (r)**, **Write (w)**, **Execute (x)**.

**Proof:**
$ echo "test" > normal.txt
$ ls -l normal.txt
-rw-r--r-- 1 imene imene 5 Sep 29 23:17 normal.txt

The owner (imene) can read and write. Others can only read.

## 2. Ownership
Every file has an **Owner** and a **Group**.

**Proof:**
From `ls -l normal.txt`:
- Owner: imene
- Group: imene

## 3. User
The user is the account that owns the file.

**Proof:**
$ whoami
imene

## 4. Group
A group is a collection of users with the same permissions.

**Proof:**
$ groups
imene adm cdrom sudo dip plugdev lpadmin sambashare

## 5. SUID (Set User ID)
SUID lets a user run a file with the owner's permissions (usually root).

**Proof:**
$ find /usr/bin /usr/sbin -perm -4000 -type f 2>/dev/null
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/su

## 6. SGID (Set Group ID)
SGID is like SUID but for groups. On folders, new files get the folder's group.

**Proof:**
$ find /usr/bin /usr/sbin -perm -2000 -type f 2>/dev/null
/usr/bin/wall
/usr/bin/ssh-agent

## 7. sudo
`sudo` lets a normal user run commands as root.

**Proof:**
$ sudo -l
User imene may run the following commands on imene-Aspire-A515-54:
    (ALL : ALL) ALL
This means user `imene` can run any command as root.


## 8. Privilege
Privilege is the level of access a user has.
- Normal user = limited access.
- Root user = full access.

**Proof:**
$ id
uid=1000(imene) gid=1000(imene) groups=1000(imene),4(adm),27(sudo)...
Having `sudo` in groups means this user can get root access.

## Conclusion
In this lab, we learned how Linux controls access using permissions, ownership, users, groups, and special bits like SUID/SGID. We also learned how `sudo` allows temporary privilege escalation. All evidence is saved in the `proof/` folder.
