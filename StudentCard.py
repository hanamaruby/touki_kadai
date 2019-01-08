class StudentCard:
    # class variables
    student_card_list = []

    def __init__(self, student_id, student_name):
        # instance variables
        self.student_id = student_id
        self.student_name = student_name
        self.account_balance = 0 # 口座残高
        self.charge_date = "" # 最新チャージ年月日
        self.favorite_word = '' # 好きな言葉(自由テキスト)
        self.img_file_path = "" # 画像ファイルのパス
        self.img = "" # 画像ファイル
        # setter
        self.student_card_list.append(self)

    @staticmethod
    #getter
    def get_student_card(student_id):
        return StudentCard.student_card_list[student_id]
