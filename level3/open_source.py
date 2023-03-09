import glob
from PIL import Image


class GifConverter:
    def __init__(self, path_in=None, path_out=None, resize=(320, 240)):
        """
        Path_in: 원본 여러 이미지 경로

        path_out: 결과 이미지 경로

        """

        self.path_in = path_in or './*.png'  # None일 경우 기본값을 or로 넣을 수 있다.
        self.path_out = path_out or './output.gif'

        self.resize = resize

    def convert_gif(self):
        """
        GIF 변환 기능을 수행한다.


        """
        print(self.path_in, self.path_out, self.resize)

        img, *images = \
            [Image.open(f).resize(self.resize, Image.ANTIALIAS)
             for f in sorted(glob.glob(self.path_in))]

        try:
            img.save(
                fp=self.path_out,
                format='GIF',
                append_images=images,
                save_all=True,
                duration=500,
                loop=0
            )

        except IOError:
            print('Can not convert!', img)


# 클래스

if __name__ == '__main__':
    c = GifConverter('./project/images/*.png',
                     './project/image_out/result.gif', (320, 240))
    c.convert_gif()
