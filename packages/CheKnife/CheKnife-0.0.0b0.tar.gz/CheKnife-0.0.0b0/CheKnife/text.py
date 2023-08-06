def remove_newlines(text):
    return text.replace('\n', '')


def remove_non_ascii(text):
    return ''.join([x if ord(x) < 128 else '' for x in text])


def replace_non_asci_with_underscore(text):
    return ''.join([x if x.isalnum() else '_' for x in text])


def add_dottorrent(text):
    return '{}.torrent'.format(text)
