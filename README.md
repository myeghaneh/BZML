
The aim of this project is improving the content analysis of ancient texts and books. We have used different state of the art machine learning and deep learning approach for this aim.  

![photo_2019-07-05_18-56-01](https://user-images.githubusercontent.com/43270094/66849384-a60cce00-ef2b-11e9-9b17-05f8b221477e.jpg)

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
 
![annotation_update_bert_04](https://user-images.githubusercontent.com/43270094/65961285-1fc09a00-e40b-11e9-9dd9-1f25f72c37f7.JPG)

Moreover, you can find the automatic classification of observational sentences in Kepler's book "Astronomia nova" using state of the art machine learning methods and NER.
![WORDCLUD](https://user-images.githubusercontent.com/43270094/65960891-4d591380-e40a-11e9-8fce-331950f18abe.jpg)


Regarding the dependency, you need to have spacy 2.1.8, scikit-learn 0.21.2. We recommend jupyterlab  1.1.3 . Alternatively you can install 
dependencies by running:
$pip install -r requirements.txt

