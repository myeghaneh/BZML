
The aim of this project is improving the content analysis of ancient texts and books. We have used different state of the art machine learning and deep learning approach for this aim.  

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


Moreover, you can find the automatic classification of observational sentences in Kepler's book "Astronomia nova" using state of the art machine learning methods and NER.
![WORDCLUD](https://user-images.githubusercontent.com/43270094/65960891-4d591380-e40a-11e9-8fce-331950f18abe.jpg)


Regarding the dependency, you need to have spacy 2.1.8, scikit-learn 0.21.2. We recommend jupyterlab  1.1.3 . Alternatively you can install 
dependencies by running:
$pip install -r requirements.txt

