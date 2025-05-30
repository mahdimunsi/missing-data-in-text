import fitz  # PyMuPDF
import easyocr
import os
from openai import OpenAI
from fpdf import FPDF

PDF_PATH = 'Honkela95.pdf' # Replace with your actual pdf
OUTPUT_PDF = 'Honkela95_refined.pdf' # Replace with your actual pdf output
TEMP_IMAGE_FOLDER = "pdf_pages"
API_KEY = "omitted"  # Replace with your actual OpenAI API key
MODEL = "gpt-4o"
CHUNK_SIZE = 3000
INSTRUCTIONS = "Clean up this OCR output by fixing errors, restoring structure, and improving readability."

os.makedirs(TEMP_IMAGE_FOLDER, exist_ok=True)

# Initialize EasyOCR and OpenAI
reader = easyocr.Reader(['en'])
client = OpenAI(api_key=API_KEY)

def refine_text(text_chunk):
    try:
        response = client.responses.create(
            model=MODEL,
            instructions=INSTRUCTIONS,
            input=text_chunk
        )
        return response.output_text
    except Exception as e:
        print(f"🛑 Error refining text chunk: {e}")
        return text_chunk  # Return the raw chunk if API fails

try:
    doc = fitz.open(PDF_PATH)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    has_content = False

    for i, page in enumerate(doc):
        try:
            pix = page.get_pixmap(dpi=300)
            image_path = os.path.join(TEMP_IMAGE_FOLDER, f"page_{i + 1}.png")
            pix.save(image_path)
            text_lines = reader.readtext(image_path, detail=0)
            raw_text = "\n".join(text_lines).strip()
            if raw_text:
                has_content = True
                chunks = [raw_text[j:j+CHUNK_SIZE] for j in range(0, len(raw_text), CHUNK_SIZE)]
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.cell(0, 10, f"--- Page {i + 1} ---", ln=True)
                for chunk in chunks:
                    refined_chunk = refine_text(chunk).strip()
                    for line in refined_chunk.split("\n"):
                        try:
                            pdf.multi_cell(0, 10, line.encode('latin-1', 'replace').decode('latin-1'))
                        except Exception as e:
                            print(f"⚠️ Encoding error in line: {line} | Error: {e}")

                print(f"✅ Successfully processed Page {i + 1}")
            os.remove(image_path)

        except Exception as e:
            print(f"🛑 Error processing Page {i + 1}: {e}")
    if has_content:
        pdf.output(OUTPUT_PDF)
        print(f"🎉 Pipeline complete! Refined PDF saved to: {OUTPUT_PDF}")
    else:
        print("⚠️ No valid text found. PDF not created.")

except Exception as e:
    print(f"🛑 Critical error: {e}")

finally:
    # Cleanup temporary image folder if empty
    if os.path.exists(TEMP_IMAGE_FOLDER) and not os.listdir(TEMP_IMAGE_FOLDER):
        os.rmdir(TEMP_IMAGE_FOLDER)
