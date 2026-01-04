import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import openpyxl

matplotlib.rcParams['agg.path.chunksize'] = 10000

def parce(filename,save = 'EMF'):
    delay = 1
    global results
    timelines = []
    voltage_list = []
    dat = os.path.join('storage',filename)
    linenum = 0
    with open(dat, "r", encoding='utf-8')as f:
        for line in f:
            try: raw = float(line.strip())
            except ValueError: continue
            linenum+=delay
            timeline = linenum
            voltage_list.append(raw)
            timelines.append(timeline)
    df = pd.DataFrame({
        "Time": timelines,
        "voltage":voltage_list
    })
    name = filename.split('.')[0]
    if os.path.isdir(os.path.join('storage',name)): pass
    else: os.makedirs(os.path.join('storage',name))
    df.to_excel(os.path.join('storage',name,f"{save}.xlsx"), index=False)

def get_offset_std(foldername,filename,save='noise'):
    df = pd.read_excel(os.path.join('storage',foldername,filename), engine='openpyxl', header=0)
    voltage = df.voltage
    voltage_arr = voltage.to_numpy()
    print(np.mean(voltage_arr))
    print(np.std(voltage_arr))
def slicer(foldername,filename,num,save = 'sliced'):
    df = pd.read_excel(os.path.join('storage',foldername,filename), engine='openpyxl', header=0)
    voltage = df.voltage
    time = df.Time
    voltage_arr = voltage.to_numpy()[::num]
    time_arr = time.to_numpy()[::num]
    df2 = pd.DataFrame({
        'Time': time_arr,
        'voltage': voltage_arr
    })
    df2.to_excel(os.path.join('storage',foldername,f'{save}.xlsx'))

def true_voltage(foldername,filename,save='trueV'):
    df = pd.read_excel(os.path.join('storage',foldername,filename),engine='openpyxl',header=0)
    voltage = df.voltage
    time = df.Time.to_numpy()
    voltage_arr = voltage.to_numpy()
    unoffset_voltage = voltage_arr * 5 / 1023
    df2 = pd.DataFrame({
        'Time': time,
        'voltage': unoffset_voltage
    })
    df2.to_excel(os.path.join('storage',foldername,f'{save}.xlsx'))
    
def moving_average(foldername,filename,num=100,save='MA'):
    df = pd.read_excel(os.path.join('storage',foldername,filename),engine='openpyxl',header=0)
    voltage = df.voltage.rolling(window=num).mean()
    time = df.Time
    df2 = pd.DataFrame({
        'Time': time,
        'voltage': voltage
    })
    df2.to_excel(os.path.join('storage',foldername,f'{save}.xlsx'))


def unoffset(foldername,filename,save='unoffset'):
    df = pd.read_excel(os.path.join('storage',foldername,filename),engine='openpyxl',header=0)
    voltage = df.voltage
    time = df.Time.to_numpy()
    voltage_arr = voltage.to_numpy()
    unoffset_voltage = voltage_arr - 505.55085039916696
    df2 = pd.DataFrame({
        'Time': time,
        'voltage': unoffset_voltage
    })
    df2.to_excel(os.path.join('storage',foldername,f'{save}.xlsx'))
def zoom(foldername,filename,save='zoom'): pass
    
def plot_2d_time(foldername,filename,save='EMF'):
    df = pd.read_excel(os.path.join('storage',foldername,filename), engine='openpyxl', header=0)
    timelines = df.Time
    voltage = df.voltage
    plt.plot(timelines, voltage, label = "Electromotive Force", color = (0.0, 0.0, 1.0, 1.0), linestyle="-", marker="")

    plt.title(f"Voltage by Induced Electromotive Force")
    plt.xticks([])
    plt.grid(axis='x', visible=False)
    plt.xlabel("Time     [   ms  ]")
    plt.ylabel("Voltage  [   V   ]")
    plt.grid(True)
    plt.legend(
        loc       = "lower right",
        frameon   =  True,
        edgecolor = "black",
        facecolor = "white",
        )

    plt.savefig(f"{save}_Graph.jpg", dpi=600, bbox_inches='tight')
    plt.close()
