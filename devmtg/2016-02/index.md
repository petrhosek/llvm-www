---
layout: "default.html"
permalink: "devmtg/2016-02/index.html"
---
# Clang/LLVM Sprint Weekend hosted by Bloomberg

1.  [What is it?](#what)
2.  [Logistics (General)](#logistics-general)
3.  [Logistics (New York)](#logistics-newyork)
4.  [Logistics (London)](#logistics-london)

*   **What**: Gathering of developers from the LLVM community to hack on Clang, LLVM, and other projects.
*   **When**: Feb 6-7, 2016
*   **Where**: New York, NY, USA and London, UK

# What is it?

[Bloomberg](http://bloomberg.com/company/technology) is hosting a gathering of developers, students, and others from around the Clang/LLVM community to spend a weekend learning how to work on Clang, LLVM, and other projects in the LLVM ecosystem. This event is intended to help new community members get started learning how to contribute, how to work on the code, and get their first patches written and submitted.

Bloomberg is providing the space, food, beverages, travel/lodging for mentors, and the organization of the event, so attendees only need to bring their laptops (with power adapters!) and a willingness to learn and contribute. At both locations there will be experienced mentors on hand to provide guidance.

# Logistics (General)

The Google Group (mailing list) [clang-llvm-sprint-2016-bloomberg@googlegroups.com](https://groups.google.com/forum/#!forum/clang-llvm-sprint-2016-bloomberg) can be used to discuss issues of general interest related to the weekend.

Kevin Fleming and Henry Kleynhans are organizing this event, in New York and London, respectively. They can be contacted through the mailing list or via the EventBrite pages (linked below).

## IRC and Social Media

Attendees at this event, and anyone else who wants to chat with them, should use channel **#bbgweekend** on irc.oftc.net.

If you want to talk about this event on Twitter, please tag TechAtBloomberg (@techatbloomberg).

## Project Planning and Tracking

The event is using a Trello board to track projects and the teams that are working on them. The board can be found [here](https://trello.com/b/zF3DqT7G/clang-llvm-sprint-weekend-feb-6-7-2016).

## Getting Started Quickly with a Virtual Machine

A virtual machine image is available, based on Ubuntu Linux 14.04, that you can use to get your laptop ready for the event quickly. You'll need a virtualization package (hypervisor); the image was created using VirtualBox 5, but has been tested with VMware and other hypervisors. Since it is a generic image, when you import it you'll need to ensure that you supply the VM with adequate CPU and memory resources; while you can build LLVM with only one CPU and 4GB of memory, it will be slow enough to be inconvenient.

New York event attendees should download the image [here](https://s3.amazonaws.com/bbg-misc-us/llvm_1.ova).

London event attendees should download the image [here](https://s3-eu-west-1.amazonaws.com/bbg-misc-eu/llvm_1.ova).

When you boot the image into a machine, you can log in with user 'llvm', password 'llvm'. As is typical with Ubuntu systems, this user has sudo privileges, so you can install additional software or make configuration changes.

Note: if you use VMware to load this image, you may receive a warning about the image being non-compliant with the Open Virtualization specification; allow the import to proceed anyway, and you'll have a working VM.

# Logistics (New York)

*   **Location**: [Civic Hall](http://civichall.org/), 156 Fifth Avenue, New York, NY, 10010 USA
*   **Time/Date**: Feb 6, 2016 9:30AM-10:00PM and Feb 7, 2016 9:30AM-5:00PM
*   **Registration**: Register on [EventBrite](https://www.eventbrite.com/e/clangllvm-sprint-hosted-by-bloomberg-registration-20770403837)

## Mentors

*   Marshall Clow
*   Sophia D'Antoine
*   Keno Fischer
*   Philip Reames
*   Chad Rosier
*   Matt Simpson

## Venue and Catering

Civic Hall is located at the intersection of 20th Street and Fifth Avenue in Manhattan. You'll enter through the [main entrance](civichallentrance.jpg) on Fifth Avenue, then take either the stairs (on your left) or the elevator bank (labeled East Elevators) on your right, to the second floor. If you have any questions or need assistance, the security guard just inside the lobby will be happy to help you.

When you arrive at the second floor, there will be a check-in desk, so please stop there to ensure that we know you've arrived. You'll then be directed to the [hacking space](civichallhackspace.jpg), where you can find a place to setup your laptop, and then head over to the kitchen to grab breakfast, coffee, juice, etc.

Note: If you arrive after 11AM, the check-in desk will no longer be present, so just enter through the main door to Civic Hall from the second floor landing, and check in at the main Civic Hall reception counter.

On both days, breakfast and lunch will be provided; on Saturday, dinner will also be provided. Please review the [menu](newyorkmenu.html) in advance, and if for any reason the options available will not meet your requirements, let us know, but be prepared to make alternate arrangements for meals. There are a large number of places to obtain food (from delis to sandwich shops to sit-down restaurants) in the area around Civic Hall, so you should be able to find something compatible.

### Meal Times

|  | Saturday | Sunday |
| --- | --- | --- |
| Breakfast | 9:30AM | 9:30AM |
| Lunch | 12:00PM | 12:00PM |
| Snacks | 2:00PM | 1:00PM |
| Dinner | 5:00PM |  |

# Logistics (London)

*   **Location**: [CodeNode](https://skillsmatter.com/contact-us), 10 South Place, London EC2M 7EB, GB
*   **Time/Date**: Feb 6, 2016 9:30AM-10:00PM and Feb 7, 2016 9:30AM-5:00PM
*   **Registration**: Register on [EventBrite](https://www.eventbrite.com/e/clangllvm-sprint-hosted-by-bloomberg-registration-20710913901)

## Mentors

*   Nuno Lopes
*   Norman Rink
*   Boris Schäling

## Venue and Catering

CodeNode is located near the Moorgate and Liverpool Street stations. The [entrance](codenodeentrance.jpg) is on South Place, where someone at reception will assist you with registration. From there, make your way down the stairs on your right to the Space Bar. Here you will be directed to breakfast and to the ALT/TAB rooms where you can setup your laptop.

On both days, breakfast and lunch will be provided; on Saturday, dinner will also be provided. Please review the [menu](londonmenu.html) in advance, and if for any reason the options available will not meet your requirements, let us know, but be prepared to make alternate arrangements for meals. On Saturdays there are some shops open in the area around CodeNode, but none of them are open on Sundays, so you'd need to travel some distance away to find a place to purchase food.

### Meal Times

|  | Saturday | Sunday |
| --- | --- | --- |
| Breakfast | 9:30 | 9:30 |
| Lunch | 12:00 | 12:00 |
| Snacks | 14:00 | 13:00 |
| Dinner | 17:00 |  |

<!-- *********************************************************************** -->

* * *
