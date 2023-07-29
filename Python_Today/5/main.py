import requests
import img2pdf

def getdata():

    imj_list = []
    for i in range(1, 49):
        url = f"https://www.recordpower.co.uk/flip/Winter2020/mobile/{i}.jpg"
        req = requests.get(url=url)
        response = req.content
        with open(f"media/{i}.jpg", "wb") as file:
            file.write(response)
            imj_list.append(f'media/{i}.jpg')
            print(f"Downloaded {i}")

    print('#' * 20)
    print(imj_list)
    with open("results.pdf", "wb") as f:
        f.write(img2pdf.convert(imj_list))

    print("PDF file created successfully")
def main():
    getdata()


if __name__ == '__main__':
    main()
