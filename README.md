# Классификация овощей по фотографиям
Репозиторий для выполнения годового проекта 1-го года магистерской программы НИУ ВШЭ "Машинное обучение и высоконагруженные системы".
## Описание проекта
Задачей данного проекта является создание сервиса для распознавания изображений различных овощей по фотографии. 
На текущий момент для распознавания изображений используется алгоритм классического машиннрго обучения - SVM(Метод опорных векторов).
Для взаимодействия с с ML-моделью был реализован [web-сервис](http://158.160.85.19:5051/) с помощью библиотеки [FastAPI](https://fastapi.tiangolo.com/).
Также был реализован [бот](https://web.telegram.org/a/#6944300570) в Telegram с помощью библиотеки [AIOgram](https://docs.aiogram.dev/en/latest/).
## Запуск проекта
Пререквизиты:
 - Docker;
 - Python 3.8 или выше (для запуска без Docker).

Запуск через Docker:
1. Клонировать репозиторий к себе на локальную машину
   ```
   git clone https://github.com/NickolayD/HSE_Image_Classification.git
   ```
2. Перейти в папку скачанного проекта
   ```
   cd HSE_Image_Classification
   ```
3. Запустить контейнеры через docker-compose
   ```
   docker-compose up
   ```
