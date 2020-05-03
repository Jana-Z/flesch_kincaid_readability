import os 
import numpy as np 
import pandas as pd 
import urllib 
import zipfile 
import xmltodict 
import matplotlib.pyplot as plt
import collections

# import readability.calculator
 
# Dataset from: http://adrien.barbaresi.eu/corpora/speeches/#data

def calculate_readabilty_per_speaker(df):
    readability = dict.fromkeys(df.speaker.unique(), 0)  
    for index, row in df.iterrows(): 
        readability[row.speaker] += (   
            calculate_score(*get_counts(row.speech, lang='de'))   
        )
    for speaker in readability:
        readability[speaker] /= df['speaker'].value_counts().at[speaker]
    return readability

def plot_readability_per_speaker(readability):
    speakers = readability.keys()
    y_pos = np.arange(len(speakers))
    readability_scores = readability.values()

    plt.barh(y_pos, readability_scores, align='center', alpha=1)
    plt.yticks(y_pos, speakers)
    plt.xlabel('readability scores')
    plt.title('Readabilty scores of politicians')

    plt.show()

def plot_readability_per_year(readability):

    plt.plot(range(len(readability)), list(readability.values()))
    plt.xticks(range(len(readability)), list(readability.keys()), rotation=65)

    plt.show()

def calculate_readabilty_per_year(df):
    df_sorted_by_date = df.sort_values(by=['date'], inplace=False)
    readability = dict.fromkeys(df_sorted_by_date.date.unique(), 0)
    for index, row in df_sorted_by_date.iterrows(): 
        readability[row.date] += (   
            calculate_score(*get_counts(row.speech, lang='de'))   
        )
    for date in readability:
        readability[date] /= df_sorted_by_date['date'].value_counts().at[date]
    return readability

def get_speeches_from_web():
    DATA_PATH = "data" 
    DATA_FILE = "speeches.json" 
    REMOTE_PATH = "http://adrien.barbaresi.eu/corpora/speeches/" 
    REMOTE_FILE = "German-political-speeches-2018-release.zip" 
    REMOTE_URL = REMOTE_PATH + REMOTE_FILE 
    REMOTE_DATASET = "Bundesregierung.xml" 
    
    print('Collecting speeches...')
    zip_path = os.path.join(DATA_PATH, REMOTE_FILE) 
    urllib.request.urlretrieve(REMOTE_URL, zip_path) 
    with zipfile.ZipFile(zip_path) as file: 
        file.extract(REMOTE_DATASET, path=DATA_PATH) 
    xml_path = os.path.join(DATA_PATH, REMOTE_DATASET)  
    with open(xml_path, mode="rb") as file: 
        xml_document = xmltodict.parse(file) 
        nodes = xml_document['collection']['text']
    print('Import completed')
    return pd.DataFrame({
                        'speaker' : [t['@person'] for t in nodes],
                        'date': [t['@datum'] for t in nodes],
                        'speech' : [t['rohtext'] for t in nodes],
                        'place' : [t['@place'] for t in nodes]
                        })

def import_speeches_local():
    DATA_PATH = './data/German-political-speeches-2018-release'
    DATA_FILES = ['AuswärtigesAmt.xml', 'Bundespräsidenten.xml', 'Bundesregierung.xml', 'Bundestagspräsidenten.xml']

    print('Importing speeches...')
    dictionary = {'speaker' :[], 'date': [], 'speech': []}
    for data_file in DATA_FILES:
        xml_path = DATA_PATH + '/' +  data_file
        with open(xml_path, mode="rb") as file: 
            xml_document = xmltodict.parse(file) 
            nodes = (xml_document['collection']['text'])
        dictionary['speaker'].extend([t['@person'] for t in nodes])
        dictionary['date'].extend([t['@datum'] for t in nodes])
        dictionary['speech'].extend([t['rohtext'] for t in nodes])
    print('Import completed')
    return pd.DataFrame(dictionary)

def clean_data(df):
    df = df[df['speaker'] != 'k.A.']
    df.date = [re.findall(r'[[1-3][0-9]{3}', date)[0] for date in df.date]   # get years out of weird data formats
    df.date = df['date'].str.extract('(\d+)', expand=False).astype(int)
    return df