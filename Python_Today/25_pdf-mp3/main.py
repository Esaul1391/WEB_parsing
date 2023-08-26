from gtts import gTTS
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path = 'test.pdf', language='ru'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':   #  Проверяю что файл находи в папке и имеет расширение pdf
        # return "File exists!"
        print(f'[+] Original file {Path(file_path).name}')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        # with open('text1.txt', 'w') as file:
        #     file.write(text)
        text = text.replace('\n', '')
        # with open('text1.txt', 'w') as file:
        #     file.write(text)

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f"{file_name}.mp3")
    else:
        return "File not exists, check the file path!"


def main():
    pdf_to_mp3(file_path='/home/user/PycharmProjects/WEB_parsing/Python_Today/25_pdf-mp3/Пример отчета по ознакомительной практике_1_.pdf')

if __name__ == "__main__":
    main()