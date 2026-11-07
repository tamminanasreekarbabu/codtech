
from pypdf import PdfMerger

merger = PdfMerger()

# Add PDF files
merger.append("file1.pdf")
merger.append("file2.pdf")
merger.append("file3.pdf")

# Merge PDFs
merger.write("merged.pdf")
merger.close()

print("PDFs merged successfully!")
