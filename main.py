import pytesseract
import shutil
import os
import random
import uvicorn
import gradio as gr
from PIL import Image
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://www.glissai.com"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get('/')
def root():
    return {"message": "hello!"}


def gradio_infer(myimg):
    if myimg is not None:
    	results = pytesseract.image_to_string(myimg)
    	return results


io = gr.Interface(fn=gradio_infer, 
	inputs=gr.Image(),
	outputs=gr.Textbox(),
	examples=[["testimg.jpg"], ["testimg2.jpg"]],
	allow_flagging = 'never',
	css="footer {visibility: hidden}",
	live=True
	)

gr.mount_gradio_app(app, io, path="/gradio")


if __name__ == "__main__":

	uvicorn.run(app, host='0.0.0.0', port=8080)

