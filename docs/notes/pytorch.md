# Deep Learning

## [Introduction to PyTorch on YouTube](https://pytorch.org/tutorials/beginner/introyt.html)

### Intro to Pytorch

Training LeNet for 3 color image classification

- Conv2d Layers
- MaxPool2d Layers

### Introduction to Pytorch Tensors

Popular Methods to Create Tensors:

- zeros_like_x = torch.zeros_like(x)
- ones_like_x = torch.ones_like(x)
- rand_like_x = torch.rand_like(x)

You can either pass a tensor shape by remove `._like`, or automatically copy the shape of a tensor.

`torch.tensor(data)` will create our tensor

Can set dtype with `dtype=`  

Tensors of the same shape can use artihemtic operators together, or similar shapes can broadcast operations

Tensors have over 300 operations that can be performed on them: Arhitmetic, Trigonmetric, Bitwise XOR, Det, SVD. Imagine a general model that determines the arthimetic calculations, what unintuitive patterns would it find? Also, hashing and zk technologies use XOR operations, could they be used in tensors or deep learning somehow? Could a neural network do stuff with hashes, ethereum transactions, etc.?

You can specify the output of a tensor operation with an already initalized tensor with the `out` parameter, which does not allocate new memory, or perform operations inplace with a `_` after the operation name.

As with any object in python, assigning a variable to it does not copy it and assigns the variable a _label_ of the tensor

## [Pytorch.org Torchvision Tutorial](https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html)
