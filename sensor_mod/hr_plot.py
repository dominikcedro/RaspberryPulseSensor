import matplotlib.pyplot as plt


def plot_hr(hr_readings):
    """
    Plot heart rate readings
    ARGS:
        hr_readings: list of heart rate readings

    """
    fig = plt.figure()
    time_points = range(len(hr_readings))
    plt.plot(time_points, hr_readings, color='orange', linestyle='solid', linewidth=2, markersize=12)
    plt.title('BPM Readings Over Time')
    plt.xlabel('Time')
    plt.xticks([])
    plt.ylabel('Heart Rate')
    return fig

