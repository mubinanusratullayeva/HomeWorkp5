from pdf2image import convert_from_path

def syncPDF_TOjpg(pdf_file):
    imgs = convert_from_path(pdf_file)
    for i, img in enumerate(imgs):
        img.save(f'page_{i + 1}.jpg', 'JPEG')
        print(f"Page {i + 1} saved")

def main():
    pdf_file_path = "multimedia.pdf"
    syncPDF_TOjpg(pdf_file_path)

if __name__ == "__main__":
    main()