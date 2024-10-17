# for i in [1,2,3]:
#     print(i)
#     for j in [1,2,3]:
#         print(j)
#         print("sum  "+str(i) + "=" +str(j)+ "=" +str(i+j))
#         print("=========")
#     print(i)
# print('End looping')    
# longwindedcomputation = (1 + 2 + 4
#                          +5 )
# print(longwindedcomputation)
# listoflists = [[1,2,3],[4,5,6],[7,8,9]]
# easier_to_read_list_of_lists =[[1,2,3],
#                                 [4,5,6],
#                                 [7,8,9]]
# print(easier_to_read_list_of_lists)
import urllib
import urllib.request
import json
# def printResults(data):
#     theJson = json.loads(data)
#     if "title" in theJson["metadata"]:
#         print(theJson["metadata"]["title"])
        
#     count = theJson["metadata"]["count"]
#     print(count, "Events recorded")    
#     for i in theJson["features"]:
#         print(i['properties']["place"])
#     print('------------------------------------------------')
#     for i in theJson["features"]:
#         if i["properties"]['mag'] > 4.0:
#             print(i["properties"]["place"],"mag",i["properties"]["felt"])
#     print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
#     print("events that were felt")
#     for i in theJson["features"]:
#         fetReports = i["properties"]["felt"]
#         if fetReports != None:
#               if int(str(fetReports)) > 0:
#                   print(i["properties"]["place"],"mag",i["properties"]["felt"])
            
def jsondata():
#    resp =urllib.request.urlopen("https://www.google.com/")
#    print(resp.getcode())
#    data = resp.read()
#    print(data)
     url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
     weburl =urllib.request.urlopen(url)
     print("Rest result: ", weburl.getcode())
     data = weburl.read()
     if(weburl.getcode() == 200):
         printResults(data) # type: ignore
     else:
         print("Recived errorl from the server")
paragraphs = 0       
from html.parser import HTMLParser
class MyHtmlParser(HTMLParser)  :
    # def __init__(self):
    #     super()
    #     print("constructing parser")
    def handle_comment(self,data)   :
        print("Encountered comment", data)   
        ln,c = self.getpos()
        print(ln, c)
    def handle_starttag(self, tag, attrs)   :
        print("Encountered start tag", tag)  
        global paragraphs
        if tag == "p":
           ++paragraphs 
        ln,c = self.getpos()
        print(ln, c)
        if len(attrs) > 0:
            for a in attrs:
                print("\t ", a[0],"=",a[1])
    def handle_data(self,data)   :
        if data.isspace():
            return
        print("Encountered data", data)   
        ln,c = self.getpos()
        print(ln, c)
import io      
def html_parsing():
    parser = MyHtmlParser(  )
    f = open("samplehtml.html")
    contents = f.read()
    parser.feed(contents)
    print("paragraphs cnt ", paragraphs)
import xml.dom.minidom   
def xmlParsingsample():
    print("main")   
    doc = xml.dom.minidom.parse("samplexml.xml") 
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    ################################
    skills = doc.getElementsByTagName("skill")
    print(len(skills))
    for skill in skills:
        atr=  skill.getAttribute("name")
        print(atr)
        
    newSkill = doc.createElement("skill")   
    newSkill.setAttribute("name", "cmd")
    doc.firstChild.appendChild(newSkill) 
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    skills = doc.getElementsByTagName("skill")
    print(len(skills))
    for skill in skills:
        atr=  skill.getAttribute("name")
        print(atr)
def string_basics():
       import string
       print(string.ascii_letters)
       print(string.digits)
       print(string.hexdigits)
       print(string.punctuation)
       test_string1 = "The quick brown fox jumps overr the lazy dog on the 1st of Decemberr"     
       test_string2 = "Supercalifragilistic"
       test_string3 = "90210"
       result = "".join([c for c in test_string1 if c in string.ascii_letters])
       print(result)
       print(test_string1.isalnum())
       print(test_string2.isalnum())
       print(all([c.isalpha() for c in test_string1]))
       print(test_string1.isnumeric())
       print(test_string3.isnumeric())
    ##===================================
def sarchig_strings():
    sampleStr = "The quick brown fox jumps overr the lazy dog"     
    print(sampleStr.startswith("The"))
    print(sampleStr.startswith("the"))
    print(sampleStr.endswith("dog"))
    print(sampleStr.find("the"))
    print(sampleStr.rfind("the"))
    print("the" in sampleStr)
    newStr = sampleStr.replace("lazy","tired")
    print(newStr)
    print(sampleStr.count("over"))
def strig_maip():
    test_string1 = "The quick brown fox jumps overr the lazy dog on the 1st of Decemberr"     
    print(len(test_string1))
    print(test_string1.upper())
    print(test_string1.lower())
    result = test_string1.split(" ")
    print(result)
    letters = ["a", "b", "c", "d", "e"]
    print(", ".join(letters))
    #=================
    names = {"Amy", "John", "George", "Michael", "Penelope"}
    biggest = max(len(name) for name in names)
    for name in names:
        print(name.ljust(biggest +2,"-")+ ":")
    for name in names:
        print(name.center(biggest +2,"-")+ ":")
    for name in names:
        print(name.rjust(biggest +2,"-")+ ":")
    #=============================
    test_string1 = "The quick brown fox jumps overr the lazy dog on the 1st of Decemberr"    
    trans_table = str.maketrans("abegilostz","4636110572") 
    print(test_string1.translate(trans_table))
def string_iterpolate_adv():
        the_str = "The quick brown $animal $action overr the lazy dog on the 1st of Decemberr"         
        from string import Template
        the_template = Template(the_str)
        output_str = the_template.substitute(animal="fox",action = "jump")
        print(output_str)
        args = {
            "animal": "cow",
            "action": "walked"
        }
        output_str = the_template.substitute(args)
        #########################################
        foo = "foo"
        bar = 123
        print("tem {} {}".format(foo,bar))
        print("tem {1} {0}".format(foo,bar))
        print("tem {var2:x} {var2:X}".format(var1= foo,var2=bar))
        print(output_str)
        ################################################
        import datetime   
        product = "Widget"
        price = 19.99
        tax = 0.07
        nyd = datetime.datetime(2019,1,1) 
        print(f"{product} has {price} with tax {tax:2%} is {round(price + (price * tax),2)}")   
def sorting_data_sample():
    print("Sorting")
    testSccores = [1,25,2,15,19,30,11]
    sortedScores = sorted(testSccores)
    print(sortedScores)
    sortedScores = sorted(testSccores, reverse=True)
    print(sortedScores)
class Product():
   def __init__(self, name, price, weight, discount) -> None:
       self.name = name
       self.price = price
       self.weight = weight
       self.discount = discount
   def __repr__(self) -> str:
        return   repr((self.name, self.price, self.weight))    
   def discountPrice(self):
       return self.price - (self.price * self.discount)
def sort_basic():
   
    prodList = [
        Product("Doohickeyt", 40,10,0.15),
        Product("Widget", 50,10,0.05),
    
        Product("Doohickeyt", 40,8,0.15),
        Product("ThingMambob", 35,12,0.0),
        Product("Gadget", 65,7,0.20)
    ]    
    print(prodList)
    def pricesort(product):
        return product.price
    
    print(sorted(prodList, key = pricesort))
    print(sorted(prodList, key = lambda p:p.price))
    print(sorted(prodList, key = lambda p:p.discountPrice("discountPrice")))
    
    result = sorted(prodList, key=lambda k:k.weight)
    result = sorted(result, key=lambda k:k.price, reverse=True)
    print(result)
def sortng_reflection():
    prodList = [
         Product("Widget A", 50,10,0.05),
         Product("Widget B", 40,8,0.15),
         Product("Widget C", 35,12,0.0),
         Product("Widget D", 65,7,0.20),
         Product("Widget E", 70,7,0.12),
    ]     
    from operator import attrgetter, methodcaller, itemgetter
    print("printed using attrgetter method:")
    print(sorted(prodList, key=attrgetter("weight"), reverse=True))
    print(sorted(prodList, key=methodcaller("discountPrice"), reverse=True))
    inventory = [
        ("Widget A",5),
        ("Widget B",2),
        ("Widget C",4),
        ("Widget D",7),
        ("Widget E",4),
                 ]
    print(sorted(inventory, key=itemgetter(1), reverse=True))
def typedArrays():
    from array import array 
    arr1 = array('i',[2,4,6,8,10,12,14,16,18,20])   
    print(arr1.typecode)
    print(f"array 1 item size: {arr1.itemsize}")
    arr1.insert(0,0)
    arr1.append(22)
    arr1.extend([24,26,28])
    print(arr1)
    for a,elem in enumerate(arr1):
        arr1[a] = elem *2
    print(arr1)
    #arr1.insert(0,1.25)
    arr2 = array("B", [18,102,182,56,89,5,254,32,64,50])
    print(arr2.typecode)
    print(f"x{arr2.itemsize}")
    #arr2.insert(0,3000)
    list1 =arr2.tolist();
    list1.append(3000)
    print(list1)
def bisct_sample():
    import bisect
    values = [5,7,13,20,25,31,36,43,47,49,50,75]
    bs = bisect.bisect(values,6)
    print(bisect.bisect_right(values,25))
    print(bisect.bisect(values,25))
    print(bisect.bisect_left(values,25))
    values.insert(bs,6)
    print(values)
    bisect.insort_left(values,25)
    print(values)
    breakpoints = [60,70,80,90]
    gradeLetters = "FDCBA"
    scores = [81,68,53,91,82,76,71,84]
    def calcGrade(score):
        bp = bisect.bisect(breakpoints,score)
        i = bp
        return gradeLetters[i]
    results = [calcGrade(a) for a in scores]
    print(results)
def io_basics():
    fp = open("testfile.txt","w")
    fp.write("This is some text\n")
    fp.close()
    #####################
    with open("testfile.txt") as  fp:
       data = fp.read()
       print(data)    
    with open("testfile.txt","a+") as fp:
        fp.write("appended\n")
        fp.seek(0)
        print(fp.read())
def read_write_wit():
    import os
    import tempfile
    print('gettmpdir: ', tempfile.gettempdir())
    print('gettpfile: ', tempfile.gettempprefix())
    (tmpfh, tempfp) = tempfile.mkstemp(".tmp", "testTemp",None,True)
    f = os.fdopen(tmpfh, "w+t")
    f.write("this is some temp data")
    f.seek(0)
    print(f.read())
    f.close()
    os.remove(tempfp)
    with tempfile.TemporaryFile(mode="w+t") as tfp:
        tfp.write("data")
        tfp.seek(0)
        print(tfp.read())
    with tempfile.TemporaryDirectory() as td:
        print(td)    
        fp=os.path.join(td,"tmpfile1.txt")
        with open(fp, "w+t") as fp:
           fp.write("fap")
           fp.seek(0)
           print(fp.read())
import csv
def readerSample():
    print( csv.list_dialects())
    with open("file.csv",'r+t') as f:
        reader= csv.reader(f)
        for row in reader:
            print(row)
def useSnifer():
     with open("file.csv",'r+t') as f:
         dialect = csv.Sniffer().sniff(f.read(128))
         f.seek(0)
         hasHeader = csv.Sniffer().has_header(f.read(128))
         f.seek(0)
         print("Headers found"+ str(hasHeader))
         print(dialect.delimiter)
         print(dialect.escapechar)
         print(dialect.quotechar)
def writeSample():
    with open("file1.csv",'w') as f:
       csvWriter = csv.writer(f)
       csvWriter.writerow(["Name","Dpt", "Location"])
       csvWriter.writerow(["a","b", "c"])
       csvWriter.writerow(["e","f", "g"])
       csvWriter.writerow(["h","i", "j"])
       csvWriter.writerow(["h","l", "m"])
       
def csvExample():
    useSnifer()
    readerSample()     
    writeSample()
def ziping_basics():
    import zipfile
    zfile = zipfile.ZipFile("archive.zip","w")
    zfile.write("file.csv")
    zfile.write("file1.csv")
    zfile.close()
    print( zipfile.is_zipfile("archive.zip"))
    with zipfile.ZipFile("archive.zip") as zfilie:
        print(zfilie.read("file1.csv"))

        print(zfilie.namelist())
        print(zfilie.infolist())
        
        zipinfo = zfilie.getinfo('file1.csv')
        print(zipinfo.file_size)
        #zfilie.extractall()
       # zfilie.extract('file1.csv')
def config_files_processing():
           import configparser
           parser = configparser.ConfigParser()
           parser.read("file.cfg")
           print(parser.sections())
           print(parser.has_section("Section 1"))
           using_time_travel = bool(parser["DEFAULT"]["UseTimeTravel"])
           print(using_time_travel)
           print(type(using_time_travel))
           opd = parser["DEFAULT"].getboolean("ObeyPrimeDirective")
           print(opd)
           speed = parser["DEFAULT"].getfloat("Ship Sped")
           print(speed)
           try:
            using_time_travel = bool(parser["s12"]["UseTimeTravel"])
           except KeyError as err:
               print(f"ERR{err}")
def downloading_web_pages(args=None):
    import urllib.request
    sample_url = "http://httpbin.org/xml"
    resp = urllib.request.urlopen(sample_url)
    print("main", resp.status)
    status_code = resp.status      
    if(status_code >= 200 and status_code <300):
        print(resp.getheaders())     
        print(resp.getheader("Content-length"))  
        print(resp.headers["Content-Type"])   
        data = resp.read().decode('utf-8')
        print(data)
metacount = 0
def html_once_again():
   
    from html.parser import HTMLParser
    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
            print("Encountered a start tag", tag)
            pos = self.getpos()
            print("At line ", pos[0], "and char: ", pos[1])
            if len(attrs) > 0:
                print("\tAtributes found:")
                for a in attrs:
                    print("\t",a[0], "val ", a[1])
            if tag == "meta":
                global metacount
                metacount+=1        
            return super().handle_starttag(tag, attrs) 
        def handle_endtag(self, tag: str) -> None:
            print("encountered end tag ", tag)
            return super().handle_endtag(tag)
        def handle_data(self, data: str) -> None:
            print("encountered data  ", data)
            return super().handle_data(data)
        def handle_comment(self, data: str) -> None:
            print("encountered comment ", data)
            return super().handle_comment(data) 
           
    parser = MyHTMLParser()
    with  open("sample.html") as f:
        content = f.read()
        parser.feed(content)   
        
    print(metacount)   
def main():
    import urllib.request
    sample_url = "http://httpbin.org/json"
    sample_json = urllib.request.urlopen(sample_url).read().decode("utf-8")
    print(sample_json)
    import json
    obj = json.loads(sample_json)
    print(obj["slideshow"]["author"])
    for slide in obj["slideshow"]["slides"]:
        print(slide)
    objdata = {
        "name": "Joe doe",
        "author": True,
        "titles":[
            "A", "B"
        ]
    }    
    with open("aFle.json", "w+") as f:
        json.dump(objdata,f, indent=4)
        f.seek(0)
        print("raded",f.read())
if __name__ == "__main__":
    main()