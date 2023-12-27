from flet import *

def processyourimage(e):
    # Ajoutez ici votre logique de traitement d'image
    # Vous pouvez utiliser pytesseract pour extraire du texte d'une image, par exemple
    pass

def main(page: Page):
    page.scroll = "auto"
    image_loc = TextField(label="Nom de votre image ")
    id_number = TextField(label="Numéro d'identification ") 
    name_txt = TextField(label="Votre nom")
    birth_day = TextField(label="Date de naissance ")
    healthy_service = TextField(label="Service médical")

    image_preview = Image(src=False, width=150, height=120)
    def proccessyouimage (e):
        #Get image for proccess
        img_pro = img.open(image_loc.value)
        
        text=pytesseract.image_to_string(img_pro, lang="ind")
        print(text)
        with open("result.txt","w") as file:
            file.write(text) 
        with open("result.txt",mode="r",encoding=utf-8) as file:
            text=file.read()
        sections = {}
        lines = text.split("\n")
        current_section = ''
        i = 1

        for line in lines:
        # Skip empty lines
             if line.strip() =="":
                continue
        if "Tanggallahir" in line:
            current_section = "section_3"
            i += 1
        elif "NIK" in line:
            current_section = "section_4"
            i += 1
        elif "Faskes Tingkat" in line:
            current_section = "section_5"
            i += 1
        elif len(line.strip()) == 16 and line.strip().isdigit():
             current_section = "section_2"
             i += 1
        else:
            current_section=f"section_{i}"
        sections[current_section] = line.strip()
        i+=1
    print(sections)

    id_number.value= sections['section_1']
    name_txt.value= sections['section_2']

    dob = sections ['section_3']
    data_regex =re.compile(r'\d{2}-\d{2}-\d{4}')
    matches = data_regex.findall(job)
    if matches:
         my_birthday = matches[0]
         birth_day.value =my_birthday
    else:
        print("no dob found !!")     
    healthy_service.value = sections['section_4']
    image_preview.value = f"{os.getcwd()}/{image_loc.value}"

    page.snack_bar = SnackBar(
        Text("succes get from image " , size=30),
        bgcolor="green"
        )
    page.snack_bar.open=True
    page.update()


    # IF SECTION ROW IS BLANK IN result.txt
    # THEN CONTINUE
    # NOW FIND SECTION LIKE NAME BIRTHDAY AND MORE
    if "Tanggallahir" in line:
        current_section = "section_3"
        i += 1        



    page.add(
        Column([
            image_loc,
            ElevatedButton(
                "Traiter votre image",
                bgcolor="blue",
                color="white",
                on_click=processyourimage
            ),
            Text("Votre résultat en image", weight="bold"),
            image_preview,
            id_number,
            name_txt,
            birth_day,
            healthy_service
        ])
    )

app(target=main)
