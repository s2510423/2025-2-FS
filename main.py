import plotter

def parce_all():
    plotter.parce('noise.txt')
    plotter.parce('real..txt')

def process_all():
    plotter.unoffset('noise','EMF.xlsx')
    plotter.unoffset('real','EMF.xlsx')
    plotter.true_voltage('noise','unoffset.xlsx')
    plotter.true_voltage('real','unoffset.xlsx')

def ma(num=100):
    plotter.moving_average('real','trueV.xlsx',num)
    plotter.moving_average('noise','trueV.xlsx',num)

def slicer(num=1000):
    plotter.slicer('real','trueV.xlsx',num)
    plotter.slicer('noise','trueV.xlsx',num)
def print_plt(file='trueV'):
    plotter.plot_2d_time('noise',f'{file}.xlsx','noise')
    plotter.plot_2d_time('real',f'{file}.xlsx','real')

    