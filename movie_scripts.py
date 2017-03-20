import requests
from bs4 import BeautifulSoup
import json
import django
print django.__file__
import re

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_links = []

for i in letters:
    url = 'http://www.imsdb.com/alphabetical/' + i
    alphabet_links.append(url)


links = []

for letter_link in alphabet_links:
    url = letter_link
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    
    for p in soup.findAll('p'):
        links.append("http://www.imsdb.com/scripts/" + unicode(p.contents[0]["href"]).replace('/Movie Scripts/', '').replace(' Script', '').replace(' ', '-')) 
        print "http://www.imsdb.com/scripts/" + unicode(p.contents[0]["href"]).replace('/Movie Scripts/', '').replace(' Script', '').replace(' ', '-')

def parseEnd(answer):
    try:
        if((answer.index('.\r\n')) > -1):
            answer = answer[0:answer.index('.\r\n')]
            return answer
        elif((answer.index('?\r\n')) > -1):
            answer = answer[0:answer.index('?\r\n')]
            return answer
        elif((answer.index('!\r\n')) > -1):
            answer = answer[0:answer.index('!\r\n')]
            return answer
    except:
        return answer

def removeParen(answer):
    try:
        if((answer.index("(") > -1) and (answer.index(")") > -1)):
            substring = answer[answer.index("("):answer.index(")") + 1]
            answer = answer.replace(substring, "")
            return answer
    except:
        return answer

counter = 0
file_count = 1
allQnA = []
for link in links:
    counter += 1
    if(counter % 50 == 0):
        file_count += 1
    
    source_code = requests.get(link)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    
    #print soup
    
    
    
    for speaker in soup.findAll('b'):
        
        qNa = {}
        
        #question_and_answer = ""
        try:
            if(unicode(speaker.next_sibling).replace('\n', '').replace('\r', '').replace('\t', '').endswith('?')):
                
                try:
                    qNa['question'] = re.sub(" +", " ", str(speaker.next_sibling.replace('\n', '').replace('\r', ' ').replace('\t', '').replace('(continuing)', '') + "\t").encode('utf-8'))
                    
                    #question_and_answer += re.sub(" +", " ", str(speaker.next_sibling.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace('(continuing)', '') + "\t").encode('utf-8'))
                except:
                    pass
                
                if(("<b>" in unicode(speaker.next_sibling.next_sibling.next_sibling)) == False):

                    try:
                        answer = re.sub(" +", " ", str(speaker.next_sibling.next_sibling.next_sibling).encode('utf-8'))
                        answer = parseEnd(answer)
                        answer = removeParen(answer)
                        answer = answer.replace("\r\n", " ")
                        qNa['answer'] = answer
                        allQnA.append(qNa)
                    except:
                        pass

                elif(("<b>" in unicode(speaker.next_sibling.next_sibling.next_sibling.next_sibling)) == False):
                    
                    try:
                        answer = re.sub(" +", " ", str(speaker.next_sibling.next_sibling.next_sibling.next_sibling).encode('utf-8'))
                        answer = parseEnd(answer)
                        answer = removeParen(answer)
                        answer = answer.replace("\r\n", " ")
                        qNa['answer'] = answer
                        allQnA.append(qNa)
                    except:
                        pass
                elif(("<b>" in unicode(speaker.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling)) == False):
                    
                    try:
                        answer = re.sub(" +", " ", str(speaker.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling).encode('utf-8'))
                        answer = parseEnd(answer)
                        answer = removeParen(answer)
                        answer = answer.replace("\r\n", " ")
                        qNa['answer'] = answer
                        allQnA.append(qNa)
                    except:
                        pass
                elif(("<b>" in unicode(speaker.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling)) == False):
                    
                    try:
                        answer = re.sub(" +", " ", str(speaker.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling).encode('utf-8'))
                        answer = parseEnd(answer)
                        answer = removeParen(answer)
                        answer = answer.replace("\r\n", " ")
                        qNa['answer'] = answer
                        allQnA.append(qNa)
                    except:
                        pass
                # try:
                #     pass
                #     # json_data = json.dumps(qNa)
                #     # #with open('movie_scripts_two/file' + str(file_count) + '.doc', 'a') as f:
                #     #     #f.write(str(question_and_answer) + '\n')
                #     # with open('jsonQuotesLoop.json', 'a') as f:
                #     #     f.write(json_data)
                # except TypeError:
                #     pass
                # except AttributeError:
                #     pass
                # except:
                #     pass
        except:
            pass
        #if actions != None, then put it in the file
        

json_data_array = json.dumps(allQnA)

with open('jsonQuotesArray.json', 'a') as f:
    f.write(json_data_array)

#get questions
#for speaker in soup.findAll('b'):
#    if(unicode(speaker.next_sibling).replace('\n', '').replace('\r', '').endswith('?')):
#        print speaker.next_sibling.replace('\n', '').replace('\r', '')

# for speaker in soup.findAll('b'):
#     if(unicode(speaker.next_sibling).replace('\n', '').replace('\r', '').endswith('?')):
#         print speaker.next_sibling.replace('\n', '').replace('\r', '')
#         print speaker.next_sibling.next_sibling.next_sibling
        
# for speaker in soup.findAll('b'):
#     if(unicode(speaker.next_sibling).replace('\n', '').replace('\r', '').endswith('?')):
#         print "*****************************************"
#         print speaker.next_sibling.replace('\n', '').replace('\r', '')
#         if("<b>" in unicode(speaker.next_sibling.next_sibling.next_sibling)):
#             print speaker.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
         
#         else:
#             print speaker.next_sibling.next_sibling.next_sibling



