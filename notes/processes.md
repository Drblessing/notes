# Processes

A process is an instance of a computer program that is being executed. A process can be a software program, a script, or a OS service. A process is started when a program is executed. A prcoess may be made up of multiple threads of execution that execute instructions concurrently.

Every process has its own address space, which is the memory that the process can use. A process cannot directly access the memory of another process. This isolation ensures that one process cannot alter the execution of another process. However, processes can communicate with each other through various inter-process communication mechanisms, like pipes, shared memory, files, sockets, etc.

Processes have various states like "new", "ready", "running", "waiting", "terminated" etc., and move from one state to another based on CPU scheduling and events such as IO or system calls. The operating system keeps track of all the processes in a data structure called the process table, which includes information such as process ID, process state, memory address space, among other things.

In summary, processes are the fundamental entities in an operating system that execute programs, and their management is key to the functioning of any modern computer system.

## Viewing Processes

On MacOS and Linux, Unix-based systems, you can use several commands to view the currently running processes.

1. **ps**: This is a basic command to report process status. By default, it only shows the processes in the current terminal session. For a comprehensive list, use `ps aux`, where:

- `a` lists processes from all users
- `u` displays the process's user/owner
- `x` lists processes not attached to a terminal

```bash
ps aux
```

2. **top**: This is an interactive command that displays the processes in a table format. It is useful for monitoring the system in real time:

```bash
top
```

3. **htop**: An improved version of `top` installable with homebrew. It is more user-friendly and has more features than `top`:

```bash
brew install htop
htop
```

4. **Activity Monitor**: A built-in MacOS program that lists processes in the CPU tab. You can also see how many threads a process has, and the CPU and memory usage of each process.

## Process Control

You can control processes using the following commands:

1. **kill**: This command sends a signal to a process. By default, it sends the `TERM` signal, which terminates the process.

```bash
kill <pid>
```

2. **killall**: This command sends a signal to all processes with the given name. Name refers to the COMMAND column in the output of `ps aux`, or the command executed to start the process.

```bash
killall <name>
```

For instance, to kill all Python processes, you can use:

```bash
killall python
```

To first see all processes with a given name, you can use:

```bash
ps aux | grep <name>
```

3. **lsof**: This command lists all open files and the processes that opened them. It is useful for finding out which process is using a file, or for finding out which process is using a port. The -i option lists all network connections.

```bash
lsof -i :8000
```

These commands can be used for example, to find a rogue process on port 8000, then kill it:

```bash
lsof -i :8000
kill <pid>
```
