from PIL import Image


from __future__ import print_function
import os, sys
from PIL import Image

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)

try:
    # image = Image.open('assets/李学锋身份证.png')  # 检查文件是否能正常打开
    image = Image.open('assets/李学锋身份证.jpg')
    print(image.format, image.size, image.mode, image.info)
    # im =
    # image.show()
    # image.close()
    image.verify()  # 检查文件完整性
    image.close()
except:
    try:
        image.close()
    except:
        pass
    raise
else:
    print('Image OK, format is %s.' % image.format)