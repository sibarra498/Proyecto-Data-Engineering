from fastapi import FastAPI, Form
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#app = Flask(__name__)
app = FastAPI()

@app.get('/')
async def root():
    return "Hello, listo pa probar esta poderosa api?"

def crearBases():
    amazon_prime_tittles = pd.read_csv("Datasets/amazon_prime_titles-score.csv")

    amazon_prime_tittles["id"] = "a" + amazon_prime_tittles["show_id"]
    amazon_prime_tittles["rating"].fillna("G", inplace = True)

    amazon_prime_tittles["type"] = amazon_prime_tittles["type"].str.lower()
    amazon_prime_tittles["title"] = amazon_prime_tittles["title"].str.lower()
    amazon_prime_tittles["director"] = amazon_prime_tittles["director"].str.lower()
    amazon_prime_tittles["cast"] = amazon_prime_tittles["cast"].str.lower()
    amazon_prime_tittles["country"] = amazon_prime_tittles["country"].str.lower()
    amazon_prime_tittles["date_added"] = amazon_prime_tittles["date_added"].str.lower()
    amazon_prime_tittles["listed_in"] = amazon_prime_tittles["listed_in"].str.lower()
    amazon_prime_tittles["description"] = amazon_prime_tittles["description"].str.lower()

    name=amazon_prime_tittles["duration"].str.split(expand=True)
    name.columns=["duration_int", "duration_type"]
    amazon_prime_tittles=pd.concat([amazon_prime_tittles, name], axis=1)

    amazon_prime_tittles.drop(["duration"], axis=1)

    amazon_prime_tittles["date_added"] = pd.to_datetime(amazon_prime_tittles["date_added"])
    amazon_prime_tittles["Plataforma"] = "amazon"
    amazon_prime_tittles["release_year"].min()

    #amazon_prime_tittles.head()
    print(amazon_prime_tittles)


    disney_plus_titles = pd.read_csv("Datasets/disney_plus_titles-score.csv")

    disney_plus_titles["id"] = "d" + disney_plus_titles["show_id"]
    disney_plus_titles["rating"].fillna("G", inplace = True)

    disney_plus_titles["type"] = disney_plus_titles["type"].str.lower()
    disney_plus_titles["title"] = disney_plus_titles["title"].str.lower()
    disney_plus_titles["director"] = disney_plus_titles["director"].str.lower()
    disney_plus_titles["cast"] = disney_plus_titles["cast"].str.lower()
    disney_plus_titles["country"] = disney_plus_titles["country"].str.lower()
    disney_plus_titles["date_added"] = disney_plus_titles["date_added"].str.lower()
    disney_plus_titles["listed_in"] = disney_plus_titles["listed_in"].str.lower()
    disney_plus_titles["description"] = disney_plus_titles["description"].str.lower()

    name=disney_plus_titles["duration"].str.split(expand=True)
    name.columns=["duration_int", "duration_type"]
    disney_plus_titles=pd.concat([disney_plus_titles, name], axis=1)

    disney_plus_titles.drop(["duration"], axis=1)

    disney_plus_titles["date_added"] = pd.to_datetime(disney_plus_titles["date_added"])
    disney_plus_titles["Plataforma"] = "disney"
    disney_plus_titles["release_year"].min()

    disney_plus_titles.head()
    print(disney_plus_titles)


    netflix_titles =pd.read_csv("Datasets/netflix_titles-score.csv")
    netflix_titles["id"] = "a" + netflix_titles["show_id"]
    netflix_titles["rating"].fillna("G", inplace = True)

    netflix_titles["type"] = netflix_titles["type"].str.lower()
    netflix_titles["title"] = netflix_titles["title"].str.lower()
    netflix_titles["director"] = netflix_titles["director"].str.lower()
    netflix_titles["cast"] = netflix_titles["cast"].str.lower()
    netflix_titles["country"] = netflix_titles["country"].str.lower()
    netflix_titles["date_added"] = netflix_titles["date_added"].str.lower()
    netflix_titles["listed_in"] = netflix_titles["listed_in"].str.lower()
    netflix_titles["description"] = netflix_titles["description"].str.lower()

    name=netflix_titles["duration"].str.split(expand=True)
    name.columns=["duration_int", "duration_type"]
    netflix_titles=pd.concat([netflix_titles, name], axis=1)
    netflix_titles.drop(["duration"], axis=1)
    netflix_titles["date_added"] = pd.to_datetime(netflix_titles["date_added"])
    netflix_titles["Plataforma"] = "netflix"
    netflix_titles.head()


    bases_datos = pd.concat([amazon_prime_tittles, disney_plus_titles, netflix_titles])
    #bases_datos

    return bases_datos
bases_datos = crearBases()

#Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
#@app.route('/CountKey', methods=["GET"])
@app.post("/CountKey")
async def login(plataforma: str = Form(), Keyword: str = Form()):
#def CountKey():
    #plataforma = request.form.get('plataforma')
    #Keyword = request.form.get('Keyword')
    print (plataforma) #, Keyword)
    #bases_datos.loc["Plataforma"]
    '''
    db_b = bases_datos[bases_datos.Plataforma == plataforma]
    db_b = db_b.loc[[True if Keyword in title else False for title in db_b["title"]]]
    #print (db_b)    
    Numero = len(db_b)
    '''
    Numero = "mrd"
    #print (Numero)
    return {
        "plataforma": plataforma,
        "Keywords": Keyword
    }
    #return Numero
#CountKey("netflix", "love")


#Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get('/score_count')
async def score_count():
#def score_count (plataforma, score, year):
    plataforma = "netflix"
    year = 2010
    score = 85

    db_b = bases_datos[bases_datos.Plataforma == plataforma]
    db_b1 = db_b[db_b.release_year == year]
    db_b2 = db_b1[db_b1.score > score]
    Numero = len(db_b2)
    print("plataforma: ",plataforma, "cantidad: ", Numero)
    return Numero
#score_count("netflix", 85, 2010)

@app.get('/Get_Second_Score')
def Get_Second_Score(plataforma):   
    db_b1 = bases_datos[(bases_datos.Plataforma == plataforma) & (bases_datos.type == "movie")]
    #db_b1 = bases_datos[]
    db_b2 = db_b1.sort_values('score', ascending=False) 
    
    #print(db_b2.iloc[0].score)
    try:
        db_b2 = db_b2[db_b2.score == db_b2.iloc[1].score]
    except:
        print("La plataforma de busqueda no fue encontrada¡¡")
        return "Error"
    db_b2 = db_b2.sort_values(by = 'title', ascending=True)
    #print(db_b2)
    #print(db_b2)
    try: 
        pelicula2 = db_b2.iloc[1].title
    except: 
        pelicula2 = db_b2.iloc[0].title
    scoreM = db_b2.iloc[0].score
    #print(pelicula2, "score: ", db_b2.iloc[0].score)
    return pelicula2 #, scoreM
#Get_Second_Score("amazon")


#Cantidad de series y películas por rating
@app.get('/longest')
def longest(plataforma, duration_type, year):
    db_b = bases_datos[bases_datos.Plataforma == plataforma]
    db_b1 = db_b[db_b.duration_type == duration_type]
    db_b2 = db_b1[db_b1.release_year == year].reset_index()
    db_b2.duration_int = db_b2.duration_int.astype(int)
    #db_b2.convert_dtypes(convert_string=False)
    #print(db_b2)
    db3 = db_b2.sort_values(by = 'duration_int', ascending=False)
    #for i in db3.duration_int:
        #print(i, type(i))
    #print(db3)
    peliculaMax = db3.iloc[0].title
    #print(max(db_b2.duration_int))
    #print(d)
    #db_b2[db_b2.duration_int.max()], db_b2[db_b2["duration_type"]]
    return peliculaMax #, db3.iloc[0].duration_int
#longest("netflix", "min", 2016)

@app.get('/rating_count')
def rating_count(rating):
    db_b = bases_datos[bases_datos.rating == rating]
    Numero = len(db_b)
    print ("rating: ",rating, "\ncantidad: ",Numero)
    return Numero
#rating_count("18+")
