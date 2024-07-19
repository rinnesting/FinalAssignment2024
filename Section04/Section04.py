import os
import datetime

def create_log_file():
    try:
        # ���݂̓������擾
        now = datetime.datetime.now()
        # Section04 �t�H���_�� .gitkeep �t�@�C���̃p�X��ݒ�
        section_directory = "Section04"
        gitkeep_filepath = os.path.join(section_directory, ".gitkeep")
        
        # Section04 �t�H���_�����݂��Ȃ���΍쐬����
        if not os.path.exists(section_directory):
            os.makedirs(section_directory)
        
        # .gitkeep �t�@�C���Ƀ��O����������
        with open(gitkeep_filepath, 'a') as log_file:
            log_file.write("���O�t�@�C�����쐬����܂����B\n")
            log_file.write("�쐬����: {}\n".format(now.strftime("%Y-%m-%d %H:%M:%S")))
        print("���O�� .gitkeep �t�@�C���ɏ������܂�܂���:", gitkeep_filepath)
    except Exception as e:
        print("���O�t�@�C���̍쐬���ɃG���[���������܂���:", e)

# �v���O�����̎��s��
if __name__ == "__main__":
    create_log_file()
