import easyocr
from googletrans import Translator



translator = Translator()
def text_recognitio(file_path, text_file_name='result.txt'):
    reader = easyocr.Reader(['ru','en'])
    result = reader.readtext(file_path, detail=0, paragraph=True)

    result_transleate = translator.translate(result[0], dest='ru')
    param = input("Нужно ли переводить текст на фотографии да или нет: ")

    with open(text_file_name, 'w') as file:
        for line in result:
            file.write(f"Текст c фото:\n_________________________________\n{line}\n\n\n\n")

        if param in ['да','Да']:
            file.write(f"Текст с переводом:\n_________________________________\n{result_transleate.text}\n")
            file.close()
        else:
            file.close()

    return f"Резултат был сохранён в файл {text_file_name}"

def main():
    file_path = input("Путь к фотографии с текстом: ")
    print(text_recognitio(file_path=file_path))


if __name__ == "__main__":
    main()