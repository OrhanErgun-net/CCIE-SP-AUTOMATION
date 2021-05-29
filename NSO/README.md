# Cisco NSO

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-nso">About NSO</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a
        href="#downloading-nso">Downloading NSO </a></li>
        <li><a href="#installation">Installation</a></li>
        <ul>
          <li><a href="#neds">NEDs</a></li> 
      </ul>
    </li>
    <li><a href="#instance-setup">Instance Setup</a></li>
      </ul>
    </li>
    <li>
    <a href="#nso-cli">NSO CLI</a>
      <ul>
        <li><a href="#authentication-group">Authentication Group</a></li>
      </ul>
      <ul>
        <li><a href="#add-device">Add Device</a></li>
      </ul>
      <ul>
        <li><a href="#test-device-connectivity">Test Device Connectivity</a></li>
      </ul>
    </li>
    <li>
    <a href="#connect-and-select">Connect and Select</a>
      <ul>
        <li><a href="#check-packages">Check Packages</a></li>
      </ul>
      <ul>
        <li><a href="show">Show Run</a></li>
      </ul>
      <ul>
        <li><a href="#test-device-connectivity">Test Device Connectivity</a></li>
      </ul>
  </ol>
</details>


<!-- ABOUT NSO -->
## About NSO

> ####  _Cisco_ Network Services Orchestrator

* Cisco Product based on Linux OS.
Mainly used to Orchestrate  network devices.
* Support physical and virtual multi-vendor OS.
* Common used with scaling service provider networks.


<!-- GETTING STARTED -->
## Getting Started

This was done in parallel with Orhan's CCIE SP video course. 

* NSO 5.5 is used


### Prerequisites

The following config are applied on Debian or 
* Development tools
  ```sh
  apt install libxml2-utils
  ```

* JAVA
  ```sh
  apt install default-jdk
  ```

* Apache Ant
  ```sh
  apt install ant
  ```

### Downloading NSO

1. Use Firefox within your Linux VM
2. Login with your Cisco account at  [https://developer.cisco.com/](https://developer.cisco.com/)

3. Open NSO doc  [https://developer.cisco.com/docs/nso/](https://developer.cisco.com/docs/nso/#!getti\and-installing-nso/getting-nso)
   
4. Download NSO 5.x directly into **Downloads** directory



### Installation
 * #####  NSO `5.5` is used in the following, Always make sure what version are you using.
 * ##### Check the latest version and release numbers

1. Navigate to **Downloads** directory
   ```sh
   cd ~/Downloads
   ```
2. Extract installation files
   ```sh
   sh nso-5.5.linux.x86_64.signed.bin
   ```
3. Start installation into `$HOME` directory
   ```sh
    sh nso-5.5.linux.x86_64.installer.bin --local-install ~/nso-5.5
   ```
4. Source **ncs** file
   ```sh
    source $HOME/nso-5.5/ncsrc
    ```
5. [Optional] you may source permanently to **.bashrc** file
   ```sh
    echo "source $HOME/nso-5.5/ncsrc" >> $HOME/.bashrc
    source ~/.bashrc
    ```

<!-- NEDs -->
### NEDs
Updating NEDs with latest from same Cisco NSO [download page.](https://developer.cisco.com/docs/nso/#!getti\and-installing-nso/getting-nso)
 
Check the latest `NEDs` version and release numbers, Cisco always updating it.

1. Download Cisco IOS-XE, IOS-XR, and NX-OS **NED files** directly into **Downloads** directory.

2. Same as NSO steps start with extracting installation files
   ```sh
   sh ncs-5.5-cisco-ios-6.69.1.signed.bin
   sh ncs-5.5-cisco-iosxr-7.33.1.signed.bin
   sh ncs-5.5-cisco-nx-5.21.4.signed.bin
   ```

3. Extract `.gz` files into NSO directory using **tar**
   ```sh
   tar -zxvf ~/Downloads/ncs-5.5-cisco-ios-6.69.1.tar.gz -C ~/nso-5.5/packages/neds/
   tar -zxvf ~/Downloads/ncs-5.5-cisco-iosxr-7.33.1.tar.gz -C ~/nso-5.5/packages/neds/
   tar -zxvf ~/Downloads/ncs-5.5-cisco-nx-5.21.4.tar.gz -C ~/nso-5.5/packages/neds/
   ```
<!-- Instance Setup -->
## Instance Setup

 Multiple instances could be created for different projects.

1. Use `ncs-setup` to create instances.
   ```sh
    ncs-setup --package ~/nso-5.5/packages/neds/cisco-ios-cli-6.69 \
      --package ~/nso-5.5/packages/neds/cisco-nx-cli-5.21 \
      --package ~/nso-5.5/packages/neds/cisco-iosxr-cli-7.33 \
      --dest nso-instance-02 --use-copy
   ```
2. To start the created instance, navigate to **instance directory** and run
   ```sh
   cd ~/nso-instance-02/
   ncs
   ```

3. Check NSO instance **status**
   ```sh
   ncs --status | grep status
   ```

<!-- NSO CLI -->
## NSO CLI

You may enter NSO **CLI** from any where by 

   ```sh
   ncs_cli -C -u admin
   ```


### Authentication Group

Used to place remote access **username** and **passwords** for targeted devices.

  ```sh
   devices authgroups group OE-NSO
   default-map remote-name cisco
   default-map remote-password cisco
   default-map remote-secondary-password cisco
  ```

### Add Device

When creating a device you will be placed under the created device **sub-mode**. Defining IP address, Protocol, and `NED`.

  ```sh
  devices device IOS-XE-01
   address 192.168.96.62
   authgroup OE
   device-type cli ned-id cisco-ios-cli-6.69
   device-type cli protocol ssh
   ssh host-key-verification none
   state admin-state unlocked
   commit
   ssh fetch-host-keys
  ```

### Test Device Connectivity

Check device connectivity by using one of the following commands.

  ```sh
   devices device IOS-XE-01 sync-from
   devices device IOS-XE-01 check-sync
  ```

<!-- Connect and Select -->
## Connect and Select

In this part troubleshooting and show command will be used. 



### Check Packages

For updating **NSO** packages `NEDs`.

  ```sh
  packages reload
  show packages package package-version
  show packages package oper-status
  ```

### Show Run

The good old `show run` command can be used within *NSO CLI*

  ```sh
  show running-config devices device IOS-XE-01   
  show running-config devices device IOS-XE-01 | de-select config
  ```

### Show Device Interfaces

*NSO* CLI provides a rich subset of methods to **parse** the output

  ```sh
    show running-config devices device IOS-XE-01 config interface
    show running-config devices device IOS-XE-01 config interface | display json
    show running-config devices device IOS-XE-01 config interface | display xml
    show running-config devices device IOS-XE-01 config interface Loopback * ip address

  ```
