# pip install aspose-words
import aspose.words as aw

def main(LOG):
    # create document object
    doc = aw.Document()

    # create a document builder object
    builder = aw.DocumentBuilder(doc)

    for u in LOG:
        builder.writeln(u)
        # add image
        builder.insert_image("test.png")

    # save document
    doc.save("Visualization.docx")
