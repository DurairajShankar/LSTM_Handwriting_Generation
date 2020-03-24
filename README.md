# LSTM_Handwriting_Generation

A recurrent neural network architecture with Long Short Term Memory to generate handwriting sequences. Based off Grzego's work which is an implementation of Alex Graves' great paper on this [Paper].

Lot of parameter changes were made and certain features were cut because I didn't need them. Overall, performance of the model was sub-par. It fares well on relatively long sequences and is messed up if you feed it special characters.

For the curious, you can try it out as a local web app.



#Local Environment Setup 

Steps:
1. Clone the Repository 
2. Setup the Database in database_connector/db_connector.py
3. Setup the Smtp and Twilio in main.py
4. Use anaconda_Navigator and Sypder (Suggestion)
5. Create a new Environment in anaconda and Install the dependencies
6. Run $ python main.py in spyder or terminal
7. Now The web app should now be accessible at http://localhost:5000/
