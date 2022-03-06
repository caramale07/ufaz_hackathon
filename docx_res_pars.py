import docx2txt

file_path = r'C:\Users\bashi\Desktop\Ufaz_Hackathon\docx\cv_with_photo_02.docx'

def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None


