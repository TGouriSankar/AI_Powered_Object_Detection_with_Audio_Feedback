import gradio as gr
from PIL import Image, ImageDraw, ImageFont
import scipy.io.wavfile as wavfile
from transformers import pipeline

# Initialize pipelines
narrator = pipeline("text-to-speech", model="kakao-enterprise/vits-ljs")
object_detector = pipeline("object-detection", model="facebook/detr-resnet-101")

# Constants
FONT_PATH = None  # Update this with the path to your custom font if needed
FONT_SIZE = 20
BOX_COLOR = "red"
TEXT_BACKGROUND_COLOR = "red"
TEXT_COLOR = "white"


def generate_audio(text):
    try:
        # Generate the narrated text
        narrated_text = narrator(text)
        # Save the audio to a WAV file
        wavfile.write("output.wav", rate=narrated_text["sampling_rate"],
                      data=narrated_text["audio"][0])
        return "output.wav"
    except Exception as e:
        print(f"Error generating audio: {e}")
        return None


def count_objects(detection_objects):
    object_counts = {}
    for detection in detection_objects:
        label = detection['label']
        if label in object_counts:
            object_counts[label] += 1
        else:
            object_counts[label] = 1
    return object_counts


def generate_text_from_objects(object_counts):
    response = "This picture contains"
    labels = list(object_counts.keys())
    for i, label in enumerate(labels):
        count = object_counts[label]
        response += f" {count} {label}"
        if count > 1:
            response += "s"
        if i < len(labels) - 2:
            response += ","
        elif i == len(labels) - 2:
            response += " and"
    response += "."
    return response


def draw_bounding_boxes(image, detections, font_path=FONT_PATH, font_size=FONT_SIZE):
    draw_image = image.copy()
    draw = ImageDraw.Draw(draw_image)
    font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default()
    
    for detection in detections:
        box = detection['box']
        xmin, ymin, xmax, ymax = box['xmin'], box['ymin'], box['xmax'], box['ymax']
        draw.rectangle([(xmin, ymin), (xmax, ymax)], outline=BOX_COLOR, width=3)
        
        label = detection['label']
        score = detection['score']
        text = f"{label} {score:.2f}"
        
        text_size = draw.textbbox((xmin, ymin), text, font=font)
        draw.rectangle([(text_size[0], text_size[1]), (text_size[2], text_size[3])], fill=TEXT_BACKGROUND_COLOR)
        draw.text((xmin, ymin), text, fill=TEXT_COLOR, font=font)
    
    return draw_image


def detect_object(image):
    try:
        detections = object_detector(image)
        processed_image = draw_bounding_boxes(image, detections)
        object_counts = count_objects(detections)
        natural_text = generate_text_from_objects(object_counts)
        processed_audio = generate_audio(natural_text)
        return processed_image, processed_audio
    except Exception as e:
        print(f"Error in object detection: {e}")
        return None, None


demo = gr.Interface(
    fn=detect_object,
    inputs=[gr.Image(label="Select Image", type="pil")],
    outputs=[gr.Image(label="Processed Image", type="pil"), gr.Audio(label="Generated Audio")],
    title="AI-Powered Object Detection with Audio Feedback",
    description="Upload an image and get object detection results using the DETR model with a ResNet-101 backbone with Audio Feedback"
)

demo.launch()
