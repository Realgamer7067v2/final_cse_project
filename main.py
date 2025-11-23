from paddleocr import PaddleOCR
from PIL import ImageGrab
import numpy as np
import time
import cv2
import translate

ocr = PaddleOCR(lang='en',use_textline_orientation=False, text_detection_model_name="PP-OCRv5_mobile_det", text_recognition_model_name="PP-OCRv5_mobile_rec",use_doc_orientation_classify=False, use_doc_unwarping=False,return_word_box=True)


def capture_screen() -> np.ndarray:
    img = ImageGrab.grab()
    img_np = np.array(img)
    return img_np

def get_ocr_data(img: np.ndarray) -> list:
    start_time = time.time()
    result = ocr.predict(img)
    end_time = time.time()
    print(f"OCR processing time: {end_time - start_time} seconds")
    return result



def process_ocr_data(ocr_data: list) -> list:
    ocr_data = ocr_data[0]
    
    
    rect_text = ocr_data['rec_texts']
    rect_text = translate.batch_translate(rect_text, src="en", tgt="fr")
    rect_score = ocr_data['rec_scores']
    rect_box = ocr_data['rec_boxes']
    return zip(rect_text, rect_score, list(rect_box))

if __name__ == "__main__":
    img = capture_screen()
    data = get_ocr_data(img)
    
    processed_data = process_ocr_data(data)
    
    for text , score , box in processed_data:
        x1,y1,x2,y2 = box
        
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        lable = text
        cv2.putText(img, lable, (x1-5, y2 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
    cv2.imshow("OCR Result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    