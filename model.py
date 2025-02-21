"""
A module for working with a machine learning model.
Contains a function for integration with the trace.moe API to search for anime by frame.

Sora Search API creator: @saykachii

"""

import requests
from config import TRACE_MOE_API_URL

def predict_anime(image_data: bytes) -> dict:
    """
    Function for predicting anime from an image.
    Sends an image to the trace.moe API and returns the result.
    
    Parameters:
      - image_data (bytes): image data
    
    Returns:
      dict: search result obtained from trace.moe
    """
    try:
        # Generate data for sending: key "image" with file
        files = {"image": ("image.jpg", image_data, "image/jpeg")}
        response = requests.post(TRACE_MOE_API_URL, files=files)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": "Error when calling external API",
                "status_code": response.status_code
            }
    except Exception as e:
        return {"error": f"Exception when calling external API: {str(e)}"}
