import io

from ..cortex import build_cortex_graph_from_header
from cortexpy.graph.parser.kmer import Kmer, KmerData, RawKmerConverter
from cortexpy.graph.parser.constants import UINT64_T
from cortexpy.graph.parser.header import from_stream


def kmer_generator_from_stream(stream):
    header = from_stream(stream)
    return kmer_generator_from_stream_and_header(stream, header)


def kmer_list_generator_from_stream(stream):
    header = from_stream(stream)
    return kmer_list_generator_from_stream_and_header(stream, header)


def kmer_string_generator_from_stream(stream):
    header = from_stream(stream)
    return kmer_string_generator_from_stream_and_header(stream, header)


def kmer_string_generator_from_stream_and_header(stream, header):
    return (l.astype('|S1').tostring().decode('utf-8') for l in
            kmer_list_generator_from_stream_and_header(stream, header))


def kmer_generator_from_stream_and_header(stream, header):
    record_size = header.kmer_container_size * UINT64_T + 5 * header.num_colors

    raw_record = stream.read(record_size)
    while raw_record != b'':
        yield Kmer(
            KmerData(raw_record,
                     header.kmer_size,
                     header.num_colors)
        )
        raw_record = stream.read(record_size)


def kmer_list_generator_from_stream_and_header(stream, header):
    record_size = header.kmer_container_size * UINT64_T + 5 * header.num_colors
    kmer_container_size = header.kmer_container_size * UINT64_T
    assert record_size >= kmer_container_size
    kmer_converter = RawKmerConverter(header.kmer_size)

    advance = record_size - kmer_container_size
    raw_kmer = stream.read(kmer_container_size)
    while raw_kmer != b'':
        yield kmer_converter.to_letters(raw_kmer)
        stream.seek(advance, io.SEEK_CUR)
        raw_kmer = stream.read(kmer_container_size)


def load_cortex_graph(stream):
    header = from_stream(stream)
    kmer_generator = kmer_generator_from_stream_and_header(stream, header)
    return build_cortex_graph_from_header(header, kmer_generator=kmer_generator)
