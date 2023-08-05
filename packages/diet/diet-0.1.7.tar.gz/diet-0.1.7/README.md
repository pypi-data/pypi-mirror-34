# DIET

Dash Import Export Tool

## Installation

```sh
pip install --user -U diet
```

## Usage

```
Dash Import and Export Tool

positional arguments:
  {import,export}  Action to perform
  target           The target of the import/export
  file             Files to import
```

**Import users into the system**
```sh
diet import user ./user-records.csv
```

## Import file structure

### Supported file types
* CSV

#### CSV Structure
The CSV file must include a header row that matches the field's name you wish to import **exactly**

### User Import
| firstName | surname       | email                                                          | gender | address           | suburb    | state | mobilePhoneNumber | password  | postcode |
|-----------|---------------|----------------------------------------------------------------|--------|-------------------|-----------|-------|-------------------|-----------|----------|
| Test      | Administrator | csss@sporga.com.au                                             | Female | 20 resolution Dr  | Caringbah | NSW   | 61410100100       | ******* | 2229     |