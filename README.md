[![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/geerlingguy/mini-rack?link=https%3A%2F%2Fgithub.com%2Fgeerlingguy%2Fmini-rack%2Fissues)](https://github.com/geerlingguy/mini-rack/issues)
 [![GitHub Repo stars](https://img.shields.io/github/stars/geerlingguy/mini-rack?link=https%3A%2F%2Fgithub.com%2Fgeerlingguy%2Fmini-rack%2Fstargazers)](https://github.com/geerlingguy/mini-rack/stargazers)

<p align="center"><img alt="Jeff Geerling's first MINI RACK" src="/assets/images/jeff-geerling-mini-racks-001-002-1200.jpg" height="auto" width="600"></p>

**Project MINI RACK** is a guide for miniature rack builds, for compact Homelabs, RF battlestations, and portable network racks. Watch the video announcing this project by clicking the image below:

<p align="center"><a href="https://www.youtube.com/watch?v=y1GCIwLm3is"><img src="/assets/images/jeff-mini-rack-play.jpeg" width="600" height="auto" alt="Jeff Geerling - Project Mini Rack - click to play"></a></p>

This site is maintained by [Jeff Geerling](https://www.jeffgeerling.com), who lives in the US. Sadly, mini rack gear is often only available in specific regions. For example, [many vendors sell only in the UK or parts of Europe](https://www.reddit.com/r/minilab/comments/1g1nto6/offtheshelf_10_gear_guide/). So this site is mainly focused on gear _I'm_ able to acquire, living in the US. That doesn't mean its scope can't broaden over time, though.

> Some links on this site are affiliate links—I earn for qualifying purchases. These links help fund the ongoing maintenance of this project :)

## Table of Contents

  - [Community](#community)
  - [The 10" Mini Rack Standard](#standard)
  - [Hardware](#hardware)
    - [10" Mini Racks](#racks)
    - [PDUs](#pdus)
    - [UPSes](#upses)
    - [Patch Panels](#patch-panels)
    - [Network Gear](#network-gear)
    - [3D-Printable mini rack systems](#3d-printable-systems)
    - [Mini PC/Server Shelves](#mini-pc-server-shelves)
    - [SBC Shelves](#sbc-shelves)
    - [Disk Shelves](#disk-shelves)
    - [Shelves and Blanking Panels](#shelves-and-blanking-panels)
  - [Cable Management](#cable-management)
  - [Build Showcase](#build-showcase)
  - [Software](#software)
  - [License](#license)

## <a name="standard"></a>The 10" Mini Rack Standard

There is no worldwide 'standard' published for what constitutes a "mini rack". However, most of the industry has settled on the same '1U' height standard as typical 19" racks (44.45mm, or 1.75"), but with the width being 236.525mm (9.312") between screw holes. This equates to an _absolute maximum_ of around 220mm (8.75") of horizontal clearance.

<p align="center"><a href="https://commons.wikimedia.org/wiki/File:19_inch_vs_10_inch_rack_dimensions.svg"><img alt="Mini Rack size standard" src="/assets/images/mini-rack-size-wikipedia.png" height="auto" width="600"></a><br>
Image source: <a href="https://commons.wikimedia.org/wiki/File:19_inch_vs_10_inch_rack_dimensions.svg">Wikipedia</a>.</p>

Allowing for extra tolerance, mini rack gear should fit within around 210mm (8.45") of horizontal space, and mounting holes should be able to accomodate a few mm of width to either side.

For screws, some manufacturers forego threads and use square holes for cage nuts, while others use standard 10/32 or 12/24 screws. Screw or square holes must follow the same vertical spacing as the 19" rack specification.

[See issue #29](https://github.com/geerlingguy/mini-rack/issues/29) for more discussion around mini rack dimensions.

## <a name="community"></a>Community

Visit [Project MINI RACK Issues](https://github.com/geerlingguy/mini-rack/issues) to discuss your own mini rack builds, ask for help finding a particular piece of equipment, or to share your experience.

Issues are categorized:

  - [help me find](https://github.com/geerlingguy/mini-rack/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+me+find%22): for help finding a particular piece of equipment
  - [build showcase](https://github.com/geerlingguy/mini-rack/issues?q=is%3Aopen+is%3Aissue+label%3A%22build+showcase%22): for complete or nearly-complete builds, to show off your stuff to the world!
  - [website issues](https://github.com/geerlingguy/mini-rack/issues?q=is%3Aopen+is%3Aissue+label%3A%22website+issues%22): for problems with this website

Besides this site, check out [Reddit's r/minilab](https://www.reddit.com/r/minilab) for discussion about about mini racks and the broader topic of mini _homelabs_ (which may or may not incorporate a rack).

## <a name="hardware"></a>Hardware

<p align="center"><img alt="Jeff Geerling's MINI RACK 003" src="/assets/images/jeff-geerling-8u-003-1200.jpg" height="auto" width="600"></p>

### <a name="racks"></a>10" Mini Racks

At the center of every mini rack is a 10" or 'half-width' rack. A typical rack is 19" wide, but half-racks fit in more places. There are only a few manufacturers of mini racks, currently, and availability varies by country.

| Model (incl. Link)    | Unit Height | Additional information | 
| :-------- | :------- | :------- |
| [Delock 10" Network Cabinet](https://www.delock.com/produkt/43379/merkmale.html) | 4U, 6U, 8U | enclosed, locking, glass door |
| [Delock 10″ Wallmount Rack](https://www.delock.com/produkt/43303/merkmale.html) | 1U | wall-mountable |
| [Digitus Network Cabinet](https://amzn.to/3ZIjjBP) | 6U, 9U, 12U | wall-mountable |
| [DIY Laser Cut Mini Rack](https://github.com/ssilverm/lasercut-mini-rack)|6U||
| [DSIT Rack](https://www.redcorp.com/en/product/servers-racks-options/dsit/server-rack-15u-glass-door-black-312x310x752mm-wxdxh--ds10-3315/y3872053#) | 15U | glass door |
| [Flyht Pro Stage Rack Double Door](https://www.thomann.de/intl/flyht_pro_stage_rack_95_6u_double_door.htm) | 6U | flight case, similar models also available down to 2U |
| [GeeekPi / DeskPi RackMate T0](https://amzn.to/4iIBsZ6) | 4U | open design |
| [GeeekPi / DeskPi RackMate T1](https://amzn.to/3DjLhfI)  | 8U | open design |
| [Intellinet Network Cabinet](https://amzn.to/3VHYJAc) | 6U | enclosed, locking, wall-mountable, glass door |
| [KENUCO SOHO Mini Rack](https://amzn.to/3OZvLIi) | 4U, 6U, 9U | enclosed, locking, wall-mountable |
| [L-com Half Rack Frame Rack](https://www.l-com.com/patch-panel-server-rack-8-space-14-half-rack-frame-rack-10-panel-width-14-deep-passive-top-open-bottom) | 8U | open design |
| [Middle Atlantic HRF-1214 Half Rack Frame](https://amzn.to/4fr2dy2) | 12U | open design |
| [NavePoint Server Cabinet I](https://amzn.to/3P3uWOS) | 6U | enclosed, locking, wall-mountable, glass door |
| [NavePoint Server Cabinet II](https://amzn.to/3BzPc7y) | 6U | enclosed, locking, wall-mountable, perforated door |
| [NavePoint Server Cabinet III](https://amzn.to/4iFBznY) | 9U | enclosed, locking, wall-mountable, perforated door | 
| [Penn Elcom Rack Rail with Full Holes](https://www.penn-elcom.com/us/4u-rack-rail-with-full-holes-0-08in-thick-r0863-2mm-04) | 4U | you can tie two of these together with some 10" gear |
| [Rack Magic Cabinet](https://www.rack-magic.com/en/p/10-wall-or-desktop-cabinet-5u-250mm-depth-network-server-studio-laboratory) | 5U | wall-mountable, black or grey |
| [Rack Magic Mini Rack](https://www.rack-magic.com/en/p/10-rack-3he-6he-9he-12he-tiefe-290-mm-wand-o-boden-montage-rack-magic) | 3U, 6U, 9U, 12U | wall-mountable, open design, black or grey |
| [Rack Magic Rack Stand](https://www.rack-magic.com/en/p/mini-rack-254mm-10-rack-stand-3u-6u-10-inch) | 3U, 6U | open design, black or grey|

### <a name="pdus"></a>PDUs (Power Distribution Units)

Every device in a rack needs power. If it's not provided by a PoE switch, it has to come from somewhere! A PDU, or Power Distribution Unit, takes one power source (usually AC wall power) and lets you plug multiple devices into it—whether through DC 12V adapters, USB-C, or AC outlets.

Some PDUs can be remotely managed, other PDUs are basically rack-mountable surge protectors. And yet others distribute power with more _panache_.

  - [GeeekPi DC PDU Lite - 7 Channel 12V 0.5U PDU](https://amzn.to/3DliKGG)
  - [PDUOnline (UK) 10" Rack PDUs](https://pduonline.co.uk/product-category/rack-pdus/10-horizontal-pdus/)
  - [Tupavco TP1713 4-outlet Mini Rack PDU with Protection](https://amzn.to/41JChus)
  - [Tripp Lite PDU15NETLX Single Phase Switched Mini PDU - 2 Outlets](https://amzn.to/3Dmy0mw)
  - [AliExpress US Power Strip - 3 socket](https://www.aliexpress.us/item/3256805777681738.html)
  - [the t.racks Power 3 Power Strip – Type F/Schuko](https://www.thomann.de/intl/the_t.racks_power_3.htm)
  - [netBooter NP-02B Remote Switched PDU 2 outlet](https://amzn.to/40lpnjZ)
  - [NETIO PowerPDU 4KB 4 outlet](https://www.netio-products.com/en/device/powerpdu-4kb)
  - [APC AP6015A](https://www.apc.com/us/en/product/AP6015A/rack-pdu-basic-0u-1u-120240v-15a-220240v-10a-8-c13)
  - [DIGITUS 10" Socket Strip with Aluminum Profile, 4-way safety sockets](https://amzn.eu/d/9gsqlp5)
  - [DIGITUS 10" Aluminium Outlet Strip, 3 safety outlets, 2m supply safety plug](https://amzn.eu/d/4CE9nbv)
  - [Atlas Power AP-S15HR 15A Half-rack Power Conditioner](https://amzn.to/4iG8oBv) (slightly too wide, may need modified mounting)

> **Note**: Some small PoE switches also have PoE+ or PoE++ power input, such as the [Ubiquiti USW-Ultra](https://store.ui.com/us/en/category/switching-utility/collections/pro-ultra/products/usw-ultra). Assuming you are in a location with another PoE++ switch, and everything is PoE-powered, you could power everything off one Ethernet cable, and bypass the need for a PDU or UPS in the mini rack!

Ongoing discussions:

  - [Find the perfect 1U 10" Mini Rack PDU](https://github.com/geerlingguy/mini-rack/issues/5)

### <a name="upses"></a>UPSes (Uninterruptible Power Supplies)

UPSes, or Uninterruptable Power Supplies, offer protection against brownouts or power loss, and usually have better power protection circuits as well.

#### Mini Rack UPSes

  - [Goal Zero Sherpa 100 AC](https://amzn.to/40tUb3r) (requires USB-C PD 60W+ input and rack shelf)
  - [Tripp Lite 600VA 300W UPS - BC600R](https://amzn.to/3WnvQdg) (fits within the bottom of a RackMate, see [this issue](https://github.com/geerlingguy/mini-rack/issues/1#issuecomment-2599063696))

Ongoing discussions:

  - [Find the perfect 1U 10" Mini Rack UPS](https://github.com/geerlingguy/mini-rack/issues/1)

#### Device-specific UPSes

  - [PiSugar 3 Plus 5000 mAh Pi model B UPS](https://amzn.to/4alpT6k) (rack mounting can be tricky, requires one per Raspberry Pi, only supplies 3A at 5V)
  - [Geekworm X1200 5V UPS HAT for Pi 5](https://www.amazon.com/Geekworm-X1200-Raspberry-Shutdown-Detection/dp/B0CRYVC8C5?ref_=ast_sto_dp) (rack mounting can be tricky)
  - [Waveshare UPS Module 3S for SBCs](https://amzn.to/3WgNajM) (rack mounting can be tricky)

### <a name="patch-panels"></a>Patch Panels

Patch panels help organize a mess of RJ45 network cables, USB, HDMI, Coax, or whatever other signals you'd like to pass through from the back to the front. Often mounted just above or below a switch for a tidy install.

| Model (incl. Link)    | Unit Height | Additional information | 
| :-------- | :------- | :------- |
| [Delock 10" Fiber Optic Patch Panel 12 Port LC Duplex](https://www.delock.com/produkt/66769/merkmale.html) | 1U | Different models available: Different colors,  SC simplex, LC duplex, LC quad, empty panels. Check website for different model numbers |
| [GeeekPi 12 Port CAT6 Network Patch Panel](https://amzn.to/3ZZ1os4) | 0.5U | Can also be used as a 0.5U Keystone patch panel |
| [INTELLINET 10 Port Keystone Patch Panel](https://amzn.to/3P1PHKF) | 1U |  |
| [INTELLINET 12 Port CAT6 Network Patch Panel](https://amzn.to/3P2ni7g) | 1U |  |
| [Rapink Patch Panel Mini 12 Port Cat6A Shielded Patch Panel](https://amzn.to/3PelLuR) | 1U |  |

### <a name="network-gear"></a>Network Gear

The heart of every homelab is a network switch or router. There aren't a lot of switches that can natively mount in a 10" rack, but every year a couple new 'half rack' models are introduced.

In this section, gear will be split between devices which natively mount in a 10" rack (e.g. with hard-mounted rack ears), and devices which can _fit_ in a 10" rack but require a shelf or 3D printed mounting adapter.

#### Rack-mountable Network Gear

  - [Digitus DN-80115 16x 1Gbps Unmanaged Switch](https://www.digitec.ch/en/s1/product/digitus-dn-80115-16-ports-network-switches-12955993)
  - [Digitus DN-80117 8x 1Gbps Managed Switch](https://de.assmann.shop/en/Active-Network-Components/Network-Switches/10-Network-Switches/8-Port-Gigabit-Switch-10-Inch-Managed.html?listtype=search&searchparam=switch)
  - [MikroTik CSS318-16G-2S+IN 8x 1Gbps 2x 10G SFP+ Router](https://mikrotik.com/product/css318_16g_2s_in)
  - [MikroTik CRS310-1G-5S-4S+IN 5x 1Gbps SFP 4x 10G SFP+ 1x 1Gbps Ethernet Switch](https://amzn.to/3VJKYBe)
  - [MikroTik CRS310-8G+2S+IN 8x 2.5Gbps 2x 10G SFP+ Router](https://amzn.to/3Dx4smb)
  - [MikroTik CRS112-8P-4S-IN 8x 1Gbps 4x 1Gbps SFP Router](https://amzn.to/4fivRpi)
  - [MikroTik CSS610-8P-2S+in 8x 1 Gbps PoE+ 2x SFP+ 10G Switch](https://amzn.to/3ZKAtP8)
  - [MikroTik CSS610-8G-2S+in 8x 1Gbps 2x SPF+ 10G Switch](https://amzn.to/3OYAjyV)
  - [MikroTik L009UiGS-RM 8 x 1Gbps 1x 2.5G SFP Router](https://mikrotik.com/product/l009uigs_rm)
  - [MikroTik RB5009UG+S+IN 7 x 1Gbps 1x 2.5Gbps 1x SFP+ Router](https://mikrotik.com/product/rb5009ug_s_in)
  - [MikroTik RB5009UPr+S+IN 7 x 1Gbps PoE+ 1x 2.5Gbps PoE+ 1x SFP+ Router](https://mikrotik.com/product/rb5009upr_s_in)
  - [YuanLey YS2083GS-P 8-port PoE+, 2-port 1 Gbps, 1-port SFP 120W Unmanaged switch](https://amzn.to/41Y3qKv)
  - [GiGaPlus GP-S25-0802P 8x 2.5G PoE+ 2x 10G SFP+ Unmanaged Switch](https://amzn.to/4iGMxJR)
  - [QNAP QSW-M2108R-2C 8x 2.5G 2x 10G SFP+/RJ45 Managed Switch](https://amzn.to/4gNoaJ4)
  - [QNAP QSW-M2106R-2S2T 6x 2.5G 2x 10G SFP+ 2x 10G RJ45 Managed Switch](https://amzn.to/3VLfwCH)
  - [QNAP QSW-M2106PR-2S2T 6x 2.5G PoE++ 2x 10G PoE++ RJ45 2x 10G SFP+ Managed Switch](https://amzn.to/4iF3Lrj)
  - [QNAP QSW-M3216R-8S8T 8x 10G RJ45 8x 10G SFP+ Managed Switch](https://amzn.to/3VOc1eP)
  - [QNAP QSW-M3212R-8S4T 4x 10G RJ45 8x 10G SFP+ Managed Switch](https://amzn.to/4fBPOaY)
  - [QNAP QSW-3216R-8S8T 8x 10G RJ45 8x 10G SFP+ Unmanaged Switch](https://amzn.to/3DtQ1zt)
  - [QNAP QSW-M7308R-4X 4x 100G QSFP 8x 25G SFP+ L3 Managed Switch](https://amzn.to/3ZO0e0X)

Note: Some switches intended for full-width rack mount ears _may_ work in a 10" rack with 'universal' rack ears, like the [Pelopy Adjustable Universal Rack Mount Ear Kit](https://amzn.to/4gJ7BxT).

Some manufacturers require special kits for 10" rack compatibility:

  - Mikrotik offers the [RMK-2/10 kit](https://amzn.to/3Pmm5rT)) for full 10" compatibility
  - QNAP offers the [SP-EAR-QSWHALFRACK-01](https://store.qnap.com/sp-ear-qswhalfrack-01.html), though you may need to buy two kits to get a short ear for each side!
    - There's also a set of [3D Printable rack ears for QNAP 10" devices](https://www.printables.com/model/1023123-qnap-switch-10-rack-mount)
  - Pelopy offers a [Universal Rack Mount Ear Kit](https://amzn.to/4gJ7BxT) for many vendors—however fitment can be tricky...

See [Issue #2: Find a perfect way to mount small switches into mini racks](https://github.com/geerlingguy/mini-rack/issues/2) for more discussion around this topic.

#### Network Gear that fits on a 10" shelf

  - [Zyxel GS1100-16 1 Gbps Unmanaged Switch](https://amzn.to/41GicFw)
  - [Ubiquiti USW-Ultra 42W 8-port Managed PoE Switch](https://store.ui.com/us/en/collections/pro-ultra/products/usw-ultra)
  - [Ubiquiti EdgeSwitch 10X 10-port Managed Switch](https://amzn.to/49Hobf2)
  - [Netgear 8-port Unmanaged Gigabit Switch GS308](https://amzn.to/4gilDq9)
  - [Real HD 8-port 2.5G Unmanaged Switch with 10G SFP+ Uplink SW8-25G](https://amzn.to/3VJuDwy)
  - [Netgear GS110EMX 8x 1 Gbps 2x 10G Managed Switch](https://amzn.to/4fyKWDj)
  - [D-Link DGS-108 8x 1 Gbps Unmanaged Switch](https://amzn.to/4ftNW3N)
  - [TRENDnet TEG-S762 4x 2.5G 2x 2.5/5/10G Unmanaged Switch](https://amzn.to/4gEau2S)
  - [GiGaPlus GP-S100-0500T 5x 10G Unmanaged Switch](https://amzn.to/3ZGUia0)
  - Many 4, 5, 6, or 8 port cheap PoE/1 Gbps switches (too many to list...)
  
Note: Many of these switches have 3D printable ears on Printables, Thingiverse, etc.

### <a name="3d-printable-systems"></a>3D Printable mini rack systems

Some makers have created entire mini rack 'systems', where you 3D print a faceplate (or cut it out of metal, like with [SendCutSend](https://sendcutsend.com)), and insert different types of gear, like SBCs, SSDs, mini network switches, etc.

This section is for _systems_, not individual 3D printable parts. For parts like cable modem or mini switch mounts, please see the respective sections elsewhere.

  - [JaredC01's LabStack mini](https://github.com/JaredC01/LabStack)
  - [Uptime Lab - Raspberry Pi Server Mark III](https://uplab.pro/2020/12/raspberry-pi-server-mark-iii/)
  - [Mauker's 10-inch rack mounts](https://makerworld.com/en/collections/2928697)
  - [dalovering's fully 3D printable half-width server rack and trays](https://www.printables.com/model/358304-fully-printable-half-width-server-rack-and-trays)
  - [jazwa's rackstack - modular 3D printable mini rack system](https://github.com/jazwa/rackstack)
  - [Paul Grove's 3D Cube Rack](https://www.printables.com/model/688952-cube-rack-10-inch-network-cabinet-server-rack)

### <a name="mini-pc-server-shelves"></a>Mini PC / Server Shelves

There are a variety of commercial options to mount Mini ITX motherboards (or SBC clusterboards, like the Turing Pi 2, or DeskPi Super6C!), or to mount Tiny/Mini/Micro PCs like a Lenovo M series computer.

  - [GeeekPi / DeskPi RackMate Mini ITX 1U shelf](https://amzn.to/3ZKq5qV)
  - [MyElectronics 10" 2U Mini ITX Short-Depth PC enclosure](https://amzn.to/41H6wCe)

### <a name="sbc-shelves"></a>SBC Shelves

SBCs, or Single Board Computers, are ideal for mini racks, due to their low power, thermal, and space requirements. You can often fit multiple SBCs per U of rack space, and there are many mini rack setups centered around an SBC cluster, or SBC routers or storage devices.

  - [GeeekPi / DeskPi RackMate SBC Shelf (Jetson/Pi 4/5 + 2.5" HDD/SSD)](https://amzn.to/49H76C6)
  - [GeeekPi / DeskPi RackMate 2U Rack mount for Pi 5/4 with M.2 NVMe](https://amzn.to/4glDzjL)
  - [Racknex UM-SBC shelves for Pi 2/3/4/5](https://racknex.com/shop/raspberry-pi/?filter_rack=10-inch)

### <a name="disk-shelves"></a>Disk Shelves

It can be difficult to adapt storage devices (especially full 3.5" hard drives!) into a mini rack, but there are always solutions—sometimes as simple as placing a 2-bay NAS on its side, or putting an entire 4-bay NAS on a shelf!

  - [GeeekPi / DeskPi RackMate SBC Shelf](https://amzn.to/49H76C6) (can hard-mount two 2.5" or 3.5" HDDs side by side)
  - [10" Rack Hard Drive Mount](https://www.printables.com/model/142325-10-rack-harddrive-mount) (can hard-mount two 3.5" drives)

### <a name="shelves-and-blanking-panels"></a>Shelves and Blanking Panels

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
  - [Digitus Shelf 1U Perforated Steel Shelf](https://amzn.to/4014ATT)
  - [Flyht Pro Rack Tray 9,5" 1U Mount – with cross holes](https://www.thomann.de/intl/flyht_pro_rack_tray_95_1u_mount.htm)
  - [Flyht Pro Rack Tray 1U 9,5"](https://www.thomann.de/intl/flyht_pro_rack_tray_1u_95.htm)
  - [Flyht Pro Rack Panel Air 1U 9,5" – vented](https://www.thomann.de/intl/flyht_pro_rack_panel_air_1u_95.htm)
  - [Flyht Pro Rack Panel 1U 9,5"](https://www.thomann.de/intl/flyht_pro_rack_panel_1u_95.htm)
  - [Flyht Pro Rack Panel 4XLR 1U 9,5" – with four D-standard holes](https://www.thomann.de/intl/flyht_pro_rack_panel_4xlr_1u_95.htm)

## <a name="cable-management"></a>Cable Management

Mini racks can quickly turn from beauty into beast, once you start plugging things into each other! Larger racks usually have areas where cables can be routed for a tidy finish and easy maintenance, but mini racks often don't have room. So you can add on accessories to tidy up unsightly cable messes.

  - [GeeekPi / DeskPi 0.5U Cable Entry brush panel](https://amzn.to/3DvacwM)
  - [GeeekPi 0.5U Horizontal Cable Manager with D-ring hooks](https://amzn.to/4gwE6PE)
  - [INTELLINET 10" 1U Cable Management Panel - 3 rings](https://amzn.to/3ZY8BZa)
  - [INTELLINET 10" 1U Cable Management Panel - covered](https://amzn.to/4fr239U)

## <a name="build-showcase"></a>Build showcase

I'm not the first person to build a mini rack. In fact, the mini-homelab community's been thriving for years! Check out [Reddit r/minilab](https://www.reddit.com/r/minilab/) for some extra inspiration.

If you would like your mini rack added to this list, please open a [new issue](https://github.com/geerlingguy/mini-rack/issues/new), add the `build showcase` label, and document your build! Once it is complete(ish), we can add it to this list:

| User | Year | Description |
| :--- | :--- | :---------- |
| geerlingguy | 2025 | [Mini Rack 001: 4U PoE, Solar, and UPS K3s cluster](https://github.com/geerlingguy/mini-rack/issues/3) |
| geerlingguy | 2025 | [Mini Rack 002: Simple USB-C powered Pi K3s Cluster](https://github.com/geerlingguy/mini-rack/issues/4) |
| geerlingguy | 2025 | [Mini Rack 003: ITX Dense Compute with external UPS](https://github.com/geerlingguy/mini-rack/issues/6) |
| timothystewart6 | 2025 | [Mini Rack 004: Complete HomeLab - Proxmox, TrueNAS, Firewall, KVM, and of course RGB](https://github.com/geerlingguy/mini-rack/issues/11) |
| sefs93 | 2025 | [Custom 3D-printable rack](https://github.com/geerlingguy/mini-rack/issues/21) |
| stirkage | 2025 | [IKEDA Eket DIY 10" rack](https://github.com/geerlingguy/mini-rack/issues/22) |
| alatnet | 2025 | [Custom 8U Homelab rack](https://github.com/geerlingguy/mini-rack/issues/23) |
| RasPiBuilder | 2025 | [Mini Rack 005: Home automation, Docker Swarm, AI Agents, NAS](https://github.com/geerlingguy/mini-rack/issues/39) |
| jeofo | 2025 | [Deskpi 8U Showcase](https://github.com/geerlingguy/mini-rack/issues/38) |
| jccherry | 2025 | [Mini Rack --> Rackception](https://github.com/geerlingguy/mini-rack/issues/37) |
| loganmarchione | 2021 | [Custom 4U mini-rack](https://github.com/geerlingguy/mini-rack/issues/33) |
| mrp-yt | 2025 | [GALAXY 10" 3D Printable Homelab Server Rack](https://github.com/geerlingguy/mini-rack/issues/55) |
| Mauker1 | 2023 | [3D printable rack](https://github.com/geerlingguy/mini-rack/issues/64) |
| paulgrove | 2023 | [3D Printed "Cube" Mini rack](https://github.com/geerlingguy/mini-rack/issues/51) |
| RustyBrakes | 2025 | [Mini Rack: with Xeon ITX NAS](https://github.com/geerlingguy/mini-rack/issues/46) |
| DJSdev | 2025 | [RackMate T1 - Side mount for laptop, Tripp Lite UPS, 10Gbe, RPis, Mac Minis](https://github.com/geerlingguy/mini-rack/issues/44) |
| symbiiote | 2025 | [Cheap DIY 10" mini rack](https://github.com/geerlingguy/mini-rack/issues/67) |
| BlackChar | 2021 | [KALLAX Custom 10" 6U rack (EU)](https://github.com/geerlingguy/mini-rack/issues/70) |

[Browse all issues tagged 'build showcase'](https://github.com/geerlingguy/mini-rack/labels/build%20showcase) (includes in-progress builds).

## <a name="software"></a>Software

There's a ton of things you can do in a Homelab—and many of them run perfectly fine on mini PCs or SBCs in a mini rack!

Here's a collection of cluster-related projects that may be a good test or starting point for your own rack, if you need the inspiration:

  - [Pi Cluster](https://github.com/geerlingguy/pi-cluster) - Build a K3s cluster with 3 or more SBCs
  - [Top500 Benchmark](https://github.com/geerlingguy/top500-benchmark) - Benchmark your cluster with HPL (High Performance Linpack)

## <a name="license"></a>License

GPLv3 or later

## <a name="open-source-repository"></a>Open Source Repository

This website is generated from the [`geerlingguy/mini-rack`](https://github.com/geerlingguy/mini-rack) GitHub repository.

## <a name="author"></a>Author

[Jeff Geerling](https://www.jeffgeerling.com)
