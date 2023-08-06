# Oscilloscope
**An oscilloscope for python that just works™**


### It's fucking simple to use

*This*

```python3
import random
from time import sleep

from oscilloscope import Osc


osc = Osc()

@osc.signal
def random_signal(update):
    while True:
        update(random.random())
        sleep(0.1)
        
osc.start()
```

*Gives you this*

<img src="https://i.imgur.com/jB3wzgT.png" height="300" />

### Parallel compute

Each `osc.signal` gets it's own process.

*This*

```python3
import random
from time import sleep

from oscilloscope import Osc


osc = Osc(nrows=2, ncols=3)

@osc.signal
def signal1(update):
    while True:
        update(random.random())
        sleep(0.1)

@osc.signal
def signal2(update):
    while True:
        update(random.random(), row=1, col=2)
        sleep(0.1)

osc.start()
```

*Gives you this*

<img src="https://i.imgur.com/JWHQ9Da.png" height="300" />

### Automatic normalization

*This*
```python3
import random
from time import sleep

from oscilloscope import Osc


# increase the time scale so we can see clearly
osc = Osc(time_axis_sec=10)

@osc.signal
def irregular_signal(update):
    for _ in range(10):
        update(random.randint(0, 1))
        sleep(0.1)

    update(0.5)

    print("so I'm totally gonna fuck up after 5 sec")
    sleep(5)

    while True:
        update(random.randint(0, 1000))
        sleep(0.1)

osc.start()
```

*Gives you this*

<img src="https://i.imgur.com/8TYCaaK.png" height="300" />

After the 5 sec pause, the signal range changes drastically, but the graph still retains its coherence!

(The Y-axis is basically the % of the max value encountered at the time)


# Install


`pip install oscilloscope[pyqt5]`

*Install using the pyQt5 backend. (tkinter by default)*
