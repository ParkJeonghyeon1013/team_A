#!/usr/bin/python
# encoding=utf-8

'''
[사용 설명] # 경로, 이름, 소리를 한꺼번에 인자로 받으려니 복잡해보여서 input으로 받는 걸로 바꿔봄
1. 클래스 호출 시, animal.txt가 있는 경로와 함께 호출
2. 찾을 동물 이름 적기
3. 동물이 내는 소리 적기
4. 동물을 animal.txt에 저장할지 여부(y/n)
    y일 경우 : 이름 / 소리 형태로 txt에 append
    n일 경우 : 동물 이름.txt 파일이 새로 생성됨. 이때 파일이 새로 생성될 경로 작성
'''

import pathlib
import argparse



class FileIO:
    def __init__(self, s_path: str) -> None:
        self.__s_path = pathlib.Path(s_path)

    # def __del__(self) -> None:
    # FileIO.get_custom_path()

    @staticmethod
    def get_custom_path() -> str:
        user_path = input('새파일 저장할 경로 입력 부탁! \n [ex)/Users/yeko/Desktop/]: ')
        return user_path

    @property
    def s_path(self) -> pathlib.Path:
        return self.__s_path

    @s_path.setter
    def s_path(self, s_path: pathlib.Path) -> None:
        assert isinstance(s_path, pathlib.Path)
        self.__s_path = s_path

    @staticmethod
    def get_anim_name() -> str:
        a_name = input('찾을 동물 이름 적어줘: ')
        return a_name

    @staticmethod
    def get_anim_sound() -> str:
        a_sound = input("동물이 내는 소리를 적어줘: ")
        return a_sound

    def is_found_str(self, res) -> bool:
        res = self.get_anim_name()
        if res is None:
            return False
        else:
            return True

    @staticmethod
    def save_file(dst_fpath: s_path, data: str) -> bool:
        '''

        :param dst_fpath: 파일이 저장되는 경로
        :param data: 파일 안에 저장되는 데이터 , 내용
        :return:
        '''
        if not dst_fpath.exists():
            with open(dst_fpath.as_posix(), 'w') as fp:
                fp.write(data)
                print("")
                return True
        return False

    def get_lst_txt(self, self_anim_name, self_anim_sound) -> bool:
        try:
            with open(self.__s_path / 'animal.txt', 'r') as file:
                animal_list = file.read()
                if self_anim_name in animal_list:
                    print(f"'{self_anim_name}'이(가) 이미 존재해!")
                    return True
                else:
                    print(f"'{self_anim_name}'을 animal.txt에 저장했어! 바이")
                    with open(self.__s_path / 'animal.txt', 'a') as file_append:
                        file_append.write(f'\n{self_anim_name} / ' + self_anim_sound)
                    return False
        except FileNotFoundError:
            print("animal.txt 파일을 찾을 수 없어.")
            return False

    def handler(self):
        self_anim_name = self.get_anim_name()
        self_anim_sound = self.get_anim_sound()

        user_input = input(f"'{self_anim_name}'를(을) animal.txt에 저장할까?? (y/n): ")

        if user_input.lower() == 'n':
            custom_path = self.get_custom_path()
            FileIO.save_file(
                pathlib.Path('{0}/{1}.txt'.format(custom_path, self_anim_name)),
                str((self_anim_name + ' / ' + self_anim_sound)))
            print("저장되었어. 바이.")
        elif user_input.lower() == 'y':
            self.get_lst_txt(self_anim_name, self_anim_sound)

def main():
    parser = argparse.ArgumentParser(description='시작 ')
    parser.add_argument('path', metavar = 'path', type = str, nargs= '?' , help='도와줘')
    args = parser.parse_args()

    fio = FileIO(args.path)  # cwd -> 다른 컴퓨터로 이동했을 떄도 가능하도록 하는 것
    # animal.txt가 있는 디렉토리 경로를 FileIO()에 넣어주면 됨!
    fio.handler()

if __name__ == '__main__':
   main()
