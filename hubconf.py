dependencies = ['torch']
import hardnet 

def hardnet68(pretrained=False, **kwargs):
    """ # This docstring shows up in hub.help()
    Harmonic DenseNet 68 model
    pretrained (bool): kwargs, load pretrained weights into the model
    """
    # Call the model, load pretrained weights
    model = hardnet.HarDNet(depth_wise=False, arch=68, pretrained=pretrained)
    return model

def hardnet85(pretrained=False, **kwargs):
    """ # This docstring shows up in hub.help()
    Harmonic DenseNet 85 model
    pretrained (bool): kwargs, load pretrained weights into the model
    """
    # Call the model, load pretrained weights
    model = hardnet.HarDNet(depth_wise=False, arch=85, pretrained=pretrained)
    return model

def hardnet68ds(pretrained=False, **kwargs):
    """ # This docstring shows up in hub.help()
    Harmonic DenseNet 68ds (Depthwise Separable) model
    pretrained (bool): kwargs, load pretrained weights into the model
    """
    # Call the model, load pretrained weights
    model = hardnet.HarDNet(depth_wise=True, arch=68, pretrained=pretrained)
    return model

def hardnet39ds(pretrained=False, **kwargs):
    """ # This docstring shows up in hub.help()
    Harmonic DenseNet 68ds (Depthwise Separable) model
    pretrained (bool): kwargs, load pretrained weights into the model
    """
    # Call the model, load pretrained weights
    model = hardnet.HarDNet(depth_wise=True, arch=39, pretrained=pretrained)
    return model

