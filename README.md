# AI_Powered_Object_Detection_with_Audio_Feedback
AI-Powered Object Detection with Audio Feedback - Gradio Application Overview This project implements an AI-powered object detection system with audio feedback using Gradio for the interface.
The application detects objects in an uploaded image and provides both a visual output with bounding boxes and a narrated audio description of the detected objects. The solution leverages pre-trained models for object detection and text-to-speech from the transformers library. Components
Model Initialization ◦ Two models are initialized using the pipeline function from the transformers library: 

▪ Object Detection Model: A model for detecting objects in images, loaded from a specified local path. 
▪ Narrator Model: A text-to-speech model to generate audio narration from text, also loaded from a specified local path.
Constants ◦ Configuration constants for drawing bounding boxes and text on images: 
▪ FONT_PATH, FONT_SIZE: Define the font properties for labels. 
▪ BOX_COLOR, TEXT_BACKGROUND_COLOR, TEXT_COLOR: Define the colors for bounding boxes and text labels.

Function: generate_audio 
                   ◦ Converts text to speech using the narrator model and saves the output as a WAV file. 
                   ◦ Handles exceptions and returns the path to the generated audio file.

Function: count_objects 
                   ◦ Counts the occurrences of each detected object type from the detection results.

Function: generate_text_from_objects 
                  ◦ Generates a natural language description based on the counts of detected objects.

Function: draw_bounding_boxes 
                  ◦ Draws bounding boxes and labels on the image for each detected object. 
                  ◦ Uses PIL (Python Imaging Library) to create the visual output.

Function: detect_object 
                  ◦ Orchestrates the object detection, image annotation, and audio generation: 
                  ▪ Runs object detection on the uploaded image. 
                  ▪ Draws bounding boxes on the detected objects. 
                  ▪ Generates a natural language description of the detected objects. 
                  ▪ Produces audio narration of the description. 
                  ◦ Handles exceptions and returns the processed image and audio file paths.

Gradio Interface 
                  ◦ A Gradio interface is defined to allow users to upload an image and receive both the annotated image and the audio feedback. 
                  ◦ The Interface class is used to set up the application with: 
                  ▪ Input: An image uploaded by the user. 
                  ▪ Outputs: The processed image with bounding boxes and the audio file with the narration. 
                  ◦ The interface includes a title and description to provide context for the users.

Launching the Application 
                  ◦ The Gradio interface is launched with specific server settings to make the application accessible: 
                  ▪ server_name="0.0.0.0": Allows the server to be accessible from any IP address. 
                  ▪ server_port=8060: Specifies the port for accessing the application.
Usage:-

To use this application, upload an image through the Gradio interface. The application will process the image to detect objects, annotate the image with bounding boxes, generate a natural language description, and produce an audio narration of the description.

Download this from docker and run it in our local system 
link -https://hub.docker.com/repository/docker/10301998/ai_object_detection_audio_feedback/general
