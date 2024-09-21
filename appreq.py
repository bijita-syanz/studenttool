def Titel(titel):
    text = f'''
<!DOCTYPE html>
<html>
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
<title>{titel}</title>    

<link rel="stylesheet" href="main.css">

</head>
<body>
    <h1 style="margin-left: 10%;">hey student</h1>
    <nav id="nav1" >
        
        <ul>
            <li><a href="index.html">HOME</a></li>
            <li><a href="courses.html">CORSES</a></li>
            <li><a href="tools.html">TOOLs</a></li>
            <li><a href="oriontation.html">ORIONTATION</a></li>
        </ul>
    
    </nav>
'''

    return text

class media :
    def add_pdf_download_button():
        pass
    def add_post_titel(titel):
        text = f"""    <div class="post" >
        <h1>{titel}</h1>\n"""
        return text
    def add_cour_in_post(file , name):
        text = f"<a href=\"{file}\"><h3 class=\"coex\">{name}</h3></a> \n"
        return text
    def add_exercice_in_post(file , name) :
        text = f"<a href=\"{file}\"><h3 class=\"coex\">{name}</h3></a> \n"
        return text
    def colse_post():
        return "    </div>\n"

def chnage_them(): 
    pass