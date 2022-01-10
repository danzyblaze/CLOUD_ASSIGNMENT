from flask import Flask, redirect, render_template
from pymongo import MongoClient

import pandas as pd
import numpy as np
from plots import *

app =  Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/refresh_plots', methods=['GET'])
def refresh_plots():

    
    
    #get and mutate dataframe 
    sugar = pd.read_csv('CEN414DATA.csv')
    sugar = sugar[['Entity','Code','Year','Sugar cane-Yield-hg/ha']]
    print(sugar)
    
    #generate plots
    bar_plots(sugar)
    dispersion_plots(sugar)
     

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)