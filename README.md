# Esp32-micropython-boot

> Version: 1.0

esp32 Micropython boot.py ，实现：Wi-Fi联网管理、程序更新，等基础固件功能


## 编译固件

git clone https://gitee.com/EspressifSystems/esp-idf.git
cd esp-idf 
git checkout v4.2
git submodule update --init --recursive
./tools/set-submodules-to-github.sh 
./install.sh
. ./export.sh

cd ports/esp32
make submodules
make




##

idf.py -D MICROPY_BOARD=GENERIC -B build-GENERIC  -p /dev/tty.usbserial-1420   -b 460800 erase_flash

idf.py -D MICROPY_BOARD=GENERIC -B build-GENERIC  -p /dev/tty.usbserial-1420   -b 460800 flash     