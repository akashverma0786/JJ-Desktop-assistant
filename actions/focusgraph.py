import matplotlib.pyplot as pt

def focus_graph():
    file = open("focus.txt", "r")
    content = file.read()
    file.close()

    # example
    # Current Time = 12:00
    # stop time = 12: 30
    # difference = 00:30
    # will change into 00.30 and save it and make graph out of it

    content = content.split(",")
    x1 = []
    for i in range(0, len(content)):
        content[i] = float(content[i])
        x1.append(i)

    print(content)
    y1 = content

    pt.plot(x1, y1, color = "red", marker = "o")
    pt.title("your Focused time", fontsize = 16)
    pt.xlabel("Times", fontsize = 14)
    pt.ylabel("FocusTime", fontsize = 14)
    pt.grid()
    pt.show()
