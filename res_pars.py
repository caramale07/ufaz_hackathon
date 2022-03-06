
from typing import final
import PyPDF2
from hashlib import new
from math import fabs

from numpy import sort
import docx_res_pars as drp
import pdf_res_pars as prp
import re
import string
import pandas as pd
import matplotlib.pyplot as plt

number_of_resumes=int(input("number of resumes"))
list_of_scores= []

recruiter=int(input("1)Information Technologies\n2)Finance\n3)Medical helthcare\n4)Engineering\n5)Marketing\n"))
keywords=[i for i in input("Write skills or knowledges you need\n").split()]

for k in range(1,number_of_resumes+1):
    try:
        filename = "C:\\Users\\bashi\\Desktop\\Ufaz_Hackathon\\resume00"+str(k)+".docx"
        text = drp.extract_text_from_docx(filename)
    except:
        filename = "C:\\Users\\bashi\\Desktop\\Ufaz_Hackathon\\resume00"+str(k)+".pdf"
        text = prp.extract_text_from_pdf(filename)


    index_of_dot = filename.find(".")
    format = filename[index_of_dot+1:]

    text = ""

    if format =="pdf":
        text = prp.extract_text_from_pdf(filename)
    elif format == "docx":
        text = drp.extract_text_from_docx(filename)
    else:
        print("Wrong format of resume. It should be pdf or docx")


    # university name
    list_of__uni =[]
    import re
    university_name = re.sub(r"[\w\W]* ((Hospital|University|Centre|Law School|School|Academy|Department)[\w -]*)[\w\W]*$", r"\1", text)
    list_of__uni.append(university_name)
    


    '''text cleaning'''
    text = text.lower()
    text = re.sub(r'\d+','',text)
    text = text.translate(str.maketrans('','',string.punctuation)) # remove punctuation



    '''Dictionary with key terms by area setup'''
    terms = {'Qualities':['teamwork','work ethic','leadership','team worker','hardworking','smart working','curious','kind', 'gentle', 'strong', 'resilient','flexible','flexibility', 'caring', 'assertive', 'hard-working',
                            'reliable', 'honest', 'practical', 'responsible', 'loyal', 'mature', 'creative', 'consistent', 'appreciative', 'capable', 'quick', 'perceptive', 'patient', 'thoughtful', 'fit', 'trustworthy', 'shows initiative', 'motivated', 'versatile', 'educated',
                            'willing', 'experienced', 'efficient', 'open-minded', 'logical', 'serious', 'supportive', 'resourceful', 'punctual',
                            'friendly', 'humane'],      
            'Operations management':['automation','bottleneck','constraints','cycle time','efficiency','fmea',
                                    'machinery','maintenance','manufacture','line balancing','oee','operations',
                                    'operations research','optimization','overall equipment effectiveness',
                                    'pfmea','process','process mapping','production','resources','safety',
                                    'stoppage','value stream mapping','utilization'],
            'Supply chain':['abc analysis','apics','customer','customs','delivery','distribution','eoq','epq',
                            'fleet','forecast','inventory','logistic','materials','outsourcing','procurement',
                            'reorder point','rout','safety stock','scheduling','shipping','stock','suppliers',
                            'third party logistics','transport','transportation','traffic','supply chain',
                            'vendor','warehouse','wip','work in progress'],
            'Project management':['administration','agile','budget','cost','direction','feasibility analysis',
                                'finance','kanban','leader','leadership','management','milestones','planning',
                                'pmi','pmp','problem','project','risk','schedule','scrum','stakeholders'],
            'Data analytics':['analytics','api','aws','big data','busines intelligence','clustering','code',
                            'coding','data','database','data mining','data science','deep learning','hadoop',
                            'hypothesis test','iot','internet','machine learning','modeling','nosql','nlp',
                            'predictive','programming','python','r','sql','tableau','text mining',
                            'visualuzation'],
            }

        
    '''input by recruitor'''
    terms_addition = {}
    list_of_areas = ["Information Technologies","Finance", "Medical helthcare", "Engineering", "Marketing"]

    if recruiter==1:
        g={'Information technologies':keywords}
        terms_addition.update(g)
        # print(terms)
    elif recruiter==2:
        g={'Finance':keywords}
        terms_addition.update(g)
        # print(terms)
    elif recruiter==3:
        g={'Medical helthcare':keywords}
        terms_addition.update(g)
        # print(terms)
    elif recruiter==4:
        g={'Engineering':keywords}
        terms_addition.update(g)
        # print(terms)
    elif recruiter==5:
        g={'Marketing':keywords}
        terms_addition.update(g)
        # print(terms)
    terms.update(terms_addition)

    # print(terms)

    '''Scores calculation per area'''
    # Initializie score counters for each area
    quality = 0
    operations = 0
    supplychain = 0
    project = 0
    data = 0
    #new counter set by recruitor
    new_counter = 0

    # Create an empty list where the scores will be stored
    scores = []

    # Obtain the scores for each area
    for area in terms.keys():
            
        if area == 'Qualities':
            for word in terms[area]:
                if word in text:
                    quality +=1
            scores.append(quality)
            
        elif area == 'Operations management':
            for word in terms[area]:
                if word in text:
                    operations +=1
            scores.append(operations)
            
        elif area == 'Supply chain':
            for word in terms[area]:
                if word in text:
                    supplychain +=1
            scores.append(supplychain)
            
        elif area == 'Project management':
            for word in terms[area]:
                if word in text:
                    project +=1
            scores.append(project)
            
        elif area == 'Data analytics':
            for word in terms[area]:
                if word in text:
                    data +=1
            scores.append(data)

        else:
            for word in terms[area]:
                if word in text:
                    new_counter +=2
            scores.append(new_counter)




    ''' Sorted data frame for final scores creation'''

    
    summary = pd.DataFrame(scores,index=terms.keys(),columns=['score']).sort_values(by='score',ascending=False)
    summary

    '''Pie chart creation'''

    # Create pie chart visualization
    pie = plt.figure(figsize=(10,10))
    plt.pie(summary['score'], labels=summary.index, explode = (0.1,0,0,0,0,0), autopct='%1.0f%%',shadow=False,startangle=90)
    plt.title('resume representation')
    plt.axis('equal')
    # plt.show()


    list_of_scores.append(scores)

    # Save pie chart as a .png file

    # pie.savefig('resume_screening_results.png')

final_scores = []
for skills in list_of_scores:
    skills[0] *=1.5
    skills[1] *=1.5
    skills[3] *=1.5
    skills[4] *=2
    skills[5] *=5
    sum_sk = sum(skills)
    final_scores.append(sum_sk)
max = max(final_scores)

# final_scores[final_scores.index(max)] = 100

# for score in final_scores[1:]:
#     final_scores[final_scores.index(score)] = round(score * 100 / max , 1)        


sortedfinalscores=sorted(final_scores)
resumes=[]
reversed_scores = sortedfinalscores[::-1]
fivescores=[]
for i in range(5):
    fivescores.append(reversed_scores[i])
for i in fivescores:
    for j in final_scores:
        if i==j:
            resumes.append("resume"+str(1+final_scores.index(i)))
k=set(resumes)
print(*k)