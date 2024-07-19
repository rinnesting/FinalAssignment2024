import os
import datetime

def create_log_file():
    try:
        # 現在の日時を取得
        now = datetime.datetime.now()
        # Section04 フォルダと .gitkeep ファイルのパスを設定
        section_directory = "Section04"
        gitkeep_filepath = os.path.join(section_directory, ".gitkeep")
        
        # Section04 フォルダが存在しなければ作成する
        if not os.path.exists(section_directory):
            os.makedirs(section_directory)
        
        # .gitkeep ファイルにログを書き込む
        with open(gitkeep_filepath, 'a') as log_file:
            log_file.write("ログファイルが作成されました。\n")
            log_file.write("作成日時: {}\n".format(now.strftime("%Y-%m-%d %H:%M:%S")))
        print("ログが .gitkeep ファイルに書き込まれました:", gitkeep_filepath)
    except Exception as e:
        print("ログファイルの作成中にエラーが発生しました:", e)

# プログラムの実行例
if __name__ == "__main__":
    create_log_file()
