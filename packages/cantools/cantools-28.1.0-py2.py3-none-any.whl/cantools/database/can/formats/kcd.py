# Load and dump a CAN database in KCD format.
import logging

from xml.etree import ElementTree

from ..signal import Signal
from ..message import Message
from ..node import Node
from ..bus import Bus
from ..internal_database import InternalDatabase
from ...utils import start_bit
from .utils import num


LOGGER = logging.getLogger(__name__)

# The KCD XML namespace.
NAMESPACE = 'http://kayak.2codeornot2code.org/1.0'
NAMESPACES = {'ns': NAMESPACE}

ROOT_TAG = '{{{}}}NetworkDefinition'.format(NAMESPACE)


def _start_bit(offset, byte_order):
    if byte_order == 'big_endian':
        return (8 * (offset // 8) + (7 - (offset % 8)))
    else:
        return offset


def _get_node_name_by_id(nodes, node_id):
    for node in nodes:
        if node['id'] == node_id:
            return node['name']


def _load_signal_element(signal):
    """Load given signal element and return a signal object.

    """

    # Default values.
    name = None
    offset = None
    length = 1
    byte_order = 'little_endian'
    is_signed = False
    is_float = False
    minimum = None
    maximum = None
    slope = 1
    intercept = 0
    unit = None
    labels = None
    notes = None

    # Signal XML attributes.
    for key, value in signal.attrib.items():
        if key == 'name':
            name = value
        elif key == 'offset':
            offset = int(value)
        elif key == 'length':
            length = int(value)
        elif key == 'endianess':
            byte_order = '{}_endian'.format(value)
        else:
            LOGGER.debug("Ignoring unsupported signal attribute '%s'.", key)

    # Value XML element.
    value = signal.find('ns:Value', NAMESPACES)

    if value is not None:
        for key, value in value.attrib.items():
            if key == 'min':
                minimum = num(value)
            elif key == 'max':
                maximum = num(value)
            elif key == 'slope':
                slope = num(value)
            elif key == 'intercept':
                intercept = num(value)
            elif key == 'unit':
                unit = value
            elif key == 'type':
                is_signed = (value == 'signed')
                is_float = (value in ['single', 'double'])
            else:
                LOGGER.debug("Ignoring unsupported signal value attribute '%s'.",
                             key)

    # Notes.
    try:
        notes = signal.find('ns:Notes', NAMESPACES).text
    except AttributeError:
        pass

    # Label set XML element.
    label_set = signal.find('ns:LabelSet', NAMESPACES)

    if label_set is not None:
        labels = {}

        for label in label_set.findall('ns:Label', NAMESPACES):
            label_value = int(label.attrib['value'])
            label_name = label.attrib['name']
            labels[label_value] = label_name

        # TODO: Label groups.

    return Signal(name=name,
                  start=_start_bit(offset, byte_order),
                  length=length,
                  receivers=[],
                  byte_order=byte_order,
                  is_signed=is_signed,
                  scale=slope,
                  offset=intercept,
                  minimum=minimum,
                  maximum=maximum,
                  unit=unit,
                  choices=labels,
                  comment=notes,
                  is_float=is_float)


def _load_multiplex_element(mux):
    """Load given multiplex elements and its signals and return list of signals.

    """

    mux_signal = _load_signal_element(mux)
    mux_signal.is_multiplexer = True
    signals = [mux_signal]

    for mux_group in mux.findall('ns:MuxGroup', NAMESPACES):
        multiplexer_id = mux_group.attrib['count']

        for signal_element in mux_group.findall('ns:Signal', NAMESPACES):
            signal = _load_signal_element(signal_element)
            signal.multiplexer_ids = [int(multiplexer_id)]
            signal.multiplexer_signal = mux_signal.name
            signals.append(signal)

    return signals


def _load_message_element(message, bus_name, nodes, strict):
    """Load given message element and return a message object.

    """

    # Default values.
    name = None
    frame_id = None
    is_extended_frame = False
    notes = None
    length = 'auto'
    interval = None
    senders = []

    # Message XML attributes.
    for key, value in message.attrib.items():
        if key == 'name':
            name = value
        elif key == 'id':
            frame_id = int(value, 0)
        elif key == 'format':
            is_extended_frame = (value == 'extended')
        elif key == 'length':
            length = value  # 'auto' needs additional processing after knowing all signals
        elif key == 'interval':
            interval = int(value)
        else:
            LOGGER.debug("Ignoring unsupported message attribute '%s'.", key)
            # TODO: triggered, count, remote

    # Comment.
    try:
        notes = message.find('ns:Notes', NAMESPACES).text
    except AttributeError:
        pass

    # Senders.
    producer = message.find('ns:Producer', NAMESPACES)

    if producer is not None:
        for sender in producer.findall('ns:NodeRef', NAMESPACES):
            senders.append(_get_node_name_by_id(nodes,
                                                sender.attrib['id']))

    # Find all signals in this message.
    signals = []

    for mux in message.findall('ns:Multiplex', NAMESPACES):
        signals += _load_multiplex_element(mux)

    for signal in message.findall('ns:Signal', NAMESPACES):
        signals.append(_load_signal_element(signal))

    if length == 'auto':
        if signals:
            last_signal = sorted(signals, key=start_bit)[-1]
            length = (start_bit(last_signal) + last_signal.length + 7) // 8
        else:
            length = 0
    else:
        length = int(length)

    return Message(frame_id=frame_id,
                   is_extended_frame=is_extended_frame,
                   name=name,
                   length=length,
                   senders=senders,
                   send_type=None,
                   cycle_time=interval,
                   signals=signals,
                   comment=notes,
                   bus_name=bus_name,
                   strict=strict)


def dump_string(database):
    """Format given database in KCD file format.

    """

    raise NotImplementedError('The KCD dump function is not yet implemented.')


def load_string(string, strict=True):
    """Parse given KCD format string.

    """

    root = ElementTree.fromstring(string)

    # Should be replaced with a validation using the XSD file.
    if root.tag != ROOT_TAG:
        raise ValueError(
            'Expected root element tag {}, but got {}.'.format(ROOT_TAG,
                                                               root.tag))

    nodes = [node.attrib for node in root.findall('./ns:Node', NAMESPACES)]
    buses = []
    messages = []

    try:
        document = root.find('ns:Document', NAMESPACES)
        version = document.attrib.get('version', None)
    except AttributeError:
        version = None

    for bus in root.findall('ns:Bus', NAMESPACES):
        bus_name = bus.attrib['name']
        bus_baudrate = int(bus.get('baudrate', 500000))
        buses.append(Bus(bus_name, baudrate=bus_baudrate))

        for message in bus.findall('ns:Message', NAMESPACES):
            messages.append(_load_message_element(message,
                                                  bus_name,
                                                  nodes,
                                                  strict))

    return InternalDatabase(messages,
                            [
                                Node(name=node['name'], comment=None)
                                for node in nodes
                            ],
                            buses,
                            version)
