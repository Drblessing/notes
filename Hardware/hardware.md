# Hardware Guide

## [PCIe](https://en.wikipedia.org/wiki/PCI_Express) - Peripheral Component Interconnect Express

The PCI Express (PCIe) interface, an expansion bus on a computer's motherboard, has become the de facto standard for connecting a wide range of peripherals to computers. These peripherals include GPUs, sound cards, SSDs, as well as Wi-Fi and Ethernet adapters.

As of this writing, the most recent commercially available version is PCIe 5.0, with 63 GB/s speed. It should be noted that while there are newer versions in development or in the early stages of deployment, these are not yet broadly available in consumer devices.

The standard works with simulatneous duplex lanes, up to x16. Note that physical lanes may be x16 but only support x4 electronically to allow x16 devices to connect.

![PCI Express x4, PCI Express x16, PCI Express x1, PCI Express x16](https://upload.wikimedia.org/wikipedia/commons/3/3e/PCI-E_%26_PCI_slots_on_DFI_LanParty_nF4_SLI-DR_20050531.jpg)

PCI Express x4, PCI Express x16, PCI Express x1, PCI Express x16

![x16 physical lanes with only 4 electronic lanes. ](https://upload.wikimedia.org/wikipedia/commons/3/3a/PCie_lanes.jpg)

x16 physical lanes with only 4 electronic lanes.

GPUs have gotten so big they exceed the standard in size, lol.

Many modern Solid State Drives (SSDs) utilize the M.2 form factor and leverage the NVMe protocol for their operation. These drives typically connect via PCIe and often utilize x4 lanes, balancing performance and cost.

## [M.2](https://en.wikipedia.org/wiki/M.2)

M.2 is a form factor specification that defines the physical aspects of the device, mostly SSDs, like its shape and the types of connectors it uses.

M.2 sockets are physical connectors on a computer’s motherboard that accept M.2 form factor devices. Most commonly used for SSDs, that can accept PCIe, or SATA interfaces.

There are different types of M.2 sockets, known as “keys,” each designed for specific functionality.

The most common types of keys are B and M. B-key is used for SATA SSDs or PCIe x2 SSDs, and M-key is used for PCIe x4 SSDs, each providing different levels of performance.

M.2 is important because it defines a slim form factor, and can accomodate PCIe, SATA, and USB. Note that the physical form factors of M.2 and standard PCIe slots are different. An M.2 NVMe SSD cannot fit into a standard PCIe slot due to these differences.

![Untitled](https://upload.wikimedia.org/wikipedia/commons/c/c2/M.2_connector_on_a_computer_motherboard.jpg)

[M2 Ars Technica Guide](https://arstechnica.com/gadgets/2015/02/understanding-m-2-the-interface-that-will-speed-up-your-next-ssd/)

## NVMe

Non-Volatile Memory Express (NVMe) is a protocol designed to specifically work over PCIe, which provides a faster and more direct path to the CPU compared to SATA. The SATA interface cannot support the NVMe protocol due to its architectural limitations.

## SATA

A physical connector type and a data transfer protocol.

## [Storage for Ethereum Node](https://gist.github.com/yorickdowne/f3a3e79a573bf35767cd002cc977b038)

## SSDs

- Native PCIe
- M.2 NVMe
- SATA
- M.2 SATA
