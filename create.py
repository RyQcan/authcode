#encoding=utf-8
import random
import string
import sys
import math
from PIL import Image,ImageDraw,ImageFont,ImageFilter

class AuthCode:
    #图片保存路径
    filename="C:/Users/13723/Desktop/python_yanzhengma/"
    #字体的位置
    font_path = 'C:/Windows/Fonts/Georgia.ttf'
    #生成验证码图片的高度和宽度
    size = (129,53)
    width,height = size
    #背景颜色，默认为灰色
    bgcolor = (36,36,36)
    #字体颜色，默认为黑色
    fontcolor = (0,0,0)
    #干扰线颜色。默认为黑色
    linecolor = (0,0,0)

    def __init__(self,number,line_num,character):
        #生成几位数的验证码
        self.number = number
        #线的数量
        self.line_num=line_num
        #字符内容
        self.character=character
        #生成字符串
        self.text = self.gene_text()  

    #用来随机生成一个字符串
    def gene_text(self):
        
        source1 = ['0','1','2','3','4','5','6','7','8','9']
        source2 = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J', 'K','L', 'M', 'N','O','P','Q','R',
                'S', 'T', 'U', 'V', 'W', 'Z','X', 'Y']
        if(self.character=='1'):
            source=source1
        elif (self.character=='2'):
            source=source2
        else:
            source=source1+source2

        return ''.join(random.sample(source,self.number))#number是生成验证码的位数

    def rnd_dis(self):
        '''
        随机一个干扰字
        :return: 
        '''
        d = ['^','-', '~', '_', '.','*']
        i = random.randint(0, len(d)-1)
        return d[i]


    #用来绘制干扰线
    def gene_line(self,draw):
        
        begin = (0, random.randint(0, self.height))
        end = (100, random.randint(0, self.height))
        draw.line([begin, end], fill = self.linecolor,width=4)

        for j in range(0, self.width, 30):
            dis = self.rnd_dis()
            w =15 + j

            # 随机距离图片上边高度，但至少距离30像素
            h = random.randint(1, self.height - 30)
            draw.text((w, h), dis, font=ImageFont.truetype(self.font_path,40), fill=self.linecolor)


    #生成验证码
    def gene_code(self):
 
        image = Image.new('RGBA',(self.width,self.height),self.bgcolor) #创建图片
        font = ImageFont.truetype(self.font_path,40) #验证码的字体
        draw = ImageDraw.Draw(image)  #创建画笔
        
        font_width, font_height = font.getsize(self.text)
        draw.text(((self.width - font_width) / self.number, (self.height - font_height) / self.number),self.text,\
                font= font,fill=self.fontcolor) #填充字符串
        for i in range(0,self.line_num):
            self.gene_line(draw)
        
        image = image.transform((self.width+30,self.height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE) #滤镜，边界加强
        
        path = self.filename + self.text + ".png"
        
        #保存验证码图片
        image.save(path)

    #验证码对应的字符
    def get_text(self):
        print(self.text)
        return self.text

if __name__ == "__main__":
    #位数 复杂度 字符内容
    cc =AuthCode(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])
    cc.gene_code()
    cc.get_text()