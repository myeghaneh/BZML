
The aim of this project is improving the content analysis of ancient texts and books using state of the art information extraction techniques empowered by machine learning and deep learning
![FrequencyplotAstronomia](https://user-images.githubusercontent.com/43270094/66916874-0c97f780-efd1-11e9-8d8f-0ddb1b230ff4.png)

 We have done a  several preprocessing steps for preparing the data and extracting useful information 

![word001](https://user-images.githubusercontent.com/43270094/66849589-fb48df80-ef2b-11e9-8b1f-c4d46225020f.png)
In this repository, you can find a refined named entity recognition (NER) model using spaCy which can annotate these labels:
<ul>
<li>LONG: Longitude and Coordinate in Different Formats</li> 
<li>PARA: Numerical Parameters</li> 
<li>ASTR: Astronomical Names</li> 
<li>DATE: Date in Different Formats </li>
<li>TIME: Time in Different Format </li>
<li>STAR: Names of Stars </li>
<li>PLAN: Planet's Names </li>
<li>NAME: Names of People and Places </li>
 <li>GEOM: Geometric Shapes </li>
</ul>
 
![annotation_update_bert_06](https://user-images.githubusercontent.com/43270094/66849737-4236d500-ef2c-11e9-93bd-9054ec6f95c2.JPG)


you can find here the result of the refined NER based on different metrics
```
{'uas': 0.0, 'las': 0.0, 'ents_p': 99.54797616601603, 'ents_r': 99.54797616601603, 'ents_f': 99.54797616601603, 'ents_per_type': {'ASTR': {'p': 99.80992608236537, 'r': 99.9154334038055, 'f': 99.86265187533017}, 'GEOM': {'p': 100.0, 'r': 99.85007496251875, 'f': 99.92498124531133}, 'NAME': {'p': 100.0, 'r': 99.25742574257426, 'f': 99.62732919254658}, 'PLAN': {'p': 99.88571428571429, 'r': 99.77168949771689, 'f': 99.82866933181039}, 'PARA': {'p': 98.51598173515981, 'r': 99.76878612716763, 'f': 99.13842619184378}, 'LONG': {'p': 99.7651203758074, 'r': 99.88242210464433, 'f': 99.82373678025851}, 'DATE': {'p': 99.5049504950495, 'r': 99.5049504950495, 'f': 99.5049504950495}, 'TIME': {'p': 97.97979797979798, 'r': 97.0, 'f': 97.48743718592964}, 'STAR': {'p': 84.61538461538461, 'r': 74.15730337078652, 'f': 79.04191616766467}}, 'tags_acc': 0.0, 'token_acc': 100.0}
```


Moreover, you can find the automatic classification of observational sentences in Kepler's book "Astronomia nova" using state of the art machine learning methods and NER.
![WORDCLUD](https://user-images.githubusercontent.com/43270094/65960891-4d591380-e40a-11e9-8fce-331950f18abe.jpg)


Regarding the dependency, you need to have spacy 2.1.8, scikit-learn 0.21.2. We recommend jupyterlab  1.1.3 . Alternatively you can install 
dependencies by running:
$pip install -r requirements.txt

