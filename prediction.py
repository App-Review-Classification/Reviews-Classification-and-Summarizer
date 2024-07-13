from src.text_preprocessing import PreProcessor
from tensorflow.keras.models import load_model
import numpy as np


class Prediction:

    def __init__(self, amazon_df, flipkart_df):
        self.amazon_df = amazon_df
        self.flipkart_df = flipkart_df
        self.testing_padded = None
        self.model_path = 'Model/Review_classification_model.h5'
        self.model = load_model(self.model_path)
        self.amazon_accuracy = None
        self.flipkart_accuracy = None

    def predict_amazon(self):
        preprocessor = PreProcessor(self.amazon_df)
        self.testing_padded = preprocessor.preprocessing_pipeline()

        y_pred = self.model.predict(self.testing_padded)
        flattened_y_pred = y_pred.flatten()

        categories = []
        for prob in flattened_y_pred:
            if prob >= 0.8:
                categories.append(5)
            elif prob >= 0.6:
                categories.append(4)
            elif prob >= 0.4:
                categories.append(3)
            elif prob >= 0.2:
                categories.append(2)
            else:
                categories.append(1)
        
        predicted_categories = np.array(categories)
        print(predicted_categories)
        actual_values = self.amazon_df['Star'].values
        accuracy = np.mean(predicted_categories == actual_values)
        print(accuracy)

        print(f"Accuracy in predicting rating from Amazon: {accuracy * 100:.2f}%")
        print(f"Average Star rating on Amazon: {np.mean(predicted_categories)}")

        self.amazon_accuracy = accuracy
    
    def predict_flipkart(self):
        preprocessor = PreProcessor(self.flipkart_df)
        self.testing_padded = preprocessor.preprocessing_pipeline()

        y_pred = self.model.predict(self.testing_padded)
        flattened_y_pred = y_pred.flatten()

        categories = []
        for prob in flattened_y_pred:
            if prob >= 0.8:
                categories.append(5)
            elif prob >= 0.6:
                categories.append(4)
            elif prob >= 0.4:
                categories.append(3)
            elif prob >= 0.2:
                categories.append(2)
            else:
                categories.append(1)
        
        predicted_categories = np.array(categories)
        actual_values = self.flipkart_df['Star'].values
        accuracy = np.mean(predicted_categories == actual_values)
        print(accuracy)
        
        print(f"Accuracy in predicting rating from Flipkart: {accuracy * 100:.2f}%")
        print(f"Average Star rating on Flipkart: {np.mean(predicted_categories)}")

        self.flipkart_accuracy = accuracy

    def predict(self):
        self.predict_amazon()
        self.predict_flipkart()

