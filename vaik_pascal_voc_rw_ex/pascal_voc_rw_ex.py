import xmltodict
import dicttoxml
from xml.dom.minidom import parseString
from pascal_voc_writer import Writer
from PIL import Image


def read_pascal_voc_xml(xml_path):
    with open(xml_path, 'r') as f:
        xml_dict = xmltodict.parse(f.read())
    return xml_dict


def get_objects_dict_template(name, xmin, ymin, xmax, ymax, pose='Unspecified', truncated=0, difficult=0,
                              object_extend_dict=None):
    if object_extend_dict is None:
        object_extend_dict = {}
    org_dict = {
        'name': name,
        'pose': pose,
        'truncated': truncated,
        'difficult': difficult,
        'bndbox': {
            'xmin': xmin,
            'ymin': ymin,
            'xmax': xmax,
            'ymax': ymax,
        },
    }
    return {**org_dict, **object_extend_dict}


def write_pascal_voc_xml_dict(output_xml_path, image_path, database='Unknown', segmented=0,
                              annotation_extend_dict=None, object_extend_dict_list=None):
    image = Image.open(image_path)
    width, height = image.size
    depth = len(image.getbands())

    writer = Writer(image_path, width, height, depth, database, segmented)
    content = writer.annotation_template.render(**writer.template_parameters)
    content_dict = xmltodict.parse(content)

    if annotation_extend_dict is not None:
        content_dict['annotation'] = {**content_dict['annotation'], **annotation_extend_dict}

    if object_extend_dict_list is not None and len(object_extend_dict_list) > 0:
        content_dict['annotation']['object'] = object_extend_dict_list

    xml = dicttoxml.dicttoxml(content_dict, root=False, attr_type=False, item_func=lambda x: 'object')
    xml = xml.decode('utf-8').replace('</object></object>', '</object>').replace('<object><object>', '<object>').encode(
        'utf-8')
    xml_string = parseString(xml).toprettyxml()
    xml_string = '\n'.join(xml_string.split('\n')[1:])
    with open(output_xml_path, 'w') as f:
        f.write(xml_string)
