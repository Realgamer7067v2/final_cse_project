# Problem Statement

Extract text from an image/screenshot/document into a machine‑readable format and automatically translate the extracted English text into another language (currently French).

## Scope of the Project
- **Core Function**: Single screenshot capture of the full desktop, run PaddleOCR (PP-OCRv5 mobile det + rec, English) to get words, confidence scores, and bounding boxes.
- **Translation**: Batch translation of the recognized English texts into French using the helper in `translate.py`, then display the translated text on-screen.
- **Processing**: Minimal post-processing; directly iterates recognized items; draws green rectangles and writes translated text above each box.
- **Performance Feedback**: Prints a timing metric (end-to-end `ocr.predict` duration). No detailed profiling of preprocessing or rendering.
- **Data Handling**: Results are only visualized; nothing is currently saved to disk, clipboard, or exported as JSON/CSV.
- **Configuration Choices**: Orientation classification and document unwarping are disabled; word-level boxes are used (`return_word_box=True`).
- **Interaction Model**: One-shot run; no loop, hotkey, region selection, or window targeting; exits after a keypress in the OpenCV window.
- **Limitations**: English-only OCR at present, fixed translation target (French), no confidence threshold filtering, no error handling for empty results, no GPU/config toggles, no scaling/resizing for speed.
- **Immediate Extension Opportunities**: Add continuous monitoring loop, confidence threshold, export formats (JSON/CSV), region/window capture, optional downscaling for speed, multi-language OCR and translation, and graceful handling of empty or low-confidence results.

## Target Users
- Business employees who want to extract data from handwritten notes or printed documents (e.g., PDFs, forms) into a machine-readable and translatable format.
- Data analysts who frequently work with heterogeneous document sources and need to normalize and translate text quickly.

## High-Level Features
- Full-screen capture via Pillow `ImageGrab`.
- Text detection and recognition using PaddleOCR (PP-OCRv5 mobile models).
- Automatic translation of recognized English text into French.
- Bounding box and translated label overlay rendered with OpenCV.
- Basic performance measurement of the OCR step.