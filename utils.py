import pickle
import json
import numpy as np
import config




class LaptopPricePredication():

    def __init__(self,processor_name, processor_gnrtn,ram_gb,ram_type,ssd,hdd,os,os_bit,graphic_card_gb,weight,warranty,Touchscreen,msoffice,rating,Number_of_Ratings,Number_of_Reviews,brand,processor_brand):

        print('we are in init function')
        self.processor_name =    processor_name
        self.processor_gnrtn=   processor_gnrtn
        self.ram_gb =           ram_gb
        self.ram_type=          ram_type
        self.ssd=               ssd
        self.hdd=               hdd
        self.os =               os
        self.os_bit=            os_bit
        self.graphic_card_gb=   graphic_card_gb
        self.weight =           weight
        self.warranty =         warranty
        self.Touchscreen =      Touchscreen
        self.msoffice =         msoffice
        self.rating=               rating
        self.Number_of_Ratings= Number_of_Ratings
        self.Number_of_Reviews =Number_of_Reviews
        self.brand=             brand 
        self.processor_brand=   processor_brand

    def __load_save_data(self):

        
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)
    


    def get_predicted_price(self):

        self.__load_save_data()


        test_array = np.zeros([1,self.model.n_features_in_])
        processor_name      =  self.json_data['processor_name'][self.processor_name]
        processor_gnrtn     =  self.json_data['processor_gnrtn'][self.processor_gnrtn]
        ram_gb              =  self.json_data['ram_gb'][self.ram_gb]
        ram_type            =  self.json_data['ram_type'][self.ram_type]
        ssd                 =  self.json_data['ssd'][self.ssd]
        hdd                 =  self.json_data['hdd'][self.hdd]
        os                  =  self.json_data['os'][self.os]
        os_bit              =  self.json_data['os_bit'][self.os_bit]
        graphic_card_gb     = self.json_data['graphic_card_gb'][self.graphic_card_gb]
        weight              = self.json_data['weight'][self.weight]
        warranty            = self.json_data['warranty'][self.warranty]
        Touchscreen         = self.json_data['Touchscreen'][self.Touchscreen]
        msoffice            = self.json_data['msoffice'][self.msoffice]
        rating              = self.json_data['rating'][self.rating]


        brand               = 'brand_'+self.brand
        brand_index =   self.json_data['column names'].index(brand)

        processor_brand     = 'processor_brand_'+self.processor_brand
        processor_brand_index  = self.json_data['column names'].index(processor_brand)

        test_array[0,0] =     processor_name
        test_array[0,1] =     processor_gnrtn
        test_array[0,2] =      ram_gb
        test_array[0,3] =      ram_type
        test_array[0,4] =      ssd
        test_array[0,5] =      hdd
        test_array[0,6] =      os
        test_array[0,7] =      os_bit
        test_array[0,8] =      graphic_card_gb
        test_array[0,9] =      weight
        test_array[0,10] =     warranty
        test_array[0,11] =     Touchscreen
        test_array[0,12] =     msoffice
        test_array[0,13] =     rating
        test_array[0,14] =      self.Number_of_Ratings
        test_array[0,15] =      self.Number_of_Reviews
        test_array[0,brand_index] =  1
        test_array[0,processor_brand_index] =  1

        predict_price = self.model.predict(test_array)[0]
        return np.around(predict_price,3)

# get_predicted_price('Core i3','10th','4 GB','DDR4','1024 GB','0 GB','Mac','64-bit','0 GB','Casual','No warranty','No','Yes','3 stars',10,20,'ASUS','AMD')



