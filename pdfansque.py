from bert_serving.client import BertClient
client = BertClient()
#vectors = client.encode(["dog is not a human"])


import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
            
            text = fake_file_handle.getvalue()
            yield text
    
            # close open handles
            converter.close()
            fake_file_handle.close()
    

bypg=[]
for page in extract_text_by_page("C:\\Users\\user\\Downloads\\model_3_owners_manual_north_america_en.pdf"):
    #print(page)
    bypg.append(page)
    print()
    
    
    








import nltk.data

        
vec1=[]
for i in bypg:
    a_list = nltk.tokenize.sent_tokenize(i)
    vec1.append(a_list)
    
all_vec1=[]
for j in vec1:
    in_vec=[]
    for p in j:
        in_vec.append(client.encode([p]))
    all_vec1.append(in_vec)    
        
        
        

from neo4j.v1 import GraphDatabase

 

# Database Credentials

uri             = "bolt://localhost:7687"

userName        = "neo4j"

password        = "meditation@69"

graphDB_Driver  = GraphDatabase.driver(uri, auth=(userName, password) , encrypted=False)  


cqlNodeQuery = """ MATCH (x:Sentence) RETURN [x.vector]  """
neovec1=[]
with graphDB_Driver.session() as graphDB_Session:

    nodes = graphDB_Session.run(cqlNodeQuery)

    for node in nodes:

       print(list(node[0][0]))




import csv 
  
# field names 
fields = ['text', 'vector', 'sent_no', 'page_no', 'pdf_no' ] 

rows=[]
for q in range(0,259):
    
    for e in range(0,len(vec1[q])):
        rows1=[]
        rows1.append(vec1[q][e])
        rows1.append(all_vec1[q][e])
        rows1.append(e+1)
        rows1.append(q+1)    
        rows1.append(1)
        rows.append(rows1)
    
        

filename = "E:\\ML_prac\\teslanlp1.csv"
  
# writing to csv file 
with open(filename, 'w' , encoding="utf-8") as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile , delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
      
    # writing the fields 
    csvwriter.writerow(fields) 
      
    # writing the data rows 
    csvwriter.writerows(rows)



fields1 = [ 'page_no'] 

rows121=[]
for q1 in range(0,259):
    rows121.append([q1+1])
    
        

filename = "E:\\ML_prac\\teslanlp2.csv"
  
# writing to csv file 
with open(filename, 'w' , encoding="utf-8") as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile , delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
      
    # writing the fields 
    csvwriter.writerow(fields1) 
      
    # writing the data rows 
    csvwriter.writerows(rows121)




