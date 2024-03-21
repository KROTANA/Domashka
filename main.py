# from ultralytics import YOLO
# import torch
# import cv2
# from PIL import Image
#
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
#
#
# # Use the model
# results = model.train(data="config.yaml", epochs=30)

import os
import cv2
import easyocr
from ultralytics import YOLO

from PIL import Image
import  matplotlib.pyplot as plt

class DetectModel:
    def __init__(self):
        pass

    def crop_detected_objects(self, image, results):
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result


            cropped_image = image[int(y1):int(y2), int(x1):int(x2)]#ВАЖНЫЙ ОБЬЕКТ КОТОРЫЙ ИДЕТ НА ОБРАБОТКУ В ДРУГИЕ ФУНКЦИИ

            # Отображаем фотку вырезаного номера
            cv2.imshow("Cropped Object", cropped_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            self.recog(cropped_image)


    def Photo(self, photo):
        PROJECT_DIR = os.getcwd()
        model_path = os.path.join(PROJECT_DIR, 'runs', 'detect', 'train', 'weights', 'last.pt')
        model = YOLO(model_path)

        def detect_and_display_objects(image_path):
            # Загружаем изображение
            image = cv2.imread(image_path)

            # Применяем модель к изображению
            results = model(image)[0]

            # Вызываем функцию для обрезки обнаруженных объектов
            self.crop_detected_objects(image, results)

            for result in results.boxes.data.tolist():
                x1, y1, x2, y2, score, class_id = result

                # Рисуем обводку вокруг объекта
                cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)

                # Добавляем подпись с классом объекта
                class_name = results.names[int(class_id)]
                cv2.putText(image, class_name, (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Показываем изображение


        image_path = photo
        detect_and_display_objects(image_path)
    def Video(self,folder,video):
        # Получаем текущую директорию проекта
        PROJECT_DIR = os.getcwd()

        # Путь к папке с видео внутри проекта
        VIDEOS_DIR = os.path.join(PROJECT_DIR, folder)

        # Путь к видеофайлу
        video_path = os.path.join(VIDEOS_DIR, video)
        video_path_out = '{}_out.mp4'.format(video_path)

        cap = cv2.VideoCapture(video_path)
        ret, frame = cap.read()
        H, W, _ = frame.shape
        out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

        # Путь к модели
        model_path = os.path.join(PROJECT_DIR, 'runs', 'detect', 'train', 'weights', 'last.pt')

        # Загружаем модель
        model = YOLO(model_path)  # загрузить пользовательскую модель

        threshold = 0.5

        while ret:

            results = model(frame)[0]

            for result in results.boxes.data.tolist():
                x1, y1, x2, y2, score, class_id = result

                if score > threshold:
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                    cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            out.write(frame)
            ret, frame = cap.read()

        cap.release()
        out.release()
        cv2.destroyAllWindows()
    def recog(self,val):
        reader = easyocr.Reader(['en'])
        image_path = val
        result = reader.readtext(image_path)
        for detection in result:
            print(detection[1])

DataM = DetectModel()
# DataM.Video('videos','test.mp4')#Проверяем видео
DataM.Photo('kakie-nomera-na-avto-ispolzuyutsya-u-spetssluzhb-rossii.jpg')#Про