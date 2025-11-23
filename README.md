# Extraction Of Text from Image/Screen using Machine Vision

This project uses pre-trained models from PaddleOCR to process an image/screenshot and extract useful text data. The script captures the screen using Pillow (PIL) `ImageGrab`, runs PaddleOCR to detect text, and then **translates the recognized English text to French** before drawing the translated text on the screen.

## Features
- Full-screen capture via Pillow `ImageGrab`.
- Text detection and recognition using PaddleOCR (PP-OCRv5 mobile models).
- Automatic batch translation of recognized English text to French (see `translate.py`).
- Bounding box and translated label overlay rendered with OpenCV.
- Processing time measurement for OCR for basic performance analysis.

## Technologies / Tools Used
- **PaddleOCR** – highly trained OCR models with multilingual support.
- **PP-OCRv5_mobile_det** – text detection model.
- **PP-OCRv5_mobile_rec** – text recognition model.
- **Pillow** – for screen capture (`ImageGrab`).
- **NumPy** – for image array manipulation.
- **OpenCV (cv2)** – for drawing bounding boxes and text overlays.

## Tech Stack
- Python 3.10+ (recommended)
- Paddle-gpu (3.2.0 recommended)
- PaddleOCR
- Pillow
- NumPy
- OpenCV (cv2)

## Prerequisites
- Install Python and ensure `pip` is available on your PATH.
- On Windows you may need Visual C++ Build Tools for some packages.
- For GPU acceleration with PaddleOCR, install a compatible PaddlePaddle GPU build, CUDA Toolkit, and cuDNN (optional; CPU-only inference also works but is slower).

## Installation
```powershell
# (Optional) create and activate a virtual environment
python -m venv .venv; .\.venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

## Usage
```powershell
python main.py
```
The script will:
1. Capture the current screen.
2. Run OCR prediction on the screenshot.
3. Translate each recognized English text segment into French.
4. Draw bounding boxes and translated French labels on the original screenshot.
5. Display the annotated image in an OpenCV window.

Press any key in the OpenCV window to close it.

## Configuration
Core OCR initialization in `main.py`:
```python
ocr = PaddleOCR(
    lang="en",
    use_textline_orientation=False,
    text_detection_model_name="PP-OCRv5_mobile_det",
    text_recognition_model_name="PP-OCRv5_mobile_rec",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    return_word_box=True,
)
```

Translation is done in `translate.py` via `batch_translate(rect_text, src="en", tgt="fr")`. You can change the `src` and `tgt` language codes there to support other languages, depending on how `translate.py` is implemented.

## Performance Notes
- Full-screen capture plus OCR and translation can be CPU/GPU intensive.
- For faster throughput, you can:
  - Capture only a region of the screen.
  - Downscale the screenshot before OCR.
  - Use lighter OCR models or run without translation.

## Project Structure
```
Real_CSE_Project/
  main.py        # Entry point – capture, OCR, draw boxes & translated labels
  translate.py   # Translation helper with batch_translate()
  README.md      # Documentation
  STATEMENT.md   # Problem statement & scope
  requirements.txt
  __pycache__/
```

## Acknowledgments
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) project
- OpenCV community

