class phone:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.text_messages = []
    
    def place_call(self, number_to_call):
        pass

    def place_text(self, number_to_text, message_to_send):
        pass

    def save_text(self, message_to_save):
        pass

    def get_texts(self):
        pass

    def get_number(self):
        pass

class CameraPhone(phone):

    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.pictures = []

    def take_picture(self, picture_name):
        self.pictures.append(picture_name)




camphone = CameraPhone(5555555555)


print(camphone.phone_number)

camphone.take_picture("picture 1")
print(camphone.pictures)