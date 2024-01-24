import matplotlib.pyplot as plt


def plot_hr(hr_readings):
    """
    Plot heart rate readings
    ARGS:
        hr_readings: list of heart rate readings

    """
    time_points = range(len(hr_readings))
    plt.plot(time_points, hr_readings,'-r')
    plt.title('BPM Readings Over Time')
    plt.xlabel('Time')
    plt.ylabel('Heart Rate')
    plt.show()
