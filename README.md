# Esp32-micropython-boot

> Version: 1.0

esp32 Micropython boot.py ，实现：Wi-Fi联网管理、程序更新，等基础固件功能


## 编译固件

IDF版本: 
ESP32-S3 >= v4.4, ESP32-S2\C3 >=4.3.1。


```
git clone -b v4.0.2 --recursive https://github.com/espressif/esp-idf.git
cd esp-idf
./install.sh       # (or install.bat on Windows)
source export.sh   # (or export.bat on Windows)
```

构建MicroPython交叉编译器
```
make -C mpy-cross
cd esp32
make submodules
make

```
