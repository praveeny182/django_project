from fileinput import filename
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
import img2pdf
from PIL import Image
from django.http import FileResponse,response
import mimetypes
import shutil
from demo.scan import scanwork
from django.http import HttpResponseRedirect
global reader

    
def imgtopdf(tmp,pic):

    # storing image path
    img_path = tmp+pic
    # storing pdf path
    pdf_path = tmp+'test.pdf'

    # opening image
    image = Image.open(img_path)

    # converting into chunks using img2pdf
    pdf_bytes = img2pdf.convert(image.filename)

    # opening or creating pdf file
    file = open(pdf_path, "wb")

    # writing pdf files with chunks
    file.write(pdf_bytes)

    # closing image file
    image.close()

    # closing pdf file
    file.close()
    os.remove(tmp+pic)
    # output
    # print("Successfully made pdf file")
    pth=os.getcwd()
    pth+='/'
    destination=pth+'static/demo/files/'+'test.pdf'
    source=pth+'test.pdf'
    dest = shutil.move(source, destination)
    return FileResponse(open(destination, 'rb'), as_attachment=True, content_type='application/pdf')
def doctopdf(tmp):
    from docx2pdf import convert
    pth=os.getcwd()
    pth+='/'
    destination=pth+'static/demo/files/'+'test.pdf'
    convert(tmp,destination)
    return FileResponse(open(destination, 'rb'), as_attachment=True, content_type='application/pdf')
# def xltopdf(tmp):
#     from win32com import client
  
#     # Open Microsoft Excel
#     excel = client.Dispatch("Excel.Application")
    
#     # Read Excel File
#     sheets = excel.Workbooks.Open(tmp)
#     work_sheets = sheets.Worksheets[0]
    
#     # Convert into PDF File
#     work_sheets.ExportAsFixedFormat(0,'C:/Users/easygov/convert/static/demo/files/test.pdf')
    
#     return FileResponse(open('C:/Users/easygov/convert/static/demo/files/test.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
def txttopdf(tmp):
    # Python program to convert
# text file to pdf file


    from fpdf import FPDF


    pdf = FPDF()


    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size = 8)

    # open the text file in read mode
    f = open(tmp, "r")

    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1, align = 'L')

    # save the pdf with name .pdf
    pdf.output("test.pdf")
    pth=os.getcwd()
    pth+='/'
    destination=pth+'static/demo/files/'+'test.pdf'
    # destination='C:/Users/easygov/convert/static/demo/files/'+'test.pdf'
    # source='C:/Users/easygov/convert/test.pdf'
    source=pth+'test.pdf'
    dest = shutil.move(source, destination)
    return FileResponse(open(destination, 'rb'), as_attachment=True, content_type='application/pdf')
# def ocr(tmp):
#     try:
#         if reader:
#             pass
#     except:
#         reader = easyocr.Reader(['en'])
#         print("pppppppppp")
#     result = reader.readtext(tmp)
#     l=[]
#     for i in range(len(result)):
#         l.append(result[i][-2])
#     with open('listfile.txt', 'w') as filehandle:
#         for listitem in l:
#             filehandle.write(f'{listitem}\n')
#     pth=os.getcwd()
#     pth+='/'
#     # filename='C:/Users/easygov/convert/listfile.txt'
#     filename=pth+'listfile.txt'
#     return txttopdf(filename)
def imgconvert(tmp):
    from django.core.files.storage import FileSystemStorage
    from PIL import Image

    file = tmp
    img = Image.open(file)

    myfile = img.convert("L")
    pth=os.getcwd()
    pth+='/'
    destination=pth+'static/demo/files/'+'test.jpeg'
    myfile.save(destination)
    return FileResponse(open(destination, 'rb'), as_attachment=False, content_type='image/jpeg')
def pdftodoc(tmp):
    import PyPDF2

    FILE_PATH = tmp

    with open(tmp, mode='rb') as f:

        reader = PyPDF2.PdfFileReader(f)

        page = reader.getPage(0)

        #print(type(page.extractText()))
        #open text file
        pth=os.getcwd()
        pth+='/'
        destination=pth+'test.txt'
        text_file = open(destination, "w")

        #write string to file
        text_file.write(page.extractText())

        #close file
        text_file.close()
        return FileResponse(open(destination, 'rb'), as_attachment=False, content_type='application/txt')
def img_resize(tmp,h,w):
    from PIL import Image
    image = Image.open(tmp)

    # Image size, in pixels. The size is given as a 2-tuple (width, height).
    # print(image.size) # Output: (1920, 1280)
    info=image.size
    new_image = image.resize((w, h))
    info_1=new_image.size
    # new_image.save('image_new.jpg')
    pth=os.getcwd()
    pth+='/'
    destination=pth+'static/demo/files/'+'test.jpeg'
    new_image.save(destination)
    context={'one':info,'two':info_1}
    return FileResponse(open(destination, 'rb'), as_attachment=False, content_type='image/jpeg')

def pdfreduce(tmp):
    from PyPDF2 import PdfReader, PdfWriter
    
    reader = PdfReader(tmp)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.add_metadata(reader.metadata)

    with open("test1.pdf", "wb") as fp:
        writer.write(fp)
    pth=os.getcwd()
    pth+='/'
    destination=pth+'test1.pdf'
    return FileResponse(open(destination, 'rb'), as_attachment=True, content_type='application/pdf')
def pdfmerger(tmp,tmp1):
    from PyPDF2 import PdfMerger

    merger = PdfMerger()

    merger.append(tmp)
    merger.append(tmp1)
    merger.write("merged-pdf.pdf")
    merger.close()
    pth=os.getcwd()
    pth+='/'
    destination=pth+'merged-pdf.pdf'
    return FileResponse(open(destination, 'rb'), as_attachment=True, content_type='application/pdf')
def lockpdf(tmp,passname):
    from PyPDF2 import PdfReader, PdfWriter

    reader = PdfReader(tmp)
    writer = PdfWriter()

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Add a password to the new PDF
    writer.encrypt(passname)

    # Save the new PDF to a file
    with open("encrypted-pdf.pdf", "wb") as f:
        writer.write(f)
    pth=os.getcwd()
    pth+='/'
    destination=pth+'encrypted-pdf.pdf'
    return FileResponse(open(destination, 'rb'), as_attachment=True, content_type='application/pdf')
def unlockpdf(tmp,passname):
    from PyPDF2 import PdfReader, PdfWriter

    reader = PdfReader(tmp)
    writer = PdfWriter()

    if reader.is_encrypted:
        reader.decrypt(passname)

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Save the new PDF to a file
    with open("decrypted-pdf.pdf", "wb") as f:
        writer.write(f)
    pth=os.getcwd()
    pth+='/'
    destination=pth+'decrypted-pdf.pdf'
    return FileResponse(open(destination, 'rb'), as_attachment=True, content_type='application/pdf')
def index(request):
    print("-----------------------------------")
    try:
        
        d={'myfile':'A','myfile_1':'B','fname':'C','lockname':'D','unlockname':'E'}
        print('aaaaa',request.FILES)
        for i in request.FILES:
            control=i
            break
        
        if request.method == 'POST' and d[control]=='A':
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            print("xxxxxx")
            
            filename = fs.save(myfile.name, myfile)
            pth=os.getcwd()
            pth+='/'
            tmp=pth+filename
            
            pk=request.POST['cars']
            # print(pk,type(pk))
            if pk=='imgtopdf':
                z= imgtopdf(pth,filename)
                return z
            elif pk=='doctopdf':
                z=doctopdf(tmp)
                os.remove(tmp)
                return z
            # elif pk=='xltopdf':
            #     return xltopdf(tmp)
            elif pk=='txt':
                z=txttopdf(tmp)
                os.remove(tmp)
                return z


            # elif pk=='ocr':
            #     z=ocr(tmp)
            #     os.remove(tmp)
            #     return z
            elif pk=='imgconvert':
                z=imgconvert(tmp)
                os.remove(tmp)
                return z
            elif pk=='pdftodoc':
                z=pdftodoc(tmp)
                os.remove(tmp)
                return z
            elif pk=='pdfreduce':
                z=pdfreduce(tmp)
                os.remove(tmp)
                return z
            elif pk=='imgscan':
                scanwork(tmp)
                os.remove(tmp)
                return FileResponse(open('./test.jpg', 'rb'), as_attachment=False, content_type='image/jpeg')
                
            

        elif request.method == "POST" and d[control]=='B':
            # print("jjjjjj")
            myfile = request.FILES['myfile_1']
            fs = FileSystemStorage()
        
            
            filename = fs.save(myfile.name, myfile)
            pth=os.getcwd()
            pth+='/'
            tmp=pth+filename
            a=request.POST['fname']
            b=request.POST['lname']
            a=int(a)
            b=int(b)
            z=img_resize(tmp,b,a)
            os.remove(tmp)
            # print("pppppppppppppppppppppppppp")
            return z    
        # return render(request,'index.html')
        elif request.method == "POST" and d[control]=='C':
            myfile = request.FILES['fname']
            myfile1 = request.FILES['lname']
            fs = FileSystemStorage()
        
            
            filename = fs.save(myfile.name, myfile)
            filename1 = fs.save(myfile1.name, myfile1)
            pth=os.getcwd()
            pth+='/'
            tmp=pth+filename
            tmp1=pth+filename1
            z=pdfmerger(tmp,tmp1)
            os.remove(tmp)
            os.remove(tmp1)
            return z
        elif request.method == "POST" and d[control]=='D':
            # print("pppppppppppppppppppppppp")
            myfile = request.FILES['lockname']
            
            passname = request.POST['passname']
            # print(myfile,passname)
            fs = FileSystemStorage()
        
            
            filename = fs.save(myfile.name, myfile)
            
            pth=os.getcwd()
            pth+='/'
            tmp=pth+filename
            z=lockpdf(tmp,passname)
            os.remove(tmp)
            
            return z
        elif request.method == "POST" and d[control]=='E':
            # print("pppppppppppppppppppppppp")
            myfile = request.FILES['unlockname']
            
            passname = request.POST['passname']
            # print(myfile,passname)
            fs = FileSystemStorage()
        
            
            filename = fs.save(myfile.name, myfile)
            
            pth=os.getcwd()
            pth+='/'
            tmp=pth+filename
            z=unlockpdf(tmp,passname)
            os.remove(tmp)
            
            return z
        
        

        return render(request,'index.html')
        
    
    except:
        
        # print("hello")
        context={'one':'Please fill required field'}
        return render(request,'index.html')
        
