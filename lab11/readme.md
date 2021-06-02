 1. Сделать image контейнера с необходимым ПО для запуска sshd

[Dockerfile](dockerfile)

[docker-compose](docker-compose.yml)

2. Запустить docker-compose поднять два ssh сервера
```
`docker-compose up --build -d`
```

3. Вход по паролю

![](1.1.png)
![](1.2.png)

4. Вход по ключу

1 to 2

![](2.png)

2 to 1

![](3.png)

5. Выполнить команду

![](4.png)

6. Передать файл

![](5.png)

7. Продемонстрировать простейший обмен данными с помощью утилиты netcat

Send

![](6.png)

Recieve

![](7.png)
