# Backups

Well now, partner, let's chew the fat 'bout why backups are as important as a trusty steed in the Wild West. Y'see, in this vast, untamed frontier of data and information, things can go south quicker than a rattlesnake on a hot griddle. One minute, your precious files, just like gold nuggets, are safe in your digital satchel, and the next, they're gone – done in by a rogue virus, a clumsy mistake, or a dastardly hardware failure. And once they're gone, well, they might as well have been blown away by a dust storm. That's why you've gotta keep a sharp eye out and make copies of your files, storing 'em in different locations – like hiding your gold in various secret spots. So, in case of a calamity, you ain't left high and dry. Backups, my friend, are your insurance in this unpredictable Wild West of technology. So, always remember to backup your data, or it might vanish into the sunset just when you need it most.

## Backup Strategies

### 3-2-1 Backup Strategy

Alrighty then, saddle up and let's dive into this 3-2-1 strategy.

**Three Copies:** First off, you need to have three copies of your data. That's right, not one, not two, but three. Think of it like this: one is your working horse, the one you ride every day. The second is a spare, in case the first one goes lame. And the third? Well, that's your prized stallion, kept safe in the barn for emergencies.

**Two Different Formats:** Now, you wouldn't want all your horses to be exactly the same, right? If they all caught the same sickness, you'd be afoot. It's the same with your data. Have it stored in two different formats – maybe one on your computer, another on an external hard drive or the cloud. That way, if one format fails, you've still got a fallback.

**One Off-Site Backup:** Lastly, you gotta keep one backup away from your main ranch. Why, you ask? Well, think about it. If a tornado sweeps through and takes your whole setup with it, it doesn't matter how many copies you had if they were all in the same place. Keep one backup in a completely different location – a relative's house, a safety deposit box, or a secure cloud service. That way, even if disaster strikes, you'll still have a copy of your precious data safe and sound.

So there you have it, the 3-2-1 backup strategy. Three copies, two different formats, and one off-site backup. Stick to this and your data will be as safe as a bank vault in the wild, wild west.

![3-2-1 backup](https://www.handybackup.net/images/features/3-2-1-backup-rule.png)

## Locations

### Local

3 usb-c drives

[Amazon link](https://www.amazon.com/dp/B09WB2NL8W/)<br>
Price = $25.99<br>
Total Price = $77.97<br>

Stored in a [fireproof safe](https://www.amazon.com/Yuanshikj-Electronic-Security-Fireproof-Business/dp/B078MYJYD5/) in a [fireproof bag](https://www.amazon.com/ROLOWAY-Fireproof-inches-Non-Itchy-Valuables/dp/B07WVC24BP/).

### Cloud

[iCloud Drive](https://www.icloud.com/storage/)<br>
200GB = $2.99/month<br>
Total Price = $35.88/year

## Format

### Directory Structure

Storing the backups in a clean directory format is key. I like storing them in a parent folder containing the name, then split it into date afterwards. Also, including the hash is a fun addition to verify data integrity. I keep hashes stored at the bottom of this page.

```
Backups/
    iCloud/
        2023-01-01/
            iCloud_2023-01-01.tgz
            iCloud_2023-01-01.keccak256
    ....


```

## Testing Backups

Now listen here, partner, and listen good. When it comes to your precious data, it ain't enough just to stash it away like hidden treasure. Nah, you gotta go a step further and make sure you can find it when the going gets tough, and that it ain't turned to dust when you do. That's where testing your backups and recovery process comes in, see?

Think of it like this – you wouldn't bury your gold without marking the spot and checking now and then to make sure it's still there, would ya? Same goes for your data. Regularly dig up those backups and restore 'em to see if everything's still in one piece. If you're doing it right, it'll be like opening a chest of gleaming gold nuggets, each one just as shiny and valuable as when you first laid eyes on 'em.

How often, you ask? Well, that depends on how fast your gold mine is filling up. If you're adding to your stash every day, you'd best be checking every week. If your stash grows more slowly, maybe you can afford to wait a month between checks. But mark my words, don't let a season pass without making sure your treasure is safe and sound. Because out here in the wild, wild west of data, the only thing certain is uncertainty, and the only protection against that is vigilance and regular testing.

## Hashes

Check the hash of the archive, as well as the diff between original with:

```bash
diff -r /path/to/original/directory /path/to/extracted/directory
```

In no particular order or reason: <br>
43b033e6f296f6363620aedcb6e065e99f106b7a35030c96f342ce7ce9a61fca
