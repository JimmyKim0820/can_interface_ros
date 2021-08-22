# can_ros_interface
This is a ros package that communicates with a vehicle through CAN

![mylogo](https://user-images.githubusercontent.com/55337221/130344677-5c436f22-9f3b-4dc7-9da9-4beefc085799.png)


# Receiving and Decoding CAN data - ROS Package

---

This package collects and decodes the CAN data of the vehicle. It was made out of KIA Niro hybrid 2016, Mobileye, and personal vehicle simulator. In addition, data on KIA Niro hybrid 2016 and Mobileye were collected by requesting Awesome It Co., Ltd.

## Getting Started

---

- First, You need a CAN converter. (I used 'kvaser leaf light v2')
- Install this package.
- This package must be modified according to the CAN converter.

### Prerequisites

- Ubuntu 18.04 (Other versions available, but not tested)
- ROS Melodic (Other versions available, but not tested)
- Install Kvaser SDK for Ubuntu ([https://www.kvaser.com/linux-drivers-and-sdk-2/](https://www.kvaser.com/linux-drivers-and-sdk-2/))

```bash
$ tar -xvzf linuxcan.tar.gz
$ sudo apt-get install build-essential
$ cd linuxcan
$ make
$ sudo make install
$ cd canlib
$ make
$ sudo make install
$ cd ..
$ cd common
$ make
$ sudo ./installscript.sh
```

- Install python-can ([https://python-can.readthedocs.io/en/2.1.0/index.html](https://python-can.readthedocs.io/en/2.1.0/index.html)) with pip

```bash
$ pip install python-can
```

### Run the Program

- Please change the codes' permissions in src with chmod
- Niro and Mobileye

```bash
$ roslaunch kaai_can can_all.launch
```

### Check the data

- topics :

    msg_n                      // raw data about Niro

    msg_m                     // raw data about Mobileye

    niro_can                   // decoded data about Niro

    mobileye_can          // decoded data about Mobileye

- check the topics with rostopic

```bash
$ rostopic echo [topic]
```

## Pictures

---

![echo_niro](https://user-images.githubusercontent.com/55337221/130344684-b355c934-e027-4223-bc93-80f076310727.png)

Niro

![echo_mobileye](https://user-images.githubusercontent.com/55337221/130344687-c2e9576e-bf28-42a3-9b55-60e0160ded94.png)

Mobileye

## Tested

---

- Cars :

    KIA Niro Hybrid 2016

    Mobileye 5

    Personal vehicle simulator (KaAI Lab, Kookmin Univ.)

- CAN converter :

    kvaser leaf light v2

- OS :

    Ubuntu 18.04 

- ROS :

    ROS Melodic
