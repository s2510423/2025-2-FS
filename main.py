import plotter

def parce_all():
    plotter.parce('noise.txt')
    plotter.parce('real..txt')

def unoffset_all():
    plotter.unoffset('noise','EMF.xlsx')
    plotter.unoffset('real','EMF.xlsx')

def downscale_real():
    double_thanos('real','unoffset.xlsx')

def print_plot_jpg():
    plotter.plot_2d_time('noise','unoffset.xlsx','noise')
    plotter.plot_2d_time('real','downscaled.xlsx','real')
    