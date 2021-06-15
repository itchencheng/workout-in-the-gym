import matplotlib.pyplot as plt

class Plotter():
    def __init__(self, title="none"):
        self.memory = list()
        self.title = title

    def add(self, data):
        self.memory.append(data)
    
    def plot(self):
        plt.title(self.title)
        plt.plot(range(len(self.memory)), self.memory, color='green', label='train-loss')

        plt.legend() # 显示图例
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()