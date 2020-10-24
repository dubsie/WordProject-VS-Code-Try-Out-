import docx


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
    	print(para.txt)
        fullText.append(para.text)
        return "\n".join(fullText)


getText("demo.docx")
