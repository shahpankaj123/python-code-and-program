import pikepdf

old = pikepdf.Pdf.open("file.pdf")

no_ext = pikepdf.Permissions(extract=False)

old.save("new.pdf",
         encryption= pikepdf.Encryption(
             user="12345",
             owner="Aryan",
             allow=no_ext
         ))