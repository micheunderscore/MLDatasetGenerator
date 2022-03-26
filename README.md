# DATASET GENERATOR!

### How to Use

1. Extract all files to project folder
2. Open & run genDataset.ipynb
3. Dataset file >>> dataset.csv
4. ENJOY!!!

### Parameters

```py
genDataset(varName = 'var', varCount = 1, dataCount = 100, target = 'target', outputDType = outType.BOOL) -> pd.DataFrame:
```

| Variable Name | Description                                           |
| ------------- | ----------------------------------------------------- |
| `varName`     | Name of dataset features _(default: 'var')_           |
| `varCount`    | Number of features in dataset _(default: 1)_          |
| `dataCount`   | Number of data to be generated _(default: 100)_       |
| `target`      | Name of target feature _(default: 'target')_          |
| `outputDType` | Data type of target feature _(default: outType.BOOL)_ |
