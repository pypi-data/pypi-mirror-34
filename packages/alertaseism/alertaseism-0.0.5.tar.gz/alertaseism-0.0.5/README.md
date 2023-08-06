O librarie folosiind date XML de la INFP pentru a afla magnitudinea la secunda.
Github: https://github.com/TudorGruian/alerta-seism-python3


Exemplu:

```python
import alertaseism

print(alertaseism.mag()) # <- pentru magnitudine
print(alertaseism.heart()) # <- pentru stare server

if alertaseism.mag() >= 1:
    print("CUTREMUUUR")
```

Tot pe Git gasesti si exemple de loop

