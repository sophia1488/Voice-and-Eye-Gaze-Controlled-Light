# FreeRTOS AWS Reference Integrations

## Cloning
This repo uses [Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) to bring in dependent components.

Note: If you download the ZIP file provided by GitHub UI, you will not get the contents of the submodules. (The ZIP file is also not a valid git repository)

To clone using HTTPS:
```
git clone https://github.com/aws/amazon-freertos.git --recurse-submodules
```
Using SSH:
```
git clone git@github.com:aws/amazon-freertos.git --recurse-submodules
```

If you have downloaded the repo without using the `--recurse-submodules` argument, you need to run:
```
git submodule update --init --recursive
```

## Important branches to know
master            --> Development is done continuously on this branch  
release           --> Fully tested released source code  
release-candidate --> Preview of upcoming release  
feature/*         --> Alpha/beta of an upcoming feature  

## Getting Started

For more information on FreeRTOS, refer to the [Getting Started section of FreeRTOS webpage](https://aws.amazon.com/freertos).

To directly access the **Getting Started Guide** for supported hardware platforms, click the corresponding link in the Supported Hardware section below.

For detailed documentation on FreeRTOS, refer to the [FreeRTOS User Guide](https://aws.amazon.com/documentation/freertos).


## amazon-freeRTOS/projects
The ```./projects``` folder contains the IDE test and demo projects for each vendor and their boards. The majority of boards can be built with both IDE and cmake (there are some exceptions!). Please refer to the Getting Started Guides above for board specific instructions.

## Mbed TLS License
This repository uses Mbed TLS under Apache 2.0

## How to start?

*OS: Ubuntu 18*

This project is cloned from [aws/amazon-freertos](https://github.com/aws/amazon-freertos), with slight modifications in file `demos/mqtt/iot_demo_mqtt.c`

1. Prerequisites: Follow the [instructions](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_espressif.html#build-and-run-example-espressif) till 'Set up your development environment'

2. Clone the code.

3. **Modify "configure.json"** to suite your environment. 

   `vim ./tools/aws_config_quick_start/configure.json` 

   ```
   { 
   	"afr_source_dir": "/home/amazon-freertos", 
   	"thing_name": "my_device", 
   	"wifi_ssid": "", 
   	"wifi_password": "", 
   	"wifi_security": "eWiFiSecurityWPA2" 
   }
   ```

4. Run `python3 SetupAWS.py setup`, make sure that package `boto3` has already been installed.

5. Environment setting 

   `export PATH="$HOME/esp/xtensa-esp32-elf/bin:$PATH"`

6. Change directories to the root of your FreeRTOS download directory and use the following command to generate the build directory: 

   `mkdir build cmake -DVENDOR=espressif -DBOARD=esp32_wrover_kit -DCOMPILER=xtensa-esp32 -S . -B build`

7. Flash and run

   `cd build make all -j4 sudo make flash`