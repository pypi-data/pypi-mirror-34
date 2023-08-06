The Fast Network Simulation Setup (FNSS) core library is
a Python library providing a set of features allowing network researchers and
engineers to simplify the setup of a network experiment.

These features include the ability to:

* Parse a topology from a dataset, a topology generator or generate it
  according to a number of synthetic models.
* Apply link capacities, link weights, link delays and buffer sizes.
* Deploy protocol stacks and applications on network nodes.
* Generate traffic matrices.
* Generate event schedules.

The core library allows users to export the generated scenarios (topologies,
traffic matrices and event schedules) to ns-2, Mininet or AutoNetKit.

It also allows to save scenarios in XML files, which can be later imported
by the FNSS Java, C++ and ns-3 libraries.


