# toJson.py

Small python tool that generates json using an easy syntax

## Example usage

```
~$:  echo "Key1=Value1 | Key2=Value2 | Key3=Value3 | Key4=Value4 | Key5=Value5" | toJson.py 
{"Key1": "Value1", "Key3": "Value3", "Key2": "Value2", "Key4": "Value4", "Key5": "Value5"}
```

```
~$:  toJson.py "Key1=Value1 | Key2=Value2 | Key3=Value3 | Key4=Value4 | Key5=Value5"
{"Key3": "Value3", "Key4": "Value4", "Key2": "Value2", "Key1": "Value1", "Key5": "Value5"}
```
