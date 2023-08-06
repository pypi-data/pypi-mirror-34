pyojm
=====
![travis](https://travis-ci.org/lune-sta/pyojm.svg?branch=master)
[![codecov](https://codecov.io/gh/lune-sta/pyojm/branch/master/graph/badge.svg)](https://codecov.io/gh/lune-sta/pyojm)

A Pythonic interface for Json that supports Python 3.

In this package, you can define a model corresponding to Json.  
It provides functions such as simple access to values, validation and so on.


## Installation
```$xslt
pip install pyojm
```

## Basic Usage
Create a model that describes your Json schemes.  
Do you want to know about json path? See [kennknowles/python-jsonpath-rw](https://github.com/kennknowles/python-jsonpath-rw).

```$xslt
from pyojm.models import Model
from pyojm.attributes import StringAttribute, StringListAttribute, NumberListAttribute


class SampleModel(Model):
    group_name = StringAttribute('group_name')
    member_names = StringListAttribute('members.[*].name')
    member_ages = NumberListAttribute('members.[*].age')
```

Create an instance and submit Json data.
```$xslt
json_dict = {
    'group_name': 'cake_shop',
    'members': [
        {
            'name': 'lune',
            'age': 9
        },
        {
            'name': 'canon',
            'age': 20
        }
    ]
}

sample = SampleModel(json_dict)
```

You can access it in the property format.
```$xslt
print(sample.group_name)
# "cake_shop"
print(sample.member_names)
# ["lune", "canon"]
print(sample.member_ages)
# [9, 20]
```

If you set Meta.strict_validation to True, it will check the type at run time.
```$xslt
class UserModel(Model):
    class Meta:
        strict_validation = True
    name = StringAttribute('name')


json_dict = {
    'name': 9
}

user = UserModel(json_dict)

print(user.name)
# TypeError: type of name must be str; got int instead
```

