from flask import Flask,request,jsonify,render_template,redirect,url_for
from utils import LaptopPricePredication
import config
import traceback
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

@app.route('/')

def home():

    return render_template('laptop_price.html')

@app.route('/price', methods = ['GET', 'POST'])
def laptop_price():

    try:
        if request.method=='GET':

            print('+'*50)
            


            data = request.form
            print('DATA',data)

            processor_name      =  data['processor_name']
            processor_gnrtn     =  data['processor_gnrtn']
            ram_gb              =  data['ram_gb']
            ram_type            =  data['ram_type']
            ssd                 =  data['ssd']
            hdd                 =  data['hdd']
            os                  =  data['os']
            os_bit              =  data['os_bit']
            graphic_card_gb     = data['graphic_card_gb']
            weight              = data['weight']
            warranty            = data['warranty']
            Touchscreen         = data['Touchscreen']
            msoffice            = data['msoffice']
            rating              = data['rating']
            Number_of_Ratings   = data['Number_of_Ratings']
            Number_of_Reviews   = data['number_of_Reviews']
            brand               = data['brand']
            processor_brand     = data['processor_brand']

            Obj = LaptopPricePredication(processor_name, processor_gnrtn,ram_gb,ram_type,ssd,hdd,os,os_bit,graphic_card_gb,weight,warranty,Touchscreen,msoffice,rating,Number_of_Ratings,Number_of_Reviews,brand,processor_brand)

            
        
            laptop_price_prediction = Obj.get_predicted_price()

            return render_template('laptop_price.html',prediction =laptop_price_prediction)
        elif request.method == "POST" :
            print('*'*50)

            data = request.form
            print('DATA',data)

            processor_name      =  data['processor_name']
            processor_gnrtn     =  data['processor_gnrtn']
            ram_gb              =  data['ram_gb']
            ram_type            =  data['ram_type']
            ssd                 =  data['ssd']
            hdd                 =  data['hdd']
            os                  =  data['os']
            os_bit              =  data['os_bit']
            graphic_card_gb     = data['graphic_card_gb']
            weight              = data['weight']
            warranty            = data['warranty']
            Touchscreen         = data['Touchscreen']
            msoffice            = data['msoffice']
            rating              = data['rating']
            Number_of_Ratings   = data['Number_of_Ratings']
            Number_of_Reviews   = data['Number_of_Reviews']
            brand               = data['brand']
            processor_brand     = data['processor_brand']

            Obj = LaptopPricePredication(processor_name, processor_gnrtn,ram_gb,ram_type,ssd,hdd,os,os_bit,graphic_card_gb,weight,warranty,Touchscreen,msoffice,rating,Number_of_Ratings,Number_of_Reviews,brand,processor_brand)

            
        
            laptop_price_prediction = Obj.get_predicted_price()

            return render_template('laptop_price.html',prediction =laptop_price_prediction)

    except:

        print(traceback.print_exc())
        return jsonify({'Result':'unsucessfull'})



if __name__ == "__main__":


     app.run(host='0.0.0.0',port = config.PORT_NUMBER)