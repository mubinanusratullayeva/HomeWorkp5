from pdf2image import convert_from_path
import os
import time

folder_url = r"C:\Users\Mubina\Documents\python 5\hometasks\Multiprocessing\singleProcess"
def pdf_to_jpg(pdf_file):
    pdf_name = os.path.splitext(os.path.basename(pdf_file))[0]
    pages = convert_from_path(pdf_file)
    for i, page in enumerate(pages):
        jpg_name = f"{pdf_name}_page_{i+1}.jpg"
        page.save(os.path.join("singleJPGs", jpg_name), "JPEG")

def single_process():
    os.makedirs("new_folder", exist_ok=True)
    pdf_files = [os.path.join(folder_url, f) for f in os.listdir(folder_url) if f.endswith(".pdf")]

    start_time = time.time()

    for pdf_file in pdf_files:
        pdf_to_jpg(pdf_file)

    end_time = time.time()

    print(end_time - start_time) # 25.312 sekund

single_process()