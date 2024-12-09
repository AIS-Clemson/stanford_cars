import torchvision

if __name__ == "__main__":
    data = torchvision.datasets.StanfordCars(root='./', download=False)
    print('loading successful...')
    print(data)
    # len(data._samples)
