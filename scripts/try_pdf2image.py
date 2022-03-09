from pdf2image import convert_from_path
import os


def get_file_list(my_dir):
    """return list of all files from my directory"""
    file_list = []
    for filename in os.listdir(my_dir):
        if filename.endswith(".pdf"):
            file = [os.path.join(my_dir, filename).replace("\\", "/")]
            file_list += file
        else:
            continue

    return file_list


pdf_file_list = get_file_list("../resources/vicky_togrobid_papers")

counter = 0
for pdf_path in pdf_file_list:
    base = os.path.basename(pdf_path)
    pmid = os.path.splitext(base)[0] + "-"
    images_from_path = convert_from_path(pdf_path, output_folder="../pdf_images", fmt="jpg", output_file=pmid)
    counter += 1

print(counter)

a = 1
