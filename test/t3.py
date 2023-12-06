import sys

import ddddocr

sys.path.append('E:\\software\\python\\Project\\pitcher_tool_python')

ocr = ddddocr.DdddOcr()

path = 'E:\\DesktopSpace\\Development\\Python\\pitcher_tool\\temp\\screenshot\\2023-12-06_23-28-13.png'

with open(path, 'rb') as f:
    image = f.read()

res = ocr.classification(image)
print(res)
