from flask import Flask,render_template,request
import os
import numpy as np
import pandas as pd
from src.datascience_project.pipeline.prediction_pipeline import PredictionPipeline

app=Flask(__name__)

@app.route('/',methods=['GET'])
def homepag():
    return render_template("index.html")