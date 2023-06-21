# System Commands

## Terminal

1. Page through output

```bash
ls -l | less
```

2. Search through output

```bash
ls -l | grep "file"
```

3. Open file in VSCode

```bash
code .
```

Use nano file.txt to open in nano.

4. Piping commands

```bash
ls -l | grep "file" | less
```

Pipes the output of one command to the input of another.

5. Redirecting output

```bash
ls -l > file.txt
```

Redirects the output of a command to a file. Use >> to append to a file.

6. Viewing the start and end of a file

```bash
head file  # Shows the first 10 lines of file
tail file  # Shows the last 10 lines of file
```

7. Counting lines, words, and characters

```bash
wc file
```

8. Finding files

```bash
find . -name "file.txt"
```

Find files by name in a directory and its subdirectories:

```bash
find /path/to/directory -name "example.txt"
```

Find files by extension:

```bash
find /path/to/directory -name "*.jpg"
```

Find files by size:
(can use -type f to find files, -type d to find directories)

```bash
find /path/to/directory -size +100M
```

Find directories:

```bash
find /path/to/directory -type d -name"example_directory"
```

9. Archiving and compressing

Tape Archive (tar) is a computer software utility for UNIX and Linux systems that creates tar archives. The name is derived from (t)ape (ar)chive, as it was originally developed to write data to sequential I/O devices with no file system of their own.

Archiving is the process of collecting multiple files and directories into a single file. This single file is called a "tarball". The tarball can be compressed or uncompressed, and has the file extension ".tar". The single tar file is portable and can be moved around your file system, shared with others, backed up to an external device, or even sent over the network. It maintains the directory structure and file permissions of the original files, which makes it ideal for backups or transferring data between systems.

Compression is an optional feature, and is a process that reduces the size of files. It's not automatic when using tar, but you can add compression to a tar archive with options like -z (gzip), -j (bzip2), or -J (xz). The compressed tar file will have the file extension ".tar.gz", ".tar.bz2", or ".tar.xz" respectively.

Can use the -a flag to automatically detect the compression type based on the file extension.

File extensions:
.tar - uncompressed tar archive
.tar.gz - compressed tar archive
.tgz - alias for .tar.gz
.gz - compressed file
.bz2 - better compressed tar archive
.xz - best compressed tar archive
.zip - windows compressed file

```bash
tar -cvf archive.tar file1 file2  # Create archive
tar -xvf archive.tar  # Extract archive
tar -zcvf archive.tar.gz file1 file2  # Create compressed archive
tar -zxvf archive.tar.gz  # Extract compressed archive
```

10. Checking disk usage

```bash
du -sh directory  # Shows the total size of directory
df -h  # Shows the disk usage and availability on your system
```

11. Findng text in files

```bash
grep -r "text" directory
```

12. Create a file

```bash
touch file.txt
```

13. Create a directory

```bash
mkdir directory
```

14. Help for a command

```bash
man command
```

15. Hashing a file

md5:
(must be a file, not a directory)

```bash
md5 file
```

sha1: (must be a file)

```bash
shasum file
```

sha256: (must be a file)

```bash
shasum -a 256 file
```

keccak256: (must be a file)

First, install sha3sum.

https://formulae.brew.sh/formula/sha3sum#default

```bash
brew install sha3sum
keccak-256sum file
```

Hash an ethereum transaction, first get the raw tx hash from etherscan. Then, convert the hex string to binary and hash it. See if it matches the tx hash from etherscan. You can also save the hex data into a txt file and hash it with the -x flag to match etherscan txn hash.

```bash
echo "hex_string" | xxd -r -p | keccak-256sum
```

sha3-256: (must be a file)

```bash
sha3-256sum file
```

16. Moving and copying files

```bash
mv -i file.txt directory  # Move file to directory
mv -i file.txt new_file.txt  # Rename file
cp file.txt directory  # Copy file to directory
cp -r directory new_directory  # Copy directory to new directory
```

17. List files

-l flag shows the modification time
-r flag reverses the order
-t flag sorts by modification time

```bash
ls -ltr
```

For size:

```bash
du -sh *
du -sh * | sort -h
```

## Hardware

### Ram

1. Get total ram

```bash
free -h
```

On a mac:

```
top -l 1 | grep PhysMem
```

Available Memory = Physical Memory - Memory Used

2. Get ram speed

```bash
sudo apt-get install dmidecode
sudo dmidecode -t memory
```

## Networking

1. Get local IP address

```bash
curl ifconfig.me
```

2. Current logged in user

```bash
whoami
```

3. Ping a server

```base
ping 1.1.1.1
```

4. Send DNS query

```bash
nslookup cloudfare.com
```
