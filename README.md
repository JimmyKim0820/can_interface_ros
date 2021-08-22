# can_ros_interface
This is a ros package that communicates with a vehicle through CAN

# Untitled

![mylogo](mylogo.png "my logo")

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

![Untitled%20b0917cf63cc84694bc5ee9eca6b62f28/Screenshot_from_2021-05-21_15-51-49.png](Untitled%20b0917cf63cc84694bc5ee9eca6b62f28/Screenshot_from_2021-05-21_15-51-49.png)

Niro

![Untitled%20b0917cf63cc84694bc5ee9eca6b62f28/Screenshot_from_2021-05-21_15-51-49%201.png](Untitled%20b0917cf63cc84694bc5ee9eca6b62f28/Screenshot_from_2021-05-21_15-51-49%201.png)

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
