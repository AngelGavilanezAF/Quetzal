# Quetzal
# Pa'la Infomatrix

def quetzal(mensaje):
    mensaje = mensaje.lower()

    for tema in intenciones.values():
        if any(palabra in mensaje for palabra in tema["palabras"]):
            return tema["respuesta"]

    return "ERROR. No entendí tu pregunta, intenta formularla de otra manera o intentalo despues."



# SALUDOS
saludos = {
    
    "saludo_hola": {"palabras":
                    ["hola", "ola", "holaa", "olaa", "holaaa", "olaa", "holaaaaa"],
                    "respuesta":
                    "Hola, ¿en qué puedo ayudarte?"},
    
    "saludo_buenos_dias": {"palabras":
                           ["buenos dias", "buen dia", "bn dias", "bn dia"],
                           "respuesta":
                           "Buenos días, ¿qué deseas saber sobre agronomía?"},
    
    "saludo_buenas_tardes": {"palabras":
                             ["buenas tardes", "bn tardes"],
                             "respuesta":
                             "Buenas tardes, dime tu pregunta."},
    
    "saludo_Buenas_noches": {"palabras":
                             ["buenas noches", "Buenas noches", "buenas nachas", "Buenas nachas", "bn noches"],
                             "respuesta":
                             "Buenas noches, estoy listo para ayudarte."},
    
    "saludo_como_estas": {"palabras":
                          ["que tal", "Que tal","que tal?", "¿que tal?", "como estas", "Como estas", "como estas?", "¿como estas?", "¿Como estas?"],
                          "respuesta":
                          "Todo bien, ¿en qué te apoyo?"},
    
    "saludo_llamar_atencion": {"palabras":
                               ["hey", "Hey", "olle", "oye", "Olle", "Oye", "ey", "Ey", "oie", "Oie"],
                               "respuesta":
                               "Hola, ¿qué información buscas?"},
    
    "saludo_saludo": {"palabras":
                      ["saludos"], "respuesta":
                      "Saludos, pregunta lo que necesites."},
    
    "saludo_al_bot": {"palabras":
                      ["ola Quetzal", "hola quetzal", "Hola quetzal", "Hola Quetzal"],
                      "respuesta":
                      "Hola, como te apoyo?."},
    
    "saludo_insultante": {"palabras":
                          ["hola bot", "ola bot", "hola robot", "ola robot", "Ola bot", "Hola BOT"],
                          "respuesta":
                          "Hola..., dime tu duda."}
    
}



# MAÍZ
maiz = {
    
    "maiz_nutrientes": {"palabras":
                        ["fertilizante para el maiz","nutrientes para el maiz","nutriente del maiz",
                         "que nutrientes necesita el maiz","como fertilizar el maiz","abonado del maiz",
                         "abono para el maiz","fertilizacion del maiz", "fertilizante para el mais",
                         "fertilisante para el maiz", "fertilisante para el mais", "cuales son los nutrientes que necesita el maiz",
                         "cuales son los nutrientes que necesita el maiz?"],
                        "respuesta":
                        "El maíz requiere principalmente nitrógeno, fósforo y potasio. El nitrógeno es clave para el crecimiento, el fósforo para el desarrollo radicular y el potasio para el llenado de grano."},
    
    "maiz_plagas_comunes": {"palabras":
                            ["plagas del maiz","plagas comunes del maiz","plaga del maiz","gusanos del maiz",
                             "insectos del maiz","que plagas atacan el maiz"],
                            "respuesta":
                            "El gusano cogollero es una de las plagas mas comunes del maíz, siendo una larva voraz que ataca principalmente el cogollo y las hojas del maíz, causando graves pérdidas de rendimiento (hasta 50-100%) al alimentarse del punto de crecimiento y perforar mazorcas."},
    
    "maiz_sur_sinaloa": {"palabras":
                         ["mejor maiz para el sur de sinaloa","maiz recomendado para el sur de sinaloa",
                          "hibridos de maiz sur de sinaloa","que maiz sembrar en el sur de sinaloa"],
                         "respuesta":
                         "se recomiendan híbridos de maíz como Caribú, Garañón y Armadillo por su buen desarrollo y adaptación, aunque también el híbrido Sargento destaca por su precocidad y buen rendimiento en condiciones de sequía."},
    
    "maiz_centro_sinaloa": {"palabras":
                            ["maiz centro sinaloa","maiz recomendado centro de sinaloa","hibridos de maiz centro sinaloa",
                             "que maiz sembrar en el centro de sinaloa"],
                            "respuesta":
                            "En el centro de Sinaloa se usan híbridos de alto rendimiento, como el H-518 (INIFAP) por su calidad para industria y resistencia, o variedades de marcas reconocidas (Asgrow, Pioneer, Dekalb) que ofrecen buen rendimiento, sanidad y tolerancia a sequía y enfermedades."},
    
    "maiz_norte_sinaloa": {"palabras":
                           ["maiz norte sinaloa","maiz recomendado norte de sinaloa","hibridos de maiz norte sinaloa",
                            "que maiz sembrar en el norte de sinaloa"],
                           "respuesta":
                           "En el norte de Sinaloa se prefieren híbridos resistentes a sequía y con ciclos de crecimiento inermedio-tardio, como el NB 789 por su fortaleza y resistencia o el Sargento por su gran capacidad de tolerancia en ambientes de poca agua."},
    
    "maiz_epoca_siembra": {"palabras":
                           ["siembra de maiz","cuando sembrar maiz","epoca de siembra del maiz",
                            "fecha de siembra del maiz","como sembrar maiz"],
                           "respuesta":
                           "La siembra de maíz depende del ciclo agrícola de la zona, pero en sinaloa se enfoca principlamente el ciclo otoño-invierno, que van desde finales de octubre hasta mediados de diciembre."},
    
    "maiz_riego": {"palabras":
                   ["riego maiz", "como regar el maiz", "como reagar el maiz", "como relgar el maiz", "riego del maiz",
                    "cuanta agua necesita el maiz","frecuencia de riego del maiz"],
                   "respuesta":
                   "El maíz requiere riegos oportunos, especialmente en germinación, floración y llenado de grano, evitando tanto el estrés hídrico como el encharcamiento."},
    
    "maiz_variedades": {"palabras":
                        ["variedades del maiz", "tipos de maiz", "clases de maiz", "maiz hibrido","maiz criollo"],
                        "respuesta":
                        "Existen variedades híbridas de alto rendimiento y variedades criollas, que suelen ser más rústicas y adaptadas a condiciones locales."},
    
    "maiz_enfermedades": {"palabras":
                          ["enfermedades del maiz", "enfermedades del miaz", "enfermedad del maiz", "hongos del maiz", "roya del maiz",
                           "tizon del maiz", "enfermedades comunes del maiz"],
                          "respuesta":
                          "Las enfermedades comunes incluyen roya y tizón, siendo enfermedades fúngicas que afectan las hojas, causando manchas y reduciendo la fotosíntesis, lo que disminuye el rendimiento de la planta."},
    
    "maiz_produccion": {"palabras":
                        ["produccion de maiz", "rendimiento del maiz", "cuanto produce el maiz", "cosecha de maiz",
                         "rendimiento por hectarea de maiz"],
                        "respuesta":
                        "La producción de maíz depende del manejo agronómico de dueño de la huerta."},
    
}


# TOMATE

tomate = {
    "tomate_nutriente": {"palabras":
                         ["fertilizante tomate", "fertilizante del tomate", "nutriente tomate", "nutriente del tomate",
                          "fertilizante para el tomate", "nutriente para el tomate", "nutrinetes para el tomate",
                          "que nutrientes necesita el tomate", "que nutrientes necesita el tomate?"],
                         "respuesta":
                         "El tomate necesita macronutrientes como Nitrógeno (N) para sus hojas y tallos, Fósforo (P) para las raíces y la floración, y especialmente Potasio (K) para su sabor y el tamaño del fruto, además de Calcio (Ca) que le ayuda a la firmeza, previene podredumbre apical y Magnesio (Mg) para la fotosíntesis."},
    
    "tomate_plagas_comunes": {"palabras":
                              ["plagas del tomate", "plaga mas comun del tomate", "posibles plagas del tomate",
                               "insectos dañinos del tomate", "posibles plagas del tomate"],
                              "respuesta":
                              "La mosca blanca es una plaga comun y muy devastadora que chupa la savia, amarillea las hojas, produce melaza (que causa fumagina negra), frena el crecimiento y transmite virus como el del Rizado Amarillo."},
    
    "tomate_sur_sinaloa": {"palabras":
                           ["tomate sur sinaloa", "mejor tomate para el sur de sinaloa", "tomate recomendado para el sur de sinaloa",
                            "que tomate me recomiendas para el sur de sinaloa", "que tomate me recomiendas para el sur de sinaloa?",
                            "cual es el tomate que me recomiendas para el sur de sinaloa?"],
                           "respuesta":
                           "En el sur de Sinaloa se recomienda tomate saladette, muy productivo, carnoso, con pocas semillas e ideal para salsas y consumo fresco, adaptado a ciclos largos y cortos en la región."},
    
    "tomate_centro_sinaloa": {"palabras":
                              ["tomate centro sinaloa", "mejor tomate para el centro de sinaloa",
                               "tomate recomendado para el centro de sinaloa", "que tomate me recomiendas para el centro de sinaloa",
                               "que tomate me recomiendas para el norte de sinaloa?", "cual es el tomate que me recomiendas para el centro de sinaloa?"],
                              "respuesta":
                              "En el centro de Sinaloa el tomate saladette (tipo Roma) es el más común y productivo, destacando por su resistencia y rendimiento para exportación."},
    
    "tomate_norte_sinaloa": {"palabras":
                             ["tomate norte sinaloa", "mejor tomate para el norte de sinaloa",
                              "tomate recomendado para el norte de sinaloa", "que tomate me recomiendas para el norte de sinaloa",
                              "que tomate me recomiendas para el norte de sinaloa?", "cual es el tomate que me recomiendas para el sur de sinaloa?"],
                             "respuesta":
                             "la Variedad SVTE8444 (Seminis) Considerada la mejor opción para tomate Roma por productores locales, destaca por su genética superior, buena producción y resistencias a enfermedades como el virus de la hoja blanca."},
    
    "tomate_riego": {"palabras":
                 ["riego tomate", "cada cuanto se debe de reguar el tomate", "que tanta agua nesesita el tomate",
                  "que tanta agua necesita el tomate", "que tanta agua necesita el tomate?"],
                 "respuesta":
                 "con una frecuencia que varía de diaria en pleno verano (2-4L/planta) a 1-2 veces por semana en primavera, teniendo cuidado de solo regar el tayo no las hojas."},
    
    "tomate_siembra": {"palabras":
                       ["siembra tomate", "cuando sembrar tomate", "cuando es la temporada del tomate",
                        "cuando sembrar tomate?", "cuando es la temporada del tomate?" ],
                       "respuesta":
                       "En Sinaloa, la temporada principal de siembra de tomate (jitomate) para el ciclo otoño-invierno es octubre y noviembre, con siembras iniciando desde finales de septiembre, para cosechar entre diciembre y mayo, siendo este estado el principal productor nacional."},
    
    "tomate_enfermedades": {"palabras":
                            ["enfermedades del tomate", "cual es la enfermedad mas comun del tomate", "infecciones del tomate",
                             "enfermedades mas comunes del tomate"],
                            "respuesta":
                            "La enfermedad más común del tomate varía por la region, pero el Tizón Temprano (Alternaria) y el Mildiu (Phytophthora infestans) son muy frecuentes, afectando hojas y frutos con manchas."}
    
    }


# CHILE

chile = {
    "chile_nutriente": {"palabras":
                        ["fertilizante chile", "nutriente que ocupa el chile", "que nutrientes necesita el chile",
                         "fertilizante para el chile", "cuales son los nutrinetes qque necesita el chile?"],
                        "respuesta":
                        "Para el cultivo de chile, los nutrientes clave son los macronutrientes NPK (Nitrógeno, Fósforo, Potasio) para crecimiento y frutos, además de Calcio, Magnesio y Azufre, que son esenciales para la estructura, floración y calidad."},
    
    "chile_plagas": {"palabras":
                     ["plagas del chile", "cuales son las plagas del chile", "cuales son las plagas del chile?",
                      "que son los pulgones en el chile", "que son los trips en el chile", "que son los trips en el chile?",
                      "que son los pulgones en el chile?"],
                     "respuesta":
                     "en general, pulgones, trips y ácaros que afectan cultivos como el chile. En ámbitos urbanos, las más frecuentes son roedores (ratas), cucarachas, chinches, hormigas y palomas."},
    
    "chile_sur_sinaloa": {"palabras":
                          ["chile sur sinaloa", "mejor chile para el sur de sinaloa", "variedades de chile para el sur de sinaloa",
                           "mejor variedad de chile para el sur de sinaloa", "chile recomendado para el sur de sinaloa"],
                          "respuesta":
                          "Para el sur de Sinaloa, los chiles más destacados son el Chiltepín (para sabor local, aguachiles y mariscos), el Serrano, y opciones comerciales como Habanero, Jalapeño, Güero y Ancho, que se cultivan extensivamente en la región, adaptándose a las fértiles tierras del sur, como el valle de Escuinapa y Rosario."},
    
    "chile_centro_sinaloa": {"palabras":
                             ["chile centro sinaloa", "mejor chile para el centro de sinaloa", "variedades de chile para el centro de sinaloa",
                              "mejor variedad de chile para el centro de sinaloa", "chile recomendado para el centro de sinaloa"],
                             "respuesta":
                             "Para el centro de Sinaloa, el Chile Chiltepín es el rey indiscutible, esencial en platillos locales como aguachiles y mariscos, usándose fresco, seco o en polvo."},
    
    "chile_norte_sinaloa": {"palabras":
                            ["chile norte sinaloa", "mejor chile para el norte de sinaloa", "variedades de chile para el norte de sinaloa",
                              "mejor variedad de chile para el norte de sinaloa", "chile recomendado para el norte de sinaloa"],
                            "respuesta":
                            "Para el norte de Sinaloa, el chile chiltepín (o piquín) es el más emblemático y consumido, apreciado en sus versiones verde (para aguachiles, molcajetes) y rojo (seco, para sazonar), destacando por su picor intenso y su uso tradicional."},
    
    "chile_riego": {"palabras":
                    ["riego chile", "cada cuanto se debe de reguar el chile", "que tanta agua nesesita el chile",
                  "que tanta agua necesita el chile", "que tanta agua necesita el chile?", "cuanto regar el chile",
                     "cada cuanto se debe reguar el chile"],
                    "respuesta":
                    "El chile necesita riego constante pero moderado, con mayor demanda durante la floración y fructificación; en climas cálidos, riega diario o cada dos días, dejando secar ligeramente la superficie entre riegos para evitar exceso, y en climas frescos, cada dos o tres días; prefiere riego profundo y por abajo para evitar enfermedades, asegurando buen drenaje y humedad en el suelo sin encharcar."},
    
    "chile_siembra": {"palabras":
                      ["siembra chile", "cuando sembrar chile", "cuando es la temporada del chile",
                       "cuando sembrar chile?", "cuando es la temporada del chile?"],
                      "respuesta":
                      "La temporada fuerte de chile en Sinaloa, especialmente para variedades como jalapeño y serrano, va de finales de otoño hasta la primavera, con picos de cosecha entre diciembre y abril/mayo, aunque las siembras inician en octubre y noviembre, marcando el inicio de la temporada de corte que se extiende varios meses y varía según la región dentro del estado."},
    
    "chile_enfermedades": {"palabras":
                           ["enfermedades chile", "cual es la enfermedad mas comun del chile", "infecciones del chile",
                            "enfermedades mas comunes del chile"],
                           "respuesta":
                           "Las enfermedades del chile incluyen problemas fúngicos como la Marchitez del Chile (causada por Phytophthora capsici), pudriciones de raíz, Damping-off, y manchas foliares como la de Alternaria y ojo de rana; bacterianas como el tizón; virales como el mosaico del tabaco y rizado amarillo, y problemas por nematodos o nutricionales, que afectan hojas, tallos y frutos, reduciendo drásticamente el rendimiento del cultivo."},
    
    
}


# MANGO

mango = {
    "mango_nutriente": {"palabras":
                        ["fertilizante mango", "nutriente que ocupa el mango", "que nutrientes necesita el mango",
                         "fertilizante para el mango", "cuales son los nutrientes que necesita el mango?"],
                        "respuesta":
                        "El cultivo de mango requiere un balance adecuado de macronutrientes como Nitrógeno (N) para el crecimiento vegetativo, Fósforo (P) para el desarrollo radicular y floración, y Potasio (K) para la formación y calidad del fruto; además, micronutrientes como Zinc, Boro, Hierro y Calcio son fundamentales para evitar deformaciones, mejorar la floración y asegurar una buena producción."},
    
    "mango_plagas": {"palabras":
                     ["plagas del mango", "cuales son las plagas del mango", "cuales son las plagas del mango?",
                      "que es la mosca de la fruta en el mango", "plagas comunes del mango",
                      "insectos que atacan al mango"],
                     "respuesta":
                     "Las principales plagas del mango incluyen la mosca de la fruta, que daña directamente el fruto, además de trips, escamas, ácaros, barrenadores del tallo y pulgones; estas plagas afectan hojas, flores y frutos, reduciendo la calidad y el rendimiento si no se controlan oportunamente."},
    
    "mango_sur_sinaloa": {"palabras":
                          ["mango sur sinaloa", "mejor mango para el sur de sinaloa", "variedades de mango para el sur de sinaloa",
                           "mango recomendado para el sur de sinaloa"],
                          "respuesta":
                          "En el sur de Sinaloa, las variedades de mango más cultivadas son Ataulfo y Manila, debido a su buena adaptación al clima cálido-húmedo, su alta demanda comercial y su excelente calidad para consumo fresco y exportación."},
    
    "mango_centro_sinaloa": {"palabras":
                             ["mango centro sinaloa", "mejor mango para el centro de sinaloa", "variedades de mango para el centro de sinaloa",
                              "mango recomendado para el centro de sinaloa"],
                             "respuesta":
                             "Para el centro de Sinaloa, destacan variedades como Kent y Haden, ampliamente cultivadas por su buen tamaño de fruto, resistencia al manejo postcosecha y su aceptación en mercados nacionales e internacionales."},
    
    "mango_norte_sinaloa": {"palabras":
                            ["mango norte sinaloa", "mejor mango para el norte de sinaloa", "variedades de mango para el norte de sinaloa",
                             "mango recomendado para el norte de sinaloa"],
                            "respuesta":
                            "En el norte de Sinaloa, el mango Tommy Atkins es el más representativo, ya que se adapta bien a condiciones más secas, tiene alta productividad y es muy resistente al transporte, lo que lo hace ideal para exportación."},
    
    "mango_riego": {"palabras":
                    ["riego mango", "cada cuanto se riega el mango", "que tanta agua necesita el mango",
                     "riego del mango", "necesidades de agua del mango"],
                    "respuesta":
                    "El mango requiere riego regular principalmente durante las etapas tempranas de desarrollo, floración y llenado del fruto; en climas cálidos se recomienda riego cada 5 a 7 días, mientras que en climas más frescos puede espaciarse, evitando encharcamientos, ya que el exceso de humedad favorece enfermedades radiculares."},
    
    "mango_siembra": {"palabras":
                      ["siembra mango", "cuando sembrar mango", "como se siembra el mango",
                       "cuando es la temporada del mango"],
                      "respuesta":
                      "La siembra del mango se realiza generalmente mediante plantas injertadas para asegurar calidad y uniformidad; la plantación se recomienda al inicio de la temporada de lluvias o con riego asegurado, permitiendo un buen establecimiento del árbol durante sus primeros meses."},
    
    "mango_enfermedades": {"palabras":
                           ["enfermedades mango", "cuales son las enfermedades del mango", "enfermedades mas comunes del mango",
                            "infecciones del mango"],
                           "respuesta":
                           "Entre las enfermedades más comunes del mango se encuentran la antracnosis, el oídio, la mancha bacteriana y pudriciones de raíz; estas afectan flores, hojas y frutos, provocando caída floral, manchas y pérdidas significativas en la producción si no se manejan adecuadamente."},
    
    "mango_variedades": {"palabras":
                         ["variedades mango", "tipos de mango", "cuales son las variedades de mango",
                          "mangos mas comunes"],
                         "respuesta":
                         "Las variedades de mango más comunes incluyen Ataulfo, Kent, Tommy Atkins, Haden y Manila, cada una con características específicas de sabor, tamaño, color y uso comercial, tanto para consumo fresco como para exportación."},
    
    "mango_produccion": {"palabras":
                         ["produccion mango", "cultivo del mango", "importancia del mango",
                          "produccion de mango en mexico"],
                         "respuesta":
                         "El mango es uno de los cultivos frutícolas más importantes de México y de Sinaloa, con alta relevancia económica y gran demanda en mercados nacionales e internacionales, destacando por su producción para exportación y generación de empleo en zonas rurales."}
    
}



# UAS

uas = {
    "uas_general": {"palabras":
                    ["uas", "universidad uas", "que es la uas", "que significa uas", "universidad de sinaloa"],
                    "respuesta":
                    "La UAS significa Universidad Autónoma de Sinaloa y es una institución pública de educación superior con presencia en todo el estado de sinaloa, dedicada a la formación académica, la investigación científica y la vinculación social."},

    "uas_nombre": {"palabras":
                   ["universidad autonoma de sinaloa", "nombre completo uas", "como se llama la uas", "siglas uas"],
                   "respuesta":
                   "El nombre completo de la UAS es Universidad Autónoma de Sinaloa, una de las universidades públicas más importantes del noroeste de México, con una amplia oferta educativa en nivel medio superior y superior."},

    "uas_agronomia": {"palabras":
                      ["facultad de agronomia", "facultad de agronomia uas", "agronomia uas",
                       "estudiar agronomia en la uas", "carrera de agronomia uas"],
                      "respuesta":
                      "La Facultad de Agronomía de la UAS forma profesionales en ingeniería agronómica, capacitados para mejorar la producción agrícola, el manejo de cultivos, suelos, agua y la sustentabilidad del campo."},

    "uas_carrera_agronomia": {"palabras":
                              ["ingenieria agronomica", "carrera de ingenieria agronomica",
                               "que es ingenieria agronomica", "para que sirve la agronomia"],
                              "respuesta":
                              "La ingeniería agronómica es una carrera clave para el desarrollo del sector agrícola, enfocada en la producción de alimentos, el manejo de recursos naturales, la sanidad vegetal y la innovación tecnológica en el campo."},

    "uas_campus": {"palabras":
                   ["campus uas", "campus de la uas", "donde hay uas", "ubicaciones uas"],
                   "respuesta":
                   "La Universidad Autónoma de Sinaloa cuenta con múltiples campus y unidades académicas distribuidas en todo el estado, permitiendo el acceso a la educación superior en zonas urbanas y rurales."},

    "uas_estudiar": {"palabras":
                     ["estudiar en la uas", "porque estudiar en la uas", "beneficios de estudiar en la uas",
                      "ventajas de la uas"],
                     "respuesta":
                     "Estudiar en la UAS representa una gran oportunidad académica, ya que ofrece educación de calidad, docentes capacitados, costos accesibles y programas acreditados a nivel nacional."},

    "uas_investigacion": {"palabras":
                          ["investigacion uas", "investigacion cientifica uas", "proyectos de investigacion uas",
                           "ciencia uas"],
                          "respuesta":
                          "La UAS realiza investigación científica y tecnológica en diversas áreas del conocimiento, contribuyendo al desarrollo social, agrícola, industrial y educativo del estado y del país."},

    "uas_infomatrix": {"palabras":
                       ["infomatrix", "infomatrix latinoamerica", "proyecto infomatrix", "concurso infomatrix"],
                       "respuesta":
                       "Infomatrix Latinoamérica es un evento académico donde se presentan proyectos científicos y tecnológicos, y la UAS participa activamente representando a Sinaloa con propuestas innovadoras."},

    "uas_proyectos": {"palabras":
                      ["proyecto uas","proyectos uas","representacion uas","proyecto universitario uas"],
                      "respuesta":
                      "Los proyectos de la UAS reflejan el compromiso de la universidad con la innovación, la investigación y la formación integral de sus estudiantes, representando a la institución en eventos regionales y nacionales."}
}



# UNIR TODO

intenciones = {}
intenciones.update(saludos)
intenciones.update(maiz)
intenciones.update(tomate)
intenciones.update(chile)
intenciones.update(mango)
intenciones.update(uas)


# PRUEBA

while True:
    mensaje_usuario = input("Usuario: ")
    
    if mensaje_usuario.lower() == "salir":
        break
    print("Quetzal:", quetzal(mensaje_usuario))
