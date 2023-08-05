from xrpc.serde import types
from xrpc.serde.abstract import SerdeInst

SERVER_SERDE_INST = SerdeInst([
    types.NoneSerde(),
    types.TypeVarSerde(),
    types.CallableArgsSerde(),
    types.CallableRetSerde(),
    types.ForwardRefSerde(),
    types.OptionalSerde(),
    types.UnionSerde(),
    types.BytesSerde(),
    types.DateTimeSerde(),
    types.AtomSerde(),
    types.UUIDSerde(),
    types.ListSerde(),
    types.DictSerde(),
    types.EnumSerde(),
    types.DataclassSerde(),
    types.NamedTupleSerde(),
    types.TupleSerde(),
])
