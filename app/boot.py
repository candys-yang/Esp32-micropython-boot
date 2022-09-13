'''
测试
'''
import network      
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Meidong_Guest','GDdadong2013') 
import webrepl
webrepl.start(password='Esp32Room')






