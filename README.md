# 3DOSM

Инструкция по запуску:
1) Скачать .mbtiles файлы, которые хотим показывать на карте. Например Москва - https://data.maptiler.com/downloads/dataset/osm/russia/moscow/#7.51/55.665/37.615
Так же можно воспользоваться сервисом https://extract.bbbike.org/

![image](https://github.com/GreatKing4615/3DOSM/assets/59148289/731208ef-edbf-47c7-9af4-ccc80c36f650)

нужно указать какого формата необходимы данные, местоположение и почту, куда придет уведомление о готовности конвертации данных

2) поместить его по такому адресу 3DOSM\tileserver-data
3) в папке 3d-osm выполнить npm install
4) правильным образом создать контейнер с TailServer смог только Docker Desctop. Не могу сказать почему - при запуске с cmd у меня он так и не увидел volume с данными

 ![image](https://github.com/GreatKing4615/3DOSM/assets/59148289/8e20aace-4f44-4737-b385-e8d36dbd5858)

5) ТейлСервер готов - можно посмотреть на него по http://localhost:8080/
6) Для запуска реакт приложения необходимо перейти в директорию 3d-osm
7) выполнить npm install (у меня v16.14.0 версия node и 9.8.0 npm )
8) npm start

карта будет доступна по http://localhost:3000/

## Изменение стилей карты:
Сейчас стиль захардкожен в 3d-osm\src\components\map.js 12 строка
для изменения стилей необходимо выбрать название стиля из tileserver-data\config.json объекта styles

## Добавление своих стилей
Для добавления своего стиля можно использовать maputnik
https://hub.docker.com/r/maputnik/editor
после чего экспортировать стиль
добавить его в tileserver-data\styles
и прописать в tileserver-data\config.json

## Добавление своих карт:
Для этого:
1) нужные .mbtiles данные необходимо положить в tileserver-data
2) в tileserver-data\config.json добавить в "data" новый объект с любым названием (в примере v3) и прописать пусть к .mbtiles файлу

