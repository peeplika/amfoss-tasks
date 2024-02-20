import sys
import json
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap,QImage,QImageReader
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTextEdit,QMessageBox
from io import BytesIO
from PIL import Image
from PIL.ImageQt import ImageQt
from plyer import notification
import requests

# ... (previous imports)

class SearchWindow(QWidget):
    def __init__(self,shared_data):
        super().__init__()

        layout = QVBoxLayout(self)
        self.background_image_path = "/Poke-Search/assets/landing.jpg"
        self.background_image = QPixmap(self.background_image_path)
        self.background_label = QLabel(self)
        self.background_label.setPixmap(self.background_image)
        self.background_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.background_label)

        self.setFixedSize(850, 500)

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 50, 280, 40)
        self.shared_data = shared_data
	
        self.image_label = QLabel(self)
        self.image_label.setGeometry(200, 10, 500, 300)

        self.label1 = QLabel(" *", self)
        self.label1.setGeometry(300, 270, 600, 250)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.search_button_clicked)

        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.capture_button_clicked)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.display_button_clicked)
        
        self.text = self.textbox.text()
        

    def search_button_clicked(self):
        self.background_label.setPixmap(QPixmap())
        entered_text = self.textbox.text()
        self.shared_data['entered_text'] = entered_text
        print(f"User entered: {entered_text}")
        url = f"https://pokeapi.co/api/v2/pokemon/{entered_text}/"
        data = requests.get(url).json()

        image_url = data["sprites"]["front_default"]
        abilities = [ability_info["ability"]["name"] for ability_info in data["abilities"]]
        types = [type_info["type"]["name"] for type_info in data["types"]]
        stats_lines = [f'{stat_info["stat"]["name"].capitalize()}: {stat_info["base_stat"]}' for stat_info in data["stats"]]
        stats_message = '\n'.join(stats_lines)

        message = (
        f'name: {data["name"]}\n'
        f'abilities: {", ".join(abilities)}\n'
        f'types: {", ".join(types)}\n'
        f'stats:\n{stats_message}'
        )
        self.label1.setText(message)
        image_response = requests.get(image_url)

        if image_response.status_code == 200:
            image_o = Image.open(BytesIO(image_response.content))
            image = image_o.convert("RGBA")
            image_data = image.getdata()
            transparent_image_data = [(r, g, b, 0) if (r, g, b) == (0, 0, 0) else (r, g, b, a) for r, g, b, a in image_data]
            transparent_image = Image.new("RGBA", image.size, (0, 0, 0, 0))
            transparent_image.putdata(transparent_image_data)
            image = transparent_image.resize((600, 400))
            image_qt = QPixmap.fromImage(ImageQt(image))
            self.image_label.setPixmap(image_qt)


    def capture_button_clicked(self):
        entered_text = self.textbox.text()
        print(f"User entered: {entered_text}")

        data_url = f"https://pokeapi.co/api/v2/pokemon/{entered_text}"
        image_url = f"https://courses.cs.washington.edu/courses/cse154/webservices/pokedex/sprites/{entered_text}.png"
        
        data = requests.get(data_url)
        image_response = requests.get(image_url)
        
        if image_response.status_code == 200:
            image = Image.open(BytesIO(image_response.content))
            image_qt = QPixmap.fromImage(ImageQt(image))
            self.background_label.setPixmap(image_qt)
            image.save(f"{entered_text}_captured.png")
            notification_title = "Image Captured"
            notification_text = f"Image for {entered_text} has been captured and saved."
            notification.notify(title=notification_title, message=notification_text)
            reply = QMessageBox.question(self, 'POKEMON', 'Pokemon captured !!!',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                print('User clicked Yes.')
            else:
                print('User clicked No.')

    def display_button_clicked(self):
        self.w = Pokemon(self.shared_data)
        self.w.show()
        
class Pokemon(QWidget):
    def __init__(self,shared_data):
        super().__init__()  
        self.setFixedSize(450, 400)
        self.image_label = QLabel(self)
        self.image_label.setGeometry(5, 10, 500, 300)
        self.entered_text = shared_data.get('entered_text',"ditto")
        print(self.entered_text,"---------------------")
        url = f"https://pokeapi.co/api/v2/pokemon/{self.entered_text}/"
        data = requests.get(url).json()
        self.id_ = data["id"]
        print(self.id_)
        image_url = data["sprites"]["front_default"]
        image_response = requests.get(image_url)

        if image_response.status_code == 200:
            image_o = Image.open(BytesIO(image_response.content))
            image = image_o.convert("RGBA")
            image_data = image.getdata()

            transparent_image_data = [(r, g, b, 0) if (r, g, b) == (0, 0, 0) else (r, g, b, a) for r, g, b, a in image_data]
            transparent_image = Image.new("RGBA", image.size, (0, 0, 0, 0))
            transparent_image.putdata(transparent_image_data)

            image = transparent_image.resize((600, 400))
            image_qt = QPixmap.fromImage(ImageQt(image))

            self.image_label.setPixmap(image_qt)
        
        button1 = QPushButton("previous", self)
        button1.setGeometry(20, 300, 120, 23)
        button1.setStyleSheet("background-color: green;")
        button1.clicked.connect(lambda:self.button_click("prev"))
           
        button2 = QPushButton("next", self)
        button2.setGeometry(300, 300, 120, 23)
        button2.setStyleSheet("background-color: red;")
        button2.clicked.connect(lambda:self.button_click("next"))
        
    def button_click(self,button):
        if button == "next":
            id_ = self.id_
            print(id_,id_)
            id_ = id_+1
        if button == "prev":
            id_ = self.id_
            print(id_,id_)
            id_ = id_-1    
        
        url = f"https://pokeapi.co/api/v2/pokemon/{id_}/" 
        data = requests.get(url).json()

        image_url = data["sprites"]["front_default"]
        image_response = requests.get(image_url)

        if image_response.status_code == 200:
            image_o = Image.open(BytesIO(image_response.content))
            image = image_o.convert("RGBA")
            image_data = image.getdata()

            transparent_image_data = [(r, g, b, 0) if (r, g, b) == (0, 0, 0) else (r, g, b, a) for r, g, b, a in image_data]
            transparent_image = Image.new("RGBA", image.size, (0, 0, 0, 0))
            transparent_image.putdata(transparent_image_data)

            image = transparent_image.resize((600, 400))
            image_qt = QPixmap.fromImage(ImageQt(image))
            self.image_label.setPixmap(image_qt)
        self.id_=id_
        
        
        


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())

