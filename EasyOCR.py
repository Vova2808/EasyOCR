# pip install easyocr
# pip install googletrans
#
# Импортирование библиотек для распознавания текста и перевода
import easyocr
import tkinter as tk
from tkinter import filedialog
from googletrans import Translator


# Создание экземпляра переводчика
translator = Translator()

# Определение функции для распознавания текста
def text_recognitio(file_path, text_file_name='result.txt'):
    # Создание экземпляра читателя
    reader = easyocr.Reader(['ru','en'])
    # Распознавание текста на изображении
    result = reader.readtext(file_path, detail=0, paragraph=True)

    # Перевод распознанного текста на русский язык
    result_transleate = translator.translate(result[0], dest='ru')

    # Запрос пользователя о необходимости перевода текста
    param = input("Нужно ли переводить текст на фотографии да или нет: ")

    # Открытие файла для записи
    with open(text_file_name, 'w') as file:
        # Запись распознанного текста в файл
        file.write(f"Текст c фото:\n_________________________________\n\n\n\n")
        for line in result:
            file.write(f"{line}\n")

        # Если пользователь хочет перевести текст
        if param in ['да','Да']:
            # Запись перевода в файл
            file.write(f"\n\n\n\nТекст с переводом:\n_________________________________\n{result_transleate.text}\n")
            file.close()
        else:
            file.close()

    # Возвращение результата
    return f"Результат был сохранён в файл {text_file_name}"


# Определение основной функции
def main():
    # Создаем основное окно
    root = tk.Tk()
    root.title("0.6 Transparency Window")
    root.geometry("400x300+300+120")
    root.attributes("-alpha", 0.8)

    # Открытие файла через tkinter
    def open_image():
        file_path = filedialog.askopenfilename()
        root.destroy()
        # Вызов функции распознавания текста
        print(text_recognitio(file_path=file_path))
        # Закрываем окно


    # Создаем кнопку
    open_button = tk.Button(root, text="Открыть изображение", command=open_image)
    open_button.pack(pady=10)
    root.mainloop()
    # Запрос у пользователя пути к изображению с текстом
    # file_path = input("Путь к фотографии с текстом: ")
    # Вызов функции распознавания текста
    # print(text_recognitio(file_path=file_path))

# Вызов основной функции
if __name__ == "__main__":
    main()
