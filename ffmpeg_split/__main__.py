import ffmpeg
import argparse
import sys

CODEC_MAP = {
    'matroska,webm': 'mkv',
    'aac': 'm4a'
}


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='input filename')
    
    args = parser.parse_args()
    
    probe = ffmpeg.probe(args.input)
    vid_container = probe['format']['format_name']
    vid_base_name = '.'.join(args.input.split('.')[:-1])
    
    for i, stream in enumerate(probe['streams']):
        if stream['codec_type'] == 'audio':
            stream_out = "{:s}-stream{:d}.{:s}".format(vid_base_name, i, CODEC_MAP[stream['codec_name']])
        elif stream['codec_type'] == 'video':
            stream_out = "{:s}-stream{:d}.{:s}".format(vid_base_name, i, CODEC_MAP[vid_container])
        else:
            sys.stderr.write('skipping stream {:d} of unknown type {:s} \n'.format(i, stream['codec_type']))
            continue
        ffmpeg.input(args.input).output(stream_out, map='0:{:d}'.format(i), c='copy', loglevel='quiet').run()
        sys.stderr.write('wrote stream {:d} as {:s} \n'.format(i, stream_out))

if __name__ == "__main__":
    main()

