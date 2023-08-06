# contils

## contils.color

Print red text

```python
from contils.color import red

print(red('red text'))
```

## contils.flash

```python
from contils.flash import Flash

flash = Flash()
flash.print('Loading 7%')
flash.print('Loading 25%')
flash.print('Loading 54%')
flash.print('Loading 100%')
flash.end()
```