from bs4 import BeautifulSoup #import beautifulsoup
import requests
from urllib.request import Request, urlopen


class Scrape :

    website = "https://www.mayoclinic.org"
    disease = {}
    def __init__(self):
        #content = urlopen('https://www.mayoclinic.org/symptom-checker/select-symptom/itt-20009075')
        url = "https://www.mayoclinic.org/symptom-checker/select-symptom/itt-20009075"
        request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"}) 
        webpage = urlopen(request_site).read()
        self.main_response = requests.get('https://www.mayoclinic.org/symptom-checker/select-symptom/itt-20009075')
         
    def Age (self, age_type ):
        response = self.main_response.text
        soup = BeautifulSoup(response,'lxml')
        if age_type == "adult" :
            age_adult = soup.find('div', class_ = 'adult').find_all('li')
            for symp in age_adult :
                symptom = symp.find('a').text
                a_href= self.website + symp.find("a").get("href")
                self.disease.update({symptom:a_href})
            return (self.disease)
        elif age_type == "child":
            age_child = soup.find('div', class_ = 'child').find_all('li')
            for symp in age_child :
                symptom = symp.find('a').text
                a_href= self.website+ symp.find("a").get("href")
                self.disease.update({symptom:a_href})
            return (self.disease)
        response.close()
    
    def Symptom_View (self, diseases) :
        for i,j in diseases.items():
            #print(i," = ", j)
            break
    
    def Get_Symptom_List(self, symptom, diseases):
        href = diseases[symptom]
        response = requests.get(href).text
        soup = BeautifulSoup(response,'lxml')
        form_item = soup.find_all('div', class_ = 'frm_item')
        symptoms = {}
        for symp in form_item:
            symp_type = symp.find('legend').text
            k = symp.find_all('label')
            l =[]
            for s in k :
                l.append(s.text)
            symptoms.update({symp_type:l})
        return symptoms

    def Get_Symptom_Link(self, symptom, diseases):
        href = diseases[symptom]
        request_site = Request(href, headers={"User-Agent": "Mozilla/5.0"}) 
        webpage = urlopen(request_site).read()
        response = requests.get(href).text
        print(response)
        soup = BeautifulSoup(response,'lxml')
        form_item = soup.find_all('div', class_ = 'frm_item')
        symptoms_id = {}
        symptoms = {}
        count= 0
        for symp in form_item:
            symp_type = symp.find('legend').text
            k = symp.find_all('label')
            l = []
            symp_info = symp.find_all('li')
            for each_symp in symp_info :
                symp_id = each_symp.find('input').get('id')
                symp_text = each_symp.find('label').text
                symptoms_id.update({symp_text:symp_id})
                count += 1
            for s in k :
                l.append(s.text)
            symptoms.update({symp_type:l})
        return(symptoms, symptoms_id)

    def Get_Final_Diagnosis (self, result ):
        soup = BeautifulSoup(result,'lxml')
        form_item = soup.find_all('div', attrs={'class':'expandable factors'})
        print(form_item)
        for j in form_item:
            x = 0
            disease_link = j.find('a').get('href')
            disease_name = j.find('a').text
            disease_description = j.find_all('li')

            print(disease_name , " = ", self.website+disease_link) 
            for des in disease_description:
                if x == 0 :
                    print("Main Reason - ", des.text)
                else :
                    print("\n",des.text)
                x += 1
            #print(disease_name , " = ", self.website+disease_link) 

                #symptom1 = each_symp.find('input').get("id")
                #print(symptom1)
                #a_href= each_symp.find("a").get("href")
                #self.disease.update({symptom:a_href})
            #return (self.disease)
            #l =[]
            #for s in k :
             #   l.append(s.text)
            #symptoms.update({symp_type:l})
        #return symptoms

    '''def Symptoms_Select(self, symptom, diseases,specific):
        href = diseases[symptom]
        response = requests.get(href).text
        soup = BeautifulSoup(response,'lxml')
        form_item = soup.find_all('div', class_ = 'frm_item')
        form = soup.find('div', class_= 'form')
        print(form)
        for symp in form_item:
            symp_type = symp.find('legend').text
            k = symp.find_all('label')
            checkbox = symp.find('input', type='checkbox')
            # Select the checkbox by setting the 'checked' attribute to True
            checkbox.attrs['checked'] = True
            break
        button = soup.find('button')
        #response = requests.post(form['action'])
        #soup = BeautifulSoup(response,'lxml')
        #form_item = soup.find_all('div', class_ = 'frm_item')
        #print(form_item)
        #print(symptom)
        #print(symptoms)
        #print(diseases)'''

#p = Scrape()
#c= p.Age("child")
#p.Symptom_View(c)
#s = p.Get_Symptom_Link("Abdominal pain in children", c)
#print(s[1])
#p.Symptoms_Select("Abdominal pain in children", c, "Crampy")