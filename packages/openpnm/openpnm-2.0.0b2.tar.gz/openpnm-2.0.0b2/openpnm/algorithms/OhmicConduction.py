from openpnm.algorithms import ReactiveTransport
from openpnm.utils import logging
logger = logging.getLogger(__name__)


class OhmicConduction(ReactiveTransport):
    r"""
    A subclass of GenericLinearTransport to simulate electron and ionic
    conduction.  The 2 main roles of this subclass are to set the default
    property names and to implement a method for calculating the effective
    conductivity of the network.

    """

    def __init__(self, settings={}, **kwargs):
        super().__init__(**kwargs)
        self.settings.update({'quantity': 'pore.voltage',
                              'conductance': 'throat.electrical_conductance'})
        self.settings.update(settings)

    def setup(self, phase=None, quantity='', conductance='', **kwargs):
        r"""
        This method takes several arguments that are essential to running the
        algorithm and adds them to the settings.

        Parameters
        ----------
        phase : OpenPNM Phase object
            The phase on which the algorithm is to be run.  If no value is
            given, the existing value is kept.

        quantity : string
            The name of the physical quantity to be calcualted.  If no value is
            given, the existing value is kept.  The default value is
            ``'pore.voltage'``.

        conductance : string
            The name of the pore-scale transport conductance values.  These
            are typically calculate by a model attached to a *Physics* object
            associated with the given *Phase*.  If no value is given, the
            existing value is kept.  The default value is
            ``'throat.electrical_conductance'``.

        Notes
        -----
        Any additional arguments are added to the ``settings`` dictionary of
        the object.

        """
        if phase:
            self.settings['phase'] = phase.name
        if quantity:
            self.settings['quantity'] = quantity
        if conductance:
            self.settings['conductance'] = conductance
        super().setup(**kwargs)

    def calc_effective_conductivity(self):
        r"""
        This calculates the effective electrical conductivity.
        """
        return self._calc_eff_prop()
