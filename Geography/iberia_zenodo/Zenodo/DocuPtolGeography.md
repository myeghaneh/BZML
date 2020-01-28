# Ptolemy's catalogue of localities of the Iberian peninsula

Extract of Ptolemy's geographical catalogue, covering the localities of the Iberian peninsula (Geography 2.4-2.6) of the two main textual recensions of the work (Xi and Omega), based on the Greek text edited by (@StueckelbergerGrasshoff2006). The coordinates of the Xi recension follow the readings of the Vaticanus gr. 191, as they are edited in the main text together with the critical apparatus by the editors.

# Files

  - **OmegaStructure.json** : Ptolemy's catalogue for the Iberian peninsula in the Omega recension of the Geography. The structure of the JSON files reproduces the structure of Ptolemy's text.
  - **XiStructure.json** : Ptolemy's catalogue for the Iberian peninsula in the Xi recension of the Geography. The structure of the JSON files reproduces the structure of Ptolemy's text.

# Database keys:

  - **ID**: identification number of a part of the catalogue. Each single part of the catalogue has a unique number, which is composed of 4 items: the numbers of the book, the chapter and the section of the catalogue, followed by a personal number -- "2.06.07.01", "2.06.07.02" etc.

  - **book_ID**: book's number. The chapters devoted to Iberia are in Book 2 of Ptolemy's Geography.

  - **category**: category of a locality. A locality can be a city, a mountain, a river source etc. and can also belong to several categories (e.g. "river mouth" and "boundary").

  - **chapters**: part of a book. The part of the catalogue devoted to Iberia covers three chapters, for each of the three provinces of the peninsula.

  - **chap_ID**: chapter's number. It is composed of 2 items: the book's number and a personal number -- "2.04", "2.05", "2.06".

  - **coord**: geographical coordinates. They are composed of a latitude ("lat") and a longitude ("long").

  - **fraction**: fractional part of a coordinate (latitude or longitude)

  - **integer**: integer part of a coordinate (latitude or longitude)

  - **lat**: latitude. Position of a locality on a north-south axis, expressed in degrees counted from the equator. Each latitude is composed of a integer number of degrees and a decimal part expressed as fractions of degrees.

  - **long**: longitude. Position of a locality on a west-east axis, expressed in degrees counted from a prime meridian, defined by Ptolemy as running through the Fortunate Islands, at the western extremity of the known world. Each longitude is composed of a integer number of degrees and a decimal part expressed as fractions of degrees.

  - **people**: name of ancient people. Ptolemy mentions 61 different peoples in the Iberian peninsula -- e.g. "Vettones", "Carpetani", "Lusitani".

  - **section**: part of a chapter. Each chapter, devoted to a single province, is divided into small units, called here "sections" and covering a specific area of the province.

  - **sec_ID**: section's number. A section's number is composed of 3 items: the numbers of the book and the chapter, followed by a personal number. -- "2.04.01", ""2.04.02" etc.

  - **sec_part**: part of a section. Each section contains one or several items, all identified with an "ID" number.

  - **text**: Greek text. Sentences or words written by Ptolemy that are not toponyms or coordinates. It can be a heading, an introduction to a section, a description of boundaries etc.

  - **toponym**: ancient locality's name in Greek -- e.g. "Ἴσπαλις", "Βαρβάριον ἄκρον".

  - **type**: type of a section's part. It can be a locality (associated with coordinates), a people, a small textual description and so on. -- e.g. "locality", "people", "text string".

  - **type_sec**: type of a section. A section of the catalogue can be a stretch of coast, a description of borders, a specific inland area of the map etc. -- e.g. "coast section", "borders description", "inland".

  # Reference

  Defaux, Olivier. 2017. _The Iberian Peninsula in Ptolemy's Geography.
  Origins of the Coordinates and Textual History_. Berlin Studies of the
  Ancient World 51. Berlin: Edition Topoi. https://doi.org/10.17171/3-51.

  Stückelberger, A., and G. Graßhoff. 2006. _Klaudios Ptolemaios. Handbuch
  der Geographie_. Basel: Schwabe.
