import requests
import fitz
import io

pdf_url = 'https://www.josharcher.uk/static/files/2018/01/Industrial_Society_and_Its_Future-Ted_Kaczynski.pdf'

response = requests.get(pdf_url)

if response.status_code == 200:
    with fitz.open(stream=io.BytesIO(response.content)) as doc:
        text = ""
        # first two pages
        for page_num in range(2):
            page = doc.load_page(page_num)
            text += page.get_text()
    print(text)
else:
    # this will not happen
    print("Failed to retrieve the PDF.")
