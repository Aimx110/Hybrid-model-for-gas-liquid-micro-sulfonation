import torchvision.transforms as transforms
from PIL import Image
from torch.utils.data import Dataset
from torchvision import datasets
from torch.utils.data import DataLoader



# 定义转换函数
preprocess = transforms.Compose([
    transforms.Resize((256, 256)),  # 调整大小为指定的尺寸（这里设置为256x256）
    transforms.ToTensor(),  # 将图像转换成张量形式
])

# 定义转换函数
transform = transforms.Compose([
    transforms.CenterCrop((128,128)),
    transforms.RandomRotation(60)
])

# 加载并预处理图像
image_path = r'../pic/datajpg/40-100\40-100-1.jpg'  # 替换为你自己的图像路径
img = Image.open(image_path)  # 打开图像文件
img.show()
img_trans = transform(img)
img_trans.show()
#print("输入张量的形状：",img_trans)

#input_tensor = preprocess(img)  # 对图像进行预处理
#print("输入张量的形状：", input_tensor)