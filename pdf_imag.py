import fitz


doc = fitz.open('file_path')


def get_imag():
    count = 0
    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            doc.extract_image(xref)
            imgout = open(f"image{i + 1}.{doc.extract_image(xref)['ext']}", 'wb')
            imgout.write(doc.extract_image(xref)['image'])
            count += 1
            imgout.close()
    print(f'Изображений загружено {count}')
