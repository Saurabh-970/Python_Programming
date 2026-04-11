#Duck typing: it is a concept where the type of an object is determined 
#by its behaviour not by its class

class InkJetPrinter:
    def printdocument(self,document):
        print("InkJet printer printing : ",document)

class LaserPrinter:
    def printdocument(self,document):
        print("Laser printer printing : ",document)

class PdfWriter:
    def printdocument(self,document):
        print(f"Saving {document} as pdf")

def StartPrinting(Device):
    Device.printdocument("Marvellous notes")

def main():
    StartPrinting(InkJetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PdfWriter())
main()