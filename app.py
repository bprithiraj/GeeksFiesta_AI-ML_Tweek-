import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import PowerTransformer
from sklearn.model_selection import train_test_split
TEMPLATES_AUTO_RELOAD=True

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

df4=pd.read_csv("file2.csv")
df5=df4.copy()

df5=df5.drop(columns=["year","month","day","hour"])
df5=df5.reindex(["wind_speed","wind_direction","pressure",'rain',"temperature",'PM2.5'],axis=1)
Y=df5['PM2.5']
df5.drop(columns=["PM2.5"],inplace=True)
X_train, X_test,Y_train, Y_test = train_test_split(df5, Y, test_size=0.2,random_state=0)

sc2=PowerTransformer()
sc2.fit(X_train)
X_train2=sc2.transform(X_train)
X_test2=sc2.transform(X_test)


sc3=PowerTransformer()
sc3.fit(Y_train.values.reshape(-1,1))
Y_train2=sc3.transform(Y_train.values.reshape(-1,1))
Y_test2=sc3.transform(Y_test.values.reshape(-1,1))
Dict = {0: 'E', 1: 'ENE', 2: 'ESE',3: 'N', 4: 'NE', 5: 'NNE', 6: 'NNW', 7: 'NW', 8: 'S', 9: 'SE', 10:'SSE', 11:'SSW', 12:'SW', 13:'W', 14:'WNW', 15:'WSW'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTMLGUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = np.array(float_features)
    final_features1=final_features[4:9:1]
    print(final_features1)
    final_features1[4]=final_features1[4]+273
    final_features1=sc2.transform(final_features1.reshape(1,-1))
    prediction = model.predict(final_features1)
    prediction[0]=sc3.inverse_transform(prediction[0].reshape(1,-1))
    output = prediction[0].astype("int")
    index=final_features[5].astype("int")
    return render_template('index.html', prediction_text1='Year= {}'.format(final_features[0].astype("int")),
                                         prediction_text2='Month= {}'.format(final_features[1].astype("int")),
                                         prediction_text3='Day= {}'.format(final_features[2].astype("int")),
                                         prediction_text4='Hour= {}'.format(final_features[3].astype("int")),
                                         prediction_text5='Wind Speed= {}'.format(final_features[4]),
                                         prediction_text6='Wind Direction= {}'.format(Dict[index]),
                                         prediction_text7='Pressure= {}'.format(final_features[6]),
                                         prediction_text8='Rain= {}'.format(final_features[7]),
                                         prediction_text9='Temperature= {}'.format(final_features[8]-273),
                                         prediction_text='PM2.5 concentration is  {}'.format(output))
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)



    

#return render_template('index.html', prediction_text='PM2.5 concentration is  {}'.format(output))