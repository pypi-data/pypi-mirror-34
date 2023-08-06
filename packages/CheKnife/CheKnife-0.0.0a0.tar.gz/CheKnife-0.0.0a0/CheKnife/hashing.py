import hashlib


def textmd5sum(text):
    md5sum = hashlib.md5()
    hash_seed = text.encode('utf-8')
    md5sum.update(hash_seed)
    md5string = str(md5sum.hexdigest())
    return md5string
