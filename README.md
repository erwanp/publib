# PubLib

Produce publication-level quality images on top of Matplotlib

For similar librairies, see seaborn, which also add neat high-end API to 
Matplotlib function calls.  

--------
Use
```
import numpy as np
import matplotlib.pyplot as plt
import publib
a = np.linspace(0,6.28)
plt.plot(a,np.cos(a))
plt.show()
```

```
publib.set_style('article')
plt.plot(a,a**2)
publib.buff_style('article')
plt.show()
```
