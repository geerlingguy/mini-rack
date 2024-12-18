# Project MINI RACK

<p align="center"><img alt="Jeff Geerling's first MINI RACK" src="/resources/jeff-geerling-mini-rack.jpeg" height="auto" width="600"></p>

A guide for miniature rack builds, for portable or compact Homelabs.

Some links in this repository are affiliate links—I earn for qualifying purchases. These links help fund the ongoing maintenance of this project :)

This repository is maintained by [Jeff Geerling](https://www.jeffgeerling.com), who lives in the US. Sadly, mini rack gear is often only available in specific regions. For example, [many vendors sell only in the UK or parts of Europe](https://www.reddit.com/r/minilab/comments/1g1nto6/offtheshelf_10_gear_guide/). So this repository is mainly focused on gear _I'm_ able to acquire, living in the US. That doesn't mean its scope can't broaden over time, though.

## Hardware

### 10" Mini Racks

At the center of every mini rack is a 10" or 'half-width' rack. A typical rack is 19" wide, but half-racks fit in more places. There are only a few manufacturers of mini racks, currently, and availability varies by country.

  - [GeeekPi / DeskPi RackMate T1 8U rack (open)](https://amzn.to/3DjLhfI)
  - [GeeekPi / DeskPi RackMate T0 4U rack (open)](https://amzn.to/4iIBsZ6)
  - [Digitus Network Cabinet - 9U (wall-mountable)](https://amzn.to/3ZIjjBP) (also 6U)
  - [KENUCO SOHO Mini 6U Rack (enclosed, locking, wall-mountable)](https://amzn.to/3OZvLIi)
  - [NavePoint 6U 10" Server Cabinet (enclosed, locking, wall-mountable, glass door)](https://amzn.to/3P3uWOS)
  - [NavePoint 6U 10" Server Cabinet (enclosed, locking, wall-mountable, glass door)](https://amzn.to/3BzPc7y)
  - [NavePoint 9U 10" Server Cabinet (enclosed, locking, wall-mountable, perforated door)](https://amzn.to/4iFBznY)
  - [INTELLINET 7U 10" Network Cabinet (enclosed, locking, wall-mountable, glass door)](https://amzn.to/3VHYJAc)
  - [L-com 8U Half Rack Frame Rack (open)](https://www.l-com.com/patch-panel-server-rack-8-space-14-half-rack-frame-rack-10-panel-width-14-deep-passive-top-open-bottom)
  - [Middle Atlantic HRF-1214 14U Half Rack Frame (open)](https://amzn.to/4fr2dy2)
  - [4U Rack Rail with Full Holes](https://www.penn-elcom.com/us/4u-rack-rail-with-full-holes-0-08in-thick-r0863-2mm-04) (you can tie two of these together with some 10" gear)

### PDUs and UPSes

Every device in a rack needs power. If it's not provided by a PoE switch, it has to come from somewhere! A PDU, or Power Distribution Unit, takes one power source (usually AC wall power) and lets you plug multiple devices into it—whether through DC 12V adapters, USB-C, or AC outlets.

Some PDUs can be remotely managed, other PDUs are basically rack-mountable surge protectors. And yet others distribute power with more _panache_.

UPSes, or Uninterruptable Power Supplies, offer protection against brownouts or power loss, and usually have better power protection circuits as well.

  - [GeeekPi DC PDU Lite - 7 Channel 12V 0.5U PDU](https://amzn.to/3DliKGG)
  - [PDUOnline (UK) 10" Rack PDUs](https://pduonline.co.uk/product-category/rack-pdus/10-horizontal-pdus/)

Ongoing discussions:

  - [Find the perfect 1U 10" Mini Rack UPS](https://github.com/geerlingguy/mini-rack/issues/1)

### Patch Panels

Patch panels help organize a mess of RJ45 network cables, USB, HDMI, Coax, or whatever other signals you'd like to pass through from the back to the front. Often mounted just above or below a switch for a tidy install.

  - [GeeekPi 12 Port 0.5U CAT6 Network Patch Panel](https://amzn.to/3ZZ1os4)
  - [INTELLINET 10 Port 1U Keystone Patch Panel](https://amzn.to/3P1PHKF)
  - [INTELLINET 12 Port 1U CAT6 Network Patch Panel](https://amzn.to/3P2ni7g)

### Network Gear

The heart of every homelab is a network switch or router. There aren't a lot of switches that can natively mount in a 10" rack, but every year a couple new 'half rack' models are introduced.

In this section, gear will be split between devices which natively mount in a 10" rack (e.g. with hard-mounted rack ears), and devices which can _fit_ in a 10" rack but require a shelf or 3D printed mounting adapter.

#### Rack-mountable gear

  - [Digitus DN-80115 16x 1Gbps Unmanaged Switch](https://www.digitec.ch/en/s1/product/digitus-dn-80115-16-ports-network-switches-12955993)
  - [MikroTik CRS310-1G-5S-4S+IN 5x 1Gbps SFP 4x 10G SFP+ 1x 1Gbps Ethernet Switch](https://amzn.to/3VJKYBe) (with [RMK-2/10 kit](https://amzn.to/3Pmm5rT))
  - [MikroTik CRS310-8G+2S+IN 8x 2.5Gbps 2x 10G SFP+ Router](https://amzn.to/3Dx4smb) (with [RMK-2/10 kit](https://amzn.to/3Pmm5rT))
  - [MikroTik CRS112-8P-4S-IN 8x 1Gbps 4x 1Gbps SFP Router](https://amzn.to/4fivRpi) (with [RMK-2/10 kit](https://amzn.to/3Pmm5rT))
  - [MikroTik CSS610-8P-2S+in 8x 1 Gbps PoE+ 2x SFP+ 10G Switch](https://amzn.to/3ZKAtP8) (with [RMK-2/10 kit](https://amzn.to/3Pmm5rT))
  - [MikroTik CSS610-8G-2S+in 8x 1Gbps 2x SPF+ 10G Switch](https://amzn.to/3OYAjyV) (with [RMK-2/10 kit](https://amzn.to/3Pmm5rT))
  - [YuanLey YS2083GS-P 8-port PoE+, 2-port 1 Gbps, 1-port SFP 120W Unmanaged switch](https://amzn.to/41Y3qKv)

#### Gear that fits on a 10" shelf

  - [Zyxel GS1100-16 1 Gbps Unmanaged Switch](https://amzn.to/41GicFw)
  - [GiGaPlus GP-S25-0802P 8x 2.5G PoE+ 2x 10G SPF+ Unmanaged Switch](https://amzn.to/4iGMxJR)
  - [Ubiquiti EdgeSwitch 10X 10-port Managed Switch](https://amzn.to/49Hobf2)
  - [Netgear 8-port Unmanaged Gigabit Switch GS308](https://amzn.to/4gilDq9)
  - [Real HD 8-port 2.5G Unmanaged Switch with 10G SFP+ Uplink SW8-25G](https://amzn.to/3VJuDwy)
  
Note: Some switches intended for full-width rack mount ears _may_ work in a 10" rack with 'universal' rack ears, like the [Pelopy Adjustable Universal Rack Mount Ear Kit](https://amzn.to/4gJ7BxT). Alternatively, _some_ switches (like the Zyxel) may have 3D printable ears on a site like Printables or Thingiverse.

### 3D Printable mini rack systems

Some makers have created entire mini rack 'systems', where you 3D print a faceplate (or cut it out of metal, like with [SendCutSend](https://sendcutsend.com)), and insert different types of gear, like SBCs, SSDs, mini network switches, etc.

This section is for _systems_, not individual 3D printable parts. For parts like cable modem or mini switch mounts, please see the respective sections elsewhere.

  - [Uptime Lab - Raspberry Pi Server Mark III](https://uplab.pro/2020/12/raspberry-pi-server-mark-iii/)

### Mini PC / Server Shelves

There are a variety of commercial options to mount Mini ITX motherboards (or SBC clusterboards, like the Turing Pi 2, or DeskPi Super6C!), or to mount Tiny/Mini/Micro PCs like a Lenovo M series computer.

  - [GeeekPi / DeskPi RackMate Mini ITX 1U shelf](https://amzn.to/3ZKq5qV)
  - [MyElectronics 10" 2U Mini ITX Short-Depth PC enclosure](https://amzn.to/41H6wCe)

### SBC Shelves

SBCs, or Single Board Computers, are ideal for mini racks, due to their low power, thermal, and space requirements. You can often fit multiple SBCs per U of rack space, and there are many mini rack setups centered around an SBC cluster, or SBC routers or storage devices.

  - [GeeekPi / DeskPi RackMate SBC Shelf (Jetson/Pi 4/5 + 2.5" HDD/SSD)](https://amzn.to/49H76C6)
  - [GeeekPi / DeskPi RackMate 2U Rack mount for Pi 5/4 with M.2 NVMe](https://amzn.to/4glDzjL)

### Disk Shelves

It can be difficult to adapt storage devices (especially full 3.5" hard drives!) into a mini rack, but there are always solutions—sometimes as simple as placing a 2-bay NAS on its side, or putting an entire 4-bay NAS on a shelf!

  - [GeeekPi / DeskPi RackMate SBC Shelf](https://amzn.to/49H76C6) (can hard-mount two 2.5" or 3.5" HDDs side by side)

### Shelves and Blanking Panels

Not all gear can be mounted on rack rails. And not every U of space needs to be filled. Often, a device needs extra room above or below for cooling or for an accessory that sticks out. In these cases, you can employ a rack shelf or blanking panels.

  - [GeeekPi / DeskPi Rackmate 1U Rack Shelf with supports](https://amzn.to/3ZZJq8T)
  - [GeeekPi / DeskPi Rackmate 0.5U Rack shelf with supports](https://amzn.to/4fjuuGY)
  - [GeeekPi / DeskPi 1U Vented blanking panel](https://amzn.to/49KQPMf)
  - [GeeekPi / DeskPi 1U Solid blanking panel](https://amzn.to/3BLnox3)
  - [INTELLINET 10" 1U Vented Cantilever Shelf](https://amzn.to/3BM80jY)
  - [INTELLINET 10" 1U Blank Panel](https://amzn.to/3ZGa6tN)
  - [L-com Half Rack Quiet Blower Panel, 50 CFM](https://www.l-com.com/patch-panel-server-rack-half-rack-quiet-blower-panel-50-cfm)
  - [L-com Half Rack 1U Blank Panel](https://www.l-com.com/patch-panel-server-rack-1-space-half-rack-blank-panel-175)
  - [L-com Half Rack 1U Vent Panel](https://www.l-com.com/patch-panel-server-rack-1-space-half-rack-vent-panel-175)
  - [L-com Half Rack 2U Vent Panel](https://www.l-com.com/patch-panel-server-rack-2-space-half-rack-vent-panel-350)
  - [L-com Half Rack 1U Universal Multi Shelf - 5.5" deep](https://www.l-com.com/patch-panel-server-rack-half-rack-1-space-universal-multi-shelf-55-deep-black)

## Cable Management

Mini racks can quickly turn from beauty into beast, once you start plugging things into each other! Larger racks usually have areas where cables can be routed for a tidy finish and easy maintenance, but mini racks often don't have room. So you can add on accessories to tidy up unsightly cable messes.

  - [GeeekPi / DeskPi 0.5U Cable Entry brush panel](https://amzn.to/3DvacwM)
  - [GeeekPi 0.5U Horizontal Cable Manager with D-ring hooks](https://amzn.to/4gwE6PE)
  - [INTELLINET 10" 1U Cable Management Panel - 3 rings](https://amzn.to/3ZY8BZa)
  - [INTELLINET 10" 1U Cable Management Panel - covered](https://amzn.to/4fr239U)

## Example builds for inspiration

I'm not the first person to build a mini rack. In fact, the mini-homelab community's been thriving for years! Check out [Reddit r/minilab](https://www.reddit.com/r/minilab/) for some extra inspiration.

  - [Jeff Geerling's 'Project Mini Rack'](TODO)
  - [u/Gold-Abalone7538's Mini 10" 9U Rack](https://www.reddit.com/r/homelab/comments/1cek9os/my_mini_10_half_width_9u_rack/)
  - [Hardware Haven's 'Favorite Home Lab So Far'](https://www.youtube.com/watch?v=wbRViRwflbI)
  - [TechnoTim's Mini Rack, HomeLab Stack](https://www.youtube.com/watch?v=kGZa-81IDGY)
  - [Raid Owl's Ultimate Mini Server Rack](https://www.youtube.com/watch?v=wJUDhQ7s9HM)

## Software

TODO

## License

GPLv3 or later

## Author

[Jeff Geerling](https://www.jeffgeerling.com)
