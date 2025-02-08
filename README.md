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
    - [Other Gear](#other-gear)
    - [3D Printable mini rack systems](#3d-printable-systems)
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
| [Rack Magic Rack Stand](https://www.rack-magic.com/en/p/mini-rack-254mm-10-rack-stand-3u-6u-10-inch) | 3U, 6U | open design, black or grey |
| [Triton RKA 10/19 Rack](https://triton-racks.com/products/data-cabinets/wall-mounted-cabinets/rka-10-19) | 10U | only 10 inch rack available with a depth > 30cm |

### <a name="pdus"></a>PDUs (Power Distribution Units)

Every device in a rack needs power. If it's not provided by a PoE switch, it has to come from somewhere! A PDU, or Power Distribution Unit, takes one power source (usually AC wall power) and lets you plug multiple devices into it—whether through DC 12V adapters, USB-C, or AC outlets.

Some PDUs can be remotely managed, other PDUs are basically rack-mountable surge protectors. And yet others distribute power with more _panache_.

| Model (incl. Link)    | Unit Height | Additional information | 
| :-------- | :------- | :------- |
| [AliExpress US Power Strip](https://www.aliexpress.us/item/3256805777681738.html) | 1U | 3x NEMA 5-15R (type B) outlet |
| [APC AP6015A](https://www.apc.com/us/en/product/AP6015A/rack-pdu-basic-0u-1u-120240v-15a-220240v-10a-8-c13) | 1U | 8x C13 (type S) outlet |
| [Atlas Power AP-S15HR 15A Half-rack Power Conditioner](https://amzn.to/4iG8oBv) | 1U | 6x NEMA 5-15R (type B) outlet; slightly too wide, may need modified mounting |
| [DIGITUS 10" Aluminium Outlet Strip](https://amzn.eu/d/4CE9nbv) | 1U | 3x Schuko (type F) outlet |
| [DIGITUS 10" Socket Strip with Aluminum Profile](https://amzn.eu/d/9gsqlp5) | 1U | 4x Schuko (type F) outlet |
| [ENERGIS - Managed PDU for 10-Inch Racks](https://github.com/DvidMakesThings/HW_10-In-Rack_PDU) | 1U | 8x C13 - GPLv3 Open Source Design ]
| [GeeekPi DC PDU Lite](https://amzn.to/3DliKGG) | 0.5U | 7x 5.5mm outlet (0V to 24V)|
| [MiniBoot Smart PDU](https://amzn.to/4axNdhm) | 1U | 4x NEMA 5-15R (type B) outlet |
| [netBooter NP-02B Remote Switched PDU](https://amzn.to/40lpnjZ) | 1U | 2x NEMA 5-15R (type B) outlet |
| [NETIO PowerPDU 4KB](https://www.netio-products.com/en/device/powerpdu-4kb) | 1U | 4x NEMA 5-15R (type B) outlet, [NETIO RM2 2x4C rack mounts](https://www.netio-products.com/en/accessory/netio-rm2-2x4c) |
| [NETIO PowerPDU 4KS](https://www.netio-products.com/en/device/powerpdu-4ks) | 1U | 4x C13 (type S) outlet, [NETIO RM2 2x4C rack mounts](https://www.netio-products.com/en/accessory/netio-rm2-2x4c) |
| [PDUOnline (UK) 10" Rack PDUs](https://pduonline.co.uk/product-category/rack-pdus/10-horizontal-pdus/) | 1U | 4x UK (type G) outlet / 2x UK (type G), 1x C13 (type S), 1x C19 (type T) outlet / 2x UK (type G), 4x C13 (type S) outlet / 8x C13 (type S) outlet |
| [Tripp Lite PDU15NETLX Single Phase Switched Mini PDU](https://amzn.to/3Dmy0mw) | 1U | 2x NEMA 5-15R (type B) outlet |
| [the t.racks Power 3 Power Strip](https://www.thomann.de/intl/the_t.racks_power_3.htm) | 1U | 3x Schuko (type F) outlet  |
| [Tupavco TP1713 Mini Rack PDU with Protection](https://amzn.to/41JChus) | 1U | 4x NEMA 5-15R (type B) outlet |

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
| [Flyht Pro Rack Panel 4XLR](https://www.thomann.de/intl/flyht_pro_rack_panel_4xlr_1u_95.htm) | 1U | 4x D-type |
| [GeeekPi / DeskPi 12 Port CAT6 Network Patch Panel](https://amzn.to/3ZZ1os4) | 0.5U | Can also be used as a 0.5U Keystone patch panel |
| [GeeekPi / DeskPi D-type Patch Panel](https://deskpi.com/products/deskpi-rackmate-accessories-10-inch-1u-d-type-patch-panel-rack-mount-7d-rackmate-xlr-hdmi-av-rj45) | 1U | 7x D-type |
| [INTELLINET 10 Port Keystone Patch Panel](https://amzn.to/3P1PHKF) | 1U |  |
| [INTELLINET 12 Port CAT6 Network Patch Panel](https://amzn.to/3P2ni7g) | 1U |  |
| [Rapink Patch Panel Mini 12 Port Cat6A Shielded Patch Panel](https://amzn.to/3PelLuR) | 1U |  |

### <a name="network-gear"></a>Network Gear

The heart of every homelab is a network switch or router. There aren't a lot of switches that can natively mount in a 10" rack, but every year a couple new 'half rack' models are introduced.

In this section, gear will be split between devices which natively mount in a 10" rack (e.g. with hard-mounted rack ears), and devices which can _fit_ in a 10" rack but require a shelf or 3D printed mounting adapter.

#### Rack-mountable Network Gear

| Model (incl. Link)    | Unit Height | Additional information | 
| :-------- | :------- | :------- |
| [Digitus DN-80115](https://de.assmann.shop/en/Active-Network-Components/Network-Switches/10-Network-Switches/16-Port-Gigabit-Switch-10-inch-Unmanaged.html) | 1U | Switch Unmanaged, 16x 1G RJ45 |
| [Digitus DN-80117](https://de.assmann.shop/en/Active-Network-Components/Network-Switches/10-Network-Switches/8-Port-Gigabit-Switch-10-Inch-Managed.html) | 1U | Switch Managed, 8x 1G RJ45 |
| [GiGaPlus GP-S25-0802P](https://amzn.to/4iGMxJR) | 1U | Switch Unmanaged, 8x 2.5G RJ45 (PoE, PoE+) / 2x 10G SFP+, [3D printed rack ears](https://github.com/geerlingguy/mini-rack/issues/76) |
| [MikroTik CRS112-8P-4S-IN](https://amzn.to/4fivRpi) | 1U | Switch Managed, 8x 1G RJ45 (PoE, PoE+) / 4x 1G SFP |
| [MikroTik CRS310-1G-5S-4S+IN](https://amzn.to/3VJKYBe) | 1U | Switch Managed, 1x 1G RJ45 / 5x 1G SFP / 4x 10G SFP+ |
| [MikroTik CRS310-8G+2S+IN](https://amzn.to/3Dx4smb) | 1U | Switch Managed, 8x 2.5G RF45 / 2x 10G SFP+ 
| [MikroTik CSS318-16G-2S+IN](https://mikrotik.com/product/css318_16g_2s_in) | 1U | Switch Managed, 16x 1G RJ45 / 2x 10G SFP+ |
| [MikroTik CSS610-8G-2S+IN](https://amzn.to/3OYAjyV) | 1U | Switch Managed, 8x 1G RF45 / 2x 10G SFP+ |
| [MikroTik CSS610-8P-2S+IN](https://amzn.to/3ZKAtP8) | 1U | Switch Managed, 8x 1G RJ45 (PoE, PoE+) / 2x 10G SFP+ | 
| [MikroTik L009UiGS-RM](https://mikrotik.com/product/l009uigs_rm) | 0.5U | Router, 8x 1G RJ45 / 1 x 2.5G SFP |
| [MikroTik RB5009UG+S+IN](https://mikrotik.com/product/rb5009ug_s_in) | 0.5U | Router, 7x 1G RJ45 / 1x 2.5G RJ45 / 1x 10G SFP+ |
| [MikroTik RB5009UPr+S+IN](https://mikrotik.com/product/rb5009upr_s_in) | 0.5U | Router, 7x 1G RJ45 (PoE, PoE+) / 1x 2.5G RJ45 (PoE, PoE+) / 1x 10G SFP+ |
| [QNAP QSW-3216R-8S8T](https://amzn.to/3DtQ1zt) | 1U | Switch Unmanaged, 8x 10G RJ45 / 8x 10G SFP+ |
| [QNAP QSW-M2106R-2S2T](https://amzn.to/3VLfwCH) | 1U | Switch Managed, 6x 2.5G RJ45 / 2x 10G RJ45 / 2x 10G SFP+ |
| [QNAP QSW-M2106PR-2S2T](https://amzn.to/4iF3Lrj) | 1U | Switch Managed, 6x 2.5G RJ45 (PoE, PoE+, PoE++) / 2x 10G RJ45 (PoE, PoE+, PoE++) / 2x 10G SFP+ |
| [QNAP QSW-M2108R-2C](https://amzn.to/4gNoaJ4) | 1U | Switch Managed, 8x 2.5G RJ45 / 2x 10G RJ45/SFP+ |
| [QNAP QSW-M3212R-8S4T](https://amzn.to/4fBPOaY) | 1U | Switch Managed, 4x 10G RJ45 / 8x 10G SFP+ |
| [QNAP QSW-M3216R-8S8T](https://amzn.to/3VOc1eP) | 1U | Switch Managed, 8x 10G RJ45 / 8x 10G SFP+ |
| [QNAP QSW-M7308R-4X](https://amzn.to/3ZO0e0X) | 1U | Switch Managed, 4x 100G QSFP28 / 8x 25G SFP28 |
| [YuanLey YS2083GS-P](https://amzn.to/41Y3qKv) | 1U | Switch Unmanaged, 8x 1G RJ45 (PoE, PoE+) / 2x 1G RJ45 / 1x 1G SFP | 

Note: Some switches intended for full-width rack mount ears _may_ work in a 10" rack with 'universal' rack ears, like the [Pelopy Adjustable Universal Rack Mount Ear Kit](https://amzn.to/4gJ7BxT).

Some manufacturers require special kits for 10" rack compatibility:

  - Mikrotik offers the [RMK-2/10 kit](https://amzn.to/3Pmm5rT) for full 10" compatibility
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

### <a name="other-gear"></a>Other Gear

Sometimes there are interesting things that don't fit into any other category.

| Model (incl. Link)    | Unit Height | Additional information | 
| :-------- | :------- | :------- |
| [DSIT 12V design LED lighting system - white](https://www.serverrack24.com/10-inch-design-led-lighting-system-white.html) | 1U | Colour of light: white |
| [DSIT 12V design LED lighting system - multicolor](https://www.serverrack24.com/10-inch-design-led-lighting-system-multicolor.html) | 1U | Colour of light: white, red, green, blue |

### <a name="3d-printable-systems"></a>3D Printable mini rack systems

Some makers have created entire mini rack 'systems', where you 3D print a faceplate (or cut it out of metal, like with [SendCutSend](https://sendcutsend.com)), and insert different types of gear, like SBCs, SSDs, mini network switches, etc.

This section is for _systems_, not individual 3D printable parts. For parts like cable modem or mini switch mounts, please see the respective sections elsewhere.

  - [JaredC01's LabStack mini](https://github.com/JaredC01/LabStack)
  - [monkizzle's MiniRax system](https://makerworld.com/en/collections/4692516)
  - [bwees' 3D Printable Mini Rack](https://www.printables.com/model/1170708-modular-10-rack)
  - [The Open Node Project - 3U 10" 3D Printable Rack](https://github.com/garrettekinsman/OpenNode/)
  - [Uptime Lab - Raspberry Pi Server Mark III](https://uplab.pro/2020/12/raspberry-pi-server-mark-iii/)
  - [Mauker's 10-inch rack mounts](https://makerworld.com/en/collections/2928697)
  - [dalovering's fully 3D printable half-width server rack and trays](https://www.printables.com/model/358304-fully-printable-half-width-server-rack-and-trays)
  - [jazwa's rackstack - modular 3D printable mini rack system](https://github.com/jazwa/rackstack)
  - [Paul Grove's 3D Cube Rack](https://www.printables.com/model/688952-cube-rack-10-inch-network-cabinet-server-rack)
  - [axiopaladin's ButterflyRack - modular, 3D printed frame for metal rails](https://github.com/axiopaladin/ButterflyRack)
  - [Mauker1's Tiny-Rack 6" and 10" 3D Printable Rack Mount System](https://github.com/geerlingguy/mini-rack/issues/105)
  - [MRP's 3D Printable 10" Mini Rack](https://www.printables.com/model/1173672-10-mini-rack-all-3d-printable)

### <a name="mini-pc-server-shelves"></a>Mini PC / Server Shelves

There are a variety of commercial options to mount Mini ITX motherboards (or SBC clusterboards, like the Turing Pi 2, or DeskPi Super6C!), or to mount Tiny/Mini/Micro PCs like a Lenovo M series computer.

  - [GeeekPi / DeskPi RackMate Mini ITX 1U shelf](https://amzn.to/3ZKq5qV)
  - [MyElectronics 10" 2U Mini ITX Short-Depth PC enclosure](https://amzn.to/41H6wCe)

### <a name="sbc-shelves"></a>SBC Shelves

SBCs, or Single Board Computers, are ideal for mini racks, due to their low power, thermal, and space requirements. You can often fit multiple SBCs per U of rack space, and there are many mini rack setups centered around an SBC cluster, or SBC routers or storage devices.

| Model (incl. Link)    | Unit Height | Additional information | 
| :-------- | :------- | :------- |
| [GeeekPi / DeskPi RackMate SBC Shelf](https://amzn.to/49H76C6) | 1U | 2x Raspberry Pi 4B/5, 2x NVidia Jetson Nano (Super), 2x 2.5" HDD/SSD |
| [GeeekPi / DeskPi RackMate Rack Mount](https://amzn.to/4glDzjL) | 2U | 4x Raspberry Pi 4B/5 with M.2 NVMe |
| [Makerworld Arduino Uno Rack Mount](https://makerworld.com/en/models/1011789) | 2U | 3x Arduino Uno, 3D printable |
| [Makerworld Raspberry Pi Zero Rack Mount](https://makerworld.com/en/models/982725) | 1U | 1x/3x Raspberry Pi Zero/Zero W/Zero 2 W, 3D printable |
| [Racknex UM-SBC-30x Shelf](https://racknex.com/shop/raspberry-pi/?filter_rack=10-inch) | 1U, 2U | Raspberry Pi 2B/3B/3B+/4B/5 |

### <a name="disk-shelves"></a>Disk Shelves

It can be difficult to adapt storage devices (especially full 3.5" hard drives!) into a mini rack, but there are always solutions—sometimes as simple as placing a 2-bay NAS on its side, or putting an entire 4-bay NAS on a shelf!

  - [GeeekPi / DeskPi RackMate SBC Shelf](https://amzn.to/49H76C6) (can hard-mount two 2.5" or 3.5" HDDs side by side)
  - [10" Rack Hard Drive Mount](https://www.printables.com/model/142325-10-rack-harddrive-mount) (can hard-mount two 3.5" drives)

### <a name="shelves-and-blanking-panels"></a>Shelves and Blanking Panels

Not all gear can be mounted on rack rails. And not every U of space needs to be filled. Often, a device needs extra room above or below for cooling or for an accessory that sticks out. In these cases, you can employ a rack shelf or blanking panels.

| Model (incl. Link)    | Unit Height | Additional information | 
| :-------- | :------- | :------- |
| All Metal Parts Half-Rack Blank Panel | [0.33U](http://www.allmetalparts.co.uk/768-1-3u-95-inch-half-rack-blank-panel-5055726299479.html), [0.5U](http://www.allmetalparts.co.uk/852-1-2u-95-inch-half-rack-blank-panel.html), [1U](http://www.allmetalparts.co.uk/half-rack-panels/355-1u-half-rack-blank-panel-5055726200017.html), [2U](http://www.allmetalparts.co.uk/half-rack-panels/356-2u-95-inch-half-rack-blank-panel-5055726200024.html), [3U](http://www.allmetalparts.co.uk/half-rack-panels/357-3u-half-rack-blank-panel-5055726200031.html) |  |
| All Metal Parts Half-Rack Perforated Vented Blank Panel | [0.5U](http://www.allmetalparts.co.uk/790-1-2u-95-inch-half-rack-perforated-vented-blank-panel.html), [1U](http://www.allmetalparts.co.uk/half-rack-panels/361-1u-half-rack-perforated-vented-blank-panel-5055726200079.html), [2U](http://www.allmetalparts.co.uk/half-rack-panels/374-2u-half-rack-perforated-vented-blank-panel-5055726203728.html), [3U](http://www.allmetalparts.co.uk/half-rack-panels/363-3u-half-rack-perforated-vented-blank-panel-5055726203735.html) |  |
| All Metal Parts Half-Rack Slot Vented Blank Panel | [0.5U](http://www.allmetalparts.co.uk/637-1-2u-95-inch-half-rack-slot-vented-blank-panel-5055726299486.html), [1U](http://www.allmetalparts.co.uk/half-rack-panels/358-1u-half-rack-vented-slotted-panel-5055726200048.html), [2U](http://www.allmetalparts.co.uk/half-rack-panels/359-2u-half-rack-vented-slotted-panel-5055726200055.html), [3U](http://www.allmetalparts.co.uk/half-rack-panels/360-3u-half-rack-vented-slotted-panel-5055726200062.html) |  |
| Delock Network Cabinet Blind Cover | [1U](https://www.delock.com/produkt/66576/merkmale.html), [2U](https://www.delock.com/produkt/66578/merkmale.html) | Tool free |
| Delock Network Cabinet Panel with Opening | [1U](https://www.delock.com/produkt/66672/merkmale.html), [2U](https://www.delock.com/produkt/66673/merkmale.html) |  |
| Delock Network Cabinet Panel with Ventilation Slots I | [1U](https://www.delock.com/produkt/66839/merkmale.html), [2U](https://www.delock.com/produkt/66840/merkmale.html), [3U](https://www.delock.com/produkt/66841/merkmale.html), [4U](https://www.delock.com/produkt/66842/merkmale.html) |  |
| Delock Network Cabinet Panel with Ventilation Slots II | [1U](https://www.delock.com/produkt/66984/merkmale.html), [2U](https://www.delock.com/produkt/66986/merkmale.html) | Tool free |
| [Digitus Shelf Perforated Steel Shelf](https://amzn.to/4014ATT) | 1U |  |
| [Flyht Pro Rack Tray Mount](https://www.thomann.de/intl/flyht_pro_rack_tray_95_1u_mount.htm) | 1U | With cross holes |
| Flyht Pro Rack Tray | [1U](https://www.thomann.de/intl/flyht_pro_rack_tray_1u_95.htm), [2U](https://www.thomann.de/intl/flyht_pro_rack_tray_2u_95.htm), [3U](https://www.thomann.de/intl/flyht_pro_rack_tray_3u_95.htm) | 3U variant has ventilation slots |
| Flyht Pro Rack Panel Air | [1U](https://www.thomann.de/intl/flyht_pro_rack_panel_air_1u_95.htm), [2U](https://www.thomann.de/intl/flyht_pro_rack_panel_air_2u_95.htm) |  |
| Flyht Pro Rack Panel | [1U](https://www.thomann.de/de/flyht_pro_rack_panel_1u_95.htm), [2U](https://www.thomann.de/intl/flyht_pro_rack_panel_2u_95.htm), [3U](https://www.thomann.de/intl/flyht_pro_rack_panel_3u_95.htm) |  |
| GeeekPi / DeskPi Rackmate Rack Shelf with Supports | [0.5U](https://amzn.to/4fjuuGY), [1U](https://amzn.to/3ZZJq8T) |   |
| GeeekPi / DeskPi Solid Blanking Panel | [1U](https://amzn.to/3BLnox3), [2U](https://deskpi.com/products/deskpi-rackmate-accessories-2u-blank-panel-for-10-inch-server-rack-network-cabinet) |  |
| GeeekPi / DeskPi Vented Blanking Panel | [1U](https://amzn.to/49KQPMf), [2U](https://deskpi.com/products/deskpi-rackmate-accessories-2u-venting-blank-panel) | 1U variant can hold 2x 40mm fan, 2U variant can hold 2x 70mm/80mm fan |
| [INTELLINET 10" Blank Panel](https://amzn.to/3ZGa6tN) | 1U |  |
| [INTELLINET 10" Vented Cantilever Shelf](https://amzn.to/3BM80jY) | 1U |  |
| [L-com Half Rack Blank Panel](https://www.l-com.com/patch-panel-server-rack-1-space-half-rack-blank-panel-175) | 1U |  |
| [L-com Half Rack Quiet Blower Panel](https://www.l-com.com/patch-panel-server-rack-half-rack-quiet-blower-panel-50-cfm) | 1U | 50 CFM |
| [L-com Half Rack Universal Multi Shelf](https://www.l-com.com/patch-panel-server-rack-half-rack-1-space-universal-multi-shelf-55-deep-black) | 1U | 5.5" deep |
| L-com Half Rack Vent Panel | [1U](https://www.l-com.com/patch-panel-server-rack-1-space-half-rack-vent-panel-175), [2U](https://www.l-com.com/patch-panel-server-rack-2-space-half-rack-vent-panel-350) |  |

## <a name="cable-management"></a>Cable Management

Mini racks can quickly turn from beauty into beast, once you start plugging things into each other! Larger racks usually have areas where cables can be routed for a tidy finish and easy maintenance, but mini racks often don't have room. So you can add on accessories to tidy up unsightly cable messes.

| Model (incl. Link)    | Unit Height | Additional information | 
| :-------- | :------- | :------- |
| [Ad-Tek / Network-Cabs Cable Management Panel with Hooks](https://www.network-cabs.co.uk/product/ad-tek-network-cabs-1u-10-inch-mini-recessed-cable-management-panel-370) | 1U | Recessed, 2x vertical hook |
| Delock Cable Management Brush Strip I | [1U](https://www.delock.com/produkt/66287/merkmale.html), [2U](https://www.delock.com/produkt/66481/merkmale.html) |  |
| Delock Cable Management Brush Strip II | [1U](https://www.delock.com/produkt/66343/merkmale.html), [2U](https://www.delock.com/produkt/66345/merkmale.html) | Tool free |
| [Delock Cable Management Brush Strip with Cable Fixing](https://www.delock.com/produkt/66845/merkmale.html) | 1U |  |
| [Delock Cable Management Brush Strip with Cable Support Plate](https://www.delock.com/produkt/66483/merkmale.html) | 1U |  |
| [Delock Cable Management Brush Strip with Hooks](https://www.delock.com/produkt/66487/merkmale.html) | 1U | 2x brush, 3 x vertical hook |
| [Delock Cable Management Brush Strip with Rings](https://www.delock.com/produkt/66485/merkmale.html) | 1U | 1x brush, 2 x vertical D-Ring hook |
| [Delock Cable Management Routing Panel with Hooks](https://www.delock.com/produkt/66847/merkmale.html) | 1U |  2 x horizontal and 1 x vertical hook |
| [Delock Cable Management Routing Panel with Rings I](https://www.delock.com/produkt/43342/merkmale.html) | 1U | 3x D-Ring hook |
| [Delock Cable Management Routing Panel with Rings II](https://www.delock.com/produkt/66666/merkmale.html) | 1U | Angled, 2 x vertical D-Ring hook |
| Delock Cable Management Routing Panel with Opening | [1U](https://www.delock.com/produkt/66843/merkmale.html), [2U](https://www.delock.com/produkt/66844/merkmale.html) | Covered, 2U variant has 2 openings |
| [Delock Cable Support Rail I](https://www.delock.com/produkt/66677/merkmale.html) | 1U |  |
| [Delock Cable Support Rail II](https://www.delock.com/produkt/66678/merkmale.html) | 1U | Recessed |
| [Digitus Cable Management Brush Strip](https://www.amazon.com/Digitus-Cable-Entry-Panel-Brush/dp/B08T19L6LR) | 0.5U |  |
| [Digitus Cable Management Routing Panel with Hooks](https://www.amazon.com/Digitus-Cable-Jumper-Panel-Brackets/dp/B08T1JJQD2) | 1U | 3x vertical hook |
| [GeeekPi / DeskPi Cable Entry Brush Panel](https://amzn.to/3DvacwM) | 0.5U |  |
| [GeeekPi / DeskPi Horizontal Cable Manager with Hooks](https://amzn.to/4gwE6PE) | 0.5U | 3x D-Ring hook |
| [INTELLINET Cable Management Panel with Rings](https://amzn.to/3ZY8BZa) | 1U | 3x retaining ring  |
| [INTELLINET Cable Management Routing Panel with Opening](https://amzn.to/4fr239U) | 1U | Covered |


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
| lukehoersten | 2025 | [Unifi 2.5Gbps Homelab 9U Mini Rack](https://github.com/geerlingguy/mini-rack/issues/79) |
| derek-tattersall | 2025 | [Homemade mini-rack](https://github.com/geerlingguy/mini-rack/issues/81) |
| ben-parker | 2025 | [The "network pile to network rack" mini rack](https://github.com/geerlingguy/mini-rack/issues/89) |
| aej-comp | 2025 | [DIY 10" Server Rack \| Open Frame](https://github.com/geerlingguy/mini-rack/issues/94) |
| monkizzle | 2025 | [MiniRax Pi 5 5G Router Ecoflow Showcase](https://github.com/geerlingguy/mini-rack/issues/97) |
| avrono | 2025 | [Cheap Wooden DIY Mini Rack](https://github.com/geerlingguy/mini-rack/issues/98) |
| bwees | 2025 | [Another 3D Printed Rack Design](https://github.com/geerlingguy/mini-rack/issues/100) |
| Chris Borge | 2025 | [Modular 3D-Printed CNC Controller](https://github.com/geerlingguy/mini-rack/issues/103) |
| wildegnux | 2025 | [Sideways IKIEA PAX rack](https://github.com/geerlingguy/mini-rack/issues/110) |
| hcschmitt | 2025 | [RackMate T0 to Organize my Mess](https://github.com/geerlingguy/mini-rack/issues/116) |
| jcmarinn | 2025 | [8U Extended-depth Custom 10" Rack](https://github.com/geerlingguy/mini-rack/issues/123) |

[Browse all issues tagged 'build showcase'](https://github.com/geerlingguy/mini-rack/labels/build%20showcase) (includes in-progress builds).

## <a name="software"></a>Software

There's a ton of things you can do in a Homelab—and many of them run perfectly fine on mini PCs or SBCs in a mini rack!

Here's a collection of cluster-related projects that may be a good test or starting point for your own rack, if you need the inspiration:

  - [Pi Cluster](https://github.com/geerlingguy/pi-cluster) - Build a K3s cluster with 3 or more SBCs
  - [Pi Hosted](https://pi-hosted.com) - Docker and Portainer-based Pi hosting
  - [Top500 Benchmark](https://github.com/geerlingguy/top500-benchmark) - Benchmark your cluster with HPL (High Performance Linpack)

## <a name="license"></a>License

GPLv3 or later

## <a name="open-source-repository"></a>Open Source Repository

This website is generated from the [`geerlingguy/mini-rack`](https://github.com/geerlingguy/mini-rack) GitHub repository.

## <a name="author"></a>Author

[Jeff Geerling](https://www.jeffgeerling.com)
