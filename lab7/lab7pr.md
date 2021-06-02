1. Произвести настройку IP адреса сетевого интерфейса eth0 через конфиг и на лету
- Через конфиг:

![](1.png)

```
systemctl restart networking
```
-на лету
```
ifconfig eth0 192.168.0.2
```
2. Остановить и запустить сетевой интерфейс eth0

```
ifconfig eth0 down
```
```
ifconfig eth0 up
```
3. Произвести смену аппаратного (MAC) адреса сетевого интерфейса eth0;

![](3-1.png)

![](3-2.png)

4. Показать таблицу сетевых маршрутов. Установить маршрут по умолчанию;

![](4.png)

5. Получить 
настройки IP от DHCP сервера;
```
iface eth0 inet dhcp
```

![](5.png)

6. Проверить пропускную способность между виртуальными машинами

![](6.png)

7. Hастроить связь между виртуальными машинами через vlan 15

![](7-1.png)

![](7-2.png)
![](7-3.png)