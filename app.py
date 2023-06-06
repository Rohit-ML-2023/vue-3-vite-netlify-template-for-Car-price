import pickle

from flask import Flask   , jsonify, request


from flask_cors import CORS, cross_origin

# import numpy as np


# # # initialize our Flask application
app = Flask(__name__)
app.config['ENV']="production"

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

with pickle.load(open('car_dekho.pickle', 'rb')) as model:

# with open("some_file.txt", "r") as file_handle:


@app.route("/")
@cross_origin()
def helloWorld():
    return "Hello, -world!"



@app.route("/model", methods=["GET"])
def predwine():
    if request.method == 'GET':

        try:

            # a = float(request.args.get('alcohol'))
            car_name =          int(request.args.get('Car_Name'))
            model_name =        int(request.args.get('Car_Model'))
            kms_driven =        int(request.args.get('Kms_Driven'))
            years_old =         int(request.args.get('No_of_Years'))
            fuel_type =         int(request.args.get('Fuel_Type'))
            transmission =      int(request.args.get('Transmission'))
            owner =             int(request.args.get('Owner'))
            #    try:
            years_old_square =  int(years_old)**2
            kms_driven_square = int(kms_driven)**2
    
            if fuel_type  == 0:
                fuel_type_petrol = 1
                fuel_type_diesel = 0
            elif fuel_type  == 1:
                fuel_type_petrol = 0
                fuel_type_diesel = 1
            if transmission  == 0:
                transmission_manual = 1
                transmission_automatic = 0

            elif transmission  == 1:
                transmission_manual = 0
                transmission_automatic = 1
            if owner == 0:
                owner_first = 1
                owner_second = 0
                owner_third_owner = 0
                owner_second_fourth_above = 0
                owner_second_test_drive_car = 0
            elif owner == 1:
                owner_first = 0
                owner_second = 1
                owner_third_owner = 0
                owner_second_fourth_above = 0
                owner_second_test_drive_car = 0

            elif owner == 2:
                owner_first = 0
                owner_second = 0
                owner_third_owner = 1
                owner_second_fourth_above = 0
                owner_second_test_drive_car = 0

            elif owner == 3:
                owner_first = 0
                owner_second = 0
                owner_third_owner = 0
                owner_second_fourth_above = 1
                owner_second_test_drive_car = 0

            elif owner == 4:
                owner_first = 0
                owner_second = 0
                owner_third_owner = 0
                owner_second_fourth_above = 0
                owner_second_test_drive_car = 1
        # except:

            #   Years_old_square= 0
            #   Kms_Driven_square=0
           
       
            #   car_name = 0
            #   model_name = 0
            #   kms_driven = 0
            #   Years_old = 0
            #   Fuel_Type = 0
            #   Fuel_type_Petrol = 0
            #   Fuel_Type_Diesel = 0
            #   Transmission  = 0
            #   Transmission_Manual = 0
            #   Transmission_Automatic = 0

            #   Owner =   0                  
  
            #   Owner_First = 0
            #   Owner_Second = 0
            #   Owner_Third_Owner = 0
            #   Owner_Second_Fourth_Above = 0
            #   Owner_Second_Test_Drive_Car = 0
        except:
            return jsonify(str("No Input  " ))

        




    final_features = ([[car_name, model_name, kms_driven, years_old,years_old_square, kms_driven_square ,fuel_type_petrol,fuel_type_diesel, transmission_manual,transmission_automatic ,owner_first,owner_second_fourth_above,owner_second,owner_second_test_drive_car,owner_third_owner]])
    # final_features = [[1,45,100.00,6,36,10000,1,0,0,1,1,0,0,0,0]]

    prediction = model.predict(final_features)
    car_x = prediction
    
    car_x= list(map(lambda car_x :str(car_x) + ' Lacs only',car_x.round(2)))
    # prediction =("{:.2f}".format(prediction))
    print(car_x)

    return jsonify(str("Price  " + str(car_x[0])))


#  main thread of execution to start the server
if __name__ == '__main__':
    app.run(debug=True)
  