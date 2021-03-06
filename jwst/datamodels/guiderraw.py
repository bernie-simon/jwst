from .model_base import DataModel

__all__ = ['GuiderRawModel']


class GuiderRawModel(DataModel):
    """
    A data model for FGS pipeline input files

    Parameters
    ----------
    init: any
        Any of the initializers supported by `~jwst.datamodels.DataModel`.

    data: numpy array
        The science data. 4-D

    dq: numpy array
        The data quality array. 2-D.

    err: numpy array
        The error array. 4-D.

    plan_star_table: table
        The planned reference star table

    flight_star_table: table
        The flight reference star table

    pointing_table: table
        The pointing table

    centroid_table: table
        The centroid packet table

    track_sub_table: table
        The track subarray table
    """

    schema_url = "guider_raw.schema.yaml"

    def __init__(self, init=None, **kwargs):

        super(GuiderRawModel, self).__init__(init=init, **kwargs)

        # Implicitly create arrays
        self.dq = self.dq
        self.err = self.err
