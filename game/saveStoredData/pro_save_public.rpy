
default _pro_save_file_format = "saveStoredData/{}.rtf"


init python:

    def pro_save_set_store(s):

        for k,v in s.items():

            curv = getattr(store, k) if hasattr(store, k) else "No value"

            if curv != v:

                if k.endswith(".state"):

                    if not hasattr(store, k[:-6]):

                        setattr(store, k[:-6], globals()[v.pop("class_name")]())

                    getattr(store, k[:-6]).__dict__.update(v)

                    continue

                setattr(store, k, v)


    def get_pro_save_data(fn):

        data = ""

        with renpy.file(fn) as f:

            data = f.read()

        return cPickle.loads(renpy.fsencode(data.replace("·","\n")))


    def missing_label_callback(lbl):

        pro_lbl = lbl[:-4]
        pro_file = _pro_save_file_format.format(pro_lbl)

        if renpy.has_label(pro_lbl) and renpy.loadable(pro_file):

            pro_save_set_store(get_pro_save_data(pro_file))

            return pro_lbl

        return None

    config.missing_label_callback = missing_label_callback
