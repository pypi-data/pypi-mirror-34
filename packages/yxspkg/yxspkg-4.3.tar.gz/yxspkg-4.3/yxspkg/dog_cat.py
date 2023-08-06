import torch as tc
from net import feature_net, classifier
from PIL import Image
from torchvision import models, transforms
from pathlib import Path
def get_feature(jpgs,model_label='vgg',batch_size=4):
    
    featurenet = feature_net(model_label)
    img_transform = transforms.Compose([
    transforms.Resize(320),
    transforms.CenterCrop(299),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    features = []
    groups = len(jpgs) // batch_size
    def get_img(img_name):
        img = Image.open(img_name)
        if img.mode=='RGBA':
            img.mode = 'RGB'
        return img_transform(img).unsqueeze(0)
    if len(jpgs) % batch_size!=0:
        groups += 1
    for i in range(groups):
        t = [get_img(name) for name in jpgs[i*batch_size:(i+1)*batch_size]]
        f = tc.cat(t,0)
        features.append(featurenet(f))
    
    return tc.cat(features,0)
def get_dog_or_cat(feature):
    mynet = classifier(512, 2)
    p = Path(__file__)
    mynet.load_state_dict(tc.load(p.with_name('feature_model.pth')))
    out = mynet(feature)
    _, pred = tc.max(out,1)
    return pred
def main(jpgs):
    m = get_feature(jpgs)
    t = get_dog_or_cat(m)
    return t
if __name__=='__main__':
    jpg = r'F:\pythonAPP\torch\code-of-learn-deep-learning-with-pytorch-master\data\dogs-vs-cats\dog\dog.0.jpg'
    jpgs = (jpg,jpg)
    import sys
    jpgs = sys.argv[1:]
    f = main(jpgs)
    d = {0:'cat',1:'dog'}
    for jpg,c in zip(jpgs,f):
        print(jpg,d[c.item()])
    