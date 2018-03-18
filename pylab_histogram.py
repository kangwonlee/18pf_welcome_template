import pylab

data_list = [pylab.randint(0, 100) for i in range(100)]


# make histogram
def main(data):
    ave = pylab.mean(data)
    std = pylab.std(data)

    ave_p_std = ave + std
    ave_m_std = ave - std

    pylab.hist(data, bins=range(0, 111, 5))
    ylims = pylab.ylim()
    pylab.plot([ave_m_std] * 2, ylims, 'r')
    pylab.plot([ave_p_std] * 2, ylims, 'r')
    pylab.grid()
    pylab.title('average = %g, std = %g' % (
        pylab.mean(data), pylab.std(data)))
    pylab.show()


if __name__ == '__main__':
    main(data_list)
