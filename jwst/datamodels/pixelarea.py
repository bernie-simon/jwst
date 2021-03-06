from .reference import ReferenceFileModel


__all__ = ['PixelAreaModel', 'NirspecSlitAreaModel', 'NirspecMosAreaModel',
           'NirspecIfuAreaModel']


class PixelAreaModel(ReferenceFileModel):
    """
    A data model for the pixel area map
    """
    schema_url = "pixelarea.schema.yaml"



class NirspecSlitAreaModel(ReferenceFileModel):
    """
    A data model for the NIRSpec fixed-slit pixel area reference file

    Parameters
    ----------
    init : any
        Any of the initializers supported by `~jwst.datamodels.DataModel`.

    area_table : numpy array
        A table-like object containing row selection criteria made up
        of the slit id and the pixel area values associated with
        the slits.

        - slit_id: str[15]
        - pixarea: float32
    """
    schema_url = "nirspec_area_slit.schema.yaml"


class NirspecMosAreaModel(ReferenceFileModel):
    """
    A data model for the NIRSpec MOS pixel area reference file

    Parameters
    ----------
    init : any
        Any of the initializers supported by `~jwst.datamodels.DataModel`.

    area_table : numpy array
        A table-like object containing row selection criteria made up
        of MOS shutter parameters and the pixel area values associated
        with the shutters.

        - quadrant: int16
        - shutter_x: int16
        - shutter_y: int16
        - pixarea: float32
    """
    schema_url = "nirspec_area_mos.schema.yaml"


class NirspecIfuAreaModel(ReferenceFileModel):
    """
    A data model for the NIRSpec IFU pixel area reference file

    Parameters
    ----------
    init : any
        Any of the initializers supported by `~jwst.datamodels.DataModel`.

    area_table : numpy array
        A table-like object containing row selection criteria made up
        of IFU slice id and the pixel area values associated
        with the slices.

        - slice_id: int16
        - pixarea: float32
    """
    schema_url = "nirspec_area_ifu.schema.yaml"

