# Special Directories

Well, well, well, partner! In this here wild frontier of code 'n' commands, we got some special watering holes, or as you might call 'em in these parts, "directories". They're the places where we stash our temporary files, log records, 'n' all sorts o' system files. Heck, we even got spots to hold onto configuration files for the whole dang system and for each and every cowpoke on their own.

## /dev/null

Ya ever find yerself with a bucket full o' something you ain't got no use for? Well, /dev/null is like the tumbleweed-strewn pit we chuck unwanted data into. Let's say you don't want none o' the output from the ls command to be seen:

```bash
ls > /dev/null
```

Anything you send off to the /dev/null directory gets swallowed up like a rattler in a sandstorm. We often use this here place to discard the noise from commands we got runnin' off in the wild. Now, don't ya go thinkin' you can get anything back from the /dev/null pit, no siree!

## /tmp

Next up, we got the /tmp directory, a kinda storage shed for our temporary goods. When the system's busy workin', this is where it puts the files it whips up. Here's how you'd create a temporary file in the /tmp shed:

```bash
touch /tmp/foo
```

These temporary goods usually get cleared out when the town gets a good cleanin' (a system reboot). Though, some towns got themselves a schedule, a cron job, to sweep out the /tmp shed every hour.

```bash
echo $TMPDIR
```

You can create tmp files and directories with the `mktemp` command.

## /bin

The /bin directory, now, that's like the town's toolshed. It's chock-full of the necessary tools (programs) that we gotta have handy when we're settin' up camp (booting the system). This here place has all the essential tools needed to give commands durin' the boot up process, when settin' up the system, and patchin' it up in single-user mode. We got all kinds of handy things here like cat, ls, cp, mv, rm, ps, sed, grep, and awk.

## $PATH

The $PATH, y'see, is like a map that tells your shell where it can find the tools it needs. It's a system variable that points to all the directories where executable files and commands might be hidin'. Whenever ya type a command into the terminal, the shell uses this here $PATH to figure out where that command's executable file might be.

So, if you run a command, let's say ls, your shell will mosey on through all the directories listed in your $PATH until it finds the ls command. It starts at the beginning of the $PATH and keeps on searchin' 'til it finds what it's lookin' for or runs out of places to look.

You can see what's in your $PATH by typing echo $PATH into your terminal.

```bash
echo $PATH
```

It will output a list of directories, separated by colons. The shell will search these directories, in order, whenever you run a command.

Now, if you add a new program and you want your shell to know where to find it, you'd add the directory containing the program to your $PATH. Be careful when you're changing the $PATH, though. If you don't set it up right, you might end up with a mess of confusion.

## .zshrc

Well now, let's mosey on over to the subject of .zshrc. If you're a cowpoke usin' the Z shell, or zsh as its kin call it, you ought to get familiar with this here .zshrc.

The .zshrc file is like your personal guidebook or trail map for how the zsh shell should behave. It's a plain ol' text file, usually located in the root of your home directory (~/.zshrc), and it gets read every time you start up a new interactive shell session.

It's in this here guidebook that you can specify your own aliases, functions, shell options, and environment variables, such as modifying that ol' $PATH we were jawing about earlier.

```bash
code .zshrc
```

```bash
echo 'export PATH=$PATH:/path/to/your/new/tool' >> ~/.zshrc
```

.zprofile and .zshenv are similar. For bash systems they replace z with b.

## ~

Finally, we got this little symbol here, ~, which stands for the homestead of the current user, or as we say in computer-speak, "the home directory". If ya wanna head back to your own personal cabin from anywhere in the system, just use this command:

```bash
cd ~
```

```bash
echo ~
```

## /etc

This here's the /etc directory, it's like the town hall of your system, housing all the system-wide configuration files. If a program runs on the system level, its config files are likely to be found here.

## /var

This here's the /var directory. It's like the town's post office, holding onto mail and system logs, and even printer jobs. Anything that tends to change or hold onto data between boots can be found here.

Well, that about covers it, partner! Those are some of the special directories in this here vast wilderness of Unix-like systems. Happy trails!
