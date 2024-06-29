import sys
import json
import base64

# Check if the correct number of arguments is provided

# Maybe add custom path to pdf within json ie /content/pdfData...
# specify encoding
if len(sys.argv) != 3:
    print("Usage: python3 savePDF.py <file_name.pdf> <json_response>")
    sys.exit(1)

name = sys.argv[1] + '.pdf'

resp = sys.argv[2]
if '.json' in resp:
    resp = open(resp, 'r').read()

try:
    json_data = json.loads(resp)

    base64_pdf_data = json_data['content']['pdfData']

    pdf_bytes = base64.b64decode(base64_pdf_data)

    with open(f'{name}', 'wb') as pdf_file:
        pdf_file.write(pdf_bytes)

    print(f"PDF file {name} saved successfully.")
except KeyError as e:
    print(f"Error: PDF data not found in JSON response. {str(e)}")
except Exception as e:
    print(f"Error: {str(e)}")
