# vaik-pascal-voc-rw-ex

Read and write extended Pascal VOC xml annotations

## Install

``` shell
pip install git+https://github.com/vaik-info/vaik-pascal-voc-rw-ex.git
```

## Usage

### Read

```python
from vaik_pascal_voc_rw_ex import pascal_voc_rw_ex

xml_dict = pascal_voc_rw_ex.read_pascal_voc_xml('sample.xml')
```

### Write

```python
from vaik_pascal_voc_rw_ex import pascal_voc_rw_ex

an_object_extend_dict_list = [
    pascal_voc_rw_ex.get_objects_dict_template('person', 100, 100, 200, 200,
                                               object_extend_dict={'actor': 'BP_Kwame_C_2147482137',
                                                                   'pitch': 0.01,
                                                                   'yaw': 0.02,
                                                                   'roll': 0.03}),
]

pascal_voc_rw_ex.write_pascal_voc_xml_dict('sample_write.xml', 'sample_write.png',
                                           annotation_extend_dict={
                                               'intensity': 0.01,
                                               'bluramount': 0.02,
                                               'bluramax': 0.03,
                                               'blurfps': 0.04},
                                           object_extend_dict_list=an_object_extend_dict_list)

```