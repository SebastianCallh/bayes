import matplotlib.pyplot as plt
import matplotlib

def get_axis(name: str):
    _, ax = plt.subplots(1, 1)
    ax.set_xlabel(r'$X$')
    ax.set_ylabel('Density')
    ax.set_title(f'Example of {name} distribution')
    return ax

colors = ['saddlebrown', 'steelblue', 'seagreen', 'turquoise', 'darkkhaki', 'firebrick']
