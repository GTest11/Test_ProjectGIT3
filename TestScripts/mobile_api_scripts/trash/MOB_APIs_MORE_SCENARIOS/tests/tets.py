

list_element_types = {
    'xpath': "mob_lib.Constants.ElementType.XPath",
    'id': "mob_lib.Constants.ElementType.Id",
    'name': "mob_lib.Constants.ElementType.Name",
    'class': "mob_lib.Constants.ElementType.ClassName",
    'access_id': "mob_lib.Constants.ElementType.AccessibilityID",
}

def function():
    elm_name = {
        'xpath': '//android.widget.ImageView[0]',  # an element which does not exist
        'id': None,
        'name': None,
        'class': "hello",
        'access_id': None
    }

    elm_type = None
    type = None
    element_type_to_test = 'class'
    try:
        print elm_name
        # if not self.elm_type in elm_name.keys():
        #     logger.Error("No element type '{}' available".format(self.elm_type))
        #     return None
        # logger.Log("self.element_type_to_test {}".format(self.element_type_to_test))

        if elm_name[element_type_to_test] is None:
            print("Element does not support the Element type '{}', so taking xpath..".format(element_type_to_test))
            elm_type = list_element_types['xpath']
            type = 'xpath'
        else:
            elm_type = list_element_types[element_type_to_test]
            type = element_type_to_test
            print("Element type to test given element is {}".format(elm_type))
            print("self.list_element_types[self.element_type_to_test] {}".format(list_element_types[element_type_to_test]))
            print("type {}".format(type))

        # logger.Log("Element type to test given element is {}".format(elm_type))
        # logger.Log("type {}".format(type))

    except Exception as e:
        print("Error in choosing element type" + str(e))
        elm_type = None
        type = None
    finally:
        return elm_type, type

print function()