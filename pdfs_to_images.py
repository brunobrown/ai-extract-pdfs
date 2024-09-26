import os
from pdf2image import convert_from_path

# Diretórios de entrada e saída
input_dir = 'files'
output_dir = 'images'

# Garantir que o diretório de saída exista
os.makedirs(output_dir, exist_ok=True)

# Iterar por todos os arquivos no diretório de PDFs
for file_index, pdf_file in enumerate(os.listdir(input_dir)):
    if pdf_file.endswith('.pdf'):
        pdf_path = os.path.join(input_dir, pdf_file)

        # Converter o PDF para imagens
        pages = convert_from_path(pdf_path, dpi=300)

        # Salvar as imagens resultantes
        for page_index, page in enumerate(pages):
            output_path = os.path.join(output_dir, f'{os.path.splitext(pdf_file)[0]}.jpg')  # salva com o mesmo nome
            # output_path = os.path.join(output_dir, f'{file_index}{page_index}.jpg')  # salva com o index como nome
            page.save(output_path, 'JPEG')

print("Conversão concluída!")