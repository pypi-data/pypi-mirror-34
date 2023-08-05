# Princeton University licenses this file to You under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.  You may obtain a copy of the License at:
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.


# ******************************************  ControlSignal *****************************************************

"""
Overview
--------

A ControlSignal is a type of `ModulatorySignal <ModulatorySignal>` that is specialized for use with a `ControlMechanism
<ControlMechanism>` and one or more `ControlProjections <ControlProjection>`, to modify the parameter(s) of one or more
`Components <Component>`. A ControlSignal receives an `allocation <ControlSignal.allocation>` value from the
ControlMechanism to which it belongs, and uses that to compute an `intensity` (also referred to as a `control_signal`)
that is assigned as the `value <ControlProjection.ControlProjection.value>` of its ControlProjections. Each
ControlProjection conveys its value to the `ParameterState` for the parameter it controls, which uses that value to
`modulate <ModulatorySignal_Modulation>` the `value <ParameterState.value>` of the parameter.  A ControlSignal also
calculates a `cost`, based on its `intensity` and/or its time course, that may be used by the ControlMechanism to
adapt the ControlSignal's `allocation <ControlSignal.allocation>` in the future.

.. _ControlSignal_Creation:

Creating a ControlSignal
------------------------

A ControlSignal is created automatically whenever the parameter of a Mechanism or of its function is `specified for
control <ControlMechanism_Control_Signals>`.  ControlSignals can also be specified in the **control_signals** argument
of the constructor for a `ControlMechanism <ControlMechanism>` or a `System <System_Control_Specification>`.  Although
a ControlSignal can be created directly using its constructor (or any of the other ways for `creating an OutputState
<OutputStates_Creation>`), this is usually not necessary nor is it advisable, as a ControlSignal has dedicated
components and requirements for configuration that must be met for it to function properly.

.. _ControlSignal_Specification:

Specifying ControlSignals
~~~~~~~~~~~~~~~~~~~~~~~~~

When a ControlSignal is specified in the **control_signals** argument of the constructor for a `ControlMechanism
<ControlMechanism>`, the parameter to be controlled must be specified.  This can take any of the following forms:

  * **ParameterState** -- of the Mechanism to which the parameter belongs;
  ..
  * **specification dictionary** -- can take either of the following two forms:

    * for controlling a single parameter, the dictionary can have the following two entries:

        * *NAME*: str
            the string must be the name of the parameter to be controlled;

        * *MECHANISM*: Mechanism
            the Mechanism must be the one to the which the parameter to be controlled belongs.

    * for controlling multiple parameters, the dictionary can have the following entry:

        * <str>:list
            the string used as the key specifies the name to be used for the ControlSignal,
            and each item of the list must be a `specification of a parameter <ParameterState_Specification>` to be
            controlled by the ControlSignal (and that will receive a `ControlProjection` from it).
  ..
  * **2-item tuple:** *(parameter name or list of them>, <Mechanism>)* -- the 1st item must be the name of the
    parameter (or list of parameter names), and the 2nd item the Mechanism to which it (they) belong(s); this is a
    convenience format, that is simpler to use than a specification dictionary (see above), but precludes
    specification of any `parameters <ControlSignal_Structure>` for the ControlSignal.
  ..

.. _ControlSignal_Structure:

Structure
---------

A ControlSignal is owned by an `ControlMechanism <ControlMechanism>`, and controls the parameters of one or more
Components by modulating the `function <ParameterState.function>` of the `ParameterState` that determines the value
of each of the parameters that it control.  Its operation is governed by several attributes of the ControlSignal,
that are described below.

.. _ControlSignal_Projections:

Projections
~~~~~~~~~~~

When a ControlSignal is created, it can be assigned one or more `ControlProjections <ControlProjection>`, using either
the **projections** argument of its constructor, or in an entry of a dictionary assigned to the **params** argument
with the key *PROJECTIONS*.  These will be assigned to its `efferents  <ControlSignal.efferents>` attribute.  See
`State Projections <State_Projections>` for additional details concerning the specification of Projections when
creating a State.

.. note::
   Although a ControlSignal can be assigned more than one `ControlProjection`, all of those Projections will receive
   the same `value <ControlProjection.value>` (based on the `intensity` of that ControlSignal), and use the same
   form of `modulation <ControlSignal_Modulation>`.  Thus, for them to be meaningful, they should project to
   ParameterStates for parameters that are meaningfully related to one another (for example, the threshold parameter
   of multiple `DDM` Mechanisms).

.. _ControlSignal_Modulation:

Modulation
~~~~~~~~~~

A ControlSignal has a `modulation <GatingSignal.modulation>` attribute that determines how its ControlSignal's
`value <ControlSignal.value>` is used by the States to which it projects to modify their `value <State_Base.value>` \\s
(see `ModulatorySignal_Modulation` for an explanation of how the `modulation <ControlSignal.modulation>`  attribute is
specified and used to modulate the `value <State_Base.value>` of a State). The `modulation <ControlSignal.modulation>`
attribute can be specified in the **modulation** argument of the constructor for a ControlSignal, or in a specification
dictionary as described `above <ControlSignal_Specification>`. The value must be a value of `ModulationParam`;  if it
is not specified, its default is the value of the `modulation <ControlMechanism.modulation>` attribute of the
ControlMechanism to which the ControlSignal belongs (which is the same for all of the ControlSignals belonging to that
ControlMechanism).  The value of the `modulation <ControlSignal.modulation>` attribute of a ControlSignal is used by
all of the `ControlProjections <ControlProjection>` that project from that ControlSignal.

.. _ControlSignal_Allocation_and_Intensity

Allocation, Function and Intensity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Allocation (variable)*. A ControlSignal is assigned an `allocation <ControlSignal>` by the ControlMechanism to
which it belongs. Some ControlMechanisms sample different allocation values for their ControlSignals to determine
which to use (such as the `EVCControlMechanism <EVC_Default_Configuration>`);  in those cases, they use each ControlSignal's
`allocation_samples <ControlSignal.allocation_samples>` attribute (specified in the **allocation_samples** argument
of the ControlSignal's constructor) to determine the allocation values to sample for that ControlSignal.  A
ControlSignal's `allocation <ControlSignal>` attribute reflects value assigned to it by the ControlMechanism
at the end of the previous `TRIAL` (i.e., when the ControlMechanism last executed --  see
`ControlMechanism Execution <ControlMechanism_Execution>`); its value from the previous `TRIAL` is assigned to the
`last_intensity` attribute.

*Function*. A ControlSignal's `allocation <ControlSignal.alloction>` serves as its`variable <ControlSignal.variable>`,
and is used by its `function <ControlSignal.function>` to generate an `intensity`. The default `function
<ControlSignal.function>` for a ControlSignal is an identity function (`Linear` with `slope <Linear.slope>` \\=1 and
`intercept <Linear.intercept>`\\=0), that simply assigns the `allocation <ControlSignal.allocation>` as the
ControlSignal's `intensity <ControlSignal.intensity>`. However, another `TransferFunction` can be assigned
(e.g., `Exponential`), or any other function that takes and returns a scalar value or 1d array.

*Intensity (value)*. The result of the function is assigned as the value of the ControlSignal's `intensity`
attribute, which serves as the ControlSignal's `value <ControlSignal.value>` (also referred to as `control_signal`).
The `intensity` is used by its `ControlProjection(s) <ControlProjection>` to modulate the parameter(s) for which the
ControlSignal is responsible. The ControlSignal's `intensity` attribute  reflects its value for the current `TRIAL`;
its value from the previous `TRIAL` is assigned to the `last_intensity` attribute.

.. _ControlSignal_Costs:

Costs and Cost Functions
~~~~~~~~~~~~~~~~~~~~~~~~

A ControlSignal has a `cost <ControlSignal.cost>` attribute that may be used by the ControlMechanism to which it
belongs to determine its future `allocation <ControlSignal.allocation>`.  The value of the `cost <ControlSignal.cost>`
is computed from the ControlSignal's `intensity` using one or more of three cost functions, each of which
computes a different component of the cost, and a function that combines them, as listed below:

    * `intensity_cost` - calculated by the `intensity_cost_function` based on the current `intensity` of the
      ControlSignal;
    ..
    * `adjustment_cost` - calculated by the `adjustment_cost_function` based on a change in the ControlSignal's
      `intensity` from its last value;
    ..
    * `duration_cost` - calculated by the `duration_cost_function` based on an integral of the the ControlSignal's
      `cost <ControlSignal.cost>`;
    ..
    * `cost` - calculated by the `cost_combination_function` that combines the results of any cost functions that are
      enabled.

The components used to determine the ControlSignal's `cost <ControlSignal.cost>` can be specified in the
**costs_options** argument of its constructor, or using its `enable_costs`, `disable_costs` and `assign_costs`
methods.  All of these take one or more values of `ControlSignalCosts`, each of which specifies a cost component.
How the enabled components are combined is determined by the `cost_combination_function`.  By default, the values of
the enabled cost components are summed, however this can be modified by specifying the `cost_combination_function`.

    COMMENT:
    .. _ControlSignal_Toggle_Costs:

    *Enabling and Disabling Cost Functions*.  Any of the cost functions (except the `cost_combination_function`) can
    be enabled or disabled using the `toggle_cost_function` method to turn it `ON` or `OFF`. If it is disabled, that
    component of the cost is not included in the ControlSignal's `cost` attribute.  A cost function  can  also be
    permanently disabled for the ControlSignal by assigning it's attribute `None`.  If a cost function is permanently
    disabled for a ControlSignal, it cannot be re-enabled using `toggle_cost_function`.
    COMMENT

.. note:: The `index <OutputState.OutputState.index>` and `assign <OutputState.OutputState.assign>`
        attributes of a ControlSignal are automatically assigned and should not be modified.

.. _ControlSignal_Execution:

Execution
---------

A ControlSignal cannot be executed directly.  It is executed whenever the `ControlMechanism <ControlMechanism>` to
which it belongs is executed.  When this occurs, the ControlMechanism provides the ControlSignal with an `allocation
<ControlSignal.allocation>`, that is used by its `function <ControlSignal.function>` to compute its `intensity` for
that `TRIAL`.  The `intensity` is used by the ControlSignal's `ControlProjections <ControlProjection>` to set the
`value <ParameterState.value>` \\(s) of the `ParameterState(s) <ParameterState>` to which the ControlSignal projects.

Recall that the ParameterState value is referenced anywhere that the controlled parameter is used in computation, and
that it does not update until the component to which the ParameterState belongs executes. If the distinction between the
base value stored in the parameter attribute (i.e. MyTransferMech.function_object.gain) and the value of the
ParameterState is unfamiliar, see `Parameter State documentation <ParameterState>` for more details, or see
`ModulatorySignal_Modulation` for a detailed description of how modulation operates.

The ControlSignal's `intensity` is also used  by its `cost functions <ControlSignal_Costs>` to compute its `cost`
attribute. That is used by some ControlMechanisms, along with the ControlSignal's `allocation_samples` attribute, to
evaluate an `allocation_policy <ControlMechanism.allocation_policy>`, and adjust the ControlSignal's `allocation
<ControlSignal.allocation>` for the next `TRIAL`.

.. note::
   The changes in a parameter in response to the execution of a ControlMechanism are not applied until the Mechanism
   with the parameter being controlled is next executed; see :ref:`Lazy Evaluation <LINK>` for an explanation of
   "lazy" updating).

.. _ControlSignal_Examples:

Examples
~~~~~~~~

*Modulate the parameter of a Mechanism's function*.  The following example assigns a
ControlSignal to the `bias <Logistic.gain>` parameter of the `Logistic` Function used by a `TransferMechanism`::

    >>> import psyneulink as pnl
    >>> my_mech = pnl.TransferMechanism(function=pnl.Logistic(bias=(1.0, pnl.ControlSignal)))

Note that the ControlSignal is specified by it class.  This will create a default ControlSignal,
with a ControlProjection that projects to the TransferMechanism's `ParameterState` for the `bias <Logistic.bias>`
parameter of its `Logistic` Function.  The default value of a ControlSignal's `modulation <ControlSignal.modulation>` attribute is Modulation.MULTIPLICATIVE, so that it will multiply the value of the `bias <Logistic.bias>` parameter. When the TransferMechanism executes, the Logistic Function will use the value of the ControlSignal as its
gain parameter.

*Specify attributes of a ControlSignal*.  Ordinarily, ControlSignals modify the *MULTIPLICATIVE_PARAM* of a
ParameterState's `function <ParameterState.function>` to modulate the parameter's value.
In the example below, this is changed by specifying the `modulation <ControlSignal.modulation>` attribute of a
`ControlSignal` for the `Logistic` Function of a `TransferMechanism`.  It is changed so that the value of the
ControlSignal adds to, rather than multiplies, the value of the `gain <Logistic.gain>` parameter of the Logistic
function::

    >>> my_mech = pnl.TransferMechanism(function=pnl.Logistic(gain=(1.0,
    ...                                                             pnl.ControlSignal(modulation=pnl.ModulationParam.ADDITIVE))))

Note that the `ModulationParam` specified for the `ControlSignal` pertains to the function of a *ParameterState*
for the *Logistic* Function (in this case, its `gain <Logistic.gain>` parameter), and *not* the Logistic function
itself -- that is, in this example, the value of the ControlSignal is added to the *gain parameter* of the Logistic
function, *not* its `variable <Logistic.variable>`).  If the value of the ControlSignal's **modulation** argument
had been ``ModulationParam.OVERRIDE``, then the ControlSignal's value would have been used as (i.e., replaced) the
value of the *Logistic* Function's `gain <Logistic.gain>` parameter, rather than added to it.

COMMENT:
    MOVE THIS EXAMPLE TO EVCControlMechanism

*Modulate the parameters of several Mechanisms by an EVCControlMechanism*.  This shows::

    My_Mech_A = TransferMechanism(function=Logistic)
    My_Mech_B = TransferMechanism(function=Linear,
                                 output_states=[RESULT, MEAN])

    Process_A = Process(pathway=[My_Mech_A])
    Process_B = Process(pathway=[My_Mech_B])
    My_System = System(processes=[Process_A, Process_B])

    My_EVC_Mechanism = EVCControlMechanism(system=My_System,
                                    monitor_for_control=[My_Mech_A.output_states[RESULT],
                                                         My_Mech_B.output_states[MEAN]],
                                    control_signals=[(GAIN, My_Mech_A),
                                                     {NAME: INTERCEPT,
                                                      MECHANISM: My_Mech_B,
                                                      MODULATION:ModulationParam.ADDITIVE}],
                                    name='My EVC Mechanism')
COMMENT

*Modulate the parameters of several Mechanisms in a System*.  The following example assigns ControlSignals to modulate
the `gain <Logistic.gain>` parameter of the `Logistic` function for ``My_Mech_A`` and the `intercept
<Logistic.intercept>` parameter of the `Linear` function for ``My_Mech_B``::

    >>> my_mech_a = pnl.TransferMechanism(function=pnl.Logistic)
    >>> my_mech_b = pnl.TransferMechanism(function=pnl.Linear,
    ...                                   output_states=[pnl.RESULT, pnl.MEAN])

    >>> process_a = pnl.Process(pathway=[my_mech_a])
    >>> process_b = pnl.Process(pathway=[my_mech_b])

    >>> my_system = pnl.System(processes=[process_a, process_b],
    ...                        monitor_for_control=[my_mech_a.output_states[pnl.RESULTS],
    ...                                             my_mech_b.output_states[pnl.MEAN]],
    ...                        control_signals=[(pnl.GAIN, my_mech_a),
    ...                                         {pnl.NAME: pnl.INTERCEPT,
    ...                                          pnl.MECHANISM: my_mech_b,
    ...                                          pnl.MODULATION: pnl.ModulationParam.ADDITIVE}],
    ...                        name='My Test System')


Class Reference
---------------

"""

import inspect
import warnings
from enum import IntEnum

import numpy as np
import typecheck as tc

from psyneulink.components.component import function_type, method_type
# import Components
# FIX: EVCControlMechanism IS IMPORTED HERE TO DEAL WITH COST FUNCTIONS THAT ARE DEFINED IN EVCControlMechanism
#            SHOULD THEY BE LIMITED TO EVC??
from psyneulink.components.functions.function import CombinationFunction, Exponential, IntegratorFunction, Linear, Reduce, SimpleIntegrator, TransferFunction, _is_modulation_param, is_function_type
from psyneulink.components.shellclasses import Function
from psyneulink.components.states.modulatorysignals.modulatorysignal import ModulatorySignal
from psyneulink.components.states.outputstate import SEQUENTIAL
from psyneulink.components.states.state import State_Base
from psyneulink.globals.context import ContextFlags
from psyneulink.globals.defaults import defaultControlAllocation
from psyneulink.globals.keywords import ALLOCATION_SAMPLES, AUTO, COMMAND_LINE, CONTROLLED_PARAMS, CONTROL_PROJECTION, CONTROL_SIGNAL, OFF, ON, OUTPUT_STATE_PARAMS, PARAMETER_STATE, PARAMETER_STATES, PROJECTION_TYPE, RECEIVER, SUM
from psyneulink.globals.preferences.componentpreferenceset import is_pref_set
from psyneulink.globals.preferences.preferenceset import PreferenceLevel
from psyneulink.globals.utilities import is_numeric, iscompatible, kwCompatibilityLength, kwCompatibilityNumeric, kwCompatibilityType

__all__ = [
    'ADJUSTMENT_COST', 'ADJUSTMENT_COST_FUNCTION', 'ControlSignal', 'ControlSignalCosts', 'ControlSignalError',
    'COST_COMBINATION_FUNCTION', 'COST_OPTIONS', 'costFunctionNames', 'DURATION_COST',
    'DURATION_COST_FUNCTION', 'INTENSITY_COST', 'INTENSITY_COST_FUNCTION', 'kpAdjustmentCost', 'kpAllocation', 'kpCost',
    'kpCostRange', 'kpDurationCost', 'kpIntensity', 'kpIntensityCost',
]

# class OutputStateLog(IntEnum):
#     NONE            = 0
#     TIME_STAMP      = 1 << 0
#     ALL = TIME_STAMP
#     DEFAULTS = NONE


# -------------------------------------------    KEY WORDS  -------------------------------------------------------

# ControlSignal Costs
INTENSITY_COST = 'INTENSITY COST'
ADJUSTMENT_COST = 'ADJUSTMENT COST'
DURATION_COST = 'DURATION COST'

# ControlSignal Cost Function Names
INTENSITY_COST_FUNCTION = 'intensity_cost_function'
ADJUSTMENT_COST_FUNCTION = 'adjustment_cost_function'
DURATION_COST_FUNCTION = 'duration_cost_function'
COST_COMBINATION_FUNCTION = 'cost_combination_function'
costFunctionNames = [INTENSITY_COST_FUNCTION,
                     ADJUSTMENT_COST_FUNCTION,
                     DURATION_COST_FUNCTION,
                     COST_COMBINATION_FUNCTION]

# Attributes / KVO keypaths
# kpLog = "Control Signal Log"
kpAllocation = "Control Signal Allocation"
kpIntensity = "Control Signal Intensity"
kpCostRange = "Control Signal Cost Range"
kpIntensityCost = "Control Signal Intensity Cost"
kpAdjustmentCost = "Control Signal Adjustment Cost"
kpDurationCost = "Control Signal duration_cost"
kpCost = "Control Signal Cost"

COST_OPTIONS = 'cost_options'
class ControlSignalCosts(IntEnum):
    """Options for selecting `cost functions <ControlSignal_Costs>` to be used by a ControlSignal.

    These can be used alone or in combination with one another, by `enabling or disabling <_ControlSignal_Toggle_Costs>`
    each using the ControlSignal's `toggle_cost_function` method.

    Attributes
    ----------

    NONE
        ControlSignal's `cost` is not computed.

    INTENSITY_COST
        `intensity_cost_function` is used to calculate a contribution to the ControlSignal's `cost
        <ControlSignal.cost>` based its current `intensity` value.

    ADJUSTMENT_COST
        `adjustment_cost_function` is used to calculate a contribution to the `cost` based on the change in its
        `intensity` from its last value.

    DURATION_COST
        `duration_cost_function` is used to calculate a contribitution to the `cost` based on an integral of the
        ControlSignal's `cost <ControlSignal.cost>` (i.e., it accumulated value over multiple executions).

    ALL
        all of the `cost functions <ControlSignal_Costs> are used to calculate the ControlSignal's
        `cost <ControlSignal.cost>`.

    DEFAULTS
        assign default set of `cost functions <ControlSignal_Costs>` (currently set to `INTENSITY_COST`).

    """
    NONE               = 0
    INTENSITY_COST     = 1 << 1
    ADJUSTMENT_COST    = 1 << 2
    DURATION_COST      = 1 << 3
    ALL                = INTENSITY_COST | ADJUSTMENT_COST | DURATION_COST
    DEFAULTS           = INTENSITY_COST


class ControlSignalError(Exception):
    def __init__(self, error_value):
        self.error_value = error_value


    def __str__(self):
        return repr(self.error_value)



class ControlSignal(ModulatorySignal):
    """
    ControlSignal(                                                \
        owner,                                                    \
        index=SEQUENTIAL,                                         \
        function=Linear(),                                        \
        costs_options=None,                                       \
        intensity_cost_function=Exponential,                      \
        adjustment_cost_function=Linear,                          \
        duration_cost_function=Integrator,                        \
        cost_combination_function=Reduce(operation=SUM),          \
        allocation_samples=self.ClassDefaults.allocation_samples, \
        modulation=ModulationParam.MULTIPLICATIVE                 \
        projections=None                                          \
        params=None,                                              \
        name=None,                                                \
        prefs=None)

    A subclass of `ModulatorySignal <ModulatorySignal>` used by a `ControlMechanism <ControlMechanism>` to
    modulate the parameter(s) of one or more other `Mechanisms <Mechanism>`.

    COMMENT:

        Description
        -----------
            The ControlSignal class is a subtype of the OutputState type in the State category of Component,
            It is used as the sender for ControlProjections
            Its FUNCTION updates its value:
                note:  currently, this is the identity function, that simply maps variable to self.value

        Class attributes:
            + componentType (str) = CONTROL_SIGNAL
            + paramClassDefaults (dict)
                + FUNCTION (Linear)
                + FUNCTION_PARAMS   (Operation.PRODUCT)

        Class methods:
            function (executes function specified in params[FUNCTION];  default: Linear)

        StateRegistry
        -------------
            All OutputStates are registered in StateRegistry, which maintains an entry for the subclass,
              a count for all instances of it, and a dictionary of those instances
    COMMENT


    Arguments
    ---------

    owner : ControlMechanism
        specifies the `ControlMechanism <ControlMechanism>` to which to assign the ControlSignal.

    index : int : default SEQUENTIAL
        specifies the item of the owner ControlMechanism's `allocation_policy <ControlMechanism.allocation_policy>`
        used as the ControlSignal's `value <ControlSignal.value>`.

    function : Function or method : default Linear
        specifies the function used to determine the `intensity` of the ControlSignal from its `allocation`.

    cost_options : ControlSignalCosts or List[ControlSignalCosts] : None
        specifies the cost components to include in the computation of the ControlSignal's `cost <ControlSignal.cost>`.

    intensity_cost_function : Optional[TransferFunction] : default Exponential
        specifies the function used to calculate the contribution of the ControlSignal's `intensity` to its
        `cost <ControlSignal.cost>`.

    adjustment_cost_function : Optional[TransferFunction] : default Linear
        specifies the function used to calculate the contribution of the change in the ControlSignal's `intensity`
        (from its `last_intensity` value) to its `cost <ControlSignal.cost>`.

    duration_cost_function : IntegratorFunction : default Integrator
        specifies the function used to calculate the contribution of the ControlSignal's duration to its
        `cost <ControlSignal.cost>`.

    cost_combination_function : function : default `Reduce(operation=SUM) <Function.Reduce>`
        specifies the function used to combine the results of any cost functions that are enabled, the result of
        which is assigned as the ControlSignal's `cost <ControlSignal.cost>` attribute.

    allocation_samples : list : default range(0.1, 1, 0.1)
        specifies the values used by `ControlSignal's `ControlSignal.owner` to determine its
        `allocation_policy <ControlMechanism.allocation_policy>` (see `ControlSignal_Execution`).

    modulation : ModulationParam : default ModulationParam.MULTIPLICATIVE
        specifies the way in which the `value <ControlSignal.value>` the ControlSignal is used to modify the value of
        the parameter(s) that it controls.

    projections : list of Projection specifications
        specifies the `ControlProjection(s) <ControlProjection>` to be assigned to the ControlSignal, and that will be
        listed in its `efferents <ControlSignal.efferents>` attribute (see `ControlSignal_Projections` for additional
        details).

    params : Dict[param keyword: param value] : default None
        a `parameter dictionary <ParameterState_Specification>` that can be used to specify the parameters for
        the ControlSignal and/or a custom function and its parameters. Values specified for parameters in the dictionary
        override any assigned to those parameters in arguments of the constructor.

    name : str : default see ModulatorySignal `name <ModulatorySignal.name>`
        specifies the name of the ControlSignal; see ControlSignal `name <ModulatorySignal.name>` for additional
        details.

    prefs : PreferenceSet or specification dict : default State.classPreferences
        specifies the `PreferenceSet` for the ControlSignal; see `prefs <ControlSignal.prefs>` for details.


    Attributes
    ----------

    owner : ControlMechanism
        the `ControlMechanism <ControlMechanism>` to which the ControlSignal belongs.

    variable : number, list or np.ndarray
        same as `allocation <ControlSignal.allocation>`;  used by `function <ControlSignal.function>` to compute the
        ControlSignal's `intensity`.

    allocation : float : default: defaultControlAllocation
        value used as `variable <ControlSignal.variable>` for the ControlSignal's `function <ControlSignal.function>`
        to determine its `intensity`.

    last_allocation : float
        value of `allocation` in the previous execution of ControlSignal's `owner <ControlSignal.owner>`.

    allocation_samples : list : DEFAULT_SAMPLE_VALUES
        set of values to sample by the ControlSignal's `owner <ControlSignal.owner>` to determine its
        `allocation_policy <ControlMechanism.allocation_policy>`.

    function : TransferFunction :  default Linear(slope=1, intercept=0)
        converts `allocation` into the ControlSignal's `intensity`.  The default is the identity function, which
        assigns the ControlSignal's `allocation` as its `intensity`.

    value : float
        result of the ControlSignal's `function <ControlSignal.function>`; same as `intensity` and `control_signal`.

    intensity : float
        result of the ControlSignal's `function <ControlSignal.function>`;
        assigned as the value of the ControlSignal's ControlProjection, and used to modify the value of the parameter
        to which the ControlSignal is assigned; same as `control_signal <ControlSignal.control_signal>`.

    last_intensity : float
        the `intensity` of the ControlSignal on the previous execution of its `owner <ControlSignal.owner>`.

    index : int
        the item of the owner ControlMechanism's `allocation_policy <ControlMechanism.allocation_policy>` used as the
        ControlSignal's `value <ControlSignal.value>`.

    control_signal : float
        result of the ControlSignal's `function <ControlSignal.function>`; same as `intensity`.

    cost_options : ControlSignalCosts or None
        boolean combination of currently assigned ControlSignalCosts. Specified initially in **costs** argument of
        ControlSignal's constructor;  can be modified using the `assign_cost_options` method.

    intensity_cost_function : TransferFunction : default default Exponential
        calculates `intensity_cost` from the current value of `intensity`. It can be any `TransferFunction`, or any
        other function that takes and returns a scalar value. The default is `Exponential`.  It can be disabled
        permanently for the ControlSignal by assigning `None`.

    intensity_cost : float
        cost associated with the current `intensity`.

    adjustment_cost_function : TransferFunction : default Linear
        calculates `adjustment_cost` based on the change in `intensity` from  `last_intensity`.  It can be any
        `TransferFunction`, or any other function that takes and returns a scalar value. It can be disabled
        permanently for the ControlSignal by assigning `None`.

    adjustment_cost : float
        cost associated with last change to `intensity`.

    duration_cost_function : IntegratorFunction : default Linear
        calculates an integral of the ControlSignal's `cost`.  It can be any `IntegratorFunction`, or any other
        function that takes a list or array of two values and returns a scalar value. It can be disabled permanently
        for the ControlSignal by assigning `None`.

    duration_cost : float
        intregral of `cost`.

    cost_combination_function : function : default Reduce(operation=SUM)
        combines the results of all cost functions that are enabled, and assigns the result to `cost`.
        It can be any function that takes an array and returns a scalar value.

    cost : float
        combined result of all `cost functions <ControlSignal_Costs>` that are enabled.

    modulation : ModulationParam
        specifies the way in which the `value <ControlSignal.value>` the ControlSignal is used to modify the value of
        the parameter(s) that it controls.

    efferents : [List[ControlProjection]]
        a list of the `ControlProjections <ControlProjection>` assigned to (i.e., that project from) the ControlSignal.

    name : str
        name of the ControlSignal; if it is not specified in the **name** argument of its constructor, a default name
        is assigned (see `name <ModulatorySignal.name>`).

        .. note::
            Unlike other PsyNeuLink components, State names are "scoped" within a Mechanism, meaning that States with
            the same name are permitted in different Mechanisms.  However, they are *not* permitted in the same
            Mechanism: States within a Mechanism with the same base name are appended an index in the order of their
            creation.

    prefs : PreferenceSet or specification dict
        the `PreferenceSet` for the ControlSignal; if it is not specified in the **prefs** argument of the constructor,
        a default is assigned using `classPreferences` defined in __init__.py (see :doc:`PreferenceSet <LINK>` for
        details).

    """

    #region CLASS ATTRIBUTES

    componentType = CONTROL_SIGNAL
    paramsType = OUTPUT_STATE_PARAMS

    class _DefaultsAliases(ModulatorySignal._DefaultsAliases):
        # alias allocation to variable for user convenience
        # NOTE: should not be used internally for consistency
        @property
        def allocation(self):
            return self.variable

        @allocation.setter
        def allocation(self, value):
            self.variable = value

    class _DefaultsMeta(ModulatorySignal._DefaultsMeta, _DefaultsAliases):
        pass

    class ClassDefaults(ModulatorySignal.ClassDefaults, metaclass=_DefaultsMeta):
        variable = defaultControlAllocation
        allocation_samples = np.arange(0.1, 1.01, 0.3)

    class InstanceDefaults(ModulatorySignal.InstanceDefaults, _DefaultsAliases):
        pass

    stateAttributes = ModulatorySignal.stateAttributes | {ALLOCATION_SAMPLES}

    connectsWith = [PARAMETER_STATE]
    connectsWithAttribute = [PARAMETER_STATES]
    projectionSocket = RECEIVER
    modulators = []

    classPreferenceLevel = PreferenceLevel.TYPE
    # Any preferences specified below will override those specified in TypeDefaultPreferences
    # Note: only need to specify setting;  level will be assigned to TYPE automatically
    # classPreferences = {
    #     kwPreferenceSetName: 'OutputStateCustomClassPreferences',
    #     kp<pref>: <setting>...}

    paramClassDefaults = State_Base.paramClassDefaults.copy()
    # paramClassDefaults = OutputState.paramClassDefaults.copy()
    paramClassDefaults.update({
        PROJECTION_TYPE: CONTROL_PROJECTION,
        CONTROLLED_PARAMS:None
    })
    #endregion


    @tc.typecheck
    def __init__(self,
                 owner=None,
                 reference_value=None,
                 variable=None,
                 size=None,
                 index=None,
                 assign=None,
                 function=Linear(),
                 cost_options:tc.optional(tc.any(ControlSignalCosts, list))=None,
                 intensity_cost_function:(is_function_type)=Exponential,
                 adjustment_cost_function:tc.optional(is_function_type)=Linear,
                 duration_cost_function:tc.optional(is_function_type)=SimpleIntegrator,
                 cost_combination_function:tc.optional(is_function_type)=Reduce(operation=SUM),
                 allocation_samples=ClassDefaults.allocation_samples,
                 modulation:tc.optional(_is_modulation_param)=None,
                 projections=None,
                 params=None,
                 name=None,
                 prefs:is_pref_set=None,
                 context=None):

        if context is None:
            context = ContextFlags.COMMAND_LINE
            self.context.source = ContextFlags.COMMAND_LINE
        else:
            context = ContextFlags.CONSTRUCTOR
            self.context.source = ContextFlags.CONSTRUCTOR

        # Note index and assign are not used by ControlSignal, but included here for consistency with OutputState
        if params and ALLOCATION_SAMPLES in params and params[ALLOCATION_SAMPLES] is not None:
            allocation_samples =  params[ALLOCATION_SAMPLES]

        # Note: assign is not currently used by GatingSignal;
        #       it is included here for consistency with OutputState and possible use by subclasses.

        # If index has not been specified, but the owner has, allocation_policy has been determined, so use that
        index = index or SEQUENTIAL

        # Assign args to params and functionParams dicts (kwConstants must == arg names)
        params = self._assign_args_to_param_dicts(function=function,
                                                  cost_options=cost_options,
                                                  intensity_cost_function=intensity_cost_function,
                                                  adjustment_cost_function=adjustment_cost_function,
                                                  duration_cost_function=duration_cost_function,
                                                  cost_combination_function=cost_combination_function,
                                                  allocation_samples=allocation_samples,
                                                  params=params)

        # IMPLEMENTATION NOTE:
        # Consider adding self to owner.output_states here (and removing from ControlProjection._instantiate_sender)
        #  (test for it, and create if necessary, as per OutputStates in ControlProjection._instantiate_sender),

        # Validate sender (as variable) and params, and assign to variable and paramInstanceDefaults
        super().__init__(owner=owner,
                         reference_value=reference_value,
                         variable=variable,
                         size=size,
                         modulation=modulation,
                         index=index,
                         assign=None,
                         projections=projections,
                         params=params,
                         name=name,
                         prefs=prefs,
                         context=context,
                         function=function,
                         )

        # Default cost params
        if self.context.initialization_status != ContextFlags.DEFERRED_INIT:
            self.intensity_cost = self.intensity_cost_function(self.instance_defaults.allocation)
        else:
            self.intensity_cost = self.intensity_cost_function(self.ClassDefaults.allocation)
        self.adjustment_cost = 0
        self.duration_cost = 0
        self.last_duration_cost = self.duration_cost
        self.cost = self.intensity_cost
        self.last_cost = self.cost

    def _validate_params(self, request_set, target_set=None, context=None):
        """Validate allocation_samples and control_signal cost functions

        Checks if:
        - cost functions are all appropriate
        - allocation_samples is a list or 1d np.array
        - all cost functions are references to valid ControlProjection costFunctions (listed in self.costFunctions)

        """

        # Validate cost functions in request_set
        #   This should be all of them if this is an initialization call;
        #   Otherwise, just those specified in assign_params
        for cost_function_name in [item for item in request_set if item in costFunctionNames]:
            cost_function = request_set[cost_function_name]

            # cost function assigned None: OK
            if not cost_function:
                continue

            # cost_function is Function class specification:
            #    instantiate it and test below
            if inspect.isclass(cost_function) and issubclass(cost_function, Function):
                cost_function = cost_function()

            # cost_function is Function object:
            #     COST_COMBINATION_FUNCTION must be CombinationFunction
            #     DURATION_COST_FUNCTION must be an IntegratorFunction
            #     others must be TransferFunction
            if isinstance(cost_function, Function):
                if cost_function_name == COST_COMBINATION_FUNCTION:
                    if not isinstance(cost_function, CombinationFunction):
                        raise ControlSignalError("Assignment of Function to {} ({}) must be a CombinationFunction".
                                                 format(COST_COMBINATION_FUNCTION, cost_function))
                elif cost_function_name == DURATION_COST_FUNCTION:
                    if not isinstance(cost_function, IntegratorFunction):
                        raise ControlSignalError("Assignment of Function to {} ({}) must be an IntegratorFunction".
                                                 format(DURATION_COST_FUNCTION, cost_function))
                elif not isinstance(cost_function, TransferFunction):
                    raise ControlSignalError("Assignment of Function to {} ({}) must be a TransferFunction".
                                             format(cost_function_name, cost_function))

            # cost_function is custom-specified function
            #     DURATION_COST_FUNCTION and COST_COMBINATION_FUNCTION must accept an array
            #     others must accept a scalar
            #     all must return a scalar
            elif isinstance(cost_function, (function_type, method_type)):
                if cost_function_name in COST_COMBINATION_FUNCTION:
                    test_value = [1, 1]
                else:
                    test_value = 1
                try:
                    result = cost_function(test_value)
                    if not (is_numeric(result) or is_numeric(np.asscalar(result))):
                        raise ControlSignalError("Function assigned to {} ({}) must return a scalar".
                                                 format(cost_function_name, cost_function))
                except:
                    raise ControlSignalError("Function assigned to {} ({}) must accept {}".
                                             format(cost_function_name, cost_function, type(test_value)))

            # Unrecognized function assignment
            else:
                raise ControlSignalError("Unrecognized function ({}) assigned to {}".
                                         format(cost_function, cost_function_name))

        # Validate allocation samples list:
        # - default is 1D np.array (defined by self.ClassDefaults.allocation_samples)
        # - however, for convenience and compatibility, allow lists:
        #    check if it is a list of numbers, and if so convert to np.array
        if ALLOCATION_SAMPLES in request_set:
            allocation_samples = request_set[ALLOCATION_SAMPLES]
            if isinstance(allocation_samples, list):
                if iscompatible(allocation_samples, **{kwCompatibilityType: list,
                                                           kwCompatibilityNumeric: True,
                                                           kwCompatibilityLength: False,
                                                           }):
                    # Convert to np.array to be compatible with default value
                    request_set[ALLOCATION_SAMPLES] = np.array(allocation_samples)
            elif isinstance(allocation_samples, np.ndarray) and allocation_samples.ndim == 1:
                pass
            else:
                raise ControlSignalError("allocation_samples argument ({}) in {} must be "
                                             "a list or 1D np.array of numbers".
                                         format(allocation_samples, self.name))

        super()._validate_params(request_set=request_set, target_set=target_set, context=context)

        # ControlProjection Cost Functions
        for cost_function_name in [item for item in target_set if item in costFunctionNames]:
            cost_function = target_set[cost_function_name]
            if not cost_function:
                continue
            if ((not isinstance(cost_function, (Function, function_type, method_type)) and
                     not issubclass(cost_function, Function))):
                raise ControlSignalError("{0} not a valid Function".format(cost_function))

    def _instantiate_attributes_before_function(self, function=None, context=None):

        super()._instantiate_attributes_before_function(function=function, context=context)

        # Instantiate cost functions (if necessary) and assign to attributes
        for cost_function_name in costFunctionNames:
            cost_function = self.paramsCurrent[cost_function_name]
            # cost function assigned None
            if not cost_function:
                self.toggle_cost_function(cost_function_name, OFF)
                continue
            # cost_function is Function class specification
            if inspect.isclass(cost_function) and issubclass(cost_function, Function):
                cost_function = cost_function()
            # cost_function is Function object
            if isinstance(cost_function, Function):
                cost_function.owner = self
                cost_function = cost_function.function
            # cost_function is custom-specified function
            elif isinstance(cost_function, function_type):
                pass
            # safeguard/sanity check (should never happen if validation is working properly)
            else:
                raise ControlSignalError("{} is not a valid cost function for {}".
                                         format(cost_function, cost_function_name))

            self.paramsCurrent[cost_function_name] = cost_function

        # Assign instance attributes
        self.allocation_samples = self.paramsCurrent[ALLOCATION_SAMPLES]

    def _parse_state_specific_specs(self, owner, state_dict, state_specific_spec):
        """Get ControlSignal specified for a parameter or in a 'control_signals' argument

        Tuple specification can be:
            (parameter name, Mechanism)
            [TBI:] (Mechanism, parameter name, weight, exponent, projection_specs)

        Returns params dict with CONNECTIONS entries if any of these was specified.

        """
        from psyneulink.components.projections.projection import _parse_connection_specs
        from psyneulink.globals.keywords import PROJECTIONS

        params_dict = {}
        state_spec = state_specific_spec

        if isinstance(state_specific_spec, dict):
            return None, state_specific_spec

        elif isinstance(state_specific_spec, tuple):

            # # In this format there is no explicit State spec;  it is the Projection (parsed below)
            # state_spec = None
            #
            # try:
            #     param_item, mech_item = state_specific_spec
            # except:
            #     raise ControlSignalError("Illegal {} specification tuple for {} ({});  "
            #                              "it must contain two items: (<param_name>, <{}>)".
            #                              format(ControlSignal.__name__, owner.name,
            #                                     state_specific_spec, Mechanism.__name__))
            # if not isinstance(mech_item, Mechanism):
            #     raise ControlSignalError("Second item of the {} specification tuple for {} ({}) must be a Mechanism".
            #                              format(ControlSignal.__name__, owner.name, mech, mech.name))
            #
            # param_specs = param_item if isinstance(param_item, list) else [param_item]
            # param_list = []
            # for param_name in param_specs:
            #
            #     if not isinstance(param_name, str):
            #         raise ControlSignalError("First item of the {} specification tuple for {} ({}) must be a string "
            #                                  "that is the name of a parameter of its second item ({})".
            #                                  format(ControlSignal.__name__, owner.name, param_name, mech_item.name))
            #     try:
            #         parameter_state = mech_item.parameter_states[param_name]
            #     except KeyError:
            #         raise ControlSignalError("No {} found for {} param of {} in {} specification tuple for {}".
            #                                  format(ParameterState.__name__, param_name, mech_item.name,
            #                                         ControlSignal.__name__, owner.name))
            #     except AttributeError:
            #         raise ControlSignalError("{} does not have any {} specified, so can't"
            #                                  "assign {} specified for {} ({})".
            #                                  format(mech_item.name, ParameterState.__name__, ControlSignal.__name__,
            #                                         owner.name, state_specific_spec))
            #     param_list.append(parameter_state)
            #
            # # Assign connection specs to PROJECTIONS entry of params dict
            # try:
            #     params_dict[PROJECTIONS] = _parse_connection_specs(self,
            #                                                        owner=owner,
            #                                                        connections=param_list)
            # except ControlSignalError:
            #     raise ControlSignalError("Unable to parse {} specification dictionary for {} ({})".
            #                                 format(ControlSignal.__name__, owner.name, state_specific_spec))
            state_spec = None
            params_dict[PROJECTIONS] = _parse_connection_specs(connectee_state_type=self,
                                                               owner=owner,
                                                               connections=state_specific_spec)

        elif state_specific_spec is not None:
            raise ControlSignalError("PROGRAM ERROR: Expected tuple or dict for {}-specific params but, got: {}".
                                  format(self.__class__.__name__, state_specific_spec))

        if params_dict[PROJECTIONS] is None:
            raise ControlSignalError("PROGRAM ERROR: No entry found in {} params dict for {} "
                                     "with specification of parameter's Mechanism or ControlProjection(s) to it".
                                        format(CONTROL_SIGNAL, owner.name))

        return state_spec, params_dict

    def update(self, params=None, context=None):
        super().update(params=params, context=context)
        if self.cost_options:
            self._compute_costs()

    def _compute_costs(self):
        """Compute costs based on self.value."""

        intensity = self.value

        try:
            intensity_change = intensity-self.last_intensity
        except AttributeError:
            intensity_change = 0

        if self.prefs.verbosePref:
            intensity_change_string = "no change"
            if intensity_change < 0:
                intensity_change_string = "-" + str(intensity_change)
            elif intensity_change > 0:
                intensity_change_string = "+" + str(intensity_change)
            if self.prefs.verbosePref:
                warnings.warn("\nAllocation: {0} [{1}]".format(intensity, intensity_change_string))

        # compute cost(s)
        intensity_cost = adjustment_cost = duration_cost = 0

        if self.cost_options & ControlSignalCosts.INTENSITY_COST:
            intensity_cost = self.intensity_cost = self.intensity_cost_function(intensity)
            if self.prefs.verbosePref:
                print("++ Used intensity cost")

        if self.cost_options & ControlSignalCosts.ADJUSTMENT_COST:
            adjustment_cost = self.adjustment_cost = self.adjustment_cost_function(intensity_change)
            if self.prefs.verbosePref:
                print("++ Used adjustment cost")

        # FIX: 12/23/17 - THIS NEEDS TO HAVE BEEN INITIALIZED
        if self.cost_options & ControlSignalCosts.DURATION_COST:
            duration_cost = self.duration_cost = self.duration_cost_function(self.cost)
            if self.prefs.verbosePref:
                print("++ Used duration cost")

        self.cost = max(0.0, self.cost_combination_function([float(intensity_cost),
                                                             adjustment_cost,
                                                             duration_cost]))

        # Store current state for use in next call as last state
        self.last_intensity = intensity
        self.last_cost = self.cost
        self.last_duration_cost = self.duration_cost

        # Report new values to stdio
        if self.prefs.verbosePref:
            try:
                cost_change = self.cost - self.last_cost
            except AttributeError:
                cost_change = 0
            cost_change_string = "no change"
            if cost_change < 0:
                cost_change_string = str(cost_change)
            elif cost_change > 0:
                cost_change_string = "+" + str(cost_change)
            print("Cost: {0} [{1}])".format(self.cost, cost_change_string))

    @property
    def allocation_samples(self):
        return self._allocation_samples

    @allocation_samples.setter
    def allocation_samples(self, samples):
        if isinstance(samples, (list, np.ndarray)):
            self._allocation_samples = list(samples)
            return
        if isinstance(samples, tuple):
            self._allocation_samples = samples
            sample_range = samples
        elif samples == AUTO:

            # (7/21/17 CW) Note that since the time of writing this "stub", the value of AUTO in Keywords.py has changed
            # from True to "auto" due to the addition of "auto" as a parameter for RecurrentTransferMechanisms! Just FYI

            # THIS IS A STUB, TO BE REPLACED BY AN ACTUAL COMPUTATION OF THE ALLOCATION RANGE
            raise ControlSignalError("AUTO not yet supported for {} param of ControlProjection; default will be used".
                                     format(ALLOCATION_SAMPLES))
        else:
            sample_range = self.ClassDefaults.allocation_samples
        self._allocation_samples = []
        i = sample_range[0]
        while i < sample_range[1]:
            self._allocation_samples.append(i)
            i += sample_range[2]

    @property
    def intensity(self):
        return self._intensity

    @intensity.setter
    def intensity(self, new_value):
        self._intensity = new_value

    @property
    def control_signal(self):
        return self.value

    @tc.typecheck
    def assign_costs(self, costs:tc.any(ControlSignalCosts, list)):
        """assign_costs(costs)
        Assigns specified costs; all others are disabled.

        Arguments
        ---------
        costs: ControlSignalCost or List[ControlSignalCosts]
            cost or list of costs to be used;  all other will be disabled.
        Returns
        -------
        cost_options :  boolean combination of ControlSignalCosts
            current value of `cost_options`.

        """
        if isinstance(costs, ControlSignalCosts):
            costs = [costs]
        self.cost_options = ControlSignalCosts.NONE
        return self.enable_costs(costs)

    @tc.typecheck
    def enable_costs(self, costs:tc.any(ControlSignalCosts, list)):
        """enable_costs(costs)
        Enables specified costs; settings for all other costs are left intact.

        Arguments
        ---------
        costs: ControlSignalCost or List[ControlSignalCosts]
            cost or list of costs to be enabled, in addition to any that are already enabled.
        Returns
        -------
        cost_options :  boolean combination of ControlSignalCosts
            current value of `cost_options`.

        """
        if isinstance(costs, ControlSignalCosts):
            options = [costs]
        for cost in costs:
            self.cost_options |= cost
        return self.cost_options

    @tc.typecheck
    def disable_costs(self, costs:tc.any(ControlSignalCosts, list)):
        """disable_costs(costs)
        Disables specified costs; settings for all other costs are left intact.

        Arguments
        ---------
        costs: ControlSignalCost or List[ControlSignalCosts]
            cost or list of costs to be disabled.
        Returns
        -------
        cost_options :  boolean combination of ControlSignalCosts
            current value of `cost_options`.

        """
        if isinstance(costs, ControlSignalCosts):
            options = [costs]
        for cost in costs:
            self.cost_options &= ~cost
        return self.cost_options

    def get_cost_options(self):
        options = []
        if self.cost_options & ControlSignalCosts.INTENSITY_COST:
            options.append(INTENSITY_COST)
        if self.cost_options & ControlSignalCosts.ADJUSTMENT_COST:
            options.append(ADJUSTMENT_COST)
        if self.cost_options & ControlSignalCosts.DURATION_COST:
            options.append(DURATION_COST)
        return

    def toggle_cost_function(self, cost_function_name, assignment=ON):
        """Enables/disables use of a cost function.

        ``cost_function_name`` should be a keyword (list under :ref:`Structure <ControlProjection_Structure>`).
        """
        if cost_function_name == INTENSITY_COST_FUNCTION:
            cost_option = ControlSignalCosts.INTENSITY_COST
        elif cost_function_name == DURATION_COST_FUNCTION:
            cost_option = ControlSignalCosts.DURATION_COST
        elif cost_function_name == ADJUSTMENT_COST_FUNCTION:
            cost_option = ControlSignalCosts.ADJUSTMENT_COST
        elif cost_function_name == COST_COMBINATION_FUNCTION:
            raise ControlSignalError("{} cannot be disabled".format(COST_COMBINATION_FUNCTION))
        else:
            raise ControlSignalError("toggle_cost_function: unrecognized cost function: {}".format(cost_function_name))

        if assignment:
            if not self.paramsCurrent[cost_function_name]:
                raise ControlSignalError("Unable to toggle {} ON as function assignment is \'None\'".
                                         format(cost_function_name))
            self.cost_options |= cost_option
        else:
            self.cost_options &= ~cost_option

    # def set_intensity_cost(self, assignment=ON):
    #     if assignment:
    #         self.control_signal_cost_options |= ControlSignalCosts.INTENSITY_COST
    #     else:
    #         self.control_signal_cost_options &= ~ControlSignalCosts.INTENSITY_COST
    #
    # def set_adjustment_cost(self, assignment=ON):
    #     if assignment:
    #         self.control_signal_cost_options |= ControlSignalCosts.ADJUSTMENT_COST
    #     else:
    #         self.control_signal_cost_options &= ~ControlSignalCosts.ADJUSTMENT_COST
    #
    # def set_duration_cost(self, assignment=ON):
    #     if assignment:
    #         self.control_signal_cost_options |= ControlSignalCosts.DURATION_COST
    #     else:
    #         self.control_signal_cost_options &= ~ControlSignalCosts.DURATION_COST
    #
    def get_costs(self):
        """Return three-element list with the values of ``intensity_cost``, ``adjustment_cost`` and ``duration_cost``
        """
        return [self.intensity_cost, self.adjustment_cost, self.duration_cost]

    # @property
    # def variable(self):
    #     return self.allocation
    #
    # @variable.setter
    # def variable(self, assignment):
    #     self.allocation = assignment

    @property
    def value(self):
        # In case the ControlSignal has not yet been assigned (and its value is INITIALIZING or DEFERRED_INITIALIZATION
        if self.context.initialization_status & (ContextFlags.DEFERRED_INIT | ContextFlags.INITIALIZING):
            return None
        else:
            return self._value

    @value.setter
    def value(self, assignment):
        self._value = assignment
        self.log._log_value(assignment)

    @property
    def intensity(self):
        return self.value
