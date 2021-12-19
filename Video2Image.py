# coding=utf-8
import cv2
import os

# Fight first

F = list(range(20))

TOV = 'train'
PATH = './' + TOV + 'NFOut/'

EXTRACT_FREQUENCY = 1

def extract_frames(path, dst_folder, index, Fraction):
    for root, dirs, files in os.walk(path):
        count = Fraction * 40
        for f in files[Fraction * 40:(Fraction + 1) * 40]:
            video = cv2.VideoCapture()
            if not video.open(PATH + f):
                print("can not open the video")
                exit(1)
            num = 0
            while True:
                _, frame = video.read()
                if frame is None:
                    break
                else:
                    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    save_path = "{}/".format(dst_folder) + TOV + "{}_{:>03d}.jpg".format(count+800, num)
                    cv2.imwrite(save_path, frame)
                    index += 1
                    num += 1
            count += 1
            video.release()
            print("Totally save {:d} pics".format(index - 1))


def main():
    import shutil
    for Fraction in F:
        EXTRACT_FOLDER = './' + TOV + 'imageOut{}'.format(Fraction+20)
        try:
            shutil.rmtree(EXTRACT_FOLDER)
        except OSError:
            pass
        import os
        os.mkdir(EXTRACT_FOLDER)
        extract_frames(PATH, EXTRACT_FOLDER, 1, Fraction)


if __name__ == '__main__':
    main()
