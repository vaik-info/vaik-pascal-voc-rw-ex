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

xml_dict = pascal_voc_rw_ex.read_pascal_voc_xml('sample_read.xml')
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

- sample_write.xml

```xml
<annotation>
    <folder>vaik-pascal-voc-rw-ex</folder>
    <filename>sample_write.png</filename>
    <path>/home/vaik-info/Github/minimum_samples/vaik-pascal-voc-rw-ex/sample_write.png</path>
    <source>
        <database>Unknown</database>
    </source>
    <size>
        <width>800</width>
        <height>600</height>
        <depth>4</depth>
    </size>
    <segmented>0</segmented>
    <intensity>0.01</intensity>
    <bluramount>0.02</bluramount>
    <bluramax>0.03</bluramax>
    <blurfps>0.04</blurfps>
    <object>
        <name>person</name>
        <bndbox>
            <xmin>100</xmin>
            <ymin>100</ymin>
            <xmax>200</xmax>
            <ymax>200</ymax>
        </bndbox>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <actor>BP_Kwame_C_2147482137</actor>
        <pitch>0.01</pitch>
        <yaw>0.02</yaw>
        <roll>0.03</roll>
    </object>
</annotation>
```