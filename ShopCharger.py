import datetime
from gensim.models import word2vec
import cv2
from StudentCard import StudentCard

class MainShopCharger:
    #method 1(insert card)
    def insert_student_card(self, student_id):
        self.inserted_student_card = StudentCard.get_student_card(student_id)

    #method2(charge money)
    def charge_money(self, money):
        if self.inserted_student_card is not None:
            self.inserted_student_card.account_balance += money
            self.inserted_student_card.charge_date = datetime.date.today()
        else:
            print('Student ID card is not inserted.')

    #method3(print balance)
    def print_account_balance(self):
        print('Display the balance')
        print('Name:' + self.inserted_student_card.student_name)
        print('Balance:' + str(self.inserted_student_card.account_balance))

    #method4(print recent charge date)
    def print_resent_charge_date(self):
        print("Display recent charge date:")
        print(self.inserted_student_card.charge_date)

    #method5(favorite word edit)
    def favorite_word_edit(self):
        print("What is your favorite word?")
        self.inserted_student_card.favorite_word = input()

    #method6(print words similar to favorite word)
    def print_similar_words(self):
        import warnings
        warnings.filterwarnings('ignore')
        print('Display words similar to your favorite word')
        model = word2vec.Word2Vec.load("./wiki.model") # モデル読み込み
        results = model.wv.most_similar(positive=[self.inserted_student_card.favorite_word]) #positive検索
        for result in results: # 結果を表示
            print(result)

    #method7(load your image)
    def load_img(self):
        print("Please enter the path of the file with your face image")
        self.inserted_student_card.img_file_path = input() # 画像ファイルのパスを入力してもらう
        self.inserted_student_card.img = cv2.imread(self.inserted_student_card.img_file_path) #cv2で読み込み

        print("Display your face image") # 読み込んだ画像を表示
        cv2.imshow('image', self.inserted_student_card.img)
        cv2.waitKey(0) #何かキーを押すと画像のウィンドウを閉じる
        cv2.destroyAllWindows()

    # method8(画像の顔だけにモザイクをかけるメソッド)
    # reference: https://note.nkmk.me/python-opencv-mosaic/
    def mosaic(self):
        face_cascade_path = './haarcascade_frontalface_default.xml'
        face_cascade = cv2.CascadeClassifier(face_cascade_path)
        img_gray = cv2.cvtColor(self.inserted_student_card.img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img_gray)
        dst_face = self.inserted_student_card.img

        def mosaic(src, ratio=0.1):
            small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
            return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

        def mosaic_area(src, x, y, width, height, ratio=0.1):
            dst = src.copy()
            dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
            return dst

        for x, y, w, h in faces:
            dst_face = mosaic_area(self.inserted_student_card.img, x, y, w, h)

        # 顔がモザイク処理された画像を表示
        print("Display the image mosaiced only on the face")
        cv2.imshow('image', dst_face)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #Execution test
    def main(self):
        student_card_1 = StudentCard(0, "Kanako")
        #student_card_2 = StudentCard(1, "Nanaka")

        self.insert_student_card(0) # カード挿入
        self.charge_money(100000) # お金をチャージ
        self.favorite_word_edit() # 好きな言葉を入力
        self.load_img() # 自分の顔画像をロード(添付ファイルでは"./kanako1.png")
        self.mosaic() # その顔画像の顔部分のみをモザイク処理
        self.print_similar_words() # 先ほど入力した好きな言葉に類似する言葉を表示
        self.print_account_balance() # ICカードの残高を表示
        self.print_resent_charge_date() # 一番最近にチャージされた年月日を表示
"""
        self.insert_student_card(1)
        self.charge_money(870)
        self.favorite_word_edit()
        self.print_similar_words()
        self.print_account_balance()
        self.print_resent_charge_date()
        self.charge_money(445)
        self.favorite_word_edit()
        self.print_similar_words()
        self.print_account_balance()
        self.print_resent_charge_date()
"""

if __name__ == '__main__':
    main_shop_charger = MainShopCharger()
    main_shop_charger.main()
